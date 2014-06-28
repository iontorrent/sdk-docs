Activepgmsequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activepgmsequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activepgmsequencingkitinfo.rst

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
	        "total_count": 5, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activepgmsequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "kitType": "SequencingKit", 
	            "description": "(200bp) Ion PGM 200 Sequencing Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "pgm", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4474004", 
	                    "id": 20009, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20009/", 
	                    "kit": "/rundb/api/v1/kitinfo/20003/"
	                }, 
	                {
	                    "barcode": "4474005", 
	                    "id": 20010, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20010/", 
	                    "kit": "/rundb/api/v1/kitinfo/20003/"
	                }, 
	                {
	                    "barcode": "4474006", 
	                    "id": 20011, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20011/", 
	                    "kit": "/rundb/api/v1/kitinfo/20003/"
	                }, 
	                {
	                    "barcode": "4474007", 
	                    "id": 20012, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20012/", 
	                    "kit": "/rundb/api/v1/kitinfo/20003/"
	                }
	            ], 
	            "flowCount": 500, 
	            "applicationType": "", 
	            "uid": "SEQ0003", 
	            "resource_uri": "/rundb/api/v1/activepgmsequencingkitinfo/20003/", 
	            "id": 20003, 
	            "categories": "", 
	            "name": "IonPGM200Kit"
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

