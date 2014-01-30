Responses
=========

Responses are HTTP messages from the server in response to application requests. The response includes header and body parts to the message.

	**Tip:** Using a REST client in your browser is a convenient way to visualize the response header and body.

Response header
^^^^^^^^^^^^^^^

A response header contains information similar to the following example::

	Status Code:200 OK
	Date: Wed, 01 Jun 2011 22:38:49 GMT
	Server: Apache/2.2.2.14 (Ubuntu)
	Content-Type: application/json; charset=utf-8
	Keep-Alive: timeout=15, max=100
	Connection: Keep-Alive
	Transfer-Encoding: chunked

``Status Code`` is of particular interest, indicating if the requested succeeded or not. Responses with 200-series status codes indicate the request was handled successfully.
Another informative data item in the header is ``Content-Type``, which describes the data format. Currently, only the JSON data format is supported.

Response body
^^^^^^^^^^^^^

For a GET request, the response body contains the data representing the resource or resource set requested. These data are formatted as specified by the ``Content-Type`` property in the header.

The following code snippet shows an example response body returned by the server, in response to a location request (``http://myhost/rundb/api/v1/location/?format=json``)::

	{
	"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1},
	 "objects":
	   [{"comments": "",
		 "id": "2",
		 "name": "IonWest",
		 "resource_uri": "/rundb/api/v1/location/2/"
	   }]
	}

A response body is not returned by the server for PUT, POST and DELETE requests.



