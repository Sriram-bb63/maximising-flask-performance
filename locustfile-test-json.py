from locust import HttpUser, task

PORT = 8000
URL = f"http://localhost:{PORT}"

class MyUser(HttpUser):
    @task
    def root(self):
        self.client.get("/get-json")