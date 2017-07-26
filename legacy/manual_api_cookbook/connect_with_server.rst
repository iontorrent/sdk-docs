.. _api-cook:

Connect with Your Torrent Server
================================

To connect to a resource, you first authenticate with the Torrent Server.

	The connection and authentication is currently as simple as logging into the server and providing your username and password.

This page contains these examples:

* :ref:`gen-form`: The general form of authentication using a browser or REST client. You are prompted for your username and password, if they are not provided in the request.
* :ref:`curl-cmd`: The cURL command line form.
* :ref:`pgm`: Programmatic methods using various Python libraries, PHP, and JavaScript.

.. _gen-form:

General form
------------

This is an example of the general form of authentication::

	http://myusername:mypassword@myhost/rundb/api/v1/experiment

.. _curl-cmd:

cURL command
------------

This authentication example uses cURL::

	curl --user myusername:mypassword
     --header "Content-Type: application/json"
     --location 'http://myhost/rundb/api/v1/experiment'

.. _pgm:

Programmatically
----------------

Python libraries
^^^^^^^^^^^^^^^^

A python restful_lib example::

	from restful_lib import Connection
	
	base_url = "http://myhost/rundb/api/v1"
	conn = Connection(base_url,
                  username="myusername", password="mypassword")

A python httplib2 example::

	import httplib2

	h = httplib2.Http()
	h.add_credentials('myusername', 'mypassword')

A python requests example::

	import requests

	result = requests.get('http://myhost/rundb/api/v1?format=json',
                      auth=('myusername', 'mypassword'))

PHP
^^^

A PHP example::

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

JavaScript jQuery AJAX Call
^^^^^^^^^^^^^^^^^^^^^^^^^^^

An AJAX example::

	$.ajax({
		url: "http://myusername:mypassword@myhost/rundb/api/v1/experiment",
		dataType: 'jsonp',
		success: handleResponse(json_results)
	});

