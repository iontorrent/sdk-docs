.. _apiug-debug:

Debug API Errors
================

API faults can be classified as either communication faults, backend server processing errors or client application program errors:

* Communication errors can be caused by connectivity issues, failure to authenticate or message protocol errors, which are listed in section 6 of the `RFC 2616, Hypertext Transfer Protocol – HTTP/1.1 standard <http://www.w3.org/Protocols/rfc2616/rfc2616.html>`_.

* Internal processing errors are those detected by the Django framework and include software bugs, database anomalies and invalid request formats.

* Client application program errors can be of many types, which can be detected and reported using common program debugging methods and tools. Some classes of errors deserving particular mention, because of the web application environment are errors related to HTML and JavaScript coding.

The :ref:`apimanref_httpresp` section of the :ref:`api-ref` document lists errors that might typically occur when using the Torrent Suite™ Software API, and their possible causes.

.. _apiug-bugstatus:

HTTP status codes
-----------------

Successful API requests return a status code of 200 or 201.

All other status codes indicate some kind of error condition, and after some experience using HTTP the cause of the error can often readily be determined. To demonstrate an error condition, the following example omits the question mark (?) symbol preceding request parameters, effectively making a request on an undefined resource::

	http://myhost/rundb/api/v1/rigformat=json

If you try sending this request, you will see that the server returns a 404 status code, indicating the resource was ``Not Found``. Additionally, the response message body contains a server-specific HTML page for the 404-type error.

Additional debugging facilities are available for backend 500-series errors, described below.

.. _apiug-bugback:

Debug backend errors
------------------------

You can receive additional, detailed information in the response message body for internal, 500-series errors, which are detected by the Django framework, by turning on debugging:

1. On your server, open the settings.py file for editing, found at the following location::
 
	/opt/ion/iondb/settings.py

2. Set the DEBUG environment variable to true::
 
	DEBUG = True

3. Restart Apache::
 
	sudo /etc/init.d/apache2 restart

Thereafter, whenever a 500-series error occurs, a message similar to the following example is provided in the response message with detailed information about the type of error and the source code location where the error was detected::

	<Response [500]>
	
	{"error_message": "The format indicated 'application/x-www-form-urlencoded' had
	no available deserialization method. Please check your ``formats`` and ``content
	_types`` on your Serializer.", "traceback": "Traceback (most recent call last):\
	n\n  File \"/usr/local/lib/python2.6/dist-packages/tastypie/resources.py\", line
	 175, in wrapper\n    response = callback(request, *args, **kwargs)\n\n  File \"
	/usr/local/lib/python2.6/dist-packages/tastypie/resources.py\", line 343, in dis
	patch_detail\n    return self.dispatch('detail', request, **kwargs)\n\n  File \"
	/usr/local/lib/python2.6/dist-packages/tastypie/resources.py\", line 364, in dis
	patch\n    response = method(request, **kwargs)\n\n  File \"/usr/local/lib/pytho
	n2.6/dist-packages/tastypie/resources.py\", line 1007, in put_detail\n    deseri
	alized = self.deserialize(request, request.raw_post_data, format=request.META.ge
	t('CONTENT_TYPE', 'application/json'))\n\n  File \"/usr/local/lib/python2.6/dist
	-packages/tastypie/resources.py\", line 325, in deserialize\n    return self._me
	ta.serializer.deserialize(data, format=request.META.get('CONTENT_TYPE', 'applica
	tion/json'))\n\n  File \"/usr/local/lib/python2.6/dist-packages/tastypie/seriali
	zers.py\", line 159, in deserialize\n    raise UnsupportedFormat(\"The format in
	dicated '%s' had no available deserialization method. Please check your ``format
	s`` and ``content_types`` on your Serializer.\" % format)\n\nUnsupportedFormat:
	The format indicated 'application/x-www-form-urlencoded' had no available deseri
	alization method. Please check your ``formats`` and ``content_types`` on your Se
	rializer.\n"}

.. _apiug-bughtml:
	
Debug HTML or JavaScript 
------------------------

Two useful browser tools available for debugging suspected HTML and JavaScript problems are Firefox Firebug and Chrome Inspector.

Firefox Firebug
^^^^^^^^^^^^^^^

If you are using the Firefox browser, download and install the Firebug plugin.

Once installed, click on the Firebug icon in the status bar to begin debugging your HTML and JavaScript code.

Chrome Inspector
^^^^^^^^^^^^^^^^

The Chrome Inspector debugger comes pre-installed with the Chrome browser.

To begin debugging, right-click on your HTML page and select Inspect Element from the drop-down menu.

.. _apiug-buglog:

Event logging
-------------

The system logs events, which can be a useful debugging tool. Logs are located in the following directory::

	/var/log/ion/

For plugins, the event log has the following name::

	/var/log/ion/ionPlugin.log



