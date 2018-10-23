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
	        "total_count": 9, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/filemonitor/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Complete", 
	            "updated": "2018-04-13T18:54:39.000796+00:00", 
	            "name": "gene.gtf", 
	            "created": "2018-04-13T18:54:08.000422+00:00", 
	            "url": "http://updates.itw/internal_reference_downloads/hg19/gene.gtf", 
	            "md5sum": "72fbd490a4d3be60e53e642d4401c944", 
	            "celery_task_id": "7db1de03-b295-4b62-9cdc-9cbb4c6065b0", 
	            "local_dir": "/tmp/tmppTeNvf", 
	            "progress": "1111970946", 
	            "size": "1111970946", 
	            "id": 7, 
	            "tags": "annotation", 
	            "resource_uri": "/rundb/api/v1/filemonitor/7/"
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

