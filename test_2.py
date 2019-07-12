""" Tests, version 2 """

from unittest import TestCase

import requests

from utils import request_jwt_token


class EnrollmentTests(TestCase):

    registrar_root = "https://registrar-kdmccormick.sandbox.edx.org/api/v2"
    path_format = registrar_root + "/programs/{program_key}/enrollments"
    allowed_url = path_format.format(program_key="master-of-popcorn")
    disallowed_url = path_format.format(program_key="master-of-cranberries")


class EnrollmentGetTests(EnrollmentTests):

    def test_accepted(self):
        headers = {"Authorization": request_jwt_token()}
        response = requests.get(self.allowed_url, headers=headers)
        self.assertEqual(response.status_code, 202)

    def test_permission_denied(self):
        headers = {"Authorization": request_jwt_token()}
        response = requests.get(self.disallowed_url, headers=headers)
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated(self):
        response_1 = requests.get(self.allowed_url)
        self.assertEqual(response_1.status_code, 401)
        response_2 = requests.get(self.disallowed_url)
        self.assertEqual(response_2.status_code, 401)


class EnrollmentPatchTests(EnrollmentTests):

    def test_ok(self):
        headers = {"Authorization": request_jwt_token()}
        data = [{"student_key": "bob", "status": "pending"}]
        response = requests.patch(self.allowed_url, headers=headers, json=data)
        self.assertEqual(response.status_code, 200)

    def test_permission_denied(self):
        headers = {"Authorization": request_jwt_token()}
        response = requests.patch(self.disallowed_url, headers=headers, json=data)
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated(self):
        response_1 = requests.patch(self.allowed_url)
        self.assertEqual(response_1.status_code, 401)
        response_2 = requests.patch(self.disallowed_url)
        self.assertEqual(response_2.status_code, 401)
