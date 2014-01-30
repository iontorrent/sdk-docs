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
**templateKitName**            Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**prebasecallerargs**          Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryKitName**             Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                       Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**chipType**                   Unicode string data. Ex: "Hello World"         false    false    false false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**alignmentargs**              Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailbasecallerargs**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequenceKitName**            Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**analysisargs**               Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**basecallerargs**             Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailanalysisargs**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**chip_default**               Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailalignmentargs**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrepKitName**          Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**active**                     Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**prethumbnailbasecallerargs** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**beadfindargs**               Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**thumbnailbeadfindargs**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                         Integer data. Ex: 2673                         false    false    true  true   integer 
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
	            "templateKitName": "", 
	            "prebasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 1000 --calibration-training=100000 --flow-signals-type scaled-residual --max-phasing-levels 2", 
	            "libraryKitName": "", 
	            "name": "AmpliseqExome_V3", 
	            "chipType": "P1.1.17", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 100000", 
	            "sequenceKitName": "ProtonI200Kit-v3", 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel on --region-size=216x224 --bkg-bfmask-update off --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "basecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 1000", 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel on --region-size=100x100 --bkg-bfmask-update off --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "chip_default": false, 
	            "thumbnailalignmentargs": "stage1 map4", 
	            "samplePrepKitName": "Ion AmpliSeq Exome Kit", 
	            "active": true, 
	            "prethumbnailbasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 100000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216x224 --total-timeout 600", 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100x100 --beadfind-thumbnail 1", 
	            "id": 18, 
	            "resource_uri": "/rundb/api/v1/analysisargs/18/"
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

