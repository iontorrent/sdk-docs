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
**applicationGroups** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**    Unicode string data. Ex: "Hello World"                                                             dna     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**barcode**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**meta**              Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**alternate_name**    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runType**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**          Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/runtype/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "applicationGroups": [
	                "/rundb/api/v1/applicationgroup/9/"
	            ], 
	            "description": "Mixed Samples (DNA/RNA)", 
	            "nucleotideType": "dna_rna", 
	            "barcode": "", 
	            "meta": {}, 
	            "alternate_name": "Mixed Samples (DNA/RNA)", 
	            "runType": "MIXED", 
	            "id": 11, 
	            "isActive": false, 
	            "resource_uri": "/rundb/api/v1/runtype/11/"
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

