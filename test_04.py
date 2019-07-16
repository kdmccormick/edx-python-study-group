""" Tests, version 8, sans GET tests """

from unittest import TestCase

import ddt
import requests

from mixins import EnrollmentTestMixin


@ddt.ddt
class EnrollmentPatchTests(EnrollmentTestMixin, TestCase):

    method = 'PATCH'

    bob_enroll = {"student_key": "bob", "status": "pending"}
    alice_enroll = {"student_key": "alice", "status": "enrolled"}
    bad_status_enroll = {"student_key": "xavier", "status": "chilling"}
    bad_keys_enroll = {"$tudenT<->KEY": "dora", "5TaTU5": "enrolled"}
    bad_type_enroll = "student_key: ellie, status: pending"

    @ddt.data(
        ([bob_enroll], 200),
        ([bob_enroll, alice_enroll], 200),
        ([bob_enroll, alice_enroll, bob_enroll], 207),
        ([bob_enroll, alice_enroll, bad_status_enroll], 207),
        ([bad_status_enroll], 422),
        ([bob_enroll, bob_enroll, bad_status_enroll], 422),
        ([bob_enroll, bad_keys_enroll], 400),
        ([bad_type_enroll, bob_enroll], 400),
    )
    @ddt.unpack
    def test_status_codes(self, data, expected_status):
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, expected_status)
