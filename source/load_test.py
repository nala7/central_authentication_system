# from locust import HttpUser, task
from random import choice

import requests
import logging
import http.client

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

URL_TOKEN = "realms/{realm-name}/protocol/openid-connect/token"

class KeycloakUser():
    def __init__(self):
        
    # def on_start(self):
        self.users = [("sandra", "a")]
        self.realm_name = "master"
        self.client_id = "nodo"
        self.secret_key = "V35a9m9GjYpslkw11mXwEMHM3Ac8hmhD"

    # @task
    def token_load_test(self):
        username, password = choice(self.users)
        params_path = {"realm-name": self.realm_name}
        payload = {
            "username": username,
            "password": password,
            "client_id": self.client_id,
            "grant_type": "password",
            "code": "",
            "redirect_uri": "",
            "client_secret": "V35a9m9GjYpslkw11mXwEMHM3Ac8hmhD"
        }
        response = requests.post('http://localhost:8080/' + URL_TOKEN.format(**params_path), data=payload)
        print(response.text)
        # self.client.post(URL_TOKEN.format(**params_path), data=payload)

KeycloakUser().token_load_test()

url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'

# params = {

#     'client_id': 'nodo',
#     'grant_type': 'password',
#     'username' : 'laila',
#     'password': '1234'
# }
# x = requests.post(url, params, verify=False).content.decode('utf-8')
# print (x)
