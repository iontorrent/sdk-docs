.. _api_reference_availableonetouchplannedexperiment:

Available Onetouch Planned Experiment  Resource
===============================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/schema/``
| 

.. include:: ../references_manual_extras/availableonetouchplannedexperiment.rst

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
	        "next": "/rundb/api/v1/availableonetouchplannedexperiment/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "alignmentargs": "tmap mapall ... stage1 map4",
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_P1.1.17_analysis.json",
	            "applicationCategoryDisplayedName": "",
	            "applicationGroup": "/rundb/api/v1/applicationgroup/2/",
	            "applicationGroupDisplayedName": "RNA",
	            "autoAnalyze": true,
	            "autoName": null,
	            "barcodeId": "IonXpress",
	            "barcodedSamples": {
	                "Sample 1": {
	                    "barcodeSampleInfo": {
	                        "IonXpress_001": {
	                            "controlSequenceType": "",
	                            "controlType": "",
	                            "description": "",
	                            "endBarcode": "",
	                            "externalId": "",
	                            "hotSpotRegionBedFile": "",
	                            "nucleotideType": "RNA",
	                            "reference": "AmpliSeq_Mouse_Transcriptome_v1",
	                            "sseBedFile": "",
	                            "targetRegionBedFile": ""
	                        }
	                    },
	                    "barcodes": [
	                        "IonXpress_001"
	                    ],
	                    "dualBarcodes": []
	                }
	            },
	            "base_recalibration_mode": "standard_recal",
	            "basecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2 --num-unfiltered 1000 --barcode-filter-postpone 1",
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_P1.1.17_beadfind.json",
	            "bedfile": "",
	            "calibrateargs": "Calibration",
	            "categories": "",
	            "chefInfo": {},
	            "childPlans": [],
	            "chipBarcode": "",
	            "chipType": "P1.1.17",
	            "controlSequencekitname": null,
	            "custom_args": false,
	            "cycles": null,
	            "date": "2018-08-02T18:54:44.000297+00:00",
	            "earlyDatFileDeletion": false,
	            "endBarcodeKitName": "",
	            "expName": "",
	            "experiment": "/rundb/api/v1/experiment/137/",
	            "flows": 500,
	            "flowsInOrder": "",
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC",
	            "id": 144,
	            "ionstatsargs": "ionstats alignment",
	            "irworkflow": "",
	            "isCustom_kitSettings": false,
	            "isDuplicateReads": false,
	            "isFavorite": false,
	            "isPlanGroup": false,
	            "isReusable": false,
	            "isReverseRun": false,
	            "isSystem": false,
	            "isSystemDefault": false,
	            "libkit": null,
	            "library": "AmpliSeq_Mouse_Transcriptome_v1",
	            "libraryKey": "TCAG",
	            "libraryPrepType": "",
	            "libraryPrepTypeDisplayedName": "",
	            "libraryReadLength": 0,
	            "librarykitname": "Ion AmpliSeq Library Kit Plus",
	            "metaData": {
	                "fromTemplate": "Ion_AmpliSeq_Transcriptome_Mouse_Gene_Expression_Panel_OT2-Proton",
	                "fromTemplateSource": "ION"
	            },
	            "mixedTypeRNA_hotSpotRegionBedFile": "",
	            "mixedTypeRNA_reference": "",
	            "mixedTypeRNA_targetRegionBedFile": "",
	            "notes": "",
	            "origin": "gui|5.10.0",
	            "pairedEndLibraryAdapterName": "",
	            "parentPlan": null,
	            "planDisplayedName": "Ion AmpliSeq Transcriptome Mouse Gene Expression ",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "685ac1ca-9a42-4d9c-af2f-29a97706cb8e",
	            "planName": "Ion_AmpliSeq_Transcriptome_Mouse_Gene_Expression",
	            "planPGM": null,
	            "planShortID": "YEN8M",
	            "planStatus": "planned",
	            "platform": "",
	            "preAnalysis": true,
	            "prebasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2",
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0",
	            "project": "",
	            "projects": [],
	            "qcValues": [
	                {
	                    "id": 409,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/144/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 1,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Bead Loading (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/409/",
	                    "threshold": 30
	                },
	                {
	                    "id": 410,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/144/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 2,
	                        "maxThreshold": 100,
	                        "minThreshold": 1,
	                        "qcName": "Key Signal (1-100)",
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/410/",
	                    "threshold": 30
	                },
	                {
	                    "id": 411,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/144/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 3,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Usable Sequence (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/411/",
	                    "threshold": 30
	                }
	            ],
	            "realign": false,
	            "regionfile": "",
	            "resource_uri": "/rundb/api/v1/availableonetouchplannedexperiment/144/",
	            "reverse3primeadapter": "",
	            "reverse_primer": null,
	            "reverselibrarykey": "",
	            "runMode": "single",
	            "runType": "AMPS_RNA",
	            "runname": null,
	            "sample": "",
	            "sampleDisplayedName": "",
	            "sampleGrouping": "/rundb/api/v1/samplegrouptype_cv/2/",
	            "sampleGroupingName": "Self",
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
	            "sampleSetDisplayedName": "",
	            "sampleSets": [],
	            "sampleTubeLabel": "",
	            "selectedPlugins": {
	                "ampliSeqRNA": {
	                    "features": [],
	                    "id": 48,
	                    "name": "ampliSeqRNA",
	                    "userInput": {},
	                    "version": "5.10.0.1"
	                }
	            },
	            "seqKitBarcode": null,
	            "sequencekitname": "ProtonI200Kit-v3",
	            "sseBedFile": "",
	            "storageHost": null,
	            "storage_options": "A",
	            "templatingKitBarcode": null,
	            "templatingKitName": "Ion PI Template OT2 200 Kit v3",
	            "tfKey": "ATCG",
	            "thumbnailalignmentargs": "tmap mapall ... stage1 map4",
	            "thumbnailanalysisargs": "Analysis --args-json /opt/ion/config/args_P1.1.17_analysis.json --thumbnail true",
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0",
	            "thumbnailbeadfindargs": "justBeadFind --args-json /opt/ion/config/args_P1.1.17_beadfind.json --thumbnail true",
	            "thumbnailcalibrateargs": "Calibration",
	            "thumbnailionstatsargs": "ionstats alignment",
	            "usePostBeadfind": false,
	            "usePreBeadfind": true,
	            "username": "ionadmin",
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

