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
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activepgmsequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "kitType": "SequencingKit", 
	            "description": "(100bp) Ion Sequencing Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "pgm", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4468997", 
	                    "id": 20001, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20001/", 
	                    "kit": "/rundb/api/v1/kitinfo/20001/"
	                }, 
	                {
	                    "barcode": "4468996", 
	                    "id": 20002, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20002/", 
	                    "kit": "/rundb/api/v1/kitinfo/20001/"
	                }, 
	                {
	                    "barcode": "4468995", 
	                    "id": 20003, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20003/", 
	                    "kit": "/rundb/api/v1/kitinfo/20001/"
	                }, 
	                {
	                    "barcode": "4468994", 
	                    "id": 20004, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20004/", 
	                    "kit": "/rundb/api/v1/kitinfo/20001/"
	                }
	            ], 
	            "flowCount": 260, 
	            "applicationType": "", 
	            "uid": "SEQ0001", 
	            "resource_uri": "/rundb/api/v1/activepgmsequencingkitinfo/20001/", 
	            "id": 20001, 
	            "categories": "", 
	            "name": "IonSeqKit"
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

