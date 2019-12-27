.. _api_reference_samplegrouptype_cv:

Sample Group Type Cv  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/schema/``
| 

.. include:: ../references_manual_extras/samplegrouptype_cv.rst

Resource Fields
---------------

======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                    help text                                                                                          default nullable readonly blank unique type    
======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**description**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**displayedName**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**iRAnnotationType**     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**iRValue**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                   Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**             Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isIRCompatible**       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**sampleAnnotation_set** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**sampleSets**           Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/samplegrouptype_cv/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 7
	    },
	    "objects": [
	        {
	            "description": "",
	            "displayedName": "Single Fusions",
	            "iRAnnotationType": "RelationshipType",
	            "iRValue": "SINGLE_RNA_FUSION",
	            "id": 7,
	            "isActive": true,
	            "isIRCompatible": true,
	            "resource_uri": "/rundb/api/v1/samplegrouptype_cv/7/",
	            "sampleAnnotation_set": [],
	            "sampleSets": [],
	            "uid": "SAMPLEGROUP_CV_0007"
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

