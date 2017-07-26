.. _api_reference_sequencingkitinfo:

Sequencing Kit Info  Resource
=============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/schema/``
| 

.. include:: ../references_manual_extras/sequencingkitinfo.rst

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
	        "total_count": 28, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": false, 
	            "samplePrep_instrumentType": "", 
	            "templatingSize": "", 
	            "kitType": "SequencingKit", 
	            "description": "Ion PI Sequencing 200 Kit", 
	            "name": "ProtonI200Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "proton", 
	            "chipTypes": "900;P1.0.19;P1.0.20;P1.1.17;P1.1.541;P1.2.18;P2.0.1;P2.1.1;P2.3.1", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4482283", 
	                    "id": 20077, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20077/", 
	                    "kit": "/rundb/api/v1/kitinfo/20041/"
	                }, 
	                {
	                    "barcode": "4482285", 
	                    "id": 20080, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20080/", 
	                    "kit": "/rundb/api/v1/kitinfo/20041/"
	                }
	            ], 
	            "flowCount": 400, 
	            "applicationType": "", 
	            "uid": "SEQ0011", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/sequencingkitinfo/20041/", 
	            "id": 20041, 
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

