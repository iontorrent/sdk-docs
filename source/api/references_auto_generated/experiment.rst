.. _api_reference_experiment:

Experiment  Resource
====================

| Resource URL ``http://mytorrentserver/rundb/api/v1/experiment/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/experiment/schema/``
| 

.. include:: ../references_manual_extras/experiment.rst

Resource Fields
---------------

============================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                         help text                                                                                          default nullable readonly blank unique type     
============================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
**autoAnalyze**               Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**baselineRun**               Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefChipExpiration1**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefChipExpiration2**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefChipType1**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefChipType2**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefEndTime**               A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefExtraInfo_1**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefExtraInfo_2**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefFlexibleWorkflow**      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInstrumentName**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefKitType**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLastUpdate**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLogPath**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLotNumber**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefManufactureDate**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefMessage**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefOperationMode**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefPackageVer**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefProgress**              Floating point numeric data. Ex: 26.73                                                             0       false    false    true  false  float    
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefProtocolDeviationName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentID**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsExpiration**    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsLot**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsPart**          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsSerialNum**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefRemainingSeconds**      Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSamplePos**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefScriptVersion**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsExpiration**   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsLot**          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsPart**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsSerialNum**    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStartTime**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStatus**                Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefTipRackBarcode**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                    Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                      A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**                 Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayName**               Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas_set**                   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expCompInfo**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expDir**                    Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                     Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**ftpStatus**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                        Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isProton**                  Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**                       Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                  Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pinnedRepResult**           Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**                      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**rawdatastyle**              Unicode string data. Ex: "Hello World"                                                             single  true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentBarcode**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**                A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**                   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runtype**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**                   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitbarcode**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**           Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**unique**                    Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**            Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**user_ack**                  Unicode string data. Ex: "Hello World"                                                             U       false    false    false false  string   
============================= ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/experiment/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 136
	    },
	    "objects": [
	        {
	            "autoAnalyze": true,
	            "baselineRun": false,
	            "chefChipExpiration1": "",
	            "chefChipExpiration2": "",
	            "chefChipType1": "",
	            "chefChipType2": "",
	            "chefEndTime": null,
	            "chefExtraInfo_1": "",
	            "chefExtraInfo_2": "",
	            "chefFlexibleWorkflow": "",
	            "chefInstrumentName": "",
	            "chefKitType": "",
	            "chefLastUpdate": null,
	            "chefLogPath": null,
	            "chefLotNumber": "",
	            "chefManufactureDate": "",
	            "chefMessage": "",
	            "chefOperationMode": "",
	            "chefPackageVer": "",
	            "chefProgress": 0,
	            "chefProtocolDeviationName": null,
	            "chefReagentID": "",
	            "chefReagentsExpiration": "",
	            "chefReagentsLot": "",
	            "chefReagentsPart": "",
	            "chefReagentsSerialNum": "",
	            "chefRemainingSeconds": null,
	            "chefSamplePos": "",
	            "chefScriptVersion": "",
	            "chefSolutionsExpiration": "",
	            "chefSolutionsLot": "",
	            "chefSolutionsPart": "",
	            "chefSolutionsSerialNum": "",
	            "chefStartTime": null,
	            "chefStatus": "",
	            "chefTipRackBarcode": "",
	            "chipBarcode": "",
	            "chipType": "530",
	            "cycles": 0,
	            "date": "2019-10-03T20:53:08.000599+00:00",
	            "diskusage": 0,
	            "displayName": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "eas_set": [
	                {
	                    "alignmentargs": "",
	                    "analysisargs": "",
	                    "barcodeKitName": "Ion Dual Barcode Kit 1-96",
	                    "barcodedSamples": {},
	                    "base_recalibration_mode": "standard_recal",
	                    "basecallerargs": "",
	                    "beadfindargs": "",
	                    "calibrateargs": "",
	                    "custom_args": false,
	                    "date": "2019-10-03T20:53:08.000599+00:00",
	                    "endBarcodeKitName": "",
	                    "experiment": "/rundb/api/v1/experiment/163/",
	                    "hotSpotRegionBedFile": "",
	                    "id": 162,
	                    "ionstatsargs": "",
	                    "isDuplicateReads": false,
	                    "isEditable": true,
	                    "isOneTimeOverride": false,
	                    "libraryKey": "TCAG",
	                    "libraryKitBarcode": null,
	                    "libraryKitName": "Ion AmpliSeq Library Kit Plus",
	                    "mixedTypeRNA_hotSpotRegionBedFile": null,
	                    "mixedTypeRNA_reference": null,
	                    "mixedTypeRNA_targetRegionBedFile": null,
	                    "prebasecallerargs": "",
	                    "prethumbnailbasecallerargs": "",
	                    "realign": false,
	                    "reference": "",
	                    "resource_uri": "/rundb/api/v1/experimentanalysissettings/162/",
	                    "results": [],
	                    "selectedPlugins": {},
	                    "sseBedFile": "",
	                    "status": "inactive",
	                    "targetRegionBedFile": "",
	                    "tfKey": "ATCG",
	                    "threePrimeAdapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC",
	                    "thumbnailalignmentargs": "",
	                    "thumbnailanalysisargs": "",
	                    "thumbnailbasecallerargs": "",
	                    "thumbnailbeadfindargs": "",
	                    "thumbnailcalibrateargs": "",
	                    "thumbnailionstatsargs": ""
	                }
	            ],
	            "expCompInfo": "",
	            "expDir": "",
	            "expName": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "flows": 500,
	            "flowsInOrder": "",
	            "ftpStatus": "",
	            "id": 163,
	            "isProton": "False",
	            "isReverseRun": false,
	            "log": {},
	            "metaData": {},
	            "notes": "",
	            "pgmName": "",
	            "pinnedRepResult": false,
	            "plan": "/rundb/api/v1/plannedexperiment/170/",
	            "platform": "S5",
	            "rawdatastyle": "single",
	            "reagentBarcode": "",
	            "resource_uri": "/rundb/api/v1/experiment/163/",
	            "resultDate": "2019-10-03T20:53:08.000620+00:00",
	            "results": [],
	            "reverse_primer": null,
	            "runMode": "single",
	            "runtype": "GENS",
	            "sample": "",
	            "samples": [],
	            "seqKitBarcode": "",
	            "sequencekitbarcode": "",
	            "sequencekitname": "Ion S5 Sequencing Kit",
	            "star": false,
	            "status": "inactive",
	            "storageHost": "",
	            "storage_options": "A",
	            "unique": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "usePreBeadfind": true,
	            "user_ack": "U"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- PATCH
- PUT
- DELETE


Allowed detail HTTP methods
---------------------------

- GET
- PATCH
- PUT
- DELETE

