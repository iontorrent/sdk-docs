Update Experiment Notes
=========================

So far, all of the examples have involved getting data from the server. This example shows you how to modify resource data by sending a PUT request to add a note to an experiment.

Get the current notes
---------------------

First, see what is currently stored for the experiment with id=3:

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment/3/'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

Among other data, the response data shows there are no notes in the notes field of experiment 3:

.. code-block:: none

		.
		.
		.
	"notes": "",
		.
		.
		.

Add a Note
----------

Construct a JSON notes string, using the json library dumps method.

.. code-block:: python

	metaData = json.dumps({ "notes" : "This is a sample note." })

For PUT and POST reqeusts, data are passed in the message body instead of as a parameter. Set the message body to the notes JSON string created, above.

Also, the JSON data format must be specified in the message header, using the form: 'content-type':'application/json'.

.. code-block:: python

	putResp = requests.put('%s/experiment/3/'%base_url,
							data=metaData,
							headers={'content-type':'application/json'},
							auth=('myusername', 'mypassword'))

Now send a GET request for the same experiment to verify that the text was added to the notes field:

.. code-block:: python

	resp = requests.get('%s/experiment/3/'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

Typically, you would also test the response status code to verify the action was performed successfully:

.. code-block:: python

	resp.status_code

The notes field now contains the string sent with the PUT request:

.. code-block:: none

		.
		.
		.
	"notes": "This is a sample note.",
		.
		.
		.
