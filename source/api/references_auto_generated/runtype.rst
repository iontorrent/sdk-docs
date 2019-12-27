.. _api_reference_runtype:

Run Type  Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/runtype/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/runtype/schema/``
| 

.. include:: ../references_manual_extras/runtype.rst

Resource Fields
---------------

===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                 help text                                                                                          default nullable readonly blank unique type    
===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**alternate_name**    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applicationGroups** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**barcode**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**          Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**meta**              Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**    Unicode string data. Ex: "Hello World"                                                             dna     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runType**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/runtype/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 15
	    },
	    "objects": [
	        {
	            "alternate_name": "AmpliSeq HD - DNA and Fusions (Single Library)",
	            "applicationGroups": [
	                "/rundb/api/v1/applicationgroup/11/"
	            ],
	            "barcode": "",
	            "description": "AmpliSeq HD - DNA and Fusions (Single Library)",
	            "id": 15,
	            "isActive": true,
	            "meta": {},
	            "nucleotideType": "dna",
	            "resource_uri": "/rundb/api/v1/runtype/15/",
	            "runType": "AMPS_HD_DNA_RNA_1"
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

