import falcon

def _test_resource_get(req=None, res=None):
    """Handle Test Resource GET requests."""
    res.status = falcon.HTTP_200
    res.body = ('This is me, Falcon, serving a resource!')
