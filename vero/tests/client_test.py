import unittest
from mock import Mock, patch
import vero

__MOCK_AUTH_TOKEN__ = '__MOCK_AUTH_TOKEN__'
__MOCK_REQUESTS__ = Mock()
__BASE_URL__ = vero.client.VeroEndpoints._BASE_URL


@patch('vero.client.requests.request', __MOCK_REQUESTS__)
class VeroEventLoggerTests(unittest.TestCase):
    def setUp(self):
        __MOCK_REQUESTS__.reset_mock()
        self.logger = vero.client.VeroEventLogger(__MOCK_AUTH_TOKEN__)

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
        user_id = 1
        user_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'birthdate': '1965-01-31',
            'phone': '555-555-5555',
        }

        self.logger.add_user(user_id, user_data)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + '/users/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'data': user_data,
                'email': None,
                'id': user_id,
            },
        )

    def test_reidentify_user(self):
        user_id = 1
        new_user_id = 2

        self.logger.reidentify_user(user_id, new_user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/reidentify',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'new_id': new_user_id,
                'id': user_id,
            },
        )

    def test_add_user__with_email(self):
        user_id = 1
        user_email = 'test@example.com'
        user_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'birthdate': '1965-01-31',
            'phone': '555-555-5555',
        }

        self.logger.add_user(user_id, user_data, user_email)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + '/users/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'data': user_data,
                'email': user_email,
                'id': user_id,
            },
        )

    def test_edit_user(self):
        user_id = 1
        user_changes = {
            'first_name': 'Jane',
        }

        self.logger.edit_user(user_id, user_changes)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'changes': user_changes,
                'id': user_id,
            },
        )

    def test_add_tags(self):
        user_id = 1
        user_tags = ['x', 'y']

        self.logger.add_tags(user_id, user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'add': user_tags,
                'id': user_id,
            },
        )

    def test_add_tags__empty_list(self):
        user_id = 1
        user_tags = []

        self.logger.add_tags(user_id, user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'add': [],
                'id': user_id,
            },
        )

    def test_remove_tags(self):
        user_id = 1
        user_tags = ['x', 'y']

        self.logger.remove_tags(user_id, user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'remove': user_tags,
                'id': user_id,
            },
        )

    def test_remove_tags__empty_list(self):
        user_id = 1
        user_tags = []

        self.logger.remove_tags(user_id, user_tags)

        __MOCK_REQUESTS__.assert_called_once_with(
            'PUT',
            __BASE_URL__ + '/users/tags/edit',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'remove': [],
                'id': user_id,
            },
        )

    def test_unsubscribe_user(self):
        user_id = 1

        self.logger.unsubscribe_user(user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'POST',
            __BASE_URL__ + '/users/unsubscribe',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': user_id,
            },
        )

    def test_resubscribe_user(self):
        user_id = 1

        self.logger.resubscribe_user(user_id)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + '/users/resubscribe',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': user_id,
            },
        )

    def test_add_event(self):
        user_id = 1
        event_name = 'track user'
        event_data = {
            'color': 'red',
            'number': 2,
        }

        self.logger.add_event(event_name, event_data, user_id)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + '/events/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'event_name': event_name,
                'data': event_data,
                'identity': {
                    'id': user_id,
                    'email': None,
                },
            },
        )

    def test_add_event__with_email(self):
        user_id = 1
        user_email = 'test@example.com'
        event_name = 'track user'
        event_data = {
            'color': 'red',
            'number': 2,
        }

        self.logger.add_event(event_name, event_data, user_id, user_email)

        __MOCK_REQUESTS__.assert_called_with(
            'POST',
            __BASE_URL__ + '/events/track',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'event_name': event_name,
                'data': event_data,
                'identity': {
                    'id': user_id,
                    'email': user_email,
                },
            },
        )

    def test_delete_user(self):
        user_id = 1

        self.logger.delete_user(user_id)

        __MOCK_REQUESTS__.assert_called_once_with(
            'DELETE',
            __BASE_URL__ + '/users/delete',
            json={
                'auth_token': __MOCK_AUTH_TOKEN__,
                'id': user_id,
            },
        )

    def test_heartbeat(self):
        self.logger.heartbeat()

        __MOCK_REQUESTS__.assert_called_once_with(
            'GET',
            __BASE_URL__ + '/heartbeat',
        )
