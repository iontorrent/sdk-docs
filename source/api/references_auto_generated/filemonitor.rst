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
**status**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**updated**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**created**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**            Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**md5sum**         Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**celery_task_id** Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**local_dir**      Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**progress**       Unicode string data. Ex: "Hello World"               0       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**size**           Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tags**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/filemonitor/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Complete", 
	            "updated": "2017-03-14T03:46:14.000171+00:00", 
	            "name": "GRCh38.p2.mask1.zip", 
	            "created": "2017-03-14T03:41:11.000026+00:00", 
	            "url": "http://ionupdates.com/reference_downloads/GRCh38.p2.mask1.zip", 
	            "md5sum": null, 
	            "celery_task_id": "cebba665-096a-48a7-82cb-2fac99d6ddad", 
	            "local_dir": "/results/referenceLibrary/temp/tmp4NGc6h", 
	            "progress": "4663793607", 
	            "size": "4663793607", 
	            "id": 2, 
	            "tags": "reference", 
	            "resource_uri": "/rundb/api/v1/filemonitor/2/"
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

