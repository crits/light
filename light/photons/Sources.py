import falcon

resources = ["SourceAccess","SourceAccessList"]

class SourceAccessList(object):
    def routes_set(self, app):
        app.add_route('/source_access', self)

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = ('Testing source access gets.')

class SourceAccess(object):
    def routes_set(self, app):
        app.add_route('/source_access/{source}', self)

    def on_get(self, req, res, source):
        res.status = falcon.HTTP_200
        res.body = ('Testing source access gets, getting item {source}.'.format(source=source))
