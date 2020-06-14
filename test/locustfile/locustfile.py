from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):
    @task
    def get_status(self):
        response = self.client.get("/status/200")

    @task
    def patch_status(self):
        response = self.client.patch("/status/200")

    @task
    def post_status(self):
        response = self.client.post("/status/200")

    @task
    def put_status(self):
        response = self.client.put("/status/200")

    @task
    def delete_status(self):
        response = self.client.delete("/status/200")

class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(1, 2)
