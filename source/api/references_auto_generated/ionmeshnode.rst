.. _api_reference_ionmeshnode:

Ion Mesh Node  Resource
=======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/ionmeshnode/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/ionmeshnode/schema/``
| 

.. include:: ../references_manual_extras/ionmeshnode.rst

Resource Fields
---------------

==================== ====================================== ======= ======== ======== ===== ====== ======= 
field                help text                              default nullable readonly blank unique type    
==================== ====================================== ======= ======== ======== ===== ====== ======= 
**apikey_local**     Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**share_plans**      Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**share_monitoring** Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**hostname**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**system_id**        Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**share_data**       Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**apikey_remote**    Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**               Integer data. Ex: 2673                         false    false    true  true   integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**     Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
==================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 0, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": []
	}

Allowed HTTP methods
--------------------

- patch
- get
- delete

