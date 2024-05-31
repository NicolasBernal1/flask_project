from locust import HttpUser, task

class HelloWorlduser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/login")
        self.client.get("/sign-up")
        self.client.get("/delete-note")
        self.client.get("/logout")
