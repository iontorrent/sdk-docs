.. _api_reference_contentupload:

Content Upload  Resource
========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/contentupload/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/contentupload/schema/``
| 

.. include:: ../references_manual_extras/contentupload.rst

Resource Fields
---------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**file_path**    Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**meta**         Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**         Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pub**          Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**source**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**upload_date**  A date & time as a string. Ex: "2010-11-10T03:07:43" true    true     false    false false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**upload_type**  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/contentupload/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 21
	    },
	    "objects": [
	        {
	            "file_path": "/results/uploads/BED/22/AmpliSeq_Mouse_Transcriptome_V1_Designed.bed",
	            "id": 22,
	            "meta": {
	                "description": "",
	                "enabled": true,
	                "hotspot": false,
	                "is_ampliseq": false,
	                "notes": "",
	                "num_bases": 2201026,
	                "num_genes": 23930,
	                "num_targets": 23930,
	                "pre_process_files": [
	                    "/results/uploads/BED/22/AmpliSeq_Mouse_Transcriptome_V1_Designed.bed"
	                ],
	                "reference": "AmpliSeq_Mouse_Transcriptome_v1",
	                "upload_date": "2018-08-02T21:43:45",
	                "username": "ionadmin"
	            },
	            "name": "AmpliSeq_Mouse_Transcriptome_V1_Designed.bed",
	            "pub": "BED",
	            "resource_uri": "/rundb/api/v1/contentupload/22/",
	            "source": "",
	            "status": "Successfully Completed",
	            "upload_date": "2018-08-02T21:43:45.000649+00:00",
	            "upload_type": "target",
	            "username": "ionadmin"
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

