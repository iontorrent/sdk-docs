Runtype Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/runtype/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/runtype/schema/``


.. include:: ../manual_api_ref_docs/runtype.rst

Fields table
------------

===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                 help text                                                                                          default nullable readonly blank unique type    
===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**applicationGroups** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**    Unicode string data. Ex: "Hello World"                                                             dna     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**barcode**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**meta**              Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runType**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**alternate_name**    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
--------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
===================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/runtype/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/runtype/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	runtypes = ts_api_response["objects"]
	
	for runtype in runtypes:
	    print runtype
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 8, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/runtype/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "applicationGroups": [
	                "/rundb/api/v1/applicationgroup/1/", 
	                "/rundb/api/v1/applicationgroup/3/", 
	                "/rundb/api/v1/applicationgroup/4/"
	            ], 
	            "description": "Generic Sequencing", 
	            "nucleotideType": "", 
	            "barcode": "", 
	            "meta": {}, 
	            "runType": "GENS", 
	            "id": 1, 
	            "alternate_name": "Other", 
	            "resource_uri": "/rundb/api/v1/runtype/1/"
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

