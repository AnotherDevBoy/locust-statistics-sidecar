from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):
    @task
    def index(self):
        response = self.client.get("/")

class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(1, 2)
