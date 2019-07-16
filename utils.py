""" Test utilities """

import requests

from secrets import CLIENT_ID, CLIENT_SECRET


LMS_ROOT = "https://kdmccormick.sandbox.edx.org"


def request_jwt():
    """
    Using our API client credentials, get a JWT from the LMS.

    Returns: str
    """
    request_jwt.times_called += 1
    _write_jwt_calls()

    url = "{}/oauth2/access_token/".format(LMS_ROOT)
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "token_type": "jwt",
        "grant_type": "client_credentials",
    }
    response = requests.post(url, data=data)
    jwt = response.json()["access_token"]
    return "JWT " + jwt


def _write_jwt_calls():
    with open("request_jwt_calls.txt", "w") as f:
        f.write("request_jwt was called {} times.\n".format(
            request_jwt.times_called
        ))


request_jwt.times_called = 0
_write_jwt_calls()


def _write_jwt_calls():
    with open("request_jwt_calls.txt", "w") as f:
        f.write("request_jwt was called {} times.\n".format(
            request_jwt.times_called
        ))
