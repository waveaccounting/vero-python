import os
import unittest
import json
import requests
from mock import patch
import vero


class VeroEventLoggerTests(unittest.TestCase):
    def setUp(self):
        self.auth_token = os.environ['VERO_AUTH_TOKEN']
        self.logger = vero.client.VeroEventLogger(self.auth_token)
        self.user_id = 1
        self.new_user_id = 2
        self.user_email = 'john@example.com'
        self.user_data = {
            'name': 'John Smith',
            'height': 72,
            'weight': 180,
            'title': 'Mr.',
            'favourites': {
                'color': 'red',
                'ice cream': 'chocolate'
            }
        }
        self.user_changes = {
            'height': 73,
            'extra': 'extra'
        }
        self.user_tags = ['x', 'y', 'z']
        self.event_name = 'test event'
        self.event_data = {
            'string data': 'a',
            'numeric data': 123,
            'float data': 1.23,
            'list data': ['a', 1],
            'tuple data': ('a', 1),
            'dict data': {
                'a': 1,
                1: 'a'
            }
        }

    def test_fire_request(self):
        endpoint = vero.client.VeroEndpoints.ADD_USER
        payload = {
            'test': 1
        }
        with patch('requests.request') as mock_request:
            self.logger._fire_request(endpoint, payload)

        mock_request.assert_called_once_with(endpoint.method, endpoint.url, json=payload)

    def test_add_user(self):
        req = self.logger.add_user(self.user_id, self.user_data)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_reidentify_user(self):
        req = self.logger.reidentify_user(self.user_id, self.new_user_id)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_user__with_email(self):
        req = self.logger.add_user(self.user_id, self.user_data, user_email=self.user_email)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_user__development_mode(self):
        req = self.logger.add_user(self.user_id, self.user_data, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_edit_user(self):

        req = self.logger.edit_user(self.user_id, self.user_changes)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_edit_user__development_mode(self):
        req = self.logger.edit_user(self.user_id, self.user_changes, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_tags(self):
        req = self.logger.add_tags(self.user_id, self.user_tags)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_tags__empyty_list(self):
        req = self.logger.add_tags(self.user_id, [])

        self.assertEqual(req.status_code, requests.codes.bad)

    def test_add_tags__development_mode(self):
        req = self.logger.add_tags(self.user_id, self.user_tags, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_remove_tags(self):
        req = self.logger.remove_tags(self.user_id, self.user_tags)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_remove_tags__empyty_list(self):
        req = self.logger.add_tags(self.user_id, [])

        self.assertEqual(req.status_code, requests.codes.bad)

    def test_remove_tags__development_mode(self):
        req = self.logger.remove_tags(self.user_id, self.user_tags, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_unsubscribe_user(self):
        req = self.logger.unsubscribe_user(self.user_id)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_resubscribe_user(self):
        self.logger.unsubscribe_user(self.user_id)
        req = self.logger.resubscribe_user(self.user_id)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_unsubscribe_user__development_mode(self):
        req = self.logger.unsubscribe_user(self.user_id, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_event(self):
        req = self.logger.add_event(self.event_name, self.event_data, self.user_id)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_event__with_email(self):
        req = self.logger.add_event(self.event_name, self.event_data, self.user_id, user_email=self.user_email)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_add_event__development_mode(self):
        req = self.logger.add_event(self.event_name, self.event_data, self.user_id, development_mode=True)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_delete_user(self):
        self.logger.add_user(self.user_id, self.user_data)
        req = self.logger.delete_user(self.user_id)

        self.assertEqual(req.status_code, requests.codes.ok)

    def test_heartbeat(self):
        success = self.logger.heartbeat()

        self.assertEqual(success, True)


if __name__ == "__main__":
    if os.environ.get('VERO_AUTH_TOKEN', None) is None:
        exit('error: must set environment variable VERO_AUTH_TOKEN')
    unittest.main()
