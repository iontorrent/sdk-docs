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
**description**  Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**direction**    Unicode string data. Ex: "Hello World" Forward false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**    Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**      Unicode string data. Ex: "Hello World" single  false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/librarykey/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 3
	    },
	    "objects": [
	        {
	            "description": "Ion TCAGT",
	            "direction": "Forward",
	            "id": 3,
	            "isDefault": false,
	            "name": "Ion TCAGT",
	            "resource_uri": "/rundb/api/v1/librarykey/3/",
	            "runMode": "single",
	            "sequence": "TCAGT"
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

