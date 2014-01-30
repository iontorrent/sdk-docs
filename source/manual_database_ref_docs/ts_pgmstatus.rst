Work with PGM™ or Proton™ Status
================================

The ``rig`` resource API has a unique syntax that permits you to update individual fields. All other resources require that you provide all fields when updating the resource.

By using the status keyword, following the key or sequencer name in the URI, you can update the following ``rig`` resource fields, individually:

	* state
	* last_init_date
	* last_clean_date
	* last_experiment
	* version
	* alarms

General form of the rig status request
--------------------------------------

.. code-block:: none

	http://myhost/rundb/api/v1/PGM_test/status?format=json

When you update rig status, you can provide either one or all of the status items as data in the request body.

A rig status update example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example formats a status request, updating all of the status fields, and displays the results.

In the example, a simple cURL or REST client request to GET the PGM_test resource element returns the following results:

.. code-block:: none

	http://myhost/rundb/api/v1/rig/PGM_test?format=json
	
	{"alarms": {}, "comments": "", "ftppassword": "ionguest",
	"ftprootdir": "results", "ftpserver": "192.168.201.1",
	"ftpusername": "anonymous", "last_clean_date": "", "last_experiment": "",
	"last_init_date": "", "location": {"comments": "", "id": "1", 
	"name": "Home", "resource_uri": "/rundb/api/v1/location/1/"},
	"name": "PGM_test", "resource_uri": "/rundb/api/v1/rig/PGM_test/",
	"state": "", "updateflag": false, "updatehome": "192.168.201.1",
	"version": {}}

You can refine the GET request to only retrieve the status fields, returning the following result:

.. code-block:: none

	http://myhost/rundb/api/v1/rig/PGM_test/status?format=json
	
	{"alarms": {}, "last_clean_date": "", "last_experiment": "",
	"last_init_date": "", "state": "", "version": {}}

You can see in this example that all of the field values are empty.

The programming example to update these fields uses the requests and simplejson Python libraries:

.. code-block:: python

	import requests
	import simplejson as json

A local status variable is initialized to assign a value to each of the status fields:

.. code-block:: python

	status = {}

	status["last_init_date"] = "rig.last_init_date"
	status["state"] = "rig.state"
	status["last_clean_date"] = "rig.last_clean_date"
	status["last_experiment"] = "rig.last_experiment"
	status["version"] = {"version":"test"}
	status["alarms"] = {"rig.alarms":"test"}

And the Python status object is encoded into a JSON string:

.. code-block:: python

	pdata = json.dumps(status)
	print pdata

The program displays the JSON string to be sent to the server in the request body:

.. code-block:: none

	{"last_clean_date": "rig.last_clean_date",
	"last_experiment": "rig.last_experiment",
	"state": "rig.state", "version": {"version": "test"}, 
	"last_init_date": "just this", "alarms": {"rig.alarms": "test"}}

Now, send the PUT request to the server to update the status fields, providing the JSON string as data:

.. code-block:: python

	status = requests.put('http://myhost/rundb/api/v1/rig/PGM_test/status/',
				data=pdata,
				headers={'content-type':'application/json'},
				auth=('myusername', 'mypassword'))
	print status

The server returns an HTTP status code of 204, indicating a successful PUT request.

To verify that the status fields have been updated, a GET request is sent, and the response is displayed:

.. code-block:: python

	resp1 = requests.get('http://myhost/rundb/api/v1/rig/PGM_test/status/',
				auth=('myusername', 'mypassword'))
	print resp1.content

You can see the status fields now contain the data sent with the PUT request:

.. code-block:: none

	{"alarms": {"rig.alarms": "test"}, "last_clean_date": "rig.last_clean_date",
	"last_experiment": "rig.last_experiment",
	"last_init_date": "rig.last_init_date", "state": rig.state",
	"version": {"version": "test"}}
