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
	        "total_count": 19, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/chip/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "slots": 1, 
	            "calibrateargs": "calibrate --skipDroop", 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "description": "316v2", 
	            "prethumbnailbasecallerargs": "", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "", 
	            "analysisargs": "Analysis --from-beadfind --use-alternative-etbR-equation", 
	            "thumbnailcalibrateargs": "", 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20", 
	            "thumbnailbeadfindargs": "", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "instrumentType": "pgm", 
	            "beadfindargs": "justBeadFind", 
	            "resource_uri": "/rundb/api/v1/chip/6/", 
	            "id": 6, 
	            "isActive": true, 
	            "name": "316v2"
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

