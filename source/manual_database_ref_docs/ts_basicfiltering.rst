Basic Filters
=============

Topics on this page:

* :ref:`Getting_resource_schema_and_filter_list`
* :ref:`Selecting_by_filter_value`
* :ref:`Specifying_multiple_filters`
* :ref:`Non-matching_filter_response`

.. _Getting_resource_schema_and_filter_list:

Get the resource schema and filter list
---------------------------------------

When you request the resource schema, the response includes a filtering field, which is a dictionary of fields you can filter on.

Filters are used in subsequent requests by adding the filter as a request parameter and assigning the filter a value, and possibly a value qualifier. All elements that match the filter criteria are returned for the request.

General form of a schema request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/location/schema?format=json

Python implementation
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/location/schema?format=json'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

Schema request response
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
		"default_format": "application/json",
		"fields": {
		"comments": {
					"help_text": "Unicode string data. Ex: \"Hello World\"",
					"nullable": false,
					"readonly": false,
					"type": "string"
				},
		"id": {
					"help_text": "Unicode string data. Ex: \"Hello World\"",
					"nullable": false,
					"readonly": false,
					"type": "string"
				},
		"name": {
					"help_text": "Unicode string data. Ex: \"Hello World\"",
					"nullable": false,
					"readonly": false,
					"type": "string"
				},
		"resource_uri": {
					"help_text": "Unicode string data. Ex: \"Hello World\"",
					"nullable": false,
					"readonly": true,
					"type": "string"
				}
		},
		"filtering": {
				"backupconfig": 2,
				"comments": 2,
				"cruncher": 2,
				"fileserver": 2,
				"id": 2,
				"name": 2,
				"rig": 2
			},
		"ordering": \[
		"backupconfig",
		"comments",
		"cruncher",
		"fileserver",
		"id",
		"name",
		"rig"
		\]
	}

.. _Selecting_by_filter_value:

Select by filter value
----------------------

The location resource is used here as an example, where location contains two elements:

.. code-block:: javascript

	"objects": [
	{
		"comments": "",
		"id": "1",
		"name": "Home",
	"resource_uri": "/rundb/api/v1/location/1/"
	},
	{
		"comments": "Test comment.",
		"id": "2",
		"name": "testDir",
		"resource_uri": "/rundb/api/v1/location/2/"
	}
	]

Using the name field, a valid filter according to the schema, a request is made to get all elements matching the value (Home) assigned to the name parameter. Only one element is expected to match.

General form of a URI with a filter parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/location?format=json&name=Home

Python implementation of a request with a filter parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests

	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/location?formatjson&name=Home'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

Only one location element is returned, having a name field with a value of Home:

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 1
		},
		"objects": [
			{
				"comments": "",
				"id": "1",
				"name": "Home",
				"resource_uri": "/rundb/api/v1/location/1/"
			}
		]
	}

.. _Specifying_multiple_filters:

Specify multiple filters
------------------------

You can use more than one filter to select resource elements by using multiple request parameters.

General form to specify multiple filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&cycles=0&rawdatastyle=single

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&cycles=0&rawdatastyle=single'%base_url, 
		auth=('myusername', 'mypassword'))
	resp_json = resp.json()

The request to return only those elements whose cycles are 0 and whose rawdatastyle is single returns a single element:

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 1
		},
		...
	}

.. _Non-matching_filter_response:

Non-matching filter response
----------------------------

Where no resource elements match your filter criteria, an empty object list is returned.

For multiple filters, all filters must match.

The following example is similar to the previous one, except that the comments fiilter is assigned a value of Test.

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/location?format=json&name=Nothing could possibly have this name'%base_url, 
		auth=('myusername', 'mypassword'))
	resp_json = resp.json()

No elements match both filter values so no elements are returned for the request, confirmed by "total_count": 0.

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 0
		},
		"objects": [ ]
	}
