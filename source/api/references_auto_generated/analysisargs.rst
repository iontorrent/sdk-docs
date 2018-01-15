.. _api_reference_analysisargs:

Analysis Args  Resource
=======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/analysisargs/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/analysisargs/schema/``
| 

.. include:: ../references_manual_extras/analysisargs.rst

Resource Fields
---------------

============================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                          help text                                                                      default nullable readonly blank unique type     
============================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**ionstatsargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chipType**                   Unicode string data. Ex: "Hello World"                                                 false    false    false false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creator**                    A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailionstatsargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailalignmentargs**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailanalysisargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                         Integer data. Ex: 2673                                                                 false    false    true  true   integer  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**               A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    true     false    false false  datetime 
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sequenceKitName**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**analysisargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailcalibrateargs**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applGroup**                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chip_default**               Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**           A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    true     false    false false  datetime 
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**beadfindargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templateKitName**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**prebasecallerargs**          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false true   string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**prethumbnailbasecallerargs** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applType**                   A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**alignmentargs**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailbasecallerargs**    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**active**                     Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystem**                   Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailbeadfindargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**calibrateargs**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libraryKitName**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**name**                       Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**basecallerargs**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedUser**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**               Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
============================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 117, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/analysisargs/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "ionstatsargs": "ionstats alignment", 
	            "chipType": "314", 
	            "creator": null, 
	            "thumbnailionstatsargs": "", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "samplePrepKitName": "", 
	            "id": 1, 
	            "creationDate": "2017-12-05T00:10:34.000865+00:00", 
	            "sequenceKitName": "", 
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_314_analysis.json", 
	            "thumbnailcalibrateargs": "", 
	            "applGroup": null, 
	            "chip_default": true, 
	            "lastModifiedDate": "2017-12-05T00:10:34.000865+00:00", 
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_314_beadfind.json", 
	            "templateKitName": "", 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20", 
	            "description": "Ion 314 chip v2 analysis arguments", 
	            "prethumbnailbasecallerargs": "", 
	            "applType": null, 
	            "alignmentargs": "tmap mapall ... stage1 map4", 
	            "thumbnailbasecallerargs": "", 
	            "active": true, 
	            "isSystem": true, 
	            "thumbnailbeadfindargs": "", 
	            "calibrateargs": "Calibration", 
	            "libraryKitName": "", 
	            "name": "ion_default_314", 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 20", 
	            "lastModifiedUser": null, 
	            "resource_uri": "/rundb/api/v1/analysisargs/1/"
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

