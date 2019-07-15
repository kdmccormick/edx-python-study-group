""" Test utilities """

import requests

from secrets import CLIENT_ID, CLIENT_SECRET


LMS_ROOT = "https://kdmccormick.sandbox.edx.org"


def request_jwt_token():
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
    return "JWT " + jwt_token
