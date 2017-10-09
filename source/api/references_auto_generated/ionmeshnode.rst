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
**apikey_local**  Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**  Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**hostname**      Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**system_id**     Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**active**        Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**apikey_remote** Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**            Integer data. Ex: 2673                         false    false    true  true   integer 
----------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**          Unicode string data. Ex: "Hello World" n/a     true     false    false true   string  
================= ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 1, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": [
	        {
	            "apikey_local": "2ef92cb0069d1d1b156fa081ec1717807c1cd105", 
	            "resource_uri": "/rundb/api/v1/ionmeshnode/4/", 
	            "hostname": "tsvm.itw", 
	            "system_id": "tsvm", 
	            "active": true, 
	            "apikey_remote": "f45e8c2251095469140a12bf47349d72c68422e9", 
	            "id": 4, 
	            "name": ""
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- patch
- get
- delete

