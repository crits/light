import falcon
import pkgutil
import sys

from .api import _test_resource_get

class TestResource(object):
    def on_get(self, req, res):
        """Handles all GET requests."""
        _test_resource_get(req, res)

def route_framework(app):
    # Instantiate the TestResource class
    test_resource = TestResource()

    # Dynamically find modules
    # Adapted from: https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
    for importer, pkgname, ispkg in pkgutil.walk_packages(['./light/photons']):
        # Build the "full package name" by joining the modules dir name
        # with the module file name (minus .py)
        full_pkg_name = 'photons.{pkgname}'.format(pkgname=pkgname)

        # Want to make sure we haven't already loaded this module, this tests that
        if full_pkg_name not in sys.modules:
            module = importer.find_module(full_pkg_name).load_module(full_pkg_name)

            # Each module contains a variable named 'resources' that is a list of
            # strings naming classes that are to be integrated as Falcon resources.
            # Each of these *must* have a function routes_set(app) defined, and the
            # requisite routing code belongs there.
            for class_name in module.resources:
                # Connect the class object to a variable
                cobj = getattr(module, class_name)

                # Then we can instantiate an instance of the class
                cinst = cobj()

                # And finally, set up routing by calling the method I defined earlier.
                # TODO: Maybe this could be a class function? TBD.
                cinst.routes_set(app)

    # Add a route to serve the resource
    app.add_route('/test', test_resource)
