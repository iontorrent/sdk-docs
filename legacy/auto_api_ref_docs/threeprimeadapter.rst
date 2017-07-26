Threeprimeadapter Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/threeprimeadapter/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/threeprimeadapter/schema/``


.. include:: ../manual_api_ref_docs/threeprimeadapter.rst

Fields table
------------

================= ====================================== ======= ======== ======== ===== ====== ======= 
field             help text                              default nullable readonly blank unique type    
================= ====================================== ======= ======== ======== ===== ====== ======= 
**direction**     Unicode string data. Ex: "Hello World" Forward false    false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**   Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**      Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**chemistryType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**       Unicode string data. Ex: "Hello World" single  false    false    true  false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**      Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**           Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**  Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**            Integer data. Ex: 2673                         false    false    true  true   integer 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**     Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**          Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
================= ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/threeprimeadapter/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/threeprimeadapter/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	threeprimeadapters = ts_api_response["objects"]
	
	for threeprimeadapter in threeprimeadapters:
	    print threeprimeadapter
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 8, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/threeprimeadapter/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "direction": "Forward", 
	            "description": "Ion Paired End Fwd", 
	            "sequence": "GCTGAGGATCACCGACTGCCCATAGAGAGG", 
	            "chemistryType": "", 
	            "runMode": "pe", 
	            "isActive": true, 
	            "uid": "FWD_0004", 
	            "resource_uri": "/rundb/api/v1/threeprimeadapter/5/", 
	            "id": 5, 
	            "isDefault": false, 
	            "name": "Ion Paired End Fwd"
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

