Log Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/log/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/log/schema/``


.. include:: ../manual_api_ref_docs/log.rst

Fields table
------------

================ ============================================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                                                      default nullable readonly blank unique type     
================ ============================================================================== ======= ======== ======== ===== ====== ======== 
**text**         Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**timeStamp**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload**       A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/log/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/log/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	logs = ts_api_response["objects"]
	
	for log in logs:
	    print log
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 0, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": []
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

