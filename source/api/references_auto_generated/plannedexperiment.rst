.. _api_reference_plannedexperiment:

Planned Experiment  Resource
============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plannedexperiment/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plannedexperiment/schema/``
| 

.. include:: ../references_manual_extras/plannedexperiment.rst

Resource Fields
---------------

===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                                 help text                                                                                          default nullable readonly blank unique type     
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**adapter**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**     Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                       Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                        Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInfo**                          A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       {}      false    false    false false  dict     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                        A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                       Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                          Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                            Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**earlyDatFileDeletion**              Boolean data. Ex: True                                                                             false   false    true     false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endBarcodeKitName**                 Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                             Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                          Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**                   Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName**      Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                 Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                    Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                          Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                        Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                  A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                       Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**                 Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                           Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                   Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                    Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**                  Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plannedexperiment/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 135
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "alignmentargs": "",
	            "analysisargs": "",
	            "applicationCategoryDisplayedName": "Oncology - Solid Tumor",
	            "applicationGroup": "/rundb/api/v1/applicationgroup/5/",
	            "applicationGroupDisplayedName": "DNA and Fusions (Separate Libraries)",
	            "autoAnalyze": true,
	            "autoName": null,
	            "barcodeId": "Ion Dual Barcode Kit 1-96",
	            "barcodedSamples": {},
	            "base_recalibration_mode": "standard_recal",
	            "basecallerargs": "",
	            "beadfindargs": "",
	            "bedfile": "",
	            "calibrateargs": "",
	            "categories": "Oncomine;onco_solidTumor;barcodes_8;p4o",
	            "chefInfo": {},
	            "childPlans": [],
	            "chipBarcode": "",
	            "chipType": "530",
	            "controlSequencekitname": null,
	            "custom_args": false,
	            "cycles": null,
	            "date": "2019-10-03T20:53:08.000623+00:00",
	            "earlyDatFileDeletion": false,
	            "endBarcodeKitName": "",
	            "expName": "",
	            "experiment": "/rundb/api/v1/experiment/163/",
	            "flows": 500,
	            "flowsInOrder": "",
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC",
	            "id": 170,
	            "ionstatsargs": "",
	            "irworkflow": "",
	            "isCustom_kitSettings": false,
	            "isDuplicateReads": false,
	            "isFavorite": false,
	            "isPlanGroup": false,
	            "isReusable": true,
	            "isReverseRun": false,
	            "isSystem": true,
	            "isSystemDefault": false,
	            "libkit": null,
	            "library": "",
	            "libraryKey": "TCAG",
	            "libraryPrepType": "",
	            "libraryPrepTypeDisplayedName": "",
	            "libraryReadLength": 200,
	            "librarykitname": "Ion AmpliSeq Library Kit Plus",
	            "metaData": {},
	            "mixedTypeRNA_hotSpotRegionBedFile": null,
	            "mixedTypeRNA_reference": null,
	            "mixedTypeRNA_targetRegionBedFile": null,
	            "notes": "",
	            "origin": "|5.12.1",
	            "pairedEndLibraryAdapterName": null,
	            "parentPlan": null,
	            "planDisplayedName": "Oncomine Tumor Specific Fusions",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "planName": "Oncomine_Tumor_Specific_Fusions",
	            "planPGM": "",
	            "planShortID": "OZT4F",
	            "planStatus": "inactive",
	            "platform": "S5",
	            "preAnalysis": true,
	            "prebasecallerargs": "",
	            "prethumbnailbasecallerargs": "",
	            "project": "",
	            "projects": [],
	            "qcValues": [
	                {
	                    "id": 487,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 1,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Bead Loading (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/487/",
	                    "threshold": 30
	                },
	                {
	                    "id": 488,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 2,
	                        "maxThreshold": 100,
	                        "minThreshold": 1,
	                        "qcName": "Key Signal (1-100)",
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/488/",
	                    "threshold": 30
	                },
	                {
	                    "id": 489,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 3,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Usable Sequence (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/489/",
	                    "threshold": 30
	                }
	            ],
	            "realign": false,
	            "regionfile": "",
	            "resource_uri": "/rundb/api/v1/plannedexperiment/170/",
	            "reverse3primeadapter": "",
	            "reverse_primer": null,
	            "reverselibrarykey": "",
	            "runMode": "single",
	            "runType": "AMPS_RNA",
	            "runname": null,
	            "sample": "",
	            "sampleDisplayedName": "",
	            "sampleGrouping": "/rundb/api/v1/samplegrouptype_cv/7/",
	            "sampleGroupingName": "Single Fusions",
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
	            "sampleSetDisplayedName": "",
	            "sampleSets": [],
	            "sampleTubeLabel": null,
	            "selectedPlugins": {},
	            "seqKitBarcode": null,
	            "sequencekitname": "Ion S5 Sequencing Kit",
	            "sseBedFile": "",
	            "storageHost": null,
	            "storage_options": "A",
	            "templatingKitBarcode": null,
	            "templatingKitName": "Ion Chef S530 V2",
	            "tfKey": "ATCG",
	            "thumbnailalignmentargs": "",
	            "thumbnailanalysisargs": "",
	            "thumbnailbasecallerargs": "",
	            "thumbnailbeadfindargs": "",
	            "thumbnailcalibrateargs": "",
	            "thumbnailionstatsargs": "",
	            "usePostBeadfind": false,
	            "usePreBeadfind": true,
	            "username": null,
	            "variantfrequency": ""
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

