""" Test utilities """

import requests

from secrets import CLIENT_ID, CLIENT_SECRET


LMS_ROOT = "https://courses.stage.edx.org"


def get_jwt_token():
    """
    Using our API client credentials, get a JWT token from the LMS.

    Returns: str
    """
    url = "{}/oauth2/access_token/".format(LMS_ROOT)
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "token_type": "jwt",
        "grant_type": "client_credentials",
    }
    response = requests.post(url, data=data)
    jwt_token = response.json()["access_token"]
    print("Retrieved JWT token from LMS.")
    return jwt_token
