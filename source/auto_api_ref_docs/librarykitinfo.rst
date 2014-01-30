Librarykitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/librarykitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/librarykitinfo/schema/``


.. include:: ../manual_api_ref_docs/librarykitinfo.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/librarykitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/librarykitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	librarykitinfos = ts_api_response["objects"]
	
	for librarykitinfo in librarykitinfos:
	    print librarykitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 16, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/librarykitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "kitType": "LibraryKit", 
	            "description": "Ion Fragment Library Kit", 
	            "nucleotideType": "dna", 
	            "id": 20004, 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "4462907", 
	                    "id": 20013, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20013/", 
	                    "kit": "/rundb/api/v1/kitinfo/20004/"
	                }
	            ], 
	            "flowCount": 0, 
	            "uid": "LIB0001", 
	            "resource_uri": "/rundb/api/v1/librarykitinfo/20004/", 
	            "instrumentType": "", 
	            "isActive": false, 
	            "name": "IonFragmentLibKit"
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

