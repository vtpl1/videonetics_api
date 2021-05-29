# Authentication and authorization


All endpoints require authentication.

## Token


The ``Authorization`` HTTP header can be specified with ``Token {{api.token}}``
to authenticate as a user of the [Videonetics API](/).


## Session


!!! warning
    Authentication via session is not enabled yet.
    When a user is trying to authenticate via session, CSRF check is performed.
    *[CSRF]: Cross-site request forgery

