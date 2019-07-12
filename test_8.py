""" Tests, version 8, sans GET tests """

from unittest import TestCase

import requests

from mixins import EnrollmentTestMixin


class EnrollmentPatchTests(TestCase, EnrollmentTestMixin):

    method = 'PATCH'

    def test_ok(self):
        data = [{"student_key": "bob", "status": "pending"}]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)
