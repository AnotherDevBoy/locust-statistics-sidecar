import time
import newrelic.agent

@newrelic.agent.background_task()
def task():
    while True:
        print("Hello")
        application = newrelic.agent.application()
        newrelic.agent.record_custom_event('hello_world_event', {'param1':'value1'}, application)
        time.sleep(5)

task()
