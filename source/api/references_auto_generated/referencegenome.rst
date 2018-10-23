.. _api_reference_referencegenome:

Reference Genome  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/referencegenome/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/referencegenome/schema/``
| 

.. include:: ../references_manual_extras/referencegenome.rst

Resource Fields
---------------

================== ==================================================== ================================ ======== ======== ===== ====== ======== 
field              help text                                            default                          nullable readonly blank unique type     
================== ==================================================== ================================ ======== ======== ===== ====== ======== 
**status**         Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**reference_path** Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**name**           Unicode string data. Ex: "Hello World"               n/a                              false    false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**short_name**     Unicode string data. Ex: "Hello World"               n/a                              false    false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**index_version**  Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**notes**          Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**enabled**        Boolean data. Ex: True                               true                             false    false    true  false  boolean  
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**species**        Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**identity_hash**  Unicode string data. Ex: "Hello World"               None                             true     false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**source**         Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**version**        Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**celery_task_id** Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**date**           A date & time as a string. Ex: "2010-11-10T03:07:43" 2018-06-19T20:40:12.000844+00:00 false    false    false false  datetime 
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**verbose_error**  Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                                                false    false    true  true   integer  
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a                              false    true     false false  string   
================== ==================================================== ================================ ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/referencegenome/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "complete", 
	            "reference_path": "/results/referenceLibrary/tmap-f3/AmpliSeq_Mouse_Transcriptome_v1", 
	            "name": "AmpliSeq Mouse Transcriptome v1", 
	            "short_name": "AmpliSeq_Mouse_Transcriptome_v1", 
	            "index_version": "tmap-f3", 
	            "notes": "", 
	            "enabled": true, 
	            "species": "", 
	            "identity_hash": "92e672f416392e46e3137388d878efe7", 
	            "source": "http://ionupdates.com/reference_downloads/AmpliSeq_Mouse_Transcriptome_v1.zip", 
	            "version": "", 
	            "celery_task_id": "370dd08d-d9d0-4f9f-8965-d0563a4461b7", 
	            "date": "2018-01-23T22:42:16.000613+00:00", 
	            "verbose_error": "", 
	            "id": 4, 
	            "resource_uri": "/rundb/api/v1/referencegenome/4/"
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

