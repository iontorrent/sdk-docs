Add a PGM™ or Proton™ Sequencer
===============================

Topics on this page:

* :ref:`view-rig-rsrc`
* :ref:`analyze-rig-schema`
* :ref:`add-rig-element`
* :ref:`view-result`

In the previous example, you modified the notes field of an experiment element. In this example, you add an element to the rig resource, which is another name for the PGM™ or Proton™ Sequencer. This example also includes the added complexity of updating a resource that includes a link to another resource.

.. _view-rig-rsrc:

View the rig resource before adding an element
----------------------------------------------

First, use the ``cURL`` command line program or your REST client to view the rigs defined for your system. Using these tools is a convenient way to view the database while developing and debugging your program. For example:

.. code-block:: none

	http://myhost/rundb/api/v1/rig?format=json

This rig resource contains three PGM™ Sequencers:

.. code-block:: javascript

	{
	"meta": {
				   .
				   .
				   .
			"total_count": 3
		},
	"objects": [
	{
					   .
					   .
					   .
				"name": "B6",
				"resource_uri": "/rundb/api/v1/rig/B6/",
				"updateflag": false,
				"updatehome": "ts"
			},
	{
					   .
					   .
					   .
				"name": "default",
				"resource_uri": "/rundb/api/v1/rig/default/",
				"updateflag": false,
				"updatehome": "ts"
			},
	{
					   .
					   .
					   .
				"name": "PGM_test",
				"resource_uri": "/rundb/api/v1/rig/PGM_test/",
				"updateflag": false,
				"updatehome": "ts"
			},
	]
	}

.. _analyze-rig-schema:

Analyze the rig schema
----------------------

The following example shows the JSON structure of a rig:

.. code-block:: javascript

	{
		"comments": "",
		"ftppassword": "ionguest",
		"ftpserver": "ts",
		"ftpusername": "ionguest",
		"location": {"comments": "", "id": "1", "name": "Home"},
		"name": "PGM_test",
		"updateflag": false,
		"updatehome": "ts"
	}

What makes this more interesting is that the structure includes a nested dictionary for the location field, with the location schema.

When creating or modifying the rig structure, you also need to provide the location structure, either an existing location or by adding a location resource to the database before adding a rig.

In the programming example, a copy of one of the existing rigs is used but the example shows how to reference a nested dictionary.

.. _add-rig-element:

Add a ``rig`` element
---------------------

Because the intention is to copy an existing rig data structure, modifying the desired fields, a GET request is sent to get the ``rig`` element ``PGM_test``, to be copied.

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/rig/PGM_test?format=json'%base_url, auth=('myusername', 'mypassword'))

The JSON data structure of the existing rig is returned in the resp variable. Use the .json() method to get a Python json object that can be manipulated as needed.

.. code-block:: python

	resp_json = resp.json()

Only the program name field is changed in the copied rig data. It is changed from ``PGM_test`` to ``myNewPgm``.

Remember that, for almost all resources, all fields must be included in the JSON string when making a PUT or POST request, not only the field you modified. An exception is the ``resource_uri`` field contained in all resources. The ``resource_uri`` field is removed in the example using the simplejson pop method.

This example demonstrates the added complication of also removing the ``resource_uri`` field from the nested location data structure, showing how to access nested data in the process.

.. code-block:: python

	resp_json.update(name='myNewPgm')
	resp_json.pop('resource_uri')
	resp_json['location'].pop('resource_uri')

Use the json dumps method to encode the Python object into a json string.

.. code-block:: python

	pdata = json.dumps(resp_json)

Use the PUT request to add the new PGM™ or Proton™ Sequencer to the database, passing the URI and message body, pdata, of the new element as parameters. You must also provide the message header and specify the content data type: {'content-type':'application/json'}.

.. code-block:: python

	status = requests.put('%s/rig/myNewPgm/'%base_url, data=pdata, headers={'content-type':'application/json'}, auth=('myusername', 'mypassword'))

.. _view-result:
	
View the result
---------------

If you again use cURL or a REST client to view the ``rig`` resource, you can see that a PGM™ or Proton™ Sequencer named ``myNewPgm`` is added:

.. code-block:: javascript

	{
	"meta": {
				   .
				   .
				   .
			"total_count": 4
		},
	"objects": [
	{
					   .
					   .
					   .
				"name": "B6",
				"resource_uri": "/rundb/api/v1/rig/B6/",
				"updateflag": false,
				"updatehome": "ts"
			},
	{
					   .
					   .
					   .
				"name": "default",
				"resource_uri": "/rundb/api/v1/rig/default/",
				"updateflag": false,
				"updatehome": "ts"
			},
	{
					   .
					   .
					   .
				"name": "PGM_test",
				"resource_uri": "/rundb/api/v1/rig/PGM_test/",
				"updateflag": false,
				"updatehome": "ts"
			},{
					   .
					   .
					   .
				"name": "myNewPgm",
				"resource_uri": "/rundb/api/v1/rig/myNewPgm/",
				"updateflag": false,
				"updatehome": "ts"
			}
	]
	}
