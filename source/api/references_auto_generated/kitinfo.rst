.. _api_reference_kitinfo:

Kit Info  Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/kitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/kitinfo/schema/``
| 

.. include:: ../references_manual_extras/kitinfo.rst

Resource Fields
---------------

============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                         help text                                                                                          default nullable readonly blank unique type    
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
**isActive**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**templatingSize**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**kitType**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**chipTypes**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**                   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**                     Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**                 Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applicationType**           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryReadLength**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultFlowOrder**          A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related 
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 112, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/kitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": false, 
	            "samplePrep_instrumentType": "OT", 
	            "templatingSize": "", 
	            "kitType": "TemplatingKit", 
	            "description": "Ion PI Template OT2 200 Kit", 
	            "name": "Ion PI Template OT2 200 Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "proton", 
	            "chipTypes": "900;P1.0.19;P1.0.20;P1.1.17;P1.1.541;P1.2.18;P2.0.1;P2.1.1;P2.3.1", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4482286", 
	                    "id": 20074, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20074/", 
	                    "kit": "/rundb/api/v1/kitinfo/20038/"
	                }, 
	                {
	                    "barcode": "4482287", 
	                    "id": 20081, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20081/", 
	                    "kit": "/rundb/api/v1/kitinfo/20038/"
	                }, 
	                {
	                    "barcode": "4482288", 
	                    "id": 20082, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20082/", 
	                    "kit": "/rundb/api/v1/kitinfo/20038/"
	                }, 
	                {
	                    "barcode": "4482289", 
	                    "id": 20083, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20083/", 
	                    "kit": "/rundb/api/v1/kitinfo/20038/"
	                }, 
	                {
	                    "barcode": "4482297", 
	                    "id": 20084, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20084/", 
	                    "kit": "/rundb/api/v1/kitinfo/20038/"
	                }
	            ], 
	            "flowCount": 0, 
	            "applicationType": "", 
	            "uid": "TEMPLT0005", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/kitinfo/20038/", 
	            "id": 20038, 
	            "categories": "", 
	            "defaultFlowOrder": null
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

