import bson
from . import backend

class LightField(object):
    def __init__(self, init=None, required=False, pk=False, unique=False):
        self.required = required
        self.pk = pk
        self.unique = unique
        self.assign(init)
        self.field_name = type(self).__name__

    def val(self):
        return self.value

    def assign(self, val):
        self.value = val
        return val

    def __str__(self):
        return str(self.val())

class LightStr(LightField):
    def __init__(self, init=None, required=False, pk=False, unique=False):
        super(LightStr, self).__init__(init, required, pk, unique)

    def assign(self, val):
        assert(isinstance(val, str))
        super(LightStr, self).assign(val)

class LightInt(LightField):
    def __init__(self, init=None, required=False, pk=False, unique=False):
        super(LightInt, self).__init__(init, required, pk, unique)

    def assign(self, val):
        assert(isinstance(val, int))
        super(LightInt, self).assign(val)

class LightBool(LightField):
    def __init__(self, init=None, required=False, pk=False, unique=False):
        super(LightBool, self).__init__(init, required, pk, unique)

    def assign(self, val):
        assert(isinstance(val, bool))
        super(LightBool, self).assign(val)

# A base type for a document object that, at least, matches the following
# signature:
#
# obj = {
#   "id": ObjectId()
# }
#
class LightDoc(object):
    def __init__(self, **kwargs):
        self.special_fields = ['set_name']
        self.valid = False
        self.set_name = type(self).set_name
        self.data = {}
        self.pk = None

        # Dynamically identify the defined fields from the subclass definition
        db_fields = filter(lambda x: isinstance(getattr(type(self),x),LightField), vars(type(self)))
        for fieldk in db_fields:
            new_field = getattr(type(self), fieldk)
            self.data[fieldk] = new_field.val()
            assert(not(self.pk and new_field.pk))
            self.pk = new_field

        if 'oid' not in kwargs or kwargs['oid'] == None:
            # If instance construction gives us a NoneType oid, then we presume
            # to be constructing a new entitiy, so give it a brand new ObjectId
            self.data['id'] = bson.ObjectId()

            # Also, walk the rest of the args for field initializers
            for fieldk in db_fields:
                if fieldk in kwargs:
                    self.data[fieldk] = type(getattr(self, fieldk))(init=kwargs[fieldk])
                else:
                    self.data[fieldk] = type(getattr(self, fieldk))()

        else:
            # Otherwise, we are to perform a lookup and load of the designated
            # object
            self.load(kwargs['oid'])

    def get_all(set_name, dtype):
        for objid in backend.current_driver.get_all(set_name=set_name):
            yield(dtype(oid=objid))

    def save(self):
        output_data = {}
        for obj_key in self.data:
            output_data[obj_key] = str(self.data[obj_key])
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
