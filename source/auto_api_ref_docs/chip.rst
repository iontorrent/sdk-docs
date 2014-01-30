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
	            "prebasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 1000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "description": "P0", 
	            "prethumbnailbasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 100000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 100000", 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel on --region-size=80x112 --bkg-bfmask-update off --gpuWorkLoad 1 --total-timeout 600 --bkg-use-proton-well-correction off --bkg-exp-tail-fit off --bkg-pca-dark-matter on", 
	            "basecallerargs": "BaseCaller --keypass-filter on --phasing-residual-filter=2.0 --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --num-unfiltered 1000", 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=50x50 --beadfind-thumbnail 1 --bkg-use-proton-well-correction off --bkg-exp-tail-fit off --bkg-pca-dark-matter on", 
	            "thumbnailalignmentargs": "stage1 map4", 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel on --region-size=50x50 --bkg-bfmask-update off --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --bkg-use-proton-well-correction off --bkg-exp-tail-fit off --bkg-pca-dark-matter on", 
	            "instrumentType": "proton", 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=80x112 --total-timeout 600 --bkg-use-proton-well-correction off --bkg-exp-tail-fit off --bkg-pca-dark-matter on", 
	            "resource_uri": "/rundb/api/v1/chip/9/", 
	            "id": 9, 
	            "isActive": false, 
	            "name": "P1.0.19"
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

