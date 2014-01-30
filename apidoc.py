# Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved

"""
A simple program that will be used to output annotation for the api docs

It is best to run this outside of the venv, or you might get import errors

"""

import os
import json
import pickle

os.environ['DJANGO_SETTINGS_MODULE'] = "iondb.settings"

from iondb.rundb import api
from iondb.rundb import urls

#the registry is way better
v1 = urls.v1_api
registry = v1._registry
wrap = {}

notes = open("notes_from_source.json","w+")

for key, value in registry.iteritems():
	print key , getattr(value,"__class__")
        wrap[key] = pickle.dumps(value)

notes.write(json.dumps(wrap))

notes.close()


