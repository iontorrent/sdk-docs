Experiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/experiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/experiment/schema/``


.. include:: ../manual_api_ref_docs/experiment.rst

Fields table
------------

====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                  help text                                                                                          default nullable readonly blank unique type     
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**isReverseRun**       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**    Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**user_ack**           Unicode string data. Ex: "Hello World"                                                             U       false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**             Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                 Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**           Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**                Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitbarcode** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas_set**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runtype**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pinnedRepResult**    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentBarcode**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**               Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isProton**           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expCompInfo**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**         A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**              Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**               A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**               A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**          Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**unique**             Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expDir**             Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**        Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**ftpStatus**          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**baselineRun**        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayName**        Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**     Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**             Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**rawdatastyle**       Unicode string data. Ex: "Hello World"                                                             single  true     false    false false  string   
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/experiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/experiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	experiments = ts_api_response["objects"]
	
	for experiment in experiments:
	    print experiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 17848, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/experiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "chipType": "", 
	            "user_ack": "U", 
	            "results": [], 
	            "sample": "E107855-a39g52_pool-L7007", 
	            "runMode": "", 
	            "reverse_primer": null, 
	            "seqKitBarcode": "", 
	            "id": 8766, 
	            "metaData": {}, 
	            "log": {}, 
	            "sequencekitbarcode": "", 
	            "resource_uri": "/rundb/api/v1/experiment/8766/", 
	            "eas_set": [
	                {
	                    "isEditable": true, 
	                    "hotSpotRegionBedFile": "", 
	                    "results": [], 
	                    "targetRegionBedFile": "", 
	                    "thumbnailalignmentargs": "", 
	                    "thumbnailanalysisargs": "", 
	                    "id": 9129, 
	                    "barcodedSamples": {}, 
	                    "reference": "hg19", 
	                    "isOneTimeOverride": false, 
	                    "analysisargs": "", 
	                    "thumbnailcalibrateargs": "", 
	                    "realign": false, 
	                    "selectedPlugins": {}, 
	                    "experiment": "/rundb/api/v1/experiment/8766/", 
	                    "barcodeKitName": "", 
	                    "beadfindargs": "", 
	                    "threePrimeAdapter": "", 
	                    "thumbnailbasecallerargs": "", 
	                    "status": "planned", 
	                    "prebasecallerargs": "", 
	                    "prethumbnailbasecallerargs": "", 
	                    "alignmentargs": "", 
	                    "isDuplicateReads": false, 
	                    "libraryKey": "", 
	                    "date": "2013-03-01T18:54:26.000817+00:00", 
	                    "libraryKitName": "", 
	                    "thumbnailbeadfindargs": "", 
	                    "calibrateargs": "", 
	                    "tfKey": "", 
	                    "libraryKitBarcode": null, 
	                    "base_recalibrate": true, 
	                    "basecallerargs": "", 
	                    "resource_uri": "/rundb/api/v1/experimentanalysissettings/9129/"
	                }
	            ], 
	            "runtype": "GENS", 
	            "platform": "PGM", 
	            "samples": [
	                {
	                    "status": "planned", 
	                    "sampleSets": [], 
	                    "description": null, 
	                    "displayedName": "E107855-a39g52_pool-L7007", 
	                    "experiments": [
	                        "/rundb/api/v1/experiment/8932/", 
	                        "/rundb/api/v1/experiment/8931/", 
	                        "/rundb/api/v1/experiment/8930/", 
	                        "/rundb/api/v1/experiment/8929/", 
	                        "/rundb/api/v1/experiment/8928/", 
	                        "/rundb/api/v1/experiment/8927/", 
	                        "/rundb/api/v1/experiment/8926/", 
	                        "/rundb/api/v1/experiment/8925/", 
	                        "/rundb/api/v1/experiment/8924/", 
	                        "/rundb/api/v1/experiment/8923/", 
	                        "/rundb/api/v1/experiment/8922/", 
	                        "/rundb/api/v1/experiment/8771/", 
	                        "/rundb/api/v1/experiment/8770/", 
	                        "/rundb/api/v1/experiment/8769/", 
	                        "/rundb/api/v1/experiment/8768/", 
	                        "/rundb/api/v1/experiment/8767/", 
	                        "/rundb/api/v1/experiment/8766/", 
	                        "/rundb/api/v1/experiment/8765/", 
	                        "/rundb/api/v1/experiment/8764/", 
	                        "/rundb/api/v1/experiment/8763/", 
	                        "/rundb/api/v1/experiment/8762/", 
	                        "/rundb/api/v1/experiment/8761/"
	                    ], 
	                    "externalId": "", 
	                    "date": "2013-02-27T23:47:37.000898+00:00", 
	                    "resource_uri": "/rundb/api/v1/sample/3961/", 
	                    "id": 3961, 
	                    "name": "E107855-a39g52_pool-L7007"
	                }
	            ], 
	            "pinnedRepResult": false, 
	            "reagentBarcode": "", 
	            "star": false, 
	            "isProton": "False", 
	            "expCompInfo": "", 
	            "resultDate": "2013-03-01T18:54:26.000936+00:00", 
	            "flows": 340, 
	            "plan": "/rundb/api/v1/plannedexperiment/90493/", 
	            "date": "2013-03-01T18:54:26.000877+00:00", 
	            "diskusage": 0, 
	            "unique": "e22b2870-72b2-426a-a7d9-47111a877879", 
	            "expDir": "", 
	            "autoAnalyze": true, 
	            "ftpStatus": "Complete", 
	            "flowsInOrder": "", 
	            "baselineRun": false, 
	            "displayName": "e22b2870-72b2-426a-a7d9-47111a877879", 
	            "notes": "OT2 a39g52_pool Lib7007 248bp lr2 ", 
	            "sequencekitname": "", 
	            "chipBarcode": "", 
	            "pgmName": "", 
	            "storageHost": null, 
	            "expName": "e22b2870-72b2-426a-a7d9-47111a877879", 
	            "status": "planned", 
	            "usePreBeadfind": false, 
	            "cycles": 0, 
	            "rawdatastyle": "single"
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

