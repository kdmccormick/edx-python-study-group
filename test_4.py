""" Tests, version 3 """

from unittest import TestCase

import requests

from utils import get_jwt_token


class EnrollmentTestMixin(object):

    api_root = "https://api.stage.edx.org/registrar/v2"
    test_url = "{}/programs/master-of-how/enrollments".format(api_root)

    method = None  # Override me in subclass!

    def test_unauthenticated_gives_401(self):
        response = requests.request(self.method, self.test_url)
        self.assertEqual(response.status_code, 401)


class EnrollmentGetTests(TestCase, EnrollmentTestMixin):

    method = 'GET'

    def test_successful_get_gives_202(self):
        jwt = get_jwt_token()
        headers = {"Authorization": "JWT {}".format(jwt)}
        response = requests.get(self.test_url, headers=headers)
        self.assertEqual(response.status_code, 202)


class EnrollmentPatchTests(TestCase, EnrollmentTestMixin):

    method = 'PATCH'

    def test_successful_patch_gives_200(self):
        jwt = get_jwt_token()
        headers = {"Authorization": "JWT {}".format(jwt)}
        data = [
            {"student_key": "bob", "status": "pending"},
        ]
        response = requests.patch(self.test_url, headers=headers, json=data)
        self.assertEqual(response.status_code, 200)
