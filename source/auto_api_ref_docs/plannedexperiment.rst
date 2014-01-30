Plannedexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plannedexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plannedexperiment/schema/``


.. include:: ../manual_api_ref_docs/plannedexperiment.rst

Fields table
------------

=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                                                                          default nullable readonly blank unique type     
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**isReverseRun**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**        Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                    Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**      Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetGroupType**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                     Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**           Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                          Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                    Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_uid**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planIndex**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planTotal**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**            Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                       Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**            Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                 Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                  Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                  A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**        Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                       Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/plannedexperiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/plannedexperiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	plannedexperiments = ts_api_response["objects"]
	
	for plannedexperiment in plannedexperiments:
	    print plannedexperiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 4193, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "-R185427-in_house-ml", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "thumbnailanalysisargs": "", 
	            "applicationGroup": null, 
	            "libkit": null, 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "", 
	            "sampleSet_planTotal": 0, 
	            "projects": [
	                "avalanche"
	            ], 
	            "notes": "1T LLP Pool 2 Lib7679 200bp psp4_test lot131113 in house reagents ", 
	            "sequencekitname": "", 
	            "storageHost": null, 
	            "expName": "", 
	            "cycles": 250, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "", 
	            "chipType": "316v2", 
	            "library": "hg19", 
	            "reverselibrarykey": "", 
	            "planName": "-R185427-in_house-ml", 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "isPlanGroup": false, 
	            "experiment": "/rundb/api/v1/experiment/12549/", 
	            "bedfile": "", 
	            "isReusable": false, 
	            "isDuplicateReads": false, 
	            "thumbnailbeadfindargs": "", 
	            "librarykitname": "", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --trim-qual-cutoff 15 --trim-qual-window-size 30 --trim-adapter-cutoff 16", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "planned", 
	            "samplePrepKitName": null, 
	            "metaData": {
	                "torrenthub.cbd_hub_id": "185427"
	            }, 
	            "sampleSet_uid": null, 
	            "isFavorite": false, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [], 
	            "analysisargs": "Analysis --from-beadfind", 
	            "templatingKitName": null, 
	            "runType": "WGNM", 
	            "username": "ml", 
	            "planShortID": "XV5JM", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "", 
	            "controlSequencekitname": null, 
	            "flowsInOrder": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": null, 
	            "runMode": "", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "avalanche", 
	            "usePostBeadfind": true, 
	            "runname": null, 
	            "planGUID": "4df71954-4746-47e6-ad8b-bd834d005e44", 
	            "sampleTubeLabel": null, 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 44458, 
	            "barcodedSamples": {}, 
	            "regionfile": "", 
	            "selectedPlugins": {
	                "pinsPerFlow": {
	                    "name": "pinsPerFlow"
	                }, 
	                "libClonality": {
	                    "name": "libClonality"
	                }, 
	                "TestFragmentTorturer": {
	                    "name": "TestFragmentTorturer"
	                }, 
	                "avalanche_slush_shovel": {
	                    "name": "avalanche_slush_shovel"
	                }, 
	                "detailedReport": {
	                    "name": "detailedReport"
	                }, 
	                "bubblePlots": {
	                    "name": "bubblePlots"
	                }, 
	                "bubbleRun": {
	                    "name": "bubbleRun"
	                }, 
	                "1_Torrent_Accuracy": {
	                    "name": "1_Torrent_Accuracy"
	                }, 
	                "ErrByFlow": {
	                    "name": "ErrByFlow"
	                }, 
	                "variantCaller": {
	                    "userInput": {
	                        "librarytype": "WGNM", 
	                        "variationtype": ""
	                    }, 
	                    "name": "variantCaller"
	                }, 
	                "Reverse_Primer_Lookup": {
	                    "name": "Reverse_Primer_Lookup"
	                }, 
	                "rawTrace": {
	                    "name": "rawTrace"
	                }, 
	                "filterAndTrim": {
	                    "name": "filterAndTrim"
	                }, 
	                "AvgTrace": {
	                    "name": "AvgTrace"
	                }, 
	                "chipDiagnostics": {
	                    "name": "chipDiagnostics"
	                }, 
	                "qv_binner": {
	                    "name": "qv_binner"
	                }, 
	                "spatialPlots": {
	                    "name": "spatialPlots"
	                }, 
	                "validateVariantCaller": {
	                    "userInput": {
	                        "truth_major_snp": "TSExomeV2_NA12878_SNPs_Confident.bed", 
	                        "Region": "Exome", 
	                        "Sample": "NA12878", 
	                        "truth_minor_snp": "None", 
	                        "truth_major_indel": "TSExomeV2_NA12878_Confident_InDels.bed", 
	                        "truth_minor_indel": "None"
	                    }, 
	                    "name": "validateVariantCaller"
	                }, 
	                "barcodeMixtureAnalysis": {
	                    "name": "barcodeMixtureAnalysis"
	                }, 
	                "PerBaseQualEval": {
	                    "name": "PerBaseQualEval"
	                }, 
	                "z_homopolymerAnalysis": {
	                    "name": "z_homopolymerAnalysis"
	                }, 
	                "start_point_analysis": {
	                    "name": "start_point_analysis"
	                }, 
	                "RateMap": {
	                    "name": "RateMap"
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
	            "beadfindargs": "justBeadFind", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 1000, 
	            "date": "2014-01-30T20:25:40.000383+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "tfKey": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/plannedexperiment/44458/", 
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

