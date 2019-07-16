""" DD tests, version 8, sans GET tests """

from unittest import TestCase

import requests

from mixins import EnrollmentTestMixin


class EnrollmentPatchTests(EnrollmentTestMixin, TestCase):

    method = 'PATCH'

    bob_enroll = {"student_key": "bob", "status": "pending"}
    alice_enroll = {"student_key": "alice", "status": "enrolled"}
    bad_status_enroll = {"student_key": "xavier", "status": "chilling"}
    bad_keys_enroll = {"$tudenT<->KEY": "dora", "5TaTU5": "enrolled"}
    bad_type_enroll = "student_key: ellie, status: pending"

    def test_ok(self):
        data = [self.bob_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)

    def test_ok_multiple(self):
        data = [self.bob_enroll, self.alice_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)

    def test_multi_status_with_duplicate(self):
        data = [self.bob_enroll, self.alice_enroll, self.bob_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 207)

    def test_multi_status_with_invalid(self):
        data = [self.bob_enroll, self.alice_enroll, self.bad_status_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 207)

    def test_processing_failed(self):
        data = [self.bad_status_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 422)

    def test_processing_failed_multiple(self):
        data = [self.bob_enroll, self.bob_enroll, self.bad_status_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 422)

    def test_bad_request_invalid_keys(self):
        data = [self.bob_enroll, self.bad_keys_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 400)

    def test_bad_request_not_a_dict(self):
        data = [self.bad_type_enroll, self.bob_enroll]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 400)
