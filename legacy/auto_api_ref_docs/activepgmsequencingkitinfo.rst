Activepgmsequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activepgmsequencingkitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	activepgmsequencingkitinfos = ts_api_response["objects"]
	
	for activepgmsequencingkitinfo in activepgmsequencingkitinfos:
	    print activepgmsequencingkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activepgmsequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "samplePrep_instrumentType": "IC", 
	            "templatingSize": "", 
	            "kitType": "SequencingKit", 
	            "description": "Ion PGM IC 200 Sequencing Kit", 
	            "name": "IonPGMIC200Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "pgm", 
	            "chipTypes": "", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4484084", 
	                    "id": 20119, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20119/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4488376", 
	                    "id": 20120, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20120/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4488375", 
	                    "id": 20121, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20121/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4484271", 
	                    "id": 20122, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20122/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4484080", 
	                    "id": 20116, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20116/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4484083", 
	                    "id": 20117, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20117/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }, 
	                {
	                    "barcode": "4484085", 
	                    "id": 20118, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20118/", 
	                    "kit": "/rundb/api/v1/kitinfo/20056/"
	                }
	            ], 
	            "flowCount": 500, 
	            "applicationType": "", 
	            "uid": "SEQ0016", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/activepgmsequencingkitinfo/20056/", 
	            "id": 20056, 
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

