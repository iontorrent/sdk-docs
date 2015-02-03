Analysisargs Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/analysisargs/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/analysisargs/schema/``


.. include:: ../manual_api_ref_docs/analysisargs.rst

Fields table
------------

============================== ====================================== ======= ======== ======== ===== ====== ======= 
field                          help text                              default nullable readonly blank unique type    
============================== ====================================== ======= ======== ======== ===== ====== ======= 
**chipType**                   Unicode string data. Ex: "Hello World"         false    false    false false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailalignmentargs**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailanalysisargs**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrepKitName**          Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                         Integer data. Ex: 2673                         false    false    true  true   integer 
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequenceKitName**            Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**analysisargs**               Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailcalibrateargs**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**chip_default**               Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**beadfindargs**               Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**templateKitName**            Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**prebasecallerargs**          Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**prethumbnailbasecallerargs** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**alignmentargs**              Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailbasecallerargs**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**active**                     Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailbeadfindargs**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**calibrateargs**              Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryKitName**             Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                       Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**basecallerargs**             Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**               Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
============================== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/analysisargs/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/analysisargs/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	analysisargss = ts_api_response["objects"]
	
	for analysisargs in analysisargss:
	    print analysisargs
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 19, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/analysisargs/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipType": "314", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "samplePrepKitName": "", 
	            "id": 1, 
	            "sequenceKitName": "", 
	            "analysisargs": "Analysis --from-beadfind --use-alternative-etbR-equation", 
	            "thumbnailcalibrateargs": "", 
	            "chip_default": true, 
	            "beadfindargs": "justBeadFind", 
	            "templateKitName": "", 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20", 
	            "prethumbnailbasecallerargs": "", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "", 
	            "active": true, 
	            "thumbnailbeadfindargs": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "libraryKitName": "", 
	            "name": "default_314", 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20", 
	            "resource_uri": "/rundb/api/v1/analysisargs/1/"
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

