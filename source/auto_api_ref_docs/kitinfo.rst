Kitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/kitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/kitinfo/schema/``


.. include:: ../manual_api_ref_docs/kitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/kitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/kitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	kitinfos = ts_api_response["objects"]
	
	for kitinfo in kitinfos:
	    print kitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 67, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/kitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "kitType": "ControlSequenceKitType", 
	            "description": "ERCC Mix 1", 
	            "nucleotideType": "rna", 
	            "instrumentType": "", 
	            "runMode": "", 
	            "parts": [], 
	            "flowCount": 0, 
	            "applicationType": "RNA", 
	            "uid": "CONSEQ0006", 
	            "resource_uri": "/rundb/api/v1/kitinfo/20061/", 
	            "id": 20061, 
	            "categories": "", 
	            "name": "ERCC Mix 1"
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

