""" Tests, version 7 """

from unittest import TestCase

import requests

from utils import request_jwt


class EnrollmentTestMixin(object):

    registrar_root = "https://registrar-kdmccormick.sandbox.edx.org/api/v2"
    path_format = registrar_root + "/programs/{program_key}/enrollments"
    allowed_url = path_format.format(program_key="master-of-popcorn")
    disallowed_url = path_format.format(program_key="master-of-cranberries")
    headers = {"Authorization": request_jwt()}

    method = None  # Override in subclass!

    def test_permission_denied(self):
        response = requests.request(
            self.method, self.disallowed_url, headers=self.headers
        )
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated(self):
        response_1 = requests.request(self.method, self.allowed_url)
        self.assertEqual(response_1.status_code, 401)
        response_2 = requests.request(self.method, self.disallowed_url)
        self.assertEqual(response_2.status_code, 401)


class EnrollmentGetTests(TestCase, EnrollmentTestMixin):

    method = 'GET'

    def test_accepted(self):
        response = requests.get(self.allowed_url, headers=self.headers)
        self.assertEqual(response.status_code, 202)


class EnrollmentPatchTests(TestCase, EnrollmentTestMixin):

    method = 'PATCH'

    def test_ok(self):
        data = [{"student_key": "bob", "status": "pending"}]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)


class UnrelatedTests(TestCase):

    def test_numbers(self):
        self.assertEqual(1 + 1, 2)

