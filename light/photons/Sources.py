import falcon

resources = ["SourceSet","SourceItem"]

class SourceSet(object):
    def routes_set(self, app):
        app.add_route('/sources', self)

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = ('Testing source access gets.')

class SourceItem(object):
    def routes_set(self, app):
        app.add_route('/sources/{source}', self)

    def on_get(self, req, res, source):
        res.status = falcon.HTTP_200
        res.body = ('Testing source access gets, getting item {source}.'.format(source=source))
