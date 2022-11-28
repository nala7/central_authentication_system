from locust import HttpUser, task
from random import choice

URL_TOKEN = "realms/{realm-name}/protocol/openid-connect/token"

class KeycloakUser(HttpUser):
    def on_start(self):
        self.users = [("sandra", "a")]
        self.realm_name = "master"
        self.client_id = "nodo"
        self.secret_key = "V35a9m9GjYpslkw11mXwEMHM3Ac8hmhD"

    @task
    def token_load_test(self):
        username, password = choice(self.users)
        params_path = {"realm-name": self.realm_name}
        payload = {
            "username": username,
            "password": password,
            "client_id": self.client_id,
            "grant_type": ["password"],
            "code": "",
            "redirect_uri": "",
            "client_secret": self.secret_key
        }
        self.client.post(URL_TOKEN.format(**params_path), data=payload)
