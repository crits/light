import falcon
import json
from bson import ObjectId
from light.light_types import LightDoc

resources = ["SourceSet","SourceItem"]

# A very simple entity schema that's built on top of the LightDoc and
# contains the following additional fields:
#
# obj = {
#    .....
#    'active': boolean,
#    'source_name': string
#}
#
class Source(LightDoc):
    set_name = 'sources'
    def __init__(self, source_name=None, active=True, oid=None):
        super(Source, self).__init__(oid=oid)

        if oid == None:
            # If oid is None, presume we're creating a new Source object
            #
            # Populate Source-specific attributes, not in LightDoc
            self.data['active'] = active
            self.data['source_name'] = source_name

            # If we are initialized with a proper source_name, then
            # set 'valid' to True
            if self.data['source_name'] != None:
                self.valid = True

    def get_all():
        for source_obj in LightDoc.get_all(Source.set_name, Source):
            yield source_obj

    def json(self):
        output_json = self.data
        output_json['id'] = str(output_json['id'])
        return output_json

    def load(self, oid):
        # First, load the content from disk into the JSON structure. This will
        # only perform a data-conversion on the 'id' (str -> ObjectId)
        super(Source, self).load(oid)

        # XXX: It is up to you to perform any remaining data conversions to the
        # fields managed by *this* class, here, after the initial load. Remember,
        # set self.valid to False if the data loaded fails any validation, as the
        # superclass load() function will have set it to True
        #
        # This could include loading data from within separate collections/tables/sets
        # which represent sub-documents of this data, and which are represented as
        # foreign keys within the core object's data fields.
        #

class SourceSet(object):
    def routes_set(self, app):
        app.add_route('/sources', self)

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps(list(x.json() for x in Source.get_all()))

    def on_post(self, req, res):
        if req.content_length > 0:
            json_input = json.load(req.stream)
            if 'active' in json_input and 'source_name' in json_input:
                src_obj = Source(json_input['source_name'], json_input['active'])
                src_obj.save()
                res.body = json.dumps({'success': True, 'oid': src_obj.json()['id']})
            else:
                res.status = 500
        else:
            res.status = 500

class SourceItem(object):
    def routes_set(self, app):
        app.add_route('/sources/{source}', self)

    def on_get(self, req, res, source):
        src_obj = Source(oid=source)
        if src_obj.valid:
            res.status = falcon.HTTP_200
            res.body = json.dumps(src_obj.json())
        else:
            res.status = falcon.HTTP_500
            res.body = json.dumps({'success': False, 'message': 'Unable to find source with id {objid}'.format(objid=source)})
