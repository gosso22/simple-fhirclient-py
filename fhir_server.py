import requests

# Keycloak authentication endpoint
KEYCLOAK_AUTH_URL = "http://192.168.100.4:8081/auth/realms/fhir-core/protocol/openid-connect/token"

# Client ID and secret
CLIENT_ID = "fhir-core-server"
CLIENT_SECRET = "6711ce3b-3b7d-41e7-ae61-58b46c6119e8"
USER_NAME = "test"
PASSWORD = "Test123"

# Request access token
data = {
    "grant_type": "password",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "username": USER_NAME,
    "password": PASSWORD
}


def get_header():
    header = {
        'Authorization': f'Bearer {get_token()}'
    }

    return header


def post_header():
    header = {
        'Authorization': f'Bearer {get_token()}',
        'Content-Type': 'application/json'
    }

    return header


def get_token():
    response = requests.post(KEYCLOAK_AUTH_URL, data=data)
    access_token = response.json()["access_token"]

    return access_token


if __name__ == '__main__':
    print(get_token())
