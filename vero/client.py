import json
import collections
import requests

Endpoint = collections.namedtuple('Endpoint', ['method', 'url'])


class VeroEndpoints(object):
    """Endpoints for Vero API calls."""
    VERO_BASE_URL = 'https://api.getvero.com/'
    ADD_USER = Endpoint(method='POST', url=VERO_BASE_URL + 'api/v2/users/track')
    DELETE_USER = Endpoint(method='DELETE', url=VERO_BASE_URL + 'api/v2/users/delete')
    REIDENTIFY_USER = Endpoint(method='PUT', url=VERO_BASE_URL + 'api/v2/users/reidentify')
    EDIT_USER = Endpoint(method='PUT', url=VERO_BASE_URL + 'api/v2/users/edit')
    EDIT_TAGS = Endpoint(method='PUT', url=VERO_BASE_URL + 'api/v2/users/tags/edit')
    RESUBSCRIBE_USER = Endpoint(method='POST', url=VERO_BASE_URL + 'api/v2/users/resubscribe')
    UNSUBSCRIBE_USER = Endpoint(method='POST', url=VERO_BASE_URL + 'api/v2/users/unsubscribe')
    ADD_EVENT = Endpoint(method='POST', url=VERO_BASE_URL + 'api/v2/events/track')
    HEARTBEAT = Endpoint(method='GET', url=VERO_BASE_URL + 'api/v2/heartbeat')


class VeroEventLogger(object):
    """Add and edit Vero events and users."""

    @classmethod
    def _fire_request(cls, endpoint, payload):
        json_payload = json.dumps(payload)
        return requests.request(endpoint.method, endpoint.url, data=json_payload)

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def add_user(self, user_id, user_data, user_email=None, development_mode=False):
        """Add a new user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'email': user_email,
            'data': user_data,
            'development_mode': development_mode
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

    def edit_user(self, user_id, user_changes, development_mode=False):
        """Edit an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'changes': user_changes,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.EDIT_USER, payload)

    def add_tags(self, user_id, tag_list, development_mode=False):
        """Add a list of tags for an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'add': tag_list,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.EDIT_TAGS, payload)

    def remove_tags(self, user_id, tag_list, development_mode=False):
        """Remove a list of tags for an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'remove': tag_list,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.EDIT_TAGS, payload)

    def unsubscribe_user(self, user_id, development_mode=False):
        """Unsubscribe an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.UNSUBSCRIBE_USER, payload)

    def resubscribe_user(self, user_id, development_mode=False):
        """Resubscribe an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.RESUBSCRIBE_USER, payload)

    def add_event(self, event_name, event_data, user_id, user_email=None, development_mode=False):
        """Add a new event and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'event_name': event_name,
            'identity': {
                'id': user_id,
                'email': user_email
            },
            'data': event_data,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.ADD_EVENT, payload)

    def delete_user(self, user_id, development_mode=False):
        """Delete an existing user and return the https request."""
        payload = {
            'auth_token': self.auth_token,
            'id': user_id,
            'development_mode': development_mode
        }
        return self._fire_request(VeroEndpoints.DELETE_USER, payload)

    def heartbeat(self):
        """Check -- is the endpoint up?"""
        endpoint = VeroEndpoints.HEARTBEAT
        resp = requests.request(endpoint.method, endpoint.url)
        return resp.status_code == requests.codes.ok
