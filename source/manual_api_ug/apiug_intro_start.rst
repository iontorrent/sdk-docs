Get started
===========

This section introduces you to the Torrent Suite REST API by giving a simple example of the basic request-response interaction between client and server. But even more involved interactions, such as select and sorting data sets, or writing data to the server use the same fundamental operations described here. (The :ref:`api-cook` builds on this simple example, introducing you to all of the functionality made available by the API.)

Your application needs data. You can programmatically get the data, stored in the PostgreSQL database, by sending requests to the serve following the prescribed format and protocol conventions.

A convenient way to become familiar with sending requests to the server and receiving responses is to use a tool that permits you to work interactively. This section uses the `Client URL Library (cURL) <curl.haxx.se/libcurl/php>`_ command line tool, which you can download and run in most environments. A convenient alternative is a browser-based REST client, but all tools and REST programming libraries work on the same principles, primarily differing in syntax and display modes.

Download and install ``cURL`` to try the API yourself as you follow along in this tutorial. (Remember to replace the hostname, myhost, with your actual server name, and to replace myusername:mypassword with  your username and password.)

.. _api-reqrsrc:

Request resource data
---------------------

A request for data is made on an resource endpoint using an Uniform Resource Identifier (URI). The URI is, effectively, the endpoint address. Depending on how you format the URI, you can get a single resource or a set of resources.

Get all resources
^^^^^^^^^^^^^^^^^

First, we get a set of resources. From the response, we can find out which specific resources are available. The ``cURL`` command for getting a rig resource has the following format. (Requests and responses are shown on multiple lines to make the individual parts easier to see. You should enter commands on a single line.) ::

	curl --user myusername:mypassword
		 --header "Content-Type: application/json"
		 --location 'http://myhost/rundb/api/v1/rig'

The command requires an username and password for authentication, which is the only form of authentication required by the API.
The command also specifies the data format in which the server should send the response data: JSON.

The URI ``http://myhost/rundb/api/v1/rig`` tells the server the location of the desired data. The URI format is similar to the familiar browser URL. Specifying the location without indicating a particular rig, requests the data for all rigs::

	{
	meta: {
		limit: 20,
		next: null,
		offset: 0,
		previous: null,
		total_count: 4
	},
	objects: [
	{
		alarms: { },
		comments: "This is a model PGM. Do not delete.",
		ftppassword: "ionguest",
		ftprootdir: "results",
		ftpserver: "192.168.201.1",
		ftpusername: "ionguest",
		last_clean_date: "",
		last_experiment: "",
		last_init_date: "",
		location: {
			comments: "",
			defaultlocation: true,
			id: 1,
			name: "Home",
			resource_uri: "/rundb/api/v1/location/1/"
		},
		name: "default",
		resource_uri: "/rundb/api/v1/rig/default/",
		serial: null,
		state: "",
		updateflag: false,
		updatehome: "192.168.201.1",
		version: { }
		},
		{
		alarms: { },
		comments: "",
		ftppassword: "ionguest",
		ftprootdir: "results",
		ftpserver: "192.168.201.1",
		ftpusername: "ionguest",
		last_clean_date: "",
		last_experiment: "",
		last_init_date: "",
		location: {
			comments: "",
			defaultlocation: true,
			id: 1,
			name: "Home",
			resource_uri: "/rundb/api/v1/location/1/"
		},
		name: "PGM_test",
		resource_uri: "/rundb/api/v1/rig/PGM_test/",
		serial: "",
		state: "",
		updateflag: false,
		updatehome: "192.168.201.1",
		version: { }
	}
	]	

A list of resource elements, or objects, are returned, and the meta field indicates the total object count is two. Looking at the object name elements, you can see one rig is named PGM_test and the other is named default.

Get a single resource
---------------------

Knowing the available rigs in the database, you can then request only the data for a single rig, PGM_test, by appending the rig name to the URI in the following way::

	curl --user myusername:mypassword
		 --header "Content-Type: application/json"
		 --location 'http://myhost/rundb/api/v1/rig/PGM_test'
	 
Only fields defined as primary key fields in the database can be used in this way. Other fields can be used to select resource elements but they are passed as URI parameters. These details are left for more extensive presentation in other API documents.

You can see that the server returns only the data for the PGM_test rig, and no metadata are included in the response::

	{
	alarms: { },
	comments: "",
	ftppassword: "ionguest",
	ftprootdir: "results",
	ftpserver: "192.168.201.1",
	ftpusername: "ionguest",
	last_clean_date: "",
	last_experiment: "",
	last_init_date: "",
	location: {
		comments: "",
		defaultlocation: true,
		id: 1,
		name: "Home",
		resource_uri: "/rundb/api/v1/location/1/"
	},
	name: "PGM_test",
	resource_uri: "/rundb/api/v1/rig/PGM_test/",
	serial: "",
	state: "",
	updateflag: false,
	updatehome: "192.168.201.1",
	version: { }
	}


.. _api-err:

Check for errors
----------------

So far, all of the requests have been successful, returning resource data.
Requests and responses include a message body and a message header component. You may have noticed that the request specified the JSON data format in the request header argument. For responses, the data are returned in the message body and the request status, success or some kind of failure, are returned in the message header.

A successful response
^^^^^^^^^^^^^^^^^^^^^

Adding the --dump-header headers.txt argument to your cURL command permits you to see the response header::

	$ curl --user myusername:mypassword
		   --dump-header headers.txt
		   --header "Content-Type: application/json"
		   --location 'http://myhost/rundb/api/v1/rig/PGM_test'
	   
Viewing the file ``headers.txt`` confirms the successful response received for the earlier commands::

	HTTP/1.1 200 OK
	Date: Thu, 30 Jun 2011 20:09:17 GMT
	Server: Apache/2.2.14 (Ubuntu)
	Content-Type: application/json; charset=utf-8
	Transfer-Encoding: chunked

The key header item is the HTTP status code in the first line, which has a value of 200. All 200-series status codes indicate a successful operation.

A request failure
^^^^^^^^^^^^^^^^^
To demonstrate an unsuccessful operation, enter a cURL command with a URI for a rig that does not exist, for instance ``PGM_xyz``. (Review the response when you request data for all rigs, and you can see there is no rig named ``PGM_xyz``). ::

	$ curl --user myusername:mypassword
		   --dump-header headers.txt
		   --header "Content-Type: application/json"
		   --location 'http://myhost/rundb/api/v1/rig/PGM_xyz'
	   
The returned status code is 410, which means the resource element does not exist::

	HTTP/1.1 410 Gone
	Date: Thu, 30 Jun 2011 20:13:38 GMT
	Server: Apache/2.2.14 (Ubuntu)
	Content-Type: text/html; charset=utf-8
	Vary: Accept-Encoding
	Content-Length: 0

.. _api-next:

Next steps
----------

Continue using ``cURL`` or a REST client to experiment with the API, consulting the :ref:`quickref` for the various ways of requesting data.

When you are sufficiently familiar with basic API usage, read the :ref:`api-cook` for more in-depth tutorials.
