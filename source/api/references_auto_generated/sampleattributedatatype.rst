.. _api_reference_sampleattributedatatype:

Sample Attribute Data Type  Resource
====================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleattributedatatype/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleattributedatatype/schema/``
| 

.. include:: ../references_manual_extras/sampleattributedatatype.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**dataType**     Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/sampleattributedatatype/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "dataType": "Integer",
	            "description": "Whole number",
	            "id": 2,
	            "isActive": true,
	            "resource_uri": "/rundb/api/v1/sampleattributedatatype/2/"
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

