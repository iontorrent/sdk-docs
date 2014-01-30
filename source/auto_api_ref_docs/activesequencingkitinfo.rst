Activesequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activesequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activesequencingkitinfo.rst

Fields table
------------

================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field              help text                                                                                          default nullable readonly blank unique type    
================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**kitType**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**             Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**      Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**   Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**       Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

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
	        "total_count": 12, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activesequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "kitType": "SequencingKit", 
	            "description": "(100bp) Ion Sequencing Kit", 
	            "nucleotideType": "", 
	            "id": 20001, 
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
	            "uid": "SEQ0001", 
	            "resource_uri": "/rundb/api/v1/activesequencingkitinfo/20001/", 
	            "instrumentType": "pgm", 
	            "isActive": true, 
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

