import asyncio
import time
import newrelic.agent

from config import get_config

@newrelic.agent.background_task()
async def stats_publisher(stats_endpoint, interval):
    while True:
        print("Hello")
        application = newrelic.agent.application()
        newrelic.agent.record_custom_event('hello_world_event', {'param1':'value1'}, application)
        time.sleep(5)

if __name__ == "__main__":
    config = get_config()

    if config['STATS_ENDPOINT'] is None:
      raise RuntimeError('The stats endpoint is needed to run the sidecar')

    asyncio.run(stats_publisher())
