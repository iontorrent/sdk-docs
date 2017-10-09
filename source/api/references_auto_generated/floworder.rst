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
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowOrder**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isSystem**     Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**    Boolean data. Ex: True                 false   false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/floworder/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "description": "Ion contradanzon flow order", 
	            "resource_uri": "/rundb/api/v1/floworder/3/", 
	            "flowOrder": "TACGTACGTAGCTTGACGTACGTCATGCATCGATCAGCTAAGCTGACGTAGCTAGCATCGATCCAGTCATGACTGACGTAGCTGACTGGATCAGTCATGCATCG", 
	            "isActive": false, 
	            "isSystem": true, 
	            "id": 3, 
	            "isDefault": false, 
	            "name": "Ion contradanzon"
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

