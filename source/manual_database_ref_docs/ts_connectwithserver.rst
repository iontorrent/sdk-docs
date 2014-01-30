Connect with the Server
=======================

To connect to a resource, you first authenticate with the server.

Topics on this page:

* :ref:`General_form`
* :ref:`cURL_command`
* :ref:`Programatically`

The connection and authentication is currently as simple as logging into the server and providing your username and password.

The following examples show:

* The general form of authentication using a browser or REST client. You are prompted for your username and password, if they are not provided in the request.

* The cURL command line form.

* Programmatic methods using various Python libraries, PHP, and JavaScript.

.. _General_form:

General form
------------

.. code-block:: none

	http://myusername:mypassword@myhost/rundb/api/v1/experiment

.. _cURL_command:

``cURL`` command
----------------

.. code-block:: none

	curl --user mysername:mypassword
	     --header "Content-Type: application/json"
	     --location 'http://myhost/rundb/api/v1/experiment'

.. _Programatically:

Programatically
---------------

Python libraries
^^^^^^^^^^^^^^^^

*restful_lib*

	NOTE: restful_lib has not been updated in over 5 years and is considered deprecated.

.. code-block:: python

	from restful_lib import Connection
	base_url = 'http://myhost/rundb/api/v1'
	conn = Connection(base_url, username="myusername", password="mypassword")

*httplib2*

.. code-block:: python

	import httplib2
	h = httplib2.Http()
	h.add_credentials('myusername', 'mypassword')

*requests (recommended)*

.. code-block:: python

	import requests
	resp = requests.get('http://myhost/rundb/api/v1?format=json', auth=('myusername', 'mypassword'))

PHP
^^^

.. code-block:: php

	<?php
	$context = stream_context_create(array(
	'http' => array(
	'header'  =>
	    "Authorization: Basic " . base64_encode("myusername:mypassword")
	)
	));

	$url = "http://myhost/rundb/api/v1?format=json";
	$feed = file_get_contents($url, false, $context);
	?>

JavaScript jQuery AJAX call
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	$.ajax({
	    url: "http://myusername:mypassword@myhost/rundb/api/v1/experiment",
	    dataType: 'jsonp',
	    success: handleResponse(json_results)
	});
