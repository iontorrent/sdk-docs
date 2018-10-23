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
**planDisplayedName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                       Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endBarcodeKitName**                 Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                       Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                        Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                            Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                   Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                          Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**                 Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                    Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**earlyDatFileDeletion**              Boolean data. Ex: True                                                                             false   false    true     false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                        Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**     Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                          Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                           Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                        A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                 Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInfo**                          A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       {}      false    false    false false  dict     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                  A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                             Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                          Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**                  Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**                   Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                       Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                    Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName**      Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 111, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "Ion AmpliSeq HD for Tumor - DNA", 
	            "autoAnalyze": true, 
	            "endBarcodeKitName": "", 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "thumbnailanalysisargs": "Analysis --args-json /opt/ion/config/args_540_analysis.json --thumbnail true", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "mixedTypeRNA_hotSpotRegionBedFile": "", 
	            "mixedTypeRNA_targetRegionBedFile": "", 
	            "platform": "", 
	            "categories": "onco_solidTumor;onco_heme;", 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2 --wells-normalization on --read-structure AmpliseqHD --tag-filter-method need-prefix", 
	            "alignmentargs": "tmap mapall -g 0 ... --context stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on --read-structure AmpliseqHD", 
	            "libkit": null, 
	            "projects": [], 
	            "notes": "", 
	            "sequencekitname": "Ion S5 Sequencing Kit", 
	            "base_recalibration_mode": "standard_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "thumbnailionstatsargs": "ionstats alignment", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "tmap mapall -g 0 ... --context stage1 map4", 
	            "chipType": "540", 
	            "library": "hg19", 
	            "runMode": "single", 
	            "sampleTubeLabel": "", 
	            "seqKitBarcode": null, 
	            "barcodeId": "Ion AmpliSeq HD Dual Barcode Kit 1-24", 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "Self", 
	            "experiment": "/rundb/api/v1/experiment/136/", 
	            "bedfile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	            "applicationCategoryDisplayedName": "Oncology - Solid Tumor | Oncology - HemeOnc", 
	            "isReusable": false, 
	            "isDuplicateReads": false, 
	            "sampleSets": [], 
	            "thumbnailbeadfindargs": "justBeadFind --args-json /opt/ion/config/args_540_beadfind.json --thumbnail true", 
	            "librarykitname": "Ion AmpliSeq HD Library Kit", 
	            "sseBedFile": "", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --max-phasing-levels 2 --num-unfiltered 1000 --barcode-filter-postpone 1 --wells-normalization on --read-structure AmpliseqHD", 
	            "earlyDatFileDeletion": false, 
	            "parentPlan": null, 
	            "origin": "gui|5.10.0.RC4", 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "pending", 
	            "isCustom_kitSettings": false, 
	            "samplePrepKitName": null, 
	            "applicationGroupDisplayedName": "DNA", 
	            "metaData": {
	                "fromTemplate": "Ion_AmpliSeq_HD_for_Tumor_-_DNA", 
	                "fromTemplateSource": "ION"
	            }, 
	            "isFavorite": false, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/143/", 
	                    "id": 407, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/407/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/143/", 
	                    "id": 408, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/408/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/143/", 
	                    "id": 406, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/406/"
	                }
	            ], 
	            "analysisargs": "Analysis --args-json /opt/ion/config/args_540_analysis.json", 
	            "thumbnailcalibrateargs": "Calibration", 
	            "templatingKitName": "Ion Chef S540 V1", 
	            "runType": "AMPS_HD_DNA", 
	            "username": "ionadmin", 
	            "planShortID": "SP1XE", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter-minreads 10 --phasing-residual-filter=2.0 --wells-normalization on --read-structure AmpliseqHD --tag-filter-method need-prefix", 
	            "controlSequencekitname": null, 
	            "tfKey": "ATCG", 
	            "mixedTypeRNA_reference": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "reverselibrarykey": "", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "", 
	            "usePostBeadfind": false, 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "chefInfo": {}, 
	            "planGUID": "1d75abf5-4d15-43f5-bb08-1c89d7344175", 
	            "ionstatsargs": "ionstats alignment", 
	            "samplePrepProtocol": "", 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 143, 
	            "barcodedSamples": {
	                "Sample 10": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0110": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0110"
	                    ]
	                }, 
	                "Sample 8": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0108": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0108"
	                    ]
	                }, 
	                "Sample 9": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0109": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0109"
	                    ]
	                }, 
	                "Sample 6": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0106": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0106"
	                    ]
	                }, 
	                "Sample 7": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0107": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0107"
	                    ]
	                }, 
	                "Sample 4": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0104": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0104"
	                    ]
	                }, 
	                "Sample 5": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0105": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0105"
	                    ]
	                }, 
	                "Sample 2": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0102": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0102"
	                    ]
	                }, 
	                "Sample 3": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0103": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0103"
	                    ]
	                }, 
	                "Sample 1": {
	                    "dualBarcodes": [], 
	                    "barcodeSampleInfo": {
	                        "IonHDdual_0101": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/2/hg19/unmerged/detail/AmpliSeqExome.20141113.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": "", 
	                            "endBarcode": "", 
	                            "controlType": "", 
	                            "sseBedFile": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonHDdual_0101"
	                    ]
	                }
	            }, 
	            "custom_args": false, 
	            "regionfile": "", 
	            "selectedPlugins": {
	                "coverageAnalysis": {
	                    "userInput": {}, 
	                    "version": "5.8.0.8", 
	                    "features": [], 
	                    "name": "coverageAnalysis", 
	                    "id": 41
	                }, 
	                "variantCaller": {
	                    "userInput": {
	                        "meta": {
	                            "configuration": "ampliseq_hd_ffpe"
	                        }
	                    }, 
	                    "version": "5.8.0.19", 
	                    "features": [], 
	                    "name": "variantCaller", 
	                    "id": 36
	                }
	            }, 
	            "beadfindargs": "justBeadFind --args-json /opt/ion/config/args_540_beadfind.json", 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 500, 
	            "date": "2018-04-13T22:17:13.000108+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "planName": "Ion_AmpliSeq_HD_for_Tumor_-_DNA", 
	            "calibrateargs": "Calibration", 
	            "flowsInOrder": "", 
	            "libraryPrepType": "", 
	            "sampleGrouping": "/rundb/api/v1/samplegrouptype_cv/2/", 
	            "chipBarcode": "", 
	            "sampleSetDisplayedName": "", 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/plannedexperiment/143/", 
	            "libraryPrepTypeDisplayedName": "", 
	            "reverse3primeadapter": ""
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

