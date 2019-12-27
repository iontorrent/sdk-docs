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
**active**                     Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**alignmentargs**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**analysisargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applCategory**               Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applGroup**                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applType**                   A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**basecallerargs**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**beadfindargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**calibrateargs**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chipType**                   Unicode string data. Ex: "Hello World"                                                 false    false    false false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chip_default**               Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**               A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    true     false    false false  datetime 
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creator**                    A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false true   string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                         Integer data. Ex: 2673                                                                 false    false    true  true   integer  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**ionstatsargs**               Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystem**                   Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**           A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    true     false    false false  datetime 
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedUser**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libraryKitName**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**name**                       Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**prebasecallerargs**          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**prethumbnailbasecallerargs** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**               Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sequenceKitName**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templateKitName**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailalignmentargs**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailanalysisargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailbasecallerargs**    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailbeadfindargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailcalibrateargs**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**thumbnailionstatsargs**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
============================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/analysisargs/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 106
	    },
	    "objects": [
	        {
	            "active": false,
	            "alignmentargs": "",
	            "analysisargs": "",
	            "applCategory": null,
	            "applGroup": null,
	            "applType": null,
	            "basecallerargs": "",
	            "beadfindargs": "",
	            "calibrateargs": "",
	            "chipType": "",
	            "chip_default": false,
	            "creationDate": "2019-11-08T21:40:55.000156+00:00",
	            "creator": null,
	            "description": "All System args will use lower pks",
	            "id": 10000,
	            "ionstatsargs": "",
	            "isSystem": false,
	            "lastModifiedDate": "2019-11-08T21:40:55.000156+00:00",
	            "lastModifiedUser": null,
	            "libraryKitName": "",
	            "name": "system_placeholder",
	            "prebasecallerargs": "",
	            "prethumbnailbasecallerargs": "",
	            "resource_uri": "/rundb/api/v1/analysisargs/10000/",
	            "samplePrepKitName": "",
	            "sequenceKitName": "",
	            "templateKitName": "",
	            "thumbnailalignmentargs": "",
	            "thumbnailanalysisargs": "",
	            "thumbnailbasecallerargs": "",
	            "thumbnailbeadfindargs": "",
	            "thumbnailcalibrateargs": "",
	            "thumbnailionstatsargs": ""
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

