Activeprotonsequencingkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activeprotonsequencingkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activeprotonsequencingkitinfo.rst

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
	            "kitType": "SequencingKit", 
	            "description": "Ion PI Sequencing 200 Kit v2 with XT", 
	            "nucleotideType": "", 
	            "id": 20046, 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4487053", 
	                    "id": 20099, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20099/", 
	                    "kit": "/rundb/api/v1/kitinfo/20046/"
	                }
	            ], 
	            "flowCount": 520, 
	            "uid": "SEQ0013", 
	            "resource_uri": "/rundb/api/v1/activeprotonsequencingkitinfo/20046/", 
	            "instrumentType": "proton", 
	            "isActive": true, 
	            "name": "ProtonI200Kit-v2XT"
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

