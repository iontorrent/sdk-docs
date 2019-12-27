.. _api_reference_filemonitor:

File Monitor  Resource
======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/filemonitor/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/filemonitor/schema/``
| 

.. include:: ../references_manual_extras/filemonitor.rst

Resource Fields
---------------

================== ==================================================== ======= ======== ======== ===== ====== ======== 
field              help text                                            default nullable readonly blank unique type     
================== ==================================================== ======= ======== ======== ===== ====== ======== 
**celery_task_id** Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**created**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**local_dir**      Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**md5sum**         Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**progress**       Unicode string data. Ex: "Hello World"               0       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**size**           Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tags**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**updated**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**            Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/filemonitor/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 9
	    },
	    "objects": [
	        {
	            "celery_task_id": "9791ab17-8fb1-409e-ab9f-1f02d8f0a256",
	            "created": "2018-08-02T23:10:55.000145+00:00",
	            "id": 11,
	            "local_dir": "/results/referenceLibrary/temp/tmpBar9cj",
	            "md5sum": null,
	            "name": "mm10.zip",
	            "progress": "4080979909",
	            "resource_uri": "/rundb/api/v1/filemonitor/11/",
	            "size": "4080979909",
	            "status": "Complete",
	            "tags": "reference",
	            "updated": "2018-08-02T23:12:07.000540+00:00",
	            "url": "http://updates.itw/internal_reference_downloads/mm10.zip"
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

