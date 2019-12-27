.. _api_reference_sequencingkitinfo:

Sequencing Kit Info  Resource
=============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/schema/``
| 

.. include:: ../references_manual_extras/sequencingkitinfo.rst

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
	        "next": "/rundb/api/v1/sequencingkitinfo/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 27
	    },
	    "objects": [
	        {
	            "applicationType": "AMPS",
	            "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	            "cartridgeExpirationDayLimit": null,
	            "categories": "filter_s5HidKit",
	            "chipTypes": "",
	            "defaultCartridgeUsageCount": null,
	            "defaultFlowOrder": null,
	            "description": "Precision ID S5 Sequencing Kit",
	            "flowCount": 650,
	            "id": 20111,
	            "instrumentType": "S5",
	            "isActive": true,
	            "kitType": "SequencingKit",
	            "libraryReadLength": 0,
	            "name": "precisionIDS5Kit",
	            "nucleotideType": "",
	            "parts": [
	                {
	                    "barcode": "100041073B",
	                    "id": 20236,
	                    "kit": "/rundb/api/v1/kitinfo/20111/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20236/"
	                },
	                {
	                    "barcode": "100041074B",
	                    "id": 20237,
	                    "kit": "/rundb/api/v1/kitinfo/20111/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20237/"
	                },
	                {
	                    "barcode": "A33208",
	                    "id": 20260,
	                    "kit": "/rundb/api/v1/kitinfo/20111/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20260/"
	                },
	                {
	                    "barcode": "100049484",
	                    "id": 20263,
	                    "kit": "/rundb/api/v1/kitinfo/20111/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20263/"
	                }
	            ],
	            "resource_uri": "/rundb/api/v1/sequencingkitinfo/20111/",
	            "runMode": "",
	            "samplePrep_instrumentType": "",
	            "uid": "SEQ0028"
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

