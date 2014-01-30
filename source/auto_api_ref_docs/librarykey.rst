Librarykey Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/librarykey/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/librarykey/schema/``


.. include:: ../manual_api_ref_docs/librarykey.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**direction**    Unicode string data. Ex: "Hello World" Forward false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**      Unicode string data. Ex: "Hello World" single  false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**    Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/librarykey/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/librarykey/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	librarykeys = ts_api_response["objects"]
	
	for librarykey in librarykeys:
	    print librarykey
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 3, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/librarykey/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "direction": "Forward", 
	            "name": "Ion TCAG", 
	            "sequence": "TCAG", 
	            "description": "Default forward library key", 
	            "runMode": "single", 
	            "id": 3, 
	            "isDefault": true, 
	            "resource_uri": "/rundb/api/v1/librarykey/3/"
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

