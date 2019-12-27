.. _api_reference_floworder:

Flow Order Resource
===================

| Resource URL ``http://mytorrentserver/rundb/api/v1/floworder/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/floworder/schema/``
| 

.. include:: ../references_manual_extras/floworder.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**description**  Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowOrder**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**    Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isSystem**     Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/floworder/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 7
	    },
	    "objects": [
	        {
	            "description": "Ion samba.c.2step.pgs flow order",
	            "flowOrder": "TACGTACGTCTGAGCATCGGATCGCGATGTACAGCTACGTACGGAGTCTAGCTGACGTACGTCATGTGCATCGATCAGCTAGCTGACGTAGCTAGCATCGATCAGTCATGACTGACGTAGCTGACTGATCAGTCATGCATCGTACGTACGTAGCTGACGTACGTCATGCATCGATCAGCTAGCTGACGTAGCTAGCATCGATCAGTCATGACTGACGTAGCTGACTGATCAGTCATGCATCGTACGTACGTAGCTGACGTACGTCATGCATCGATCAGCTAGCTGACGTAGCTAGCATCGATCAGTCATGACTGACGTAGCTGACTGATCAGTCATGCATCG",
	            "id": 7,
	            "isActive": true,
	            "isDefault": false,
	            "isSystem": true,
	            "name": "Ion samba.c.2step.pgs",
	            "resource_uri": "/rundb/api/v1/floworder/7/"
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

