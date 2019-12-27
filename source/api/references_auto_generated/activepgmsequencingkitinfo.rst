.. _api_reference_activepgmsequencingkitinfo:

Active Pgm Sequencing Kit Info  Resource
========================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/schema/``
| 

.. include:: ../references_manual_extras/activepgmsequencingkitinfo.rst

Resource Fields
---------------

============================================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                                        help text                                                                                          default nullable readonly blank unique type    
============================================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
**applicationType**                          Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**cartridgeBetweenUsageAbsoluteMaxDayLimit** Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**cartridgeExpirationDayLimit**              Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**                               Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**chipTypes**                                Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultCartridgeUsageCount**               Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultFlowOrder**                         A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**                              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**                                Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                                       Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**                                 Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**kitType**                                  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryReadLength**                        Integer data. Ex: 2673                                                                             0       false    false    false false  integer 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                                     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**                                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**                             Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**                                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType**                Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
-------------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                                      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
============================================ ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/activepgmsequencingkitinfo/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 4
	    },
	    "objects": [
	        {
	            "applicationType": "",
	            "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	            "cartridgeExpirationDayLimit": null,
	            "categories": "flowOverridable;readLengthDerivableFromFlows;",
	            "chipTypes": "",
	            "defaultCartridgeUsageCount": null,
	            "defaultFlowOrder": null,
	            "description": "Ion PGM Hi-Q View Sequencing Kit",
	            "flowCount": 500,
	            "id": 20090,
	            "instrumentType": "pgm",
	            "isActive": true,
	            "kitType": "SequencingKit",
	            "libraryReadLength": 0,
	            "name": "IonPGMHiQView",
	            "nucleotideType": "",
	            "parts": [
	                {
	                    "barcode": "A30044",
	                    "id": 20203,
	                    "kit": "/rundb/api/v1/kitinfo/20090/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20203/"
	                },
	                {
	                    "barcode": "A30043",
	                    "id": 20204,
	                    "kit": "/rundb/api/v1/kitinfo/20090/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20204/"
	                },
	                {
	                    "barcode": "A30275",
	                    "id": 20205,
	                    "kit": "/rundb/api/v1/kitinfo/20090/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20205/"
	                },
	                {
	                    "barcode": "A25590",
	                    "id": 20206,
	                    "kit": "/rundb/api/v1/kitinfo/20090/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20206/"
	                }
	            ],
	            "resource_uri": "/rundb/api/v1/activepgmsequencingkitinfo/20090/",
	            "runMode": "",
	            "samplePrep_instrumentType": "OT_IC_IA",
	            "uid": "SEQ0024"
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

