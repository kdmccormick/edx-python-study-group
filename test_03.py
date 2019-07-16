""" DD tests, version 8, sans GET tests """

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
        [bob_enroll],  # One record
        [bob_enroll, alice_enroll],  # Multiple records
    )
    def test_ok(self, data):
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)

    @ddt.data(
        [bob_enroll, alice_enroll, bob_enroll],  # Duplicate
        [bob_enroll, alice_enroll, bad_status_enroll],  # Record with invalid status
    )
    def test_multi_status(self, data):
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 207)

    @ddt.data(
        [bad_status_enroll],  # One record
        [bob_enroll, bob_enroll, bad_status_enroll],  # Multiple records
    )
    def test_processing_failed(self, data):
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 422)

    @ddt.data(
        [bob_enroll, bad_keys_enroll],  # Record with invalid keys
        [bad_type_enroll, bob_enroll],  # Record that is just a string
    )
    def test_bad_request(self, data):
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 400)
