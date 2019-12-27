.. _api_reference_chip:

Chip Resource
=============

| Resource URL ``http://mytorrentserver/rundb/api/v1/chip/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/chip/schema/``
| 

.. include:: ../references_manual_extras/chip.rst

Resource Fields
---------------

======================== ====================================== ======= ======== ======== ===== ====== ======= 
field                    help text                              default nullable readonly blank unique type    
======================== ====================================== ======= ======== ======== ===== ====== ======= 
**description**          Unicode string data. Ex: "Hello World"         false    false    false false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**earlyDatFileDeletion** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                   Integer data. Ex: 2673                         false    false    true  true   integer 
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**       Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**             Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                 Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**         Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**slots**                Integer data. Ex: 2673                 n/a     false    false    false false  integer 
======================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/chip/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 15
	    },
	    "objects": [
	        {
	            "alignmentargs": "tmap mapall ... stage1 map4",
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_520_analysis.json",
	            "basecallerargs": "BaseCaller --trim-qual-cutoff 15 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --num-unfiltered 1000 --barcode-filter-postpone 1 --qual-filter true --qual-filter-slope 0.040 --qual-filter-offset 1.0 --wells-normalization on",
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_520_beadfind.json",
	            "calibrateargs": "Calibration --num-calibration-regions 1,1",
	            "description": "510",
	            "earlyDatFileDeletion": "",
	            "id": 28,
	            "instrumentType": "S5",
	            "ionstatsargs": "ionstats alignment",
	            "isActive": true,
	            "name": "510",
	            "prebasecallerargs": "BaseCaller --trim-qual-cutoff 15 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on",
	            "prethumbnailbasecallerargs": "BaseCaller --trim-qual-cutoff 15 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on",
	            "resource_uri": "/rundb/api/v1/chip/28/",
	            "slots": 1,
	            "thumbnailalignmentargs": "tmap mapall ... stage1 map4",
	            "thumbnailanalysisargs": "Analysis --args-json /opt/ion/config/args_520_analysis.json --thumbnail true",
	            "thumbnailbasecallerargs": "BaseCaller --trim-qual-cutoff 15 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --qual-filter true --qual-filter-slope 0.040 --qual-filter-offset 1.0 --wells-normalization on",
	            "thumbnailbeadfindargs": "justBeadFind --args-json /opt/ion/config/args_520_beadfind.json --thumbnail true",
	            "thumbnailcalibrateargs": "Calibration",
	            "thumbnailionstatsargs": "ionstats alignment"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

