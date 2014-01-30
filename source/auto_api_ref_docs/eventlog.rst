Eventlog Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/eventlog/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/eventlog/schema/``


.. include:: ../manual_api_ref_docs/eventlog.rst

Fields table
------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**username**     Unicode string data. Ex: "Hello World"               ION     false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**text**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**object_pk**    Integer data. Ex: 2673                               n/a     false    false    false false  integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/eventlog/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/eventlog/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	eventlogs = ts_api_response["objects"]
	
	for eventlog in eventlogs:
	    print eventlog
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 118644, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/eventlog/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "ION", 
	            "created": "2012-06-20T13:13:30.000951+00:00", 
	            "text": "Created during migration from Experiment project label.", 
	            "object_pk": 1, 
	            "id": 1, 
	            "resource_uri": "/rundb/api/v1/eventlog/1/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

