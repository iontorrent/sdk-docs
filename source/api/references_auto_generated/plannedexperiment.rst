.. _api_reference_plannedexperiment:

Planned Experiment  Resource
============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plannedexperiment/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plannedexperiment/schema/``
| 

.. include:: ../references_manual_extras/plannedexperiment.rst

Resource Fields
---------------

==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                                help text                                                                                          default nullable readonly blank unique type     
==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**planDisplayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                      Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                      Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                 A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                       Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**                  Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**          Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                           Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                  Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                         Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                          Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**                Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                        Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                          Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**               Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                 Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                       Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sseBedFile**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**earlyDatFileDeletion**             Boolean data. Ex: True                                                                             false   false    true     false false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                       Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**    Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                         Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                          Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingSize**                   Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                       A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                          Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInfo**                         A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       {}      false    false    false false  dict     
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**               Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                               Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**                  Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**                  Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                            Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                         Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**                 Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                     Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**                  Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                      Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName**     Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**             Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 88, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "Chef  - 220a9897 - 2017.08.28", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "thumbnailanalysisargs": "Analysis --args-json /opt/ion/config/args_540_analysis.json --thumbnail true", 
	            "applicationGroup": null, 
	            "platform": "", 
	            "categories": "", 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2 --wells-normalization on", 
	            "alignmentargs": "tmap mapall -q 50000 ... stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on", 
	            "libkit": null, 
	            "projects": [], 
	            "notes": null, 
	            "sequencekitname": "Ion S5 Sequencing Kit", 
	            "base_recalibration_mode": "standard_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "thumbnailionstatsargs": "ionstats alignment", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "tmap mapall -q 50000 ... stage1 map4", 
	            "chipType": "540", 
	            "library": null, 
	            "runMode": "", 
	            "planName": "Chef_-_220a9897_-_2017.08.28", 
	            "seqKitBarcode": null, 
	            "barcodeId": null, 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/95/", 
	            "bedfile": null, 
	            "applicationCategoryDisplayedName": "", 
	            "isReusable": false, 
	            "isDuplicateReads": false, 
	            "sampleSets": [], 
	            "thumbnailbeadfindargs": "justBeadFind --args-json /opt/ion/config/args_540_beadfind.json --thumbnail true", 
	            "librarykitname": null, 
	            "sseBedFile": "", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2 --num-unfiltered 1000 --barcode-filter-postpone 1 --wells-normalization on", 
	            "earlyDatFileDeletion": false, 
	            "parentPlan": null, 
	            "origin": "api|5.6.0.RC4", 
	            "forward3primeadapter": null, 
	            "planStatus": "reserved", 
	            "samplePrepKitName": null, 
	            "applicationGroupDisplayedName": "", 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "qcValues": [], 
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_540_analysis.json", 
	            "thumbnailcalibrateargs": "Calibration", 
	            "templatingKitName": "Ion Chef S540 V1", 
	            "runType": "GENS", 
	            "username": null, 
	            "planShortID": "X8W9R", 
	            "sampleDisplayedName": "Sample  - 89022e10", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on", 
	            "controlSequencekitname": null, 
	            "tfKey": "ATCG", 
	            "templatingSize": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": null, 
	            "reverselibrarykey": "", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "", 
	            "usePostBeadfind": false, 
	            "libraryReadLength": 0, 
	            "runname": null, 
	            "chefInfo": {
	                "chefLotNumber": "", 
	                "chefProtocolDeviationName": "", 
	                "chefReagentID": "", 
	                "chefSolutionsPart": "A27754C", 
	                "chefLastUpdate": "2017-08-28T14:07:47+00:00", 
	                "chefChipExpiration1": "None", 
	                "chefChipExpiration2": "None", 
	                "chefStatus": "starting", 
	                "chefReagentsPart": "A27758C", 
	                "chefInstrumentName": "VIRTUALCHEF01", 
	                "chefLogPath": "", 
	                "chefScriptVersion": "604", 
	                "chefOperationMode": "Customer Mode", 
	                "chefManufactureDate": "", 
	                "chefSamplePos": "1", 
	                "chefReagentsExpiration": "200131", 
	                "chefSolutionsLot": "12345678", 
	                "chefProgress": 5, 
	                "chefKitType": "Ion 540 Kit-Chef", 
	                "chefPackageVer": "IC.5.6.0.SIM.99", 
	                "chefTipRackBarcode": "456250074", 
	                "chefRemainingSeconds": 8000, 
	                "chefExtraInfo_1": "", 
	                "chefExtraInfo_2": "", 
	                "chefMessage": "", 
	                "chefEndTime": null, 
	                "chefStartTime": "2017-08-28T13:54:39+00:00", 
	                "chefReagentsLot": "061215", 
	                "chefChipType2": "S500", 
	                "chefChipType1": "540v1", 
	                "chefSolutionsExpiration": "170131"
	            }, 
	            "planGUID": "f651801b-394d-4083-a6d7-ee342d27a9f1", 
	            "sampleTubeLabel": null, 
	            "ionstatsargs": "ionstats alignment", 
	            "samplePrepProtocol": "", 
	            "sample": "Sample_-_89022e10", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 103, 
	            "barcodedSamples": {}, 
	            "custom_args": false, 
	            "regionfile": null, 
	            "selectedPlugins": {
	                "RunTransfer": {
	                    "userInput": {}, 
	                    "version": "5.6.0.6", 
	                    "features": [], 
	                    "name": "RunTransfer", 
	                    "id": 21
	                }, 
	                "FileExporter": {
	                    "userInput": {}, 
	                    "version": "5.6.0.0", 
	                    "features": [], 
	                    "name": "FileExporter", 
	                    "id": 10
	                }, 
	                "immuneResponseRNA": {
	                    "userInput": {}, 
	                    "version": "5.6.0.0", 
	                    "features": [], 
	                    "name": "immuneResponseRNA", 
	                    "id": 11
	                }
	            }, 
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_540_beadfind.json", 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 500, 
	            "date": "2017-08-28T20:58:58.000662+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "Calibration", 
	            "flowsInOrder": "", 
	            "libraryPrepType": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": "", 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/plannedexperiment/103/", 
	            "libraryPrepTypeDisplayedName": "", 
	            "reverse3primeadapter": ""
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

