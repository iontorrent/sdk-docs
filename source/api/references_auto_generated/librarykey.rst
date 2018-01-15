.. _api_reference_librarykey:

Library Key Resource
====================

| Resource URL ``http://mytorrentserver/rundb/api/v1/librarykey/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/librarykey/schema/``
| 

.. include:: ../references_manual_extras/librarykey.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	            "id": 1, 
	            "isDefault": true, 
	            "resource_uri": "/rundb/api/v1/librarykey/1/"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

