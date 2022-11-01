from keycloak.keycloak_openid import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/",
                                 client_id="example_client",
                                 realm_name="example_realm",
                                 client_secret_key="secret")

print(keycloak_openid.client_id)

# Get WellKnow
config_well_known = keycloak_openid.well_know()

# Get Code With Oauth Authorization Request
auth_url = keycloak_openid.auth_url(
    redirect_uri="your_call_back_url",
    scope="email",
    state="your_state_info")

# Get Access Token With Code
access_token = keycloak_openid.token(
    grant_type='authorization_code',
    code='the_code_you_get_from_auth_url_callback',
    redirect_uri="your_call_back_url")


# Get Token
token = keycloak_openid.token("user", "password")
token = keycloak_openid.token("user", "password", totp="012345")

print (token)