.. _api_reference_activeioncheflibraryprepkitinfo:

Active Ion Chef Library Prep Kit Info  Resource
===============================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/schema/``
| 

.. include:: ../references_manual_extras/activeioncheflibraryprepkitinfo.rst

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
	        "next": "/rundb/api/v1/activeioncheflibraryprepkitinfo/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "applicationType": "AMPS",
	            "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	            "cartridgeExpirationDayLimit": null,
	            "categories": "filter_s5HidKit",
	            "chipTypes": "",
	            "defaultCartridgeUsageCount": null,
	            "description": "Precision ID Chef DL8",
	            "flowCount": 0,
	            "id": 20105,
	            "instrumentType": "",
	            "isActive": true,
	            "kitType": "LibraryPrepKit",
	            "libraryReadLength": 0,
	            "name": "Ion Chef HID Library V2",
	            "nucleotideType": "",
	            "parts": [
	                {
	                    "barcode": "A32926C",
	                    "id": 20245,
	                    "kit": "/rundb/api/v1/kitinfo/20105/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20245/"
	                },
	                {
	                    "barcode": "A33212",
	                    "id": 20261,
	                    "kit": "/rundb/api/v1/kitinfo/20105/",
	                    "resource_uri": "/rundb/api/v1/kitpart/20261/"
	                }
	            ],
	            "resource_uri": "/rundb/api/v1/activeioncheflibraryprepkitinfo/20105/",
	            "runMode": "",
	            "samplePrep_instrumentType": "IC",
	            "uid": "LPREP0003"
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

