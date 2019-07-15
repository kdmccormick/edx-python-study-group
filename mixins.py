""" Mixins for testing endpoints """

import requests

from utils import request_jwt_token


class EnrollmentTestMixin(object):

    registrar_root = "https://registrar-kdmccormick.sandbox.edx.org/api/v2"
    path_format = registrar_root + "/programs/{program_key}/enrollments"
    allowed_url = path_format.format(program_key="master-of-popcorn")
    disallowed_url = path_format.format(program_key="master-of-cranberries")

    method = None  # Override in subclass!

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.headers = {"Authorization": request_jwt_token()}
        print("Requested JWT token!")

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
