import asyncio
import aiohttp
import newrelic.agent
import logging
import sys

from config import get_config

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def send_summary_event(app, stats):
    newrelic.agent.record_custom_event("LocustSummary", stats, app)


def send_request_statistics(app, req_stats):
    for stats in req_stats:
        newrelic.agent.record_custom_event("LocustRequestStatistics", stats, app)


async def get_stats(session, locust_url):
    async with session.get(f"{locust_url}/stats/requests", ssl=False) as resp:
        stats_body = await resp.json()
        if stats_body["state"] != "running":
            return None

        summary = {
            "error_rate": stats_body["fail_ratio"],
            "latency_p50": stats_body["current_response_time_percentile_50"],
            "latency_p95": stats_body["current_response_time_percentile_95"],
            "rps": stats_body["total_rps"],
            "user_count": stats_body["user_count"]
        }

        request_stats = []

        for stats in stats_body["stats"]:
            request_stats.append({
                "avg_content_length": stats["avg_content_length"],
                "avg_response_time": stats["avg_response_time"],
                "current_fail_per_sec": stats["current_fail_per_sec"],
                "current_rps": stats["current_rps"],
                "max_response_time": stats["max_response_time"],
                "median_response_time": stats["median_response_time"],
                "method": stats["method"],
                "min_response_time": stats["min_response_time"],
                "name": stats["name"],
                "ninetieth_response_time": stats["ninetieth_response_time"],
                "num_failures": stats["num_failures"],
                "num_requests": stats["num_requests"],
                "safe_name": stats["safe_name"]
            })

        return (summary, request_stats)


@newrelic.agent.background_task()
async def stats_publisher(locust_url, interval):
    async with aiohttp.ClientSession() as session:
        while True:
            logger.debug(f"Collect statistics from Locust: {locust_url}")
            stats = await get_stats(session, locust_url)

            if stats is None:
                logger.debug("Locust is not running. Skipping event submission.")
            else:
                logger.debug("Sending event to NewRelic")
                send_summary_event(newrelic.agent.application(), stats[0])
                send_request_statistics(newrelic.agent.application(), stats[1])

            await asyncio.sleep(interval)

if __name__ == "__main__":
    logger.info("Starting Locust NewRelic sidecar")
    config = get_config()

    if config["LOCUST_URL"] is None:
        raise RuntimeError("The stats endpoint is needed to run the sidecar")

    asyncio.run(stats_publisher(config["LOCUST_URL"], config["POLL_INTERVAL_SECONDS"]))
