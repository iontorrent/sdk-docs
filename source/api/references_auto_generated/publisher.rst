.. _api_reference_publisher:

Publisher Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/publisher/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/publisher/schema/``
| 

.. include:: ../references_manual_extras/publisher.rst

Resource Fields
---------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**date**         A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     false    false    false false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**global_meta**  Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**         Unicode string data. Ex: "Hello World"               n/a     false    false    false true   string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**      Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/publisher/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "date": "2017-07-22T21:17:13.000054+00:00",
	            "global_meta": {},
	            "id": 2,
	            "name": "BED",
	            "path": "/results/publishers/BED",
	            "resource_uri": "/rundb/api/v1/publisher/BED/",
	            "version": "1.0"
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

