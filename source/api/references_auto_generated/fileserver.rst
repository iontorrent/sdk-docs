.. _api_reference_fileserver:

File Server  Resource
=====================

| Resource URL ``http://mytorrentserver/rundb/api/v1/fileserver/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/fileserver/schema/``
| 

.. include:: ../references_manual_extras/fileserver.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**comments**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**filesPrefix**  Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**percentfull**  Floating point numeric data. Ex: 26.73 0       true     false    false false  float   
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
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
	        "total_count": 1
	    },
	    "objects": [
	        {
	            "comments": "",
	            "filesPrefix": "/results/",
	            "id": 1,
	            "name": "Home",
	            "percentfull": 40.1362957221239,
	            "resource_uri": "/rundb/api/v1/fileserver/1/"
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

