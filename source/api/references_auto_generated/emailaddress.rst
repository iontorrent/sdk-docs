.. _api_reference_emailaddress:

Email Address Resource
======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/emailaddress/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/emailaddress/schema/``
| 

.. include:: ../references_manual_extras/emailaddress.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**email**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**selected**     Boolean data. Ex: True                         false    false    true  false  boolean 
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 0
	    },
	    "objects": []
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

