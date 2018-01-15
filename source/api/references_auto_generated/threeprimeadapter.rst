.. _api_reference_threeprimeadapter:

Three Prime Adapter  Resource
=============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/threeprimeadapter/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/threeprimeadapter/schema/``
| 

.. include:: ../references_manual_extras/threeprimeadapter.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	            "description": "Default forward adapter", 
	            "sequence": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "chemistryType": "", 
	            "runMode": "single", 
	            "isActive": true, 
	            "uid": "FWD_0001", 
	            "resource_uri": "/rundb/api/v1/threeprimeadapter/1/", 
	            "id": 1, 
	            "isDefault": true, 
	            "name": "Ion P1B"
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

