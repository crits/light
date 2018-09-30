import os
import json
import bson

# A simple driver that uses a directory structure to manage
# data objects as discrete text files containing JSON data

class disk_driver(object):
    def __init__(self, root_dir='.'):
        self.root = root_dir

        # If they provided the trailing slash, remove it
        # for consistency
        if self.root[-1] == '/':
            self.root = self.root[:-1]

        if not os.access('{root}'.format(root=self.root), os.W_OK):
            os.mkdir(path='{root}'.format(root=self.root), mode=0o755)

    # Indiscriminantly write the object back to disk. Overwrite any existing instance.
    def store(self, set_name, obj):
        if not os.access('{root}/{set_name}'.format(root=self.root, set_name=set_name), os.W_OK):
            os.mkdir(path='{root}/{set_name}'.format(root=self.root, set_name=set_name), mode=0o755)
        with open('{root}/{set_name}/{objid}.json'.format(root=self.root, set_name=set_name,
                                                          objid=obj['id']), 'w') as objfh:
            json.dump(obj, objfh)

    # Given a set_name and objid, load the object identified by that objid. If it isn't present,
    # return None
    def load(self, set_name, objid):
        if os.access('{root}/{set_name}/{objid}.json'.format(root=self.root, set_name=set_name,
                                                             objid=str(objid)), os.R_OK):
            with open('{root}/{set_name}/{objid}.json'.format(root=self.root, set_name=set_name,
                                                              objid=str(objid)), 'r') as objfh:
                obj = json.load(objfh)
                return obj

            return None

    # Fetch all entities from a given set (given by set_name)
    def get_all(self, set_name):
        if not os.access('{root}/{set_name}'.format(root=self.root, set_name=set_name), os.W_OK):
            return

        with os.scandir('{root}/{set_name}'.format(root=self.root, set_name=set_name)) as dir_handle:
            for d_ent in dir_handle:
                if not d_ent.name.startswith('.') and d_ent.is_file():
                    # Yields only the ObjectId portion of the name, wraps it in an ObjectId
                    yield bson.ObjectId(d_ent.name.split('.')[0])
