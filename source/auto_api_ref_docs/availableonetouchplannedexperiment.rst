Availableonetouchplannedexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/schema/``


.. include:: ../manual_api_ref_docs/availableonetouchplannedexperiment.rst

Fields table
------------

=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                                                                          default nullable readonly blank unique type     
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**planDisplayedName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                 Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planTotal**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                       Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                    Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefProgress**                Floating point numeric data. Ex: 26.73                                                             0.0     false    false    true  false  float    
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                     Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLogPath**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                     Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**            Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                  Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**        Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupName**        Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLastUpdate**              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                    Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_uid**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planIndex**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefMessage**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                  A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**           Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**             Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetGroupType**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                          Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**instrumentType**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                       Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**            Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**      Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibrate**            Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**        Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	availableonetouchplannedexperiments = ts_api_response["objects"]
	
	for availableonetouchplannedexperiment in availableonetouchplannedexperiments:
	    print availableonetouchplannedexperiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 57, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/availableonetouchplannedexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "-R61916-4BC_910-smn-", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "chefStatus": "", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "libkit": null, 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 1000 --calibration-training=100000 --flow-signals-type scaled-residual --max-phasing-levels 2", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000", 
	            "sampleSet_planTotal": 0, 
	            "projects": [
	                "chemdev"
	            ], 
	            "notes": "", 
	            "sequencekitname": "ProtonI200Kit-v3", 
	            "storageHost": null, 
	            "expName": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "stage1 map4", 
	            "chipType": "P1.1.17", 
	            "chefProgress": 0.0, 
	            "library": "hg19", 
	            "runMode": "single", 
	            "sampleTubeLabel": "", 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/22492/", 
	            "bedfile": "/results/uploads/BED/50/hg19/unmerged/detail/Exome_pool_BENQ_Designed_20130326_NoChrY.bed", 
	            "isReusable": false, 
	            "isDuplicateReads": false, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "tfKey": "ATCG", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "applicationGroupName": "DNA", 
	            "planStatus": "planned", 
	            "chefLastUpdate": null, 
	            "samplePrepKitName": "Ion AmpliSeq Exome Kit", 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/104224/", 
	                    "id": 280107, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/280107/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/104224/", 
	                    "id": 280106, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/280106/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/104224/", 
	                    "id": 280105, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/280105/"
	                }
	            ], 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "templatingKitName": "Ion PI Template OT2 200 Kit v3", 
	            "runType": "AMPS_EXOME", 
	            "username": "ionuser", 
	            "planName": "-R61916-4BC_910-smn-", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "controlSequencekitname": "", 
	            "chefMessage": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "reverselibrarykey": "", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "chemdev", 
	            "usePostBeadfind": false, 
	            "runname": null, 
	            "planGUID": "cef01668-ca4f-4a0f-a469-5394d4756a3a", 
	            "planShortID": "C2AJH", 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 104224, 
	            "barcodedSamples": {
	                "P1-LQ910-01": {
	                    "barcodeSampleInfo": {
	                        "IonXpress_011": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/50/hg19/unmerged/detail/Exome_pool_BENQ_Designed_20130326_NoChrY.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "", 
	                            "controlSequenceType": "", 
	                            "externalId": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonXpress_011"
	                    ]
	                }
	            }, 
	            "regionfile": "", 
	            "selectedPlugins": {}, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "instrumentType": "", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 520, 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "date": "2014-05-01T19:35:00.000743+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "flowsInOrder": "", 
	            "sampleGrouping": null, 
	            "base_recalibrate": true, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/availableonetouchplannedexperiment/104224/", 
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

