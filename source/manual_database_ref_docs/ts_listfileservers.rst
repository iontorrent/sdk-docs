List File Servers
=================

This example accesses the fileserver resource to find all file server directories.

This example demonstrates the use of the ``httplib2`` Python REST library:

.. code-block:: python

	import httplib2
	import json

On the first request, perform authentication:

.. code-block:: python

	h = httplib2.Http(".cache")
	h.add_credentials('myusername', 'mypassword')

Request all fileserver elements using the GET method:

.. code-block:: python

	resp, content = h.request("http://localhost/rundb/api/v1/fileserver?format=json", "GET")

Parse the JSON string response into Python objects:

.. code-block:: python

	contentdict = json.loads(content)

Loop through each object in the list and display the directory name:

.. code-block:: python

	objects = contentdict['objects']

	for obj in objects:
		print obj['filesPrefix']
