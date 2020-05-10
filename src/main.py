import asyncio
import aiohttp
import newrelic.agent
import logging

from config import get_config

logger = logging.getLogger('locust-newrelic-sidecar')


def send_stats_event(app, stats):
    newrelic.agent.record_custom_event('locust_statistics', stats, app)


async def get_stats(session, stats_endpoint):
    async with session.get(stats_endpoint) as resp:
        stats_body = await resp.json()
        if stats_endpoint['state'] != 'running':
            return None

        return {
            'error_rate': stats_endpoint['fail_ratio'],
            'latency_p50': stats_endpoint['current_response_time_percentile_50'],
            'latency_p95': stats_endpoint['current_response_time_percentile_95'],
            'rps': stats_endpoint['total_rps'],
            'user_count': stats_endpoint['user_count']
        }


@newrelic.agent.background_task()
async def stats_publisher(stats_endpoint, interval):
    async with aiohttp.ClientSession() as session:
        while True:
            logger.info(f'Collect statistics from Locust endpoint: ${stats_endpoint}')
            stats = await get_stats(session, stats_endpoint)

            if stats is None:
                logger.info('Locust is not running. Skipping event submission.')
            else:
                logger.info('Sending event to NewRelic')
                send_stats_event(newrelic.agent.application(), stats)

            await asyncio.sleep(interval)

if __name__ == '__main__':
    config = get_config()

    if config['STATS_ENDPOINT'] is None:
        raise RuntimeError('The stats endpoint is needed to run the sidecar')

    asyncio.run(stats_publisher(config['STATS_ENDPOINT'], config['POLL_INTERVAL_SECONDS']))
