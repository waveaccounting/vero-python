import collections
import requests

Endpoint = collections.namedtuple('Endpoint', ['method', 'url'])


class VeroEndpoints(object):
    """Endpoints for Vero API calls."""
    _BASE_URL = 'https://api.getvero.com/api/v2'

    ADD_USER = Endpoint('POST', _BASE_URL + '/users/track')
    DELETE_USER = Endpoint('DELETE', _BASE_URL + '/users/delete')
    REIDENTIFY_USER = Endpoint('PUT', _BASE_URL + '/users/reidentify')
    EDIT_USER = Endpoint('PUT', _BASE_URL + '/users/edit')
    EDIT_TAGS = Endpoint('PUT', _BASE_URL + '/users/tags/edit')
    RESUBSCRIBE_USER = Endpoint('POST', _BASE_URL + '/users/resubscribe')
    UNSUBSCRIBE_USER = Endpoint('POST', _BASE_URL + '/users/unsubscribe')
    ADD_EVENT = Endpoint('POST', _BASE_URL + '/events/track')
    HEARTBEAT = Endpoint('GET', _BASE_URL + '/heartbeat')


class VeroEventLogger(object):
    """Add and edit Vero events and users."""

    @classmethod
    def _fire_request(cls, endpoint, payload):
        return requests.request(endpoint.method, endpoint.url, json=payload)

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def add_user(self, user_id, user_data, user_email=None):
        """Add a new user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'email': user_email,
            'data': user_data,
        }
        return self._fire_request(VeroEndpoints.ADD_USER, payload)

    def reidentify_user(self, user_id, new_user_id):
        """Reidentify (alias) a new user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'new_id': new_user_id
        }
        return self._fire_request(VeroEndpoints.REIDENTIFY_USER, payload)

    def edit_user(self, user_id, user_changes):
        """Edit an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'changes': user_changes,
        }
        return self._fire_request(VeroEndpoints.EDIT_USER, payload)

    def add_tags(self, user_id, tag_list):
        """Add a list of tags for an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'add': tag_list,
        }
        return self._fire_request(VeroEndpoints.EDIT_TAGS, payload)

    def remove_tags(self, user_id, tag_list):
        """Remove a list of tags for an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'remove': tag_list,
        }
        return self._fire_request(VeroEndpoints.EDIT_TAGS, payload)

    def unsubscribe_user(self, user_id):
        """Unsubscribe an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
        }
        return self._fire_request(VeroEndpoints.UNSUBSCRIBE_USER, payload)

    def resubscribe_user(self, user_id):
        """Resubscribe an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
        }
        return self._fire_request(VeroEndpoints.RESUBSCRIBE_USER, payload)

    def add_event(self, event_name, event_data, user_id, user_email=None):
        """Add a new event and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'event_name': event_name,
            'identity': {
                'id': user_id,
                'email': user_email
            },
            'data': event_data,
        }
        return self._fire_request(VeroEndpoints.ADD_EVENT, payload)

    def delete_user(self, user_id):
        """Delete an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
        }
        return self._fire_request(VeroEndpoints.DELETE_USER, payload)

    def heartbeat(self):
        """Check -- is the endpoint up?"""
        endpoint = VeroEndpoints.HEARTBEAT
        resp = requests.request(endpoint.method, endpoint.url)
        return resp.status_code == requests.codes.ok
