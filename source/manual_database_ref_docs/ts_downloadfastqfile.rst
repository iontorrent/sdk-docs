Download a FASTQ File
=====================

This example shows the REST API facilities for working with the file system.

Making the following request on the results resource,

.. code-block:: none

	http://myhost/rundb/api/v1/results/13?format=json

shows the path of the associated FASTQ file. The database schema includes a number of file path entries, which can all be accessed in the same way.

.. code-block:: javascript

	{
			 .
			 .
			 .
		"fastqLink": "/output/Home/Auto_B15-45_4_013/R_2010_11 ... B15-45_Au…",
			 .
			 .
			 .
	}

You can get the file contents by copying the path to the URI, following the host name.

.. code-block:: none

	http://myhost/output/Home/Auto_B15-45_4_013/R_2010_11 ... B15-45_4.fastq

The entire sequence is shown in the following programming example.

The GET request on the results resource returns the FASTQ file path in the fastqLink field.

.. code-block:: python

	import requests
	import simplejson as json
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/results/13?format=json'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

To GET the file contents, append the fastqLink value to the URI, following the host name.

.. code-block:: python

	resp = requests.get('http://myhost/%s'%resp_json['fastqLink'], auth=('myusername', 'mypassword'))

Display the FASTQ file path and the contents of the file.

.. code-block:: python

	print resp_json['fastqlink']
	print resp.content
