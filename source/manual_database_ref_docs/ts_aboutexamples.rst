About the Examples
==================

* Cookbook examples are discussed in snippets to elaborate on important interface details. Refer to `Torrent Suite™ Software SDK Source Code Samples <../manual_code_examples_index.html>`_ for full example listings.

* Where the server name and authorization credentials are shown, the following convention is used:

	+-------------+-------------+
	| Entity      || Placeholder|
	+=============+=============+
	| Server name || myhost     |
	+-------------+-------------+
	| Username    || myusername |
	+-------------+-------------+
	| Password    || mypassword |
	+-------------+-------------+

To run the examples, replace these strings with the host name and credentials required for your server.

* You can interactively explore the REST interface using either the cURL command line utility, a REST client, or a web browser. These tools require less infrastructure than program development and providing a more convenient way to learn the interface.

	* `cURL <http://curl.haxx.se/docs/>`_
	* `Firefox REST client <https://addons.mozilla.org/en-us/firefox/addon/restclient/>`_
	* `Chrome REST client <https://chrome.google.com/webstore/detail/fhjcajmcbmldlhcimfajhfbgofnpcjmb>`_
	* `Generic REST client <http://restclient.org/>`_

	(!) Each example shows the equivalent URI used with these tools before describing the programming language implementation.

* If you run the examples in your browser using either the browser address window or a REST client, you must include the ``?format=json`` parameter. This is because the browser requests XML-formatted data before JSON-formatted data but the current implementation does not support XML. This requirement does not apply to your programs, although, the programming examples in this document include the format parameter.

* For examples that demonstrate the API using the Python programming language, one of the following REST libraries is used. You may need to modify the example code for your preferred REST library.

	* `httplib2 <http://code.google.com/p/httplib2/>`_
	* `restful_lib (deprecated) <http://code.google.com/p/python-rest-client/source/browse/trunk/restful_lib.py?r=10>`_
	* `requests <http://readthedocs.org/docs/requests/latest/api.html#module-requests>`_

* Currently, only the JSON data format is supported. The examples use the `simplejson <http://pypi.python.org/pypi/simplejson/>`_ library to encode and decode JSON data into Python objects.

* JavaScript examples use the `jQuery <http://docs.jquery.com/Main_Page>`_ framework.
