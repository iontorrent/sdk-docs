.. _api_reference_ionmeshnode:

Ion Mesh Node  Resource
=======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/ionmeshnode/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/ionmeshnode/schema/``
| 

.. include:: ../references_manual_extras/ionmeshnode.rst

Resource Fields
---------------

================= ====================================== ======= ======== ======== ===== ====== ======= 
field             help text                              default nullable readonly blank unique type    
================= ====================================== ======= ======== ======== ===== ====== ======= 
**active**        Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**apikey_local**  Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**apikey_remote** Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**hostname**      Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**            Integer data. Ex: 2673                         false    false    true  true   integer 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**          Unicode string data. Ex: "Hello World" n/a     true     false    false true   string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**  Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**system_id**     Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
================= ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/ionmeshnode/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 4
	    },
	    "objects": [
	        {
	            "active": true,
	            "apikey_local": "cc85a45c95e2079ecdec862bbd92a2ec904ee129",
	            "apikey_remote": "e448e2cecc9b7e9e0d6a54aeae9ad3ac588cd75e",
	            "hostname": "hawk.itw",
	            "id": 10,
	            "name": "hawk.itw",
	            "resource_uri": "/rundb/api/v1/ionmeshnode/10/",
	            "system_id": "4C4C4544-0033-4610-8043-B6C04F383432"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- PATCH
- GET
- DELETE


Allowed detail HTTP methods
---------------------------

- PATCH
- GET
- DELETE

