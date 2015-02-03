Clusterinfohistory Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/clusterinfohistory/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/clusterinfohistory/schema/``


.. include:: ../manual_api_ref_docs/clusterinfohistory.rst

Fields table
------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**username**     Unicode string data. Ex: "Hello World"               ION     false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**         Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
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

Request URL: ``http://mytorrentserver/rundb/api/v1/clusterinfohistory/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/clusterinfohistory/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	clusterinfohistorys = ts_api_response["objects"]
	
	for clusterinfohistory in clusterinfohistorys:
	    print clusterinfohistory
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 27, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/clusterinfohistory/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "system", 
	            "name": null, 
	            "created": "2014-07-28T17:39:23.000473+00:00", 
	            "network_test": "success", 
	            "object_pk": 1, 
	            "state": "Error", 
	            "address_test": "success", 
	            "text": "charm01 state changed from Good to Error<br>Error: Host key verification failed.\r\nCannot access server charm01 with secure shell\n <br>address_test: success<br>network_test: success<br>access_test: failure<br>", 
	            "error": "Host key verification failed.\r\nCannot access server charm01 with secure shell\n ", 
	            "access_test": "failure", 
	            "id": 650559, 
	            "resource_uri": "/rundb/api/v1/clusterinfohistory/650559/"
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

