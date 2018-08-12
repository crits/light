import bson
from . import backend

# A base type for a document object that, at least, matches the following
# signature:
#
# obj = {
#   "id": ObjectId()
# }
#
class LightDoc(object):
    def __init__(self, set_name, oid=None):
        self.valid = False
        self.set_name = set_name

        if oid == None:
            # If instance construction gives us a NoneType oid, then we presume
            # to be constructing a new entitiy, so give it a brand new ObjectId
            self.data = {'id': bson.ObjectId()}
        else:
            # Otherwise, we are to perform a lookup and load of the designated
            # object
            self.load(oid)

    def get_all(set_name, dtype):
        for objid in backend.current_driver.get_all(set_name=set_name):
            yield(dtype(oid=objid))

    def save(self):
        output_data = {}
        for obj_key in self.data:
            if isinstance(self.data[obj_key], bson.ObjectId):
                output_data[obj_key] = str(self.data[obj_key])
            else:
                output_data[obj_key] = self.data[obj_key]
        backend.current_driver.store(self.set_name, output_data)

    def load(self, objid):
        input_data = backend.current_driver.load(self.set_name, objid)

        # Clear the instance data
        self.data = {}

        if input_data:
            for obj_key in input_data:
                if obj_key == 'id':
                    self.data[obj_key] = bson.ObjectId(input_data[obj_key])
                else:
                    self.data[obj_key] = input_data[obj_key]
            self.valid = True
        else:
            # Invalidate if the object doesn't exist
            self.valid = False
