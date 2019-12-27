.. _api_reference_monitordata:

Monitor Data  Resource
======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/monitordata/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/monitordata/schema/``
| 

.. include:: ../references_manual_extras/monitordata.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World"         false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**treeDat**      Unicode string data. Ex: "Hello World" {}      false    false    true  false  string  
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

