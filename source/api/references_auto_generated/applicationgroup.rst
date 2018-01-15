.. _api_reference_applicationgroup:

Application Group  Resource
===========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/applicationgroup/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/applicationgroup/schema/``
| 

.. include:: ../references_manual_extras/applicationgroup.rst

Resource Fields
---------------

================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                                          default nullable readonly blank unique type    
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
**name**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applications** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 10, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/applicationgroup/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "DNA", 
	            "description": "DNA", 
	            "applications": [
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/", 
	                        "/rundb/api/v1/applicationgroup/3/", 
	                        "/rundb/api/v1/applicationgroup/4/"
	                    ], 
	                    "description": "Generic Sequencing", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "alternate_name": "Other", 
	                    "runType": "GENS", 
	                    "id": 1, 
	                    "isActive": true, 
	                    "resource_uri": "/rundb/api/v1/runtype/1/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/", 
	                        "/rundb/api/v1/applicationgroup/6/", 
	                        "/rundb/api/v1/applicationgroup/8/", 
	                        "/rundb/api/v1/applicationgroup/10/"
	                    ], 
	                    "description": "AmpliSeq DNA", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "alternate_name": "AmpliSeq DNA", 
	                    "runType": "AMPS", 
	                    "id": 2, 
	                    "isActive": true, 
	                    "resource_uri": "/rundb/api/v1/runtype/2/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/"
	                    ], 
	                    "description": "TargetSeq", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "alternate_name": "TargetSeq", 
	                    "runType": "TARS", 
	                    "id": 3, 
	                    "isActive": true, 
	                    "resource_uri": "/rundb/api/v1/runtype/3/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/", 
	                        "/rundb/api/v1/applicationgroup/4/"
	                    ], 
	                    "description": "Whole Genome", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "alternate_name": "Whole Genome", 
	                    "runType": "WGNM", 
	                    "id": 4, 
	                    "isActive": true, 
	                    "resource_uri": "/rundb/api/v1/runtype/4/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/"
	                    ], 
	                    "description": "AmpliSeq Exome", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "alternate_name": "AmpliSeq Exome", 
	                    "runType": "AMPS_EXOME", 
	                    "id": 7, 
	                    "isActive": true, 
	                    "resource_uri": "/rundb/api/v1/runtype/7/"
	                }
	            ], 
	            "uid": "APPLGROUP_0001", 
	            "id": 1, 
	            "isActive": true, 
	            "resource_uri": "/rundb/api/v1/applicationgroup/1/"
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

