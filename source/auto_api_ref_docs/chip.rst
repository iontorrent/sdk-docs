Chip Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/chip/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/chip/schema/``


.. include:: ../manual_api_ref_docs/chip.rst

Fields table
------------

================== ====================================== ======= ======== ======== ===== ====== ======= 
field              help text                              default nullable readonly blank unique type    
================== ====================================== ======= ======== ======== ===== ====== ======= 
**name**           Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**    Unicode string data. Ex: "Hello World"         false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**             Integer data. Ex: 2673                         false    false    true  true   integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**slots**          Integer data. Ex: 2673                 n/a     false    false    false false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**       Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**   Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/chip/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/chip/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	chips = ts_api_response["objects"]
	
	for chip in chips:
	    print chip
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 20, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/chip/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "slots": 1, 
	            "calibrateargs": "calibrate", 
	            "prebasecallerargs": "BaseCaller", 
	            "description": "PIv2", 
	            "prethumbnailbasecallerargs": "BaseCaller", 
	            "alignmentargs": "", 
	            "thumbnailbasecallerargs": "BaseCaller", 
	            "analysisargs": "Analysis", 
	            "basecallerargs": "BaseCaller", 
	            "thumbnailbeadfindargs": "justBeadFind", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "Analysis", 
	            "instrumentType": "proton", 
	            "beadfindargs": "justBeadFind", 
	            "resource_uri": "/rundb/api/v1/chip/16/", 
	            "id": 16, 
	            "isActive": false, 
	            "name": "900AMPS_EXOME"
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

