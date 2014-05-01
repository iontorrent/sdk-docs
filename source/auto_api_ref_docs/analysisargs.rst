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
	        "total_count": 25, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/analysisargs/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipType": "900v2", 
	            "thumbnailalignmentargs": "stage1 map4", 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1", 
	            "samplePrepKitName": "", 
	            "id": 8, 
	            "sequenceKitName": "", 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "chip_default": true, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "templateKitName": "", 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --calibration-training=100000 --flow-signals-type scaled-residual --max-phasing-levels 2", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000", 
	            "active": true, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "libraryKitName": "", 
	            "name": "default_900v2", 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "resource_uri": "/rundb/api/v1/analysisargs/8/"
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

