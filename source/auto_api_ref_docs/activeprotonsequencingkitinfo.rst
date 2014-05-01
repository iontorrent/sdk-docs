Activeprotonsequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activeprotonsequencingkitinfo.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field               help text                                                                                          default nullable readonly blank unique type    
=================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**isActive**        Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**kitType**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**           Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**       Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applicationType** Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**             Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**      Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	activeprotonsequencingkitinfos = ts_api_response["objects"]
	
	for activeprotonsequencingkitinfo in activeprotonsequencingkitinfos:
	    print activeprotonsequencingkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 4, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activeprotonsequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "kitType": "SequencingKit", 
	            "description": "Ion PI Sequencing 200 Kit v2", 
	            "nucleotideType": "", 
	            "instrumentType": "proton", 
	            "runMode": "", 
	            "parts": [
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
	                }, 
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
	                }
	            ], 
	            "flowCount": 500, 
	            "applicationType": "", 
	            "uid": "SEQ0012", 
	            "resource_uri": "/rundb/api/v1/activeprotonsequencingkitinfo/20044/", 
	            "id": 20044, 
	            "categories": "", 
	            "name": "ProtonI200Kit-v2"
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

