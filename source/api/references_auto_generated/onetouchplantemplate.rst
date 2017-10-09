.. _api_reference_onetouchplantemplate:

Onetouch Plan Template  Resource
================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/schema/``
| 

.. include:: ../references_manual_extras/onetouchplantemplate.rst

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
	        "total_count": 35, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/onetouchplantemplate/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "Ion AmpliSeq Transcriptome Mouse Gene Expression Panel OT2-Proton", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "thumbnailanalysisargs": "", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/2/", 
	            "platform": "PROTON", 
	            "categories": "", 
	            "planPGM": "", 
	            "prebasecallerargs": "", 
	            "alignmentargs": "", 
	            "thumbnailbasecallerargs": "", 
	            "libkit": null, 
	            "projects": [], 
	            "notes": "", 
	            "sequencekitname": "ProtonI200Kit-v3", 
	            "base_recalibration_mode": "standard_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "thumbnailionstatsargs": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "", 
	            "chipType": "P1.1.17", 
	            "library": "AmpliSeq_Mouse_Transcriptome_v1", 
	            "runMode": "single", 
	            "planName": "Ion_AmpliSeq_Transcriptome_Mouse_Gene_Expression_Panel_OT2-Proton", 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "Self", 
	            "experiment": "/rundb/api/v1/experiment/81/", 
	            "bedfile": "/AmpliSeq_Mouse_Transcriptome_v1/unmerged/detail/AmpliSeq_Mouse_Transcriptome_V1.Designed.bed", 
	            "applicationCategoryDisplayedName": "", 
	            "isReusable": true, 
	            "isDuplicateReads": false, 
	            "sampleSets": [], 
	            "thumbnailbeadfindargs": "", 
	            "librarykitname": "Ion AmpliSeq Library Kit Plus", 
	            "sseBedFile": "", 
	            "adapter": null, 
	            "basecallerargs": "", 
	            "earlyDatFileDeletion": false, 
	            "parentPlan": null, 
	            "origin": "|5.6.0.RC1", 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "inactive", 
	            "samplePrepKitName": null, 
	            "applicationGroupDisplayedName": "RNA", 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/89/", 
	                    "id": 265, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/265/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/89/", 
	                    "id": 266, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/266/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/89/", 
	                    "id": 267, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/267/"
	                }
	            ], 
	            "analysisargs": "", 
	            "thumbnailcalibrateargs": "", 
	            "templatingKitName": "Ion PI Template OT2 200 Kit v3", 
	            "runType": "AMPS_RNA", 
	            "username": null, 
	            "planShortID": "FDXPW", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "", 
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
	            "chefInfo": {}, 
	            "planGUID": "c5299ab6-9142-4034-95f9-c1d178c67dda", 
	            "sampleTubeLabel": null, 
	            "ionstatsargs": "", 
	            "samplePrepProtocol": "", 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 89, 
	            "barcodedSamples": {}, 
	            "custom_args": false, 
	            "regionfile": "", 
	            "selectedPlugins": {
	                "ampliSeqRNA": {
	                    "userInput": {}, 
	                    "version": "5.6.0.3", 
	                    "features": [], 
	                    "name": "ampliSeqRNA", 
	                    "id": 20
	                }
	            }, 
	            "beadfindargs": "", 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 500, 
	            "date": "2017-08-10T22:57:27.000213+00:00", 
	            "isSystem": true, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "", 
	            "flowsInOrder": "", 
	            "libraryPrepType": "", 
	            "sampleGrouping": "/rundb/api/v1/samplegrouptype_cv/2/", 
	            "chipBarcode": "", 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/onetouchplantemplate/89/", 
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

