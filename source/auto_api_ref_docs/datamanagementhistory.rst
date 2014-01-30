Datamanagementhistory Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/datamanagementhistory/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/datamanagementhistory/schema/``


.. include:: ../manual_api_ref_docs/datamanagementhistory.rst

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
**resultsName**  Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/datamanagementhistory/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/datamanagementhistory/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	datamanagementhistorys = ts_api_response["objects"]
	
	for datamanagementhistory in datamanagementhistorys:
	    print datamanagementhistory
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 117134, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/datamanagementhistory/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "ION", 
	            "created": "2013-03-05T14:15:18.000131+00:00", 
	            "text": "Created DMFileStat (Signal Processing Input)", 
	            "object_pk": 15215, 
	            "resultsName": "Auto_user_EN2-262--R166223-PCRRPA-1GC_11440", 
	            "id": 769, 
	            "resource_uri": "/rundb/api/v1/datamanagementhistory/769/"
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

