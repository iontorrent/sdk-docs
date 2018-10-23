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
**status**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**upload_date**  A date & time as a string. Ex: "2010-11-10T03:07:43" true    true     false    false false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**         Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pub**          Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**source**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**meta**         Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**upload_type**  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**file_path**    Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 20, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/contentupload/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Successfully Completed", 
	            "upload_date": "2018-04-13T18:54:45.000418+00:00", 
	            "name": "gencode.v19.annotation_and_tRNAs.gtf", 
	            "pub": "refAnnot", 
	            "id": 21, 
	            "username": "ionadmin", 
	            "source": "http://updates.itw/internal_reference_downloads/hg19/gencode.v19.annotation_and_tRNAs.gtf", 
	            "meta": {
	                "username": "ionadmin", 
	                "upload_date": "2018-04-13T18:54:45", 
	                "description": "hg19 and tRNA gene annotation file for smallRNA", 
	                "reference": "hg19", 
	                "url": "http://updates.itw/internal_reference_downloads/hg19/gencode.v19.annotation_and_tRNAs.gtf", 
	                "upload_type": "Annotation", 
	                "identity_hash": "c47c7d854a9767400224e119246494ec", 
	                "application_tags": "smallRNA", 
	                "updateversion": "1.0", 
	                "filesize": "1109491", 
	                "short_description": "hg19 and tRNA GTF annotation", 
	                "publication_date": "2018-02-14", 
	                "annot_type": "GTF"
	            }, 
	            "upload_type": "Annotation", 
	            "file_path": "/results/uploads/refAnnot/21/gencode.v19.annotation_and_tRNAs.gtf", 
	            "resource_uri": "/rundb/api/v1/contentupload/21/"
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

