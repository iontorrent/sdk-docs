.. _api_reference_content:

Content  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/content/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/content/schema/``
| 

.. include:: ../references_manual_extras/content.rst

Resource Fields
---------------

==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                help text                                                                      default nullable readonly blank unique type     
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**application_tags** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**contentupload**    A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**enabled**          Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**extra**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**file**             Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**               Integer data. Ex: 2673                                                                 false    false    true  true   integer  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**meta**             Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**name**             Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**notes**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**path**             Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**publisher**        A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**type**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload_date**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     false    true     false false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload_id**        Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/content/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 35
	    },
	    "objects": [
	        {
	            "application_tags": "",
	            "contentupload": "/rundb/api/v1/contentupload/22/",
	            "description": "",
	            "enabled": true,
	            "extra": "AmpliSeq_Mouse_Transcriptome_v1",
	            "file": "/results/uploads/BED/22/AmpliSeq_Mouse_Transcriptome_v1/merged/detail/AmpliSeq_Mouse_Transcriptome_V1_Designed.bed",
	            "id": 36,
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
	            "notes": "",
	            "path": "/AmpliSeq_Mouse_Transcriptome_v1/merged/detail/AmpliSeq_Mouse_Transcriptome_V1_Designed.bed",
	            "publisher": "/rundb/api/v1/publisher/BED/",
	            "resource_uri": "/rundb/api/v1/content/36/",
	            "type": "target",
	            "upload_date": "2018-08-02T21:43:45.000649+00:00",
	            "upload_id": "22"
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

