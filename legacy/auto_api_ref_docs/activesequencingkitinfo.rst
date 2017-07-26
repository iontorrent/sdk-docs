Activesequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activesequencingkitinfo.rst

Fields table
------------

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

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	activesequencingkitinfos = ts_api_response["objects"]
	
	for activesequencingkitinfo in activesequencingkitinfos:
	    print activesequencingkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 17, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activesequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "samplePrep_instrumentType": "", 
	            "templatingSize": "", 
	            "kitType": "SequencingKit", 
	            "description": "Ion PI Sequencing 200 Kit v2", 
	            "name": "ProtonI200Kit-v2", 
	            "nucleotideType": "", 
	            "instrumentType": "proton", 
	            "chipTypes": "900;P1.0.19;P1.0.20;P1.1.17;P1.1.541;P1.2.18;P2.0.1;P2.1.1;P2.3.1", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4485149", 
	                    "id": 20094, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20094/", 
	                    "kit": "/rundb/api/v1/kitinfo/20044/"
	                }, 
	                {
	                    "barcode": "4485521", 
	                    "id": 20095, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20095/", 
	                    "kit": "/rundb/api/v1/kitinfo/20044/"
	                }, 
	                {
	                    "barcode": "4484082", 
	                    "id": 20096, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20096/", 
	                    "kit": "/rundb/api/v1/kitinfo/20044/"
	                }, 
	                {
	                    "barcode": "4482282", 
	                    "id": 20078, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20078/", 
	                    "kit": "/rundb/api/v1/kitinfo/20044/"
	                }, 
	                {
	                    "barcode": "4482284", 
	                    "id": 20079, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20079/", 
	                    "kit": "/rundb/api/v1/kitinfo/20044/"
	                }
	            ], 
	            "flowCount": 500, 
	            "applicationType": "", 
	            "uid": "SEQ0012", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/activesequencingkitinfo/20044/", 
	            "id": 20044, 
	            "categories": "readLengthDerivableFromFlows;", 
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

