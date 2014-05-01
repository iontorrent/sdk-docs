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
	        "total_count": 421411, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/datamanagementhistory/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "ION", 
	            "created": "2013-03-05T03:57:46.000452+00:00", 
	            "text": "Created DMFileStat (Signal Processing Input)", 
	            "object_pk": 35520, 
	            "resultsName": "Auto_user_D6--122-R33890-am0042-l6155_8871_tn", 
	            "id": 10351, 
	            "resource_uri": "/rundb/api/v1/datamanagementhistory/10351/"
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

