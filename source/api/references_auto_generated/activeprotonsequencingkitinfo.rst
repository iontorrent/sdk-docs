.. _api_reference_activeprotonsequencingkitinfo:

Active Proton Sequencing Kit Info  Resource
===========================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/schema/``
| 

.. include:: ../references_manual_extras/activeprotonsequencingkitinfo.rst

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
	        "next": "/rundb/api/v1/activeprotonsequencingkitinfo/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 5
	    },
	    "objects": [
	        {
	            "applicationType": "",
	            "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	            "cartridgeExpirationDayLimit": null,
	            "categories": "readLengthDerivableFromFlows;",
	            "chipTypes": "900;P1.0.19;P1.0.20;P1.1.17;P1.1.541;P1.2.18;P2.0.1;P2.1.1;P2.1.2;P2.3.1",
	            "defaultCartridgeUsageCount": null,
	            "defaultFlowOrder": null,
	            "description": "Ion PI Hi-Q Sequencing 200 Kit",
	            "flowCount": 520,
	            "id": 20071,
	            "instrumentType": "proton",
	            "isActive": true,
	            "kitType": "SequencingKit",
	            "libraryReadLength": 0,
	            "name": "IonProtonIHiQ",
	            "nucleotideType": "",
	            "parts": [
	                {
	                    "barcode": "A26433",
	                    "id": 20154,
	                    "kit": "/rundb/api/v1/kitinfo/20071/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20154/"
	                },
	                {
	                    "barcode": "A26430",
	                    "id": 20155,
	                    "kit": "/rundb/api/v1/kitinfo/20071/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20155/"
	                },
	                {
	                    "barcode": "A26431",
	                    "id": 20156,
	                    "kit": "/rundb/api/v1/kitinfo/20071/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20156/"
	                },
	                {
	                    "barcode": "A26432",
	                    "id": 20157,
	                    "kit": "/rundb/api/v1/kitinfo/20071/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20157/"
	                }
	            ],
	            "resource_uri": "/rundb/api/v1/activeprotonsequencingkitinfo/20071/",
	            "runMode": "",
	            "samplePrep_instrumentType": "OT_IC_IA",
	            "uid": "SEQ0020"
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

