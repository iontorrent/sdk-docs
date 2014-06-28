Sequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/sequencingkitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/sequencingkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	sequencingkitinfos = ts_api_response["objects"]
	
	for sequencingkitinfo in sequencingkitinfos:
	    print sequencingkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 18, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sequencingkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": false, 
	            "kitType": "SequencingKit", 
	            "description": "(200bp) Ion Sequencing 200 Kit", 
	            "nucleotideType": "", 
	            "instrumentType": "pgm", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4471258", 
	                    "id": 20005, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20005/", 
	                    "kit": "/rundb/api/v1/kitinfo/20002/"
	                }, 
	                {
	                    "barcode": "4471257", 
	                    "id": 20006, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20006/", 
	                    "kit": "/rundb/api/v1/kitinfo/20002/"
	                }, 
	                {
	                    "barcode": "4471259", 
	                    "id": 20007, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20007/", 
	                    "kit": "/rundb/api/v1/kitinfo/20002/"
	                }, 
	                {
	                    "barcode": "4471260", 
	                    "id": 20008, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20008/", 
	                    "kit": "/rundb/api/v1/kitinfo/20002/"
	                }
	            ], 
	            "flowCount": 520, 
	            "applicationType": "", 
	            "uid": "SEQ0002", 
	            "resource_uri": "/rundb/api/v1/sequencingkitinfo/20002/", 
	            "id": 20002, 
	            "categories": "", 
	            "name": "IonSeq200Kit"
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

