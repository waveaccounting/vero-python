Vero Python
===========

Version 2.0.1
-------------

Released on March 22, 2017

- Removed pinned version from `requests` and `mock` dependencies

Version 2.0.0
-------------

Released on February 29, 2016

Breaking Changes

- Changed ``VeroEndpoints.VERO_BASE_URL`` to ``VeroEndpoints._BASE_URL`` and
  moved the ``api/v2`` path prefix into it to avoid repetition in each endpoint
- Removed deprecated ``development_mode`` parameter. Will throw a ``TypeError``
  for consumers that have this value set. To upgrade, remove the parameter,
  since Vero ignores it anyways.
- Explicitly uses json as content type for payloads (thanks @vibrant)
- Management: removed Travis and BitDeli, added CircleCI and Read the Docs

Version 1.3.0
-------------

Released on September 18, 2015

- Adds support for re-subscribe, delete, and heartbeat endpoints
- Thanks @jlebzelter

Version 1.2.0
-------------

Released on July 7, 2015

- Adds support for Re-identify endpoint
- Thanks @chexton

Version 1.1.4
-------------

Released on June 5, 2015

- Bumped requests library to 2.7.0
- Adds support for Python 3.4

Version 1.1.3
-------------

Released on July 11, 2013

- Updated VERO_BASE_URL
- Thanks @damienbrz
