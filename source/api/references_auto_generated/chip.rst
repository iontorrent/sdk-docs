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
**name**                 Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                   Integer data. Ex: 2673                         false    false    true  true   integer 
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**earlyDatFileDeletion** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**slots**                Integer data. Ex: 2673                 n/a     false    false    false false  integer 
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**         Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**       Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**             Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**          Unicode string data. Ex: "Hello World"         false    false    false false  string  
======================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 28, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/chip/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "ionstatsargs": "ionstats alignment", 
	            "thumbnailionstatsargs": "", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "slots": 1, 
	            "id": 1, 
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_314_analysis.json", 
	            "thumbnailcalibrateargs": "", 
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_314_beadfind.json", 
	            "instrumentType": "pgm", 
	            "prebasecallerargs": "BaseCaller --barcode-filter-minreads 20", 
	            "description": "314v2", 
	            "prethumbnailbasecallerargs": "", 
	            "alignmentargs": "tmap mapall ... stage1 map4", 
	            "thumbnailbasecallerargs": "", 
	            "isActive": true, 
	            "thumbnailbeadfindargs": "", 
	            "calibrateargs": "Calibration", 
	            "name": "314", 
	            "basecallerargs": "BaseCaller --barcode-filter-minreads 20", 
	            "earlyDatFileDeletion": "", 
	            "resource_uri": "/rundb/api/v1/chip/1/"
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

