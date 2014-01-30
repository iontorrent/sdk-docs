Ionchefprepkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/ionchefprepkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/ionchefprepkitinfo/schema/``


.. include:: ../manual_api_ref_docs/ionchefprepkitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/ionchefprepkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/ionchefprepkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	ionchefprepkitinfos = ts_api_response["objects"]
	
	for ionchefprepkitinfo in ionchefprepkitinfos:
	    print ionchefprepkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/ionchefprepkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "kitType": "IonChefPrepKit", 
	            "description": "Ion PI IC 200 Kit", 
	            "nucleotideType": "", 
	            "id": 20057, 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "100023442", 
	                    "id": 20130, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20130/", 
	                    "kit": "/rundb/api/v1/kitinfo/20057/"
	                }, 
	                {
	                    "barcode": "100022895", 
	                    "id": 20124, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20124/", 
	                    "kit": "/rundb/api/v1/kitinfo/20057/"
	                }, 
	                {
	                    "barcode": "100022894", 
	                    "id": 20125, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20125/", 
	                    "kit": "/rundb/api/v1/kitinfo/20057/"
	                }, 
	                {
	                    "barcode": "02", 
	                    "id": 20126, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20126/", 
	                    "kit": "/rundb/api/v1/kitinfo/20057/"
	                }
	            ], 
	            "flowCount": 0, 
	            "uid": "ICPREP0002", 
	            "resource_uri": "/rundb/api/v1/ionchefprepkitinfo/20057/", 
	            "instrumentType": "proton", 
	            "isActive": true, 
	            "name": "Ion PI IC 200 Kit"
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

