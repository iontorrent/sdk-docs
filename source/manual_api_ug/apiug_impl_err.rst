Error Messages
==============

API errors can be classified as either communication or internal server processing errors:

* Communication errors can be caused by connectivity issues, failure to authenticate or message protocol errors, which are listed in section 6 of the `RFC 2616, Hypertext Transfer Protocol – HTTP/1.1 standard <http://www.w3.org/Protocols/rfc2616/rfc2616.html>`_.

* Internal processing errors are those detected by the Django framework and include software bugs, database anomalies and invalid request formats.

The :ref:`apimanref_httpresp` section of the :ref:`api-ref` document lists errors that might typically occur when using the Torrent Suite™ Software API, and their possible causes.

Topics on this page:

* :ref:`httpstatus`
* :ref:`debuginternal`

**Note:** Errors detected by the server are reported in the status code returned with any create, read, update or delete request. To help determine the cause of the error, the returned message body contains additional information about the error. For internal, 500-series server errors, in particular, Django returns very detailed information about the error cause and location. Debugging must be enable to receive the more extensive Django error reports.

Using a REST client with your browser to interactively exercise the API provides an easy way to investigate error conditions, by examining the status code and message body returned with the request. When writing an application program, it is helpful to include exception handling around API calls to catch possible errors, and to always check the returned status code before continuing to process a response.

.. _httpstatus:

HTTP status codes
-----------------

Successful API requests have a return status code of 200 or 201.

All other status codes indicate some kind of error condition, and after some experience using HTTP the cause of the error can often readily be determined. To demonstrate an error condition, the following example omits the question mark (?) symbol preceding request parameters, effectively making a request on an undefined resource::

	http://myhost/rundb/api/v1/rigformat=json

If you try sending this request, you will see that the server returns a 404 status code, indicating the resource was ``Not Found``. Additionally, the response message body contains a server-specific HTML page for the 404-type error.

.. _debuginternal:

Debug internal errors
---------------------

You can receive additional, detailed information in the response message body for internal, 500-series errors, which are detected by the Django framework, by turning on debugging. 

Follow these steps to turn on debugging:

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

