Activeioncheflibraryprepkitinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/schema/``


.. include:: ../manual_api_ref_docs/activeioncheflibraryprepkitinfo.rst

Fields table
------------

============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                         help text                                                                                          default nullable readonly blank unique type    
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
**isActive**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**templatingSize**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**kitType**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**chipTypes**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**                   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**                     Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**                 Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applicationType**           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryReadLength**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/activeioncheflibraryprepkitinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	activeioncheflibraryprepkitinfos = ts_api_response["objects"]
	
	for activeioncheflibraryprepkitinfo in activeioncheflibraryprepkitinfos:
	    print activeioncheflibraryprepkitinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activeioncheflibraryprepkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "samplePrep_instrumentType": "IC", 
	            "templatingSize": "", 
	            "kitType": "LibraryPrepKit", 
	            "description": "Precision ID Chef DL8", 
	            "nucleotideType": "", 
	            "instrumentType": "", 
	            "chipTypes": "", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "A32926C", 
	                    "id": 20245, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20245/", 
	                    "kit": "/rundb/api/v1/kitinfo/20105/"
	                }, 
	                {
	                    "barcode": "A33212", 
	                    "id": 20261, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20261/", 
	                    "kit": "/rundb/api/v1/kitinfo/20105/"
	                }
	            ], 
	            "flowCount": 0, 
	            "applicationType": "AMPS", 
	            "uid": "LPREP0003", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/activeioncheflibraryprepkitinfo/20105/", 
	            "id": 20105, 
	            "categories": "filter_s5HidKit", 
	            "name": "Ion Chef HID Library V2"
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

