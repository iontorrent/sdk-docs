Availableonetouchplannedexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/availableonetouchplannedexperiment/schema/``


.. include:: ../manual_api_ref_docs/availableonetouchplannedexperiment.rst

Fields table
------------

================================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                             help text                                                                                          default nullable readonly blank unique type     
================================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
**planDisplayedName**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                   Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                   Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStatus**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planTotal**           Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**       Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                        Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**               Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                      Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefProgress**                  Floating point numeric data. Ex: 26.73                                                             0       false    false    true  false  float    
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                       Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**             Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                     Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLogPath**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                       Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**              Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                    Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**          Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                      Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_uid**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planIndex**           Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                       Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefMessage**                   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingSize**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                    A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                       Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**               Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**             Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetGroupType**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                        Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                            Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet**                     A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**               Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                    Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**              Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**        Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                  Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                  Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
--------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**          Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
================================= ================================================================================================== ======= ======== ======== ===== ====== ======== 

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
	        "total_count": 85, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/availableonetouchplannedexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "-R78595-2X_POU_L040_W3_3", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "chefStatus": "", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "libkit": null, 
	            "platform": "", 
	            "categories": "", 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --max-phasing-levels 2", 
	            "alignmentargs": "-J 25 --end-repair 15 --do-repeat-clip --context stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 100000", 
	            "sampleSet_planTotal": 0, 
	            "projects": [
	                "p1_ie_chem"
	            ], 
	            "notes": "HiQ_val settings", 
	            "sequencekitname": "IonProtonIHiQ", 
	            "base_recalibration_mode": "standard_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "-J 25 --end-repair 15 --do-repeat-clip --context stage1 map4", 
	            "chipType": "P1.1.17", 
	            "chefProgress": 0, 
	            "library": "hg19", 
	            "reverselibrarykey": "", 
	            "sampleTubeLabel": "", 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/32970/", 
	            "bedfile": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	            "isReusable": false, 
	            "isDuplicateReads": false, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "tfKey": "ATCG", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "planned", 
	            "samplePrepKitName": "Ion AmpliSeq Exome Kit", 
	            "applicationGroupDisplayedName": "DNA", 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111207/", 
	                    "id": 289470, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289470/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111207/", 
	                    "id": 289469, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289469/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111207/", 
	                    "id": 289468, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289468/"
	                }
	            ], 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "templatingKitName": "Ion PI Hi-Q OT2 200 Kit", 
	            "runType": "AMPS_EXOME", 
	            "username": "ionuser", 
	            "planName": "-R78595-2X_POU_L040_W3_3", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 100000", 
	            "controlSequencekitname": "", 
	            "chefMessage": "", 
	            "templatingSize": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "runMode": "single", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "p1_ie_chem", 
	            "usePostBeadfind": false, 
	            "libraryReadLength": 0, 
	            "runname": null, 
	            "planGUID": "e6b0a446-7b90-4a9a-aa3b-d59336da12d3", 
	            "planShortID": "FIWLX", 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 111207, 
	            "barcodedSamples": {
	                "609463": {
	                    "barcodeSampleInfo": {
	                        "IonXpress_089": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": ""
	                        }, 
	                        "IonXpress_078": {
	                            "description": "", 
	                            "reference": "hg19", 
	                            "targetRegionBedFile": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	                            "hotSpotRegionBedFile": "", 
	                            "nucleotideType": "DNA", 
	                            "controlSequenceType": "", 
	                            "externalId": ""
	                        }
	                    }, 
	                    "barcodes": [
	                        "IonXpress_078", 
	                        "IonXpress_089"
	                    ]
	                }
	            }, 
	            "regionfile": "", 
	            "selectedPlugins": {
	                "SystematicErrorAnalysis": {
	                    "userInput": "", 
	                    "version": "0.8.5", 
	                    "features": [], 
	                    "name": "SystematicErrorAnalysis", 
	                    "id": 734
	                }, 
	                "pixelDrift": {
	                    "userInput": "", 
	                    "version": "1.1.1", 
	                    "features": [], 
	                    "name": "pixelDrift", 
	                    "id": 1000
	                }, 
	                "variantCaller": {
	                    "userInput": {
	                        "torrent_variant_caller": {
	                            "snp_min_allele_freq": "0.1", 
	                            "snp_strand_bias": "0.98", 
	                            "hotspot_min_coverage": 6, 
	                            "hotspot_min_cov_each_strand": 3, 
	                            "position_bias": "0.75", 
	                            "hotspot_min_allele_freq": "0.1", 
	                            "snp_min_variant_score": 15, 
	                            "mnp_min_variant_score": 60, 
	                            "hotspot_strand_bias": "0.95", 
	                            "hp_max_length": 8, 
	                            "filter_insertion_predictions": "0.2", 
	                            "indel_min_variant_score": 20, 
	                            "indel_min_coverage": 10, 
	                            "heavy_tailed": 3, 
	                            "outlier_probability": "0.01", 
	                            "position_bias_ref_fraction": "0.05", 
	                            "indel_strand_bias_pval": 1, 
	                            "data_quality_stringency": 5, 
	                            "snp_min_cov_each_strand": 0, 
	                            "indel_as_hpindel": 1, 
	                            "snp_strand_bias_pval": "0.01", 
	                            "mnp_strand_bias": "0.98", 
	                            "mnp_strand_bias_pval": "0.01", 
	                            "hotspot_strand_bias_pval": 1, 
	                            "hotspot_min_variant_score": 10, 
	                            "sse_prob_threshold": "0.2", 
	                            "do_mnp_realignment": 0, 
	                            "indel_strand_bias": "0.9", 
	                            "downsample_to_coverage": 400, 
	                            "filter_unusual_predictions": "0.25", 
	                            "indel_min_allele_freq": "0.25", 
	                            "mnp_min_allele_freq": "0.1", 
	                            "mnp_min_coverage": 5, 
	                            "do_snp_realignment": 0, 
	                            "mnp_min_cov_each_strand": 0, 
	                            "snp_min_coverage": 5, 
	                            "prediction_precision": 1, 
	                            "indel_min_cov_each_strand": 5, 
	                            "filter_deletion_predictions": "0.2", 
	                            "realignment_threshold": 0, 
	                            "suppress_recalibration": 0, 
	                            "position_bias_pval": "0.05", 
	                            "use_position_bias": 1
	                        }, 
	                        "meta": {
	                            "ts_version": "4.4", 
	                            "name": "Generic - Proton - Germ Line - Low Stringency", 
	                            "user_selections": {
	                                "chip": "proton_p1", 
	                                "frequency": "germline", 
	                                "library": "ampliseq", 
	                                "panel": ""
	                            }, 
	                            "librarytype": "ampliseq", 
	                            "trimreads": true, 
	                            "tooltip": "Parameter settings optimized for high frequency variants and minimum false negatives on AmpliSeq libraries and Proton chips", 
	                            "tvcargs": "tvc", 
	                            "barcode_mode": "match", 
	                            "based_on": "ampliseqexome_germline_lowstringency_p1_parameters.json", 
	                            "built_in": true, 
	                            "configuration": "germline_low_stringency_proton", 
	                            "compatibility": {
	                                "chip": [
	                                    "proton_p1"
	                                ], 
	                                "frequency": [
	                                    "germline"
	                                ], 
	                                "stringency": [
	                                    "low"
	                                ], 
	                                "library": [
	                                    "wholegenome", 
	                                    "ampliseq"
	                                ]
	                            }
	                        }, 
	                        "long_indel_assembler": {
	                            "min_indel_size": 4, 
	                            "short_suffix_match": 5, 
	                            "output_mnv": 0, 
	                            "min_var_count": 5, 
	                            "min_var_freq": "0.15", 
	                            "kmer_len": 19, 
	                            "max_hp_length": 8, 
	                            "relative_strand_bias": "0.8"
	                        }, 
	                        "freebayes": {
	                            "gen_min_coverage": 5, 
	                            "allow_mnps": 1, 
	                            "allow_complex": 0, 
	                            "read_snp_limit": 10, 
	                            "read_max_mismatch_fraction": 1, 
	                            "allow_indels": 1, 
	                            "min_mapping_qv": 4, 
	                            "gen_min_alt_allele_freq": "0.1", 
	                            "allow_snps": 1, 
	                            "gen_min_indel_alt_allele_freq": "0.15"
	                        }
	                    }, 
	                    "version": "4.4.0.6", 
	                    "features": [], 
	                    "name": "variantCaller", 
	                    "id": 994
	                }, 
	                "validateVariantCaller": {
	                    "userInput": {
	                        "variant_caller_name": "variantCaller", 
	                        "truth_major_snp": "NA12878_NIST_NoChrY_SNP.bed", 
	                        "region": "NIST", 
	                        "sample": "NA12878", 
	                        "truth_minor_snp": "None", 
	                        "truth_major_indel": "NA12878_NIST_NoChrY_indel.bed", 
	                        "truth_minor_indel": "None"
	                    }, 
	                    "version": "0.2.1", 
	                    "features": [], 
	                    "name": "validateVariantCaller", 
	                    "id": 732
	                }, 
	                "flowCell": {
	                    "userInput": "", 
	                    "version": "0.2.2", 
	                    "features": [], 
	                    "name": "flowCell", 
	                    "id": 195
	                }, 
	                "validateVariantCaller-Lite": {
	                    "userInput": {
	                        "variant_caller_name": "recent", 
	                        "truth_major": "NA12878_AmpliseqExome_nist_new2.18.vcf", 
	                        "region": "NIST-new", 
	                        "sample": "NA12878", 
	                        "runmode": "Lite", 
	                        "truth_minor": "None", 
	                        "truth_region": "NIST_AExome.new2.18.bed"
	                    }, 
	                    "version": "1.1.6", 
	                    "features": [], 
	                    "name": "validateVariantCaller-Lite", 
	                    "id": 964
	                }, 
	                "coverageAnalysis": {
	                    "userInput": "", 
	                    "version": "4.4.0.12", 
	                    "features": [], 
	                    "name": "coverageAnalysis", 
	                    "id": 995
	                }, 
	                "flowErr": {
	                    "userInput": "", 
	                    "version": "0.2", 
	                    "features": [], 
	                    "name": "flowErr", 
	                    "id": 131
	                }
	            }, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 520, 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "date": "2015-01-29T18:04:59.000418+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "flowsInOrder": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/availableonetouchplannedexperiment/111207/", 
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

