""" Tests, version 3 """

from unittest import TestCase

import requests

from utils import request_jwt


class EnrollmentTests(TestCase):

    registrar_root = "https://registrar-kdmccormick.sandbox.edx.org/api/v2"
    path_format = registrar_root + "/programs/{program_key}/enrollments"
    allowed_url = path_format.format(program_key="master-of-popcorn")
    disallowed_url = path_format.format(program_key="master-of-cranberries")

    method = None  # Override in subclass!

    __test__ = False

    def test_permission_denied(self):
        headers = {"Authorization": request_jwt()}
        response = requests.request(
            self.method, self.disallowed_url, headers=headers
        )
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated(self):
        response_1 = requests.request(self.method, self.allowed_url)
        self.assertEqual(response_1.status_code, 401)
        response_2 = requests.request(self.method, self.disallowed_url)
        self.assertEqual(response_2.status_code, 401)


class EnrollmentGetTests(EnrollmentTests):

    method = 'GET'
    __test__ = True

    def test_accepted(self):
        headers = {"Authorization": request_jwt()}
        response = requests.get(self.allowed_url, headers=headers)
        self.assertEqual(response.status_code, 202)


class EnrollmentPatchTests(EnrollmentTests):

    method = 'PATCH'
    __test__ = True

    def test_ok(self):
        headers = {"Authorization": request_jwt()}
        data = [{"student_key": "bob", "status": "pending"}]
        response = requests.patch(self.allowed_url, headers=headers, json=data)
        self.assertEqual(response.status_code, 200)
