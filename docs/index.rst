vero-python: Python client for Vero
===================================

vero-python makes it easy to send events to Vero:

::

    >>> from vero import VeroEventLogger
    >>> logger = VeroEventLogger(auth_token)
    >>> user_id = 42
    >>> user_data = {
            'full_name': 'Jane Doe',
            'height': 72,
            'weight': 108,
            'address': {
                'street_name': 'Cherry St.',
                'street_number': 13,
            },
        }
    >>> response = logger.add_user(user_id, user_data)
    >>> response.status_code
    >>> 200

User Guide
-----------

This part of the documentation explains how to use vero-python as a developer.

.. toctree::
   :maxdepth: 2

   user/install.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

