""" DD tests, version 8, sans GET tests """

from unittest import TestCase

import requests

from mixins import EnrollmentTestMixin


class EnrollmentPatchTests(EnrollmentTestMixin, TestCase):

    method = 'PATCH'

    def test_ok(self):
        data = [{"student_key": "bob", "status": "pending"}]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)

    def test_ok_multiple(self):
        data = [
            {"student_key": "bob", "status": "pending"},
            {"student_key": "alice", "status": "enrolled"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 200)

    def test_multi_status_with_duplicate(self):
        data = [
            {"student_key": "bob", "status": "pending"},
            {"student_key": "alice", "status": "enrolled"},
            {"student_key": "bob", "status": "pending"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 207)

    def test_multi_status_with_invalid(self):
        data = [
            {"student_key": "bob", "status": "pending"},
            {"student_key": "alice", "status": "enrolled"},
            {"student_key": "xavier", "status": "chilling"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 207)

    def test_processing_failed(self):
        data = [
            {"student_key": "xavier", "status": "chilling"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 422)

    def test_processing_failed_multiple(self):
        data = [
            {"student_key": "bob", "status": "pending"},
            {"student_key": "bob", "status": "pending"},
            {"student_key": "xavier", "status": "chilling"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 422)

    def test_bad_request_invalid_keys(self):
        data = [
            {"student_key": "alice", "status": "enrolled"},
            {"$tudenT<->KEY": "dora", "5TaTU5": "enrolled"}
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 400)

    def test_bad_request_not_a_dict(self):
        data = [
            "student_key: ellie, status: pending",
            {"student_key": "bob", "status": "pending"},
        ]
        response = requests.patch(self.allowed_url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 400)
