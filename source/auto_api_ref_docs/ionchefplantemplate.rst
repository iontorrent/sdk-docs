Ionchefplantemplate Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/ionchefplantemplate/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/ionchefplantemplate/schema/``


.. include:: ../manual_api_ref_docs/ionchefplantemplate.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/ionchefplantemplate/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/ionchefplantemplate/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	ionchefplantemplates = ts_api_response["objects"]
	
	for ionchefplantemplate in ionchefplantemplates:
	    print ionchefplantemplate
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 17, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/ionchefplantemplate/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "IC_P1v2_VAL_ccp", 
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
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 100000", 
	            "sampleSet_planTotal": 0, 
	            "projects": [
	                "IC_P1v2_val"
	            ], 
	            "notes": "", 
	            "sequencekitname": "IonProtonIHiQ", 
	            "base_recalibration_mode": "no_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "stage1 map4", 
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
	            "experiment": "/rundb/api/v1/experiment/32917/", 
	            "bedfile": "/results/uploads/BED/44/hg19/unmerged/detail/CCP.20131001.designed.bed", 
	            "isReusable": true, 
	            "isDuplicateReads": false, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "tfKey": "ATCG", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "pending", 
	            "samplePrepKitName": "", 
	            "applicationGroupDisplayedName": "DNA", 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111154/", 
	                    "id": 289314, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289314/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111154/", 
	                    "id": 289313, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289313/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111154/", 
	                    "id": 289312, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289312/"
	                }
	            ], 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "templatingKitName": "Ion PROTON IC v2 Universal", 
	            "runType": "AMPS", 
	            "username": "ionuser", 
	            "planName": "IC_P1v2_VAL_ccp", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 100000", 
	            "controlSequencekitname": "", 
	            "chefMessage": "", 
	            "templatingSize": "200", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "runMode": "single", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "IC_P1v2_val", 
	            "usePostBeadfind": false, 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "planGUID": "b55face2-df5f-434c-89df-210f384170cb", 
	            "planShortID": "IL9TF", 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 111154, 
	            "barcodedSamples": {}, 
	            "regionfile": "/results/uploads/BED/47/hg19/unmerged/detail/CCP.20131001.hotspots.bed", 
	            "selectedPlugins": {
	                "SystematicErrorAnalysis": {
	                    "userInput": "", 
	                    "version": "0.8.5", 
	                    "features": [], 
	                    "name": "SystematicErrorAnalysis", 
	                    "id": 734
	                }, 
	                "IonReporterUploader": {
	                    "userInput": {
	                        "accountName": "None", 
	                        "userInputInfo": "", 
	                        "accountId": "0"
	                    }, 
	                    "version": "4.4.0.2", 
	                    "features": [
	                        "export"
	                    ], 
	                    "name": "IonReporterUploader", 
	                    "id": 993
	                }, 
	                "variantCaller": {
	                    "userInput": {
	                        "torrent_variant_caller": {
	                            "snp_min_allele_freq": "0.02", 
	                            "snp_strand_bias": "0.95", 
	                            "hotspot_min_coverage": 6, 
	                            "hotspot_min_cov_each_strand": 2, 
	                            "position_bias": "0.75", 
	                            "hotspot_min_allele_freq": "0.01", 
	                            "snp_min_variant_score": 6, 
	                            "mnp_min_variant_score": 400, 
	                            "hotspot_strand_bias": "0.95", 
	                            "hp_max_length": 8, 
	                            "filter_insertion_predictions": "0.2", 
	                            "indel_min_variant_score": 6, 
	                            "indel_min_coverage": 15, 
	                            "heavy_tailed": 3, 
	                            "outlier_probability": "0.005", 
	                            "position_bias_ref_fraction": "0.05", 
	                            "indel_strand_bias_pval": 1, 
	                            "data_quality_stringency": "6.5", 
	                            "snp_min_cov_each_strand": 0, 
	                            "indel_as_hpindel": 0, 
	                            "snp_strand_bias_pval": 1, 
	                            "mnp_strand_bias": "0.95", 
	                            "mnp_strand_bias_pval": 1, 
	                            "hotspot_strand_bias_pval": 1, 
	                            "hotspot_min_variant_score": 6, 
	                            "do_mnp_realignment": 1, 
	                            "indel_strand_bias": "0.9", 
	                            "downsample_to_coverage": 2000, 
	                            "filter_unusual_predictions": "0.3", 
	                            "indel_min_allele_freq": "0.05", 
	                            "mnp_min_allele_freq": "0.02", 
	                            "mnp_min_coverage": 6, 
	                            "do_snp_realignment": 1, 
	                            "mnp_min_cov_each_strand": 0, 
	                            "snp_min_coverage": 6, 
	                            "prediction_precision": 1, 
	                            "indel_min_cov_each_strand": 2, 
	                            "filter_deletion_predictions": "0.2", 
	                            "realignment_threshold": 1, 
	                            "suppress_recalibration": 0, 
	                            "position_bias_pval": "0.05", 
	                            "use_position_bias": 0
	                        }, 
	                        "meta": {
	                            "ts_version": "4.4", 
	                            "name": "Generic - Proton - Somatic - Low Stringency", 
	                            "user_selections": {
	                                "chip": "proton_p1", 
	                                "frequency": "somatic", 
	                                "library": "ampliseq", 
	                                "panel": "/rundb/api/v1/contentupload/48/"
	                            }, 
	                            "librarytype": "ampliseq", 
	                            "trimreads": true, 
	                            "tooltip": "Parameter settings optimized for low frequency variants and minimum false negatives on Proton chips", 
	                            "tvcargs": "tvc", 
	                            "barcode_mode": "match", 
	                            "based_on": "ampliseqexome_somatic_lowstringency_p1_parameters.json", 
	                            "built_in": true, 
	                            "configuration": "somatic_low_stringency_proton", 
	                            "compatibility": {
	                                "chip": [
	                                    "proton_p1"
	                                ], 
	                                "frequency": [
	                                    "somatic"
	                                ], 
	                                "stringency": [
	                                    "low"
	                                ], 
	                                "library": [
	                                    "wholegenome", 
	                                    "ampliseq", 
	                                    "targetseq"
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
	                            "gen_min_coverage": 6, 
	                            "allow_mnps": 1, 
	                            "allow_complex": 0, 
	                            "read_snp_limit": 10, 
	                            "read_max_mismatch_fraction": 1, 
	                            "allow_indels": 1, 
	                            "min_mapping_qv": 4, 
	                            "gen_min_alt_allele_freq": "0.035", 
	                            "allow_snps": 1, 
	                            "gen_min_indel_alt_allele_freq": "0.1"
	                        }
	                    }, 
	                    "version": "4.4.0.6", 
	                    "features": [], 
	                    "name": "variantCaller", 
	                    "id": 994
	                }, 
	                "validateVariantCaller": {
	                    "userInput": "", 
	                    "version": "0.2.1", 
	                    "features": [], 
	                    "name": "validateVariantCaller", 
	                    "id": 732
	                }, 
	                "validateVariantCaller-Lite": {
	                    "userInput": "", 
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
	                }
	            }, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 400, 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "date": "2015-01-28T19:57:42.000445+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "flowsInOrder": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/ionchefplantemplate/111154/", 
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

