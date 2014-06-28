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
	        "total_count": 21008, 
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
	            "sample": "E115943-lq204-01-L8095", 
	            "runMode": "", 
	            "reverse_primer": null, 
	            "seqKitBarcode": "", 
	            "id": 10132, 
	            "metaData": {}, 
	            "log": {}, 
	            "sequencekitbarcode": "", 
	            "resource_uri": "/rundb/api/v1/experiment/10132/", 
	            "eas_set": [
	                {
	                    "isEditable": true, 
	                    "hotSpotRegionBedFile": "", 
	                    "results": [], 
	                    "targetRegionBedFile": "/results/uploads/BED/19/hg19/unmerged/detail/Ion-TargetSeq-Exome-50Mb-hg19_revA.bed", 
	                    "thumbnailalignmentargs": "", 
	                    "thumbnailanalysisargs": "", 
	                    "id": 10575, 
	                    "barcodedSamples": {}, 
	                    "reference": "hg19", 
	                    "isOneTimeOverride": false, 
	                    "analysisargs": "", 
	                    "thumbnailcalibrateargs": "", 
	                    "realign": false, 
	                    "selectedPlugins": {
	                        "pinsPerFlow": {
	                            "name": "pinsPerFlow"
	                        }, 
	                        "duplicateReads_useZC": {
	                            "name": "duplicateReads_useZC"
	                        }, 
	                        "libClonality": {
	                            "name": "libClonality"
	                        }, 
	                        "ProtonErrors": {
	                            "name": "ProtonErrors"
	                        }, 
	                        "PhasingReport": {
	                            "name": "PhasingReport"
	                        }, 
	                        "detailedReport": {
	                            "name": "detailedReport"
	                        }, 
	                        "extended_chip_check": {
	                            "name": "extended_chip_check"
	                        }, 
	                        "1_Torrent_Accuracy": {
	                            "name": "1_Torrent_Accuracy"
	                        }, 
	                        "ConversionRate": {
	                            "name": "ConversionRate"
	                        }, 
	                        "rawTrace": {
	                            "name": "rawTrace"
	                        }, 
	                        "filterAndTrim": {
	                            "name": "filterAndTrim"
	                        }, 
	                        "fsRecalibration": {
	                            "name": "fsRecalibration"
	                        }, 
	                        "timingPerformance": {
	                            "name": "timingPerformance"
	                        }, 
	                        "NucRiseParams": {
	                            "name": "NucRiseParams"
	                        }, 
	                        "AvgTrace": {
	                            "name": "AvgTrace"
	                        }, 
	                        "autoCal": {
	                            "name": "autoCal"
	                        }, 
	                        "flowCell": {
	                            "name": "flowCell"
	                        }, 
	                        "chipDiagnostics": {
	                            "name": "chipDiagnostics"
	                        }, 
	                        "rawPlots": {
	                            "name": "rawPlots"
	                        }, 
	                        "spatialPlots": {
	                            "name": "spatialPlots"
	                        }, 
	                        "RateMapEDA": {
	                            "name": "RateMapEDA"
	                        }, 
	                        "barcodeMixtureAnalysis": {
	                            "name": "barcodeMixtureAnalysis"
	                        }, 
	                        "z_homopolymerAnalysis": {
	                            "name": "z_homopolymerAnalysis"
	                        }, 
	                        "separator": {
	                            "name": "separator"
	                        }, 
	                        "GC_seq_performance": {
	                            "name": "GC_seq_performance"
	                        }, 
	                        "flowErr": {
	                            "name": "flowErr"
	                        }
	                    }, 
	                    "experiment": "/rundb/api/v1/experiment/10132/", 
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
	                    "date": "2013-05-15T18:30:24.000115+00:00", 
	                    "libraryKitName": "", 
	                    "thumbnailbeadfindargs": "", 
	                    "calibrateargs": "", 
	                    "tfKey": "", 
	                    "libraryKitBarcode": null, 
	                    "base_recalibrate": true, 
	                    "basecallerargs": "", 
	                    "resource_uri": "/rundb/api/v1/experimentanalysissettings/10575/"
	                }
	            ], 
	            "runtype": "GENS", 
	            "platform": "PGM", 
	            "samples": [
	                {
	                    "status": "run", 
	                    "sampleSets": [], 
	                    "description": null, 
	                    "displayedName": "E115943-lq204-01-L8095", 
	                    "experiments": [
	                        "/rundb/api/v1/experiment/10142/", 
	                        "/rundb/api/v1/experiment/10132/"
	                    ], 
	                    "externalId": "", 
	                    "date": "2013-05-15T18:30:24.000176+00:00", 
	                    "resource_uri": "/rundb/api/v1/sample/2379/", 
	                    "id": 2379, 
	                    "name": "E115943-lq204-01-L8095"
	                }
	            ], 
	            "pinnedRepResult": false, 
	            "reagentBarcode": "", 
	            "star": false, 
	            "isProton": "False", 
	            "expCompInfo": "", 
	            "resultDate": "2013-05-15T18:30:24.000171+00:00", 
	            "flows": 400, 
	            "plan": "/rundb/api/v1/plannedexperiment/88364/", 
	            "date": "2013-05-15T18:30:24.000167+00:00", 
	            "diskusage": null, 
	            "unique": "ea5aefc7-e1ec-4c79-9843-b0e299253a9a", 
	            "expDir": "", 
	            "autoAnalyze": true, 
	            "ftpStatus": "Complete", 
	            "flowsInOrder": "", 
	            "baselineRun": false, 
	            "displayName": "ea5aefc7-e1ec-4c79-9843-b0e299253a9a", 
	            "notes": "OT2 lq204_01 Lib8095 275bp lr2 4B bead 1.2B lib SDS_10mMEDTA break ", 
	            "sequencekitname": "", 
	            "chipBarcode": "", 
	            "pgmName": "", 
	            "storageHost": null, 
	            "expName": "ea5aefc7-e1ec-4c79-9843-b0e299253a9a", 
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

