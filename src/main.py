import asyncio
import time
import newrelic.agent

from config import get_config


@newrelic.agent.background_task()
async def stats_publisher(stats_endpoint, interval):
    while True:
        print("Hello")
        app = newrelic.agent.application()

        event_name = 'hello_world_event'
        event_body = {'param1': 'value1'}

        newrelic.agent.record_custom_event(event_name, event_body, app)
        time.sleep(5)

if __name__ == "__main__":
    config = get_config()

    if config['STATS_ENDPOINT'] is None:
        raise RuntimeError('The stats endpoint is needed to run the sidecar')

    asyncio.run(stats_publisher())
