from locust import HttpUser, task

PORT = 8000
URL = f"http://localhost:{PORT}"

class MyUser(HttpUser):
    @task
    def root(self):
        self.client.get("/")

    @task
    def cpu_bound_task(self):
        self.client.get("/cpu-bound")

    @task
    def io_bound_task(self):
        self.client.get("/io-bound")