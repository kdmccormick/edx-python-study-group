""" Tests, version 8, sans GET tests """

from itertools import product
from unittest import TestCase

import requests

from mixins import EnrollmentTestMixin


class EnrollmentPatchTests(EnrollmentTestMixin, TestCase):

    method = 'PATCH'

    names = ["alice", "bob", "xavier"]
    statuses = ["enrolled", "pending", "suspended", "canceled"]
    extras = [{}, {"extra_key": "extra_value"}]

    def test_ok_variants(self):
        for name in self.names:
            for status in self.statuses:
                for extra in self.extras:
                    record = {
                        "student_key": name,
                        "status": status,
                    }
                    record.update(extra)
                    data = [record]
                    response = requests.patch(self.allowed_url, headers=self.headers, json=data)
                    self.assertEqual(response.status_code, 200)
