import falcon

from .api import _test_resource_get

class TestResource(object):
    def on_get(self, req, res):
        """Handles all GET requests."""
        _test_resource_get(req, res)


def route_framework(app):
    # Instantiate the TestResource class
    test_resource = TestResource()

    # Add a route to serve the resource
    app.add_route('/test', test_resource)
