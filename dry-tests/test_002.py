""" Product tests, version 8, sans GET tests """

from itertools import product
from unittest import TestCase

import ddt
import requests

from mixins import EnrollmentTestMixin


@ddt.ddt
class EnrollmentPatchTests(EnrollmentTestMixin, TestCase):

    method = 'PATCH'

    names = ["alice", "bob", "xavier"]
    statuses = ["enrolled", "pending", "suspended", "canceled"]
    extras = [{}, {"extra_key": "extra_value"}]

    @ddt.data(*product(names, statuses, extras))
    @ddt.unpack
    def test_ok_variants(self, name, status, extra):
        record = {
            "student_key": name,
            "status": status,
        }
        record.update(extra)
        data = [record]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)
