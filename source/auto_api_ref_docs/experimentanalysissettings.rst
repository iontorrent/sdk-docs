Experimentanalysissettings Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/experimentanalysissettings/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/experimentanalysissettings/schema/``


.. include:: ../manual_api_ref_docs/experimentanalysissettings.rst

Fields table
------------

============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                          help text                                                                                          default nullable readonly blank unique type     
============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**isEditable**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**thumbnailalignmentargs**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**thumbnailanalysisargs**      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                         Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**            Unicode string data. Ex: "Hello World"                                                             {}      true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reference**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isOneTimeOverride**          Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysisargs**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**            Unicode string data. Ex: "Hello World"                                                             {}      true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                 A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeKitName**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**beadfindargs**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**threePrimeAdapter**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**thumbnailbasecallerargs**    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**prebasecallerargs**          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**prethumbnailbasecallerargs** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**alignmentargs**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**           Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKitName**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**thumbnailbeadfindargs**      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKitBarcode**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**basecallerargs**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**               Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/experimentanalysissettings/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/experimentanalysissettings/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	experimentanalysissettingss = ts_api_response["objects"]
	
	for experimentanalysissettings in experimentanalysissettingss:
	    print experimentanalysissettings
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11564, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/experimentanalysissettings/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isEditable": true, 
	            "hotSpotRegionBedFile": "", 
	            "results": [], 
	            "targetRegionBedFile": "", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "id": 4, 
	            "barcodedSamples": {}, 
	            "reference": "", 
	            "isOneTimeOverride": false, 
	            "analysisargs": "", 
	            "selectedPlugins": {}, 
	            "experiment": "/rundb/api/v1/experiment/10955/", 
	            "barcodeKitName": "", 
	            "beadfindargs": "", 
	            "threePrimeAdapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "thumbnailbasecallerargs": "", 
	            "status": "planned", 
	            "prebasecallerargs": "", 
	            "prethumbnailbasecallerargs": "", 
	            "alignmentargs": "", 
	            "isDuplicateReads": false, 
	            "libraryKey": "TCAG", 
	            "date": "2012-11-20T13:49:55.000699+00:00", 
	            "libraryKitName": "Ion Xpress Plus Fragment Library Kit", 
	            "thumbnailbeadfindargs": "", 
	            "tfKey": "", 
	            "libraryKitBarcode": null, 
	            "basecallerargs": "", 
	            "resource_uri": "/rundb/api/v1/experimentanalysissettings/4/"
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

