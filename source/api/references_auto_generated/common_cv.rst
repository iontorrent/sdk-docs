.. _api_reference_common_cv:

Common Cv  Resource
===================

| Resource URL ``http://mytorrentserver/rundb/api/v1/common_cv/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/common_cv/schema/``
| 

.. include:: ../references_manual_extras/common_cv.rst

Resource Fields
---------------

============================= ====================================== ======= ======== ======== ===== ====== ======= 
field                         help text                              default nullable readonly blank unique type    
============================= ====================================== ======= ======== ======== ===== ====== ======= 
**categories**                Unicode string data. Ex: "Hello World"         true     false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**cv_type**                   Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**               Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**displayedValue**            Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                         false    false    true  true   integer 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**                  Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**                 Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isVisible**                 Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequencing_instrumentType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                       Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**value**                     Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
============================= ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/common_cv/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 16
	    },
	    "objects": [
	        {
	            "categories": "AMPS;AMPS_RNA;AMPS_DNA_RNA;AMPS_HD_DNA;AMPS_HD_RNA;AMPS_HD_DNA_RNA;AMPS_HD_DNA_RNA_1",
	            "cv_type": "applicationCategory",
	            "description": "Oncomine Tumor Specific Panels",
	            "displayedValue": "P4O",
	            "id": 16,
	            "isActive": true,
	            "isDefault": false,
	            "isVisible": false,
	            "resource_uri": "/rundb/api/v1/common_cv/16/",
	            "samplePrep_instrumentType": "",
	            "sequencing_instrumentType": "",
	            "uid": "APPCAT0011",
	            "value": "p4o"
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

