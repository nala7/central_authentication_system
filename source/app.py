from flask import Flask
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from keycloak.keycloak_openid import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError, KeycloakGetError

import json

app = Flask(__name__)
Bootstrap5(app)

keycloak_open_id = KeycloakOpenID(server_url="http://localhost:8080/",
                                 client_id="nodo",
                                 realm_name="master",
                                 client_secret_key="V35a9m9GjYpslkw11mXwEMHM3Ac8hmhD")
keycloak_open_id.well_know()

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        success = True
        result = { "access_token": "token", "refresh_token": "refresh", "error_description": "incorrect username" }
        success, result = valid_login(username, request.form['password'])
        if success:
            return log_the_user_in(username, result["access_token"], result["refresh_token"])
        else:
            error = result["error_description"]
    # The code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username, password):
    # import pdb
    # pdb.set_trace()
    try:
        token = keycloak_open_id.token(username, password)
    except (KeycloakAuthenticationError, KeycloakGetError) as e:
        return False, json.loads(e.error_message)
    return True, token

def log_the_user_in(username, token, refresh_token):
    return render_template('success.html', username=username, token=token, refresh_token=refresh_token)

# # Get Userinfo
# userinfo = keycloak_openid.userinfo(token['access_token'])

# # Refresh token
# token = keycloak_openid.refresh_token(token['refresh_token'])

# # Logout
# keycloak_openid.logout(token['refresh_token'])

# # Chequear roles
# keycloak_open_id.introspect(token['access_token'])["resource_access"]["account"]["roles"]

# Automáticamente darle un rol a los estudiantes y otro a los profesores