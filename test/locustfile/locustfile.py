from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

class MyLocust(FastHttpUser):
    wait_time = between(1, 2)

    @task
    def get_status_200(self):
        response = self.client.get("/status/200")

    @task
    def patch_status_200(self):
        response = self.client.patch("/status/200")

    @task
    def post_status_200(self):
        response = self.client.post("/status/200")

    @task
    def put_status_200(self):
        response = self.client.put("/status/200")

    @task
    def delete_status_200(self):
        response = self.client.delete("/status/200")

    @task
    def get_status_400(self):
        response = self.client.get("/status/400")

    @task
    def patch_status_400(self):
        response = self.client.patch("/status/400")

    @task
    def post_status_400(self):
        response = self.client.post("/status/400")

    @task
    def put_status_400(self):
        response = self.client.put("/status/400")

    @task
    def delete_status_400(self):
        response = self.client.delete("/status/400")

    @task
    def get_status_500(self):
        response = self.client.get("/status/500")

    @task
    def patch_status_500(self):
        response = self.client.patch("/status/500")

    @task
    def post_status_500(self):
        response = self.client.post("/status/500")

    @task
    def put_status_500(self):
        response = self.client.put("/status/500")

    @task
    def delete_status_500(self):
        response = self.client.delete("/status/500")
