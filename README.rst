vero: Python client for Vero
============================

.. image:: https://circleci.com/gh/waveaccounting/vero-python.svg?style=svg
   :target: https://circleci.com/gh/waveaccounting/vero-python
   :alt: Circle CI

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest
   :target: https://vero.readthedocs.org/en/latest/
   :alt: Read the Docs

Full documentation can be found on `ReadTheDocs <https://vero.readthedocs.org/en/latest/>`_

Vero is an API wrapper for event logging in your Python application.
Fetch your auth token from your `Vero <http://getvero.com>`_ account and use the python interface instead of `API <http://github.com/getvero/vero-api>`_ web hooks.
::

    >>> from vero import VeroEventLogger
    >>> logger = VeroEventLogger(auth_token)
    >>> user_id = 42
    >>> user_data = {
            'full_name': 'Jane Doe'
        }
    >>> response = logger.add_user(user_id, user_data)
    >>> response.status_code
    200

Features
--------

Modify user data and log events. Run in live or test mode.

- Add user
- Delete user
- Edit user
- Add user tags
- Remove user tags
- Unsubscribe user
- Resubscribe user
- Add event
- Check heartbeat

Installation
------------
Install the package from PyPI
::

  pip install vero

Run Tests
------------
Run Tests from command line.
::

   VERO_AUTH_TOKEN=[ Your Token here ] python setup.py test

Usage
-----

Create instance
~~~~~~~~~~~~~~~
Use the authorization token from your Vero account page to create a VeroEventLogger object.
::

    >>> from vero import VeroEventLogger
    >>> auth_token = "foobar"
    >>> logger = VeroEventLogger(auth_token)

After creating an instance of VeroEventLogger as ``logger`` use any of the following methods to access Vero.

Add user
~~~~~~~~
Create a new user with the information in ``user_data``. ``user_email`` is optional but is needed to trigger emails to the user.
::

    >>> user_id = 1
    >>> user_email = 'johndoe@example.com'
    >>> user_data = {
            'first name': 'John',
            'last name': 'Doe'
        }
    >>> logger.add_user(user_id, user_data, user_email=user_email)

Edit user
~~~~~~~~~
Add or change fields in ``user_data`` for the user.
::

    >>> user_id = 1
    >>> user_data = {
            'first name': 'Jane'
        }
    >>> logger.edit_user(user_id, user_data)

Add user tags
~~~~~~~~~~~~~
Add each tag in ``tag_list`` to the user.
::

    >>> user_id = 1
    >>> tag_list = ['blue', 'red', 'yellow']
    >>> logger.add_tags(user_id, tag_list)

Remove user tags
~~~~~~~~~~~~~~~~
Remove each tag in ``tag_list`` from the user.
::

    >>> user_id = 1
    >>> tag_list = ['yellow']
    >>> logger.remove_tags(user_id, tag_list)

Unsubscribe user
~~~~~~~~~~~~~~~~
Unsubscribe the user from triggering future events.
::

    >>> user_id = 1
    >>> logger.unsubscribe_user(user_id)

Resubscribe user
~~~~~~~~~~~~~~~~
Resubscribe the user to allow triggering future events.
::

    >>> user_id = 1
    >>> logger.resubscribe_user(user_id)

Add event
~~~~~~~~~
Note: adding an event with a user id that doesn't exist will create the user.

Event data can contain whatever fields are needed.
::

    >>> user_id = 2
    >>> user_email = 'janedoe@example.com'
    >>> event_name = 'Visited Website'
    >>> event_data = {
            'date': 'today',
            'visited': 'front page'
        }
    >>> logger.add_event(event_name, event_data, user_id, user_email=user_email)

Re-identify a user
~~~~~~~~~~~~~
Change a user's ``identifier`` (or ID) in Vero. This method accept their current (old) ``identifier`` and the ``identifier`` to replace it.
::

    >>> user_id = 1
    >>> new_user_id = 2 
    >>> logger.reidentify_user(user_id, new_user_id)

Delete user
~~~~~~~~~~~~~~~~
Delete the user
::

    >>> user_id = 1
    >>> logger.delete_user(user_id)
