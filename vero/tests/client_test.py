import unittest
from mock import Mock, patch
import vero

__MOCK_AUTH_TOKEN__ = '__MOCK_AUTH_TOKEN__'
__MOCK_REQUESTS__ = Mock()
__BASE_URL__ = vero.client.VeroEndpoints.VERO_BASE_URL


@patch('vero.client.requests.request', __MOCK_REQUESTS__)
class VeroEventLoggerTests(unittest.TestCase):
    def setUp(self):
        __MOCK_REQUESTS__.reset_mock()
        self.logger = vero.client.VeroEventLogger(__MOCK_AUTH_TOKEN__)
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
        endpoint = vero.client.Endpoint('method', 'url')

        self.logger._fire_request(endpoint, {'test': 1})

        __MOCK_REQUESTS__.assert_called_once_with(
            'method',
            'url',
            json={
                'test': 1
            },
        )

    def test_add_user(self):
        self.logger.add_user(self.user_id, self.user_data)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + 'api/v2/users/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'data': self.user_data,
                'id': self.user_id,
                'email': None,
            },
        )

    def test_reidentify_user(self):
        self.logger.reidentify_user(self.user_id, self.new_user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/reidentify',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'new_id': self.new_user_id,
                'id': self.user_id,
            },
        )

    def test_add_user__with_email(self):
        self.logger.add_user(self.user_id, self.user_data, user_email=self.user_email)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + 'api/v2/users/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'data': self.user_data,
                'id': self.user_id,
                'email': self.user_email,
            },
        )

    def test_edit_user(self):
        self.logger.edit_user(self.user_id, self.user_changes)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'changes': self.user_changes,
                'id': self.user_id,
            },
        )

    def test_add_tags(self):
        self.logger.add_tags(self.user_id, self.user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'add': self.user_tags,
                'id': self.user_id,
            },
        )

    def test_add_tags__empty_list(self):
        self.logger.add_tags(self.user_id, [])

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'add': [],
                'id': self.user_id,
            },
        )

    def test_remove_tags(self):
        self.logger.remove_tags(self.user_id, self.user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'remove': self.user_tags,
                'id': self.user_id,
            },
        )

    def test_remove_tags__empty_list(self):
        self.logger.remove_tags(self.user_id, [])

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + 'api/v2/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'remove': [],
                'id': self.user_id,
            },
        )

    def test_unsubscribe_user(self):
        self.logger.unsubscribe_user(self.user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + 'api/v2/users/unsubscribe',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': self.user_id,
            },
        )

    def test_resubscribe_user(self):
        self.logger.resubscribe_user(self.user_id)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + 'api/v2/users/resubscribe',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': self.user_id,
            },
        )

    def test_add_event(self):
        self.logger.add_event(self.event_name, self.event_data, self.user_id)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + 'api/v2/events/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'event_name': self.event_name,
                'data': self.event_data,
                'identity': {
                    'id': self.user_id,
                    'email': None,
                },
            },
        )

    def test_add_event__with_email(self):
        self.logger.add_event(self.event_name, self.event_data, self.user_id, user_email=self.user_email)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + 'api/v2/events/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'event_name': self.event_name,
                'data': self.event_data,
                'identity': {
                    'id': self.user_id,
                    'email': self.user_email,
                },
            },
        )

    def test_delete_user(self):
        self.logger.delete_user(self.user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'DELETE',
            __BASE_URL__ + 'api/v2/users/delete',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': self.user_id,
            },
        )

    def test_heartbeat(self):
        self.logger.heartbeat()

        __MOCK_REQUESTS__.assert_called_once_with(
            'GET',
            __BASE_URL__ + 'api/v2/heartbeat',
        )
