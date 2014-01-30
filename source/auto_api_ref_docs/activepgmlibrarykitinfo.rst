Activepgmlibrarykitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activepgmlibrarykitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activepgmlibrarykitinfo/schema/``


.. include:: ../manual_api_ref_docs/activepgmlibrarykitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/activepgmlibrarykitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/activepgmlibrarykitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	activepgmlibrarykitinfos = ts_api_response["objects"]
	
	for activepgmlibrarykitinfo in activepgmlibrarykitinfos:
	    print activepgmlibrarykitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activepgmlibrarykitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "kitType": "LibraryKit", 
	            "description": "Ion Fragment Library Kit", 
	            "nucleotideType": "dna", 
	            "id": 20005, 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4466464", 
	                    "id": 20014, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20014/", 
	                    "kit": "/rundb/api/v1/kitinfo/20005/"
	                }
	            ], 
	            "flowCount": 0, 
	            "uid": "LIB0002", 
	            "resource_uri": "/rundb/api/v1/activepgmlibrarykitinfo/20005/", 
	            "instrumentType": "", 
	            "isActive": true, 
	            "name": "IonFragmentLibKit2"
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

