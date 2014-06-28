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
**chefProgress**                  Floating point numeric data. Ex: 26.73                                                             0.0     false    false    true  false  float    
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
**chefLogPath**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
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
**chefLastUpdate**                A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
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
**base_recalibrate**              Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
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
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/ionchefplantemplate/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "chef_useGUI_Exome Panel_AmpliSeqExome.20131001", 
	            "autoAnalyze": true, 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "chefStatus": "", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "libkit": null, 
	            "platform": "", 
	            "categories": "", 
	            "planPGM": null, 
	            "prebasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 1000 --calibration-training=100000 --flow-signals-type scaled-residual --max-phasing-levels 2", 
	            "alignmentargs": "stage1 map4", 
	            "thumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000", 
	            "sampleSet_planTotal": 0, 
	            "projects": [], 
	            "notes": "Uploaded from amplseq.com and available at-jira.itw_wiki_x_HAHcAg\r\nReplace _ with slashes for link to Document collection on JIRA\r\nAdded AmpliseqExome.germline_lowstringency_p1.4_0.20130920.parameters.json parameter file.", 
	            "sequencekitname": "ProtonIIC200Kit", 
	            "storageHost": null, 
	            "expName": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "stage1 map4", 
	            "chipType": "P1.1.17", 
	            "chefProgress": 0.0, 
	            "library": "hg19", 
	            "reverselibrarykey": "", 
	            "sampleTubeLabel": "", 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/21899/", 
	            "bedfile": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	            "isReusable": true, 
	            "isDuplicateReads": false, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "tfKey": "ATCG", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "pending", 
	            "chefLastUpdate": null, 
	            "samplePrepKitName": "Ion AmpliSeq Exome Kit", 
	            "applicationGroupDisplayedName": "DNA", 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/100136/", 
	                    "id": 262521, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/262521/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/100136/", 
	                    "id": 262520, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/262520/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/100136/", 
	                    "id": 262519, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/262519/"
	                }
	            ], 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "templatingKitName": "Ion PI IC 200 Kit", 
	            "runType": "AMPS_EXOME", 
	            "username": "ionuser", 
	            "planName": "chef_useGUI_Exome_Panel_AmpliSeqExome.20131001", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0  --num-unfiltered 100000 --calibration-training=100000 --flow-signals-type scaled-residual", 
	            "controlSequencekitname": "", 
	            "chefMessage": "", 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "runMode": "single", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "", 
	            "usePostBeadfind": false, 
	            "runname": null, 
	            "planGUID": "83e69cd8-ca3a-4ff2-b4ac-dd637184e28e", 
	            "planShortID": "YHFWJ", 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 100136, 
	            "barcodedSamples": {}, 
	            "regionfile": "", 
	            "selectedPlugins": {
	                "IonReporterUploader": {
	                    "userInput": {
	                        "accountName": "None", 
	                        "userInputInfo": "", 
	                        "accountId": "0"
	                    }, 
	                    "version": "4.1-r87449", 
	                    "features": [
	                        "export"
	                    ], 
	                    "name": "IonReporterUploader", 
	                    "id": 804
	                }, 
	                "coverageAnalysis": {
	                    "userInput": "", 
	                    "version": "4.2-r86949", 
	                    "features": [], 
	                    "name": "coverageAnalysis", 
	                    "id": 800
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
	                "variantCaller": {
	                    "userInput": {
	                        "torrent_variant_caller": {
	                            "snp_min_allele_freq": "0.10000000000000001", 
	                            "snp_strand_bias": "0.97999999999999998", 
	                            "hotspot_min_coverage": 6, 
	                            "hotspot_min_cov_each_strand": 3, 
	                            "hotspot_min_allele_freq": "0.10000000000000001", 
	                            "snp_min_variant_score": 15, 
	                            "hotspot_strand_bias": "0.94999999999999996", 
	                            "hp_max_length": 8, 
	                            "filter_insertion_predictions": "0.20000000000000001", 
	                            "indel_min_variant_score": 20, 
	                            "indel_min_coverage": 10, 
	                            "heavy_tailed": 3, 
	                            "outlier_probability": "0.01", 
	                            "data_quality_stringency": 5, 
	                            "snp_min_cov_each_strand": 0, 
	                            "hotspot_min_variant_score": 10, 
	                            "indel_strand_bias": "0.90000000000000002", 
	                            "tvc_parameters_version": "germline_low_stringency_proton-3.6.66827", 
	                            "downsample_to_coverage": 400, 
	                            "filter_unusual_predictions": "0.25", 
	                            "indel_min_allele_freq": "0.14999999999999999", 
	                            "do_snp_realignment": 1, 
	                            "prediction_precision": 1, 
	                            "indel_min_cov_each_strand": 5, 
	                            "filter_deletion_predictions": "0.20000000000000001", 
	                            "suppress_recalibration": 0, 
	                            "snp_min_coverage": 5
	                        }, 
	                        "meta": {
	                            "repository_id": "", 
	                            "ts_version": "4.0", 
	                            "name": "External file AmpliseqExome.germline_lowstringency_p1.4_0.20130920.parameters.json", 
	                            "user_selections": {
	                                "chip": "proton_p1", 
	                                "frequency": "germline", 
	                                "library": "ampliseq", 
	                                "panel": "/rundb/api/v1/contentupload/53/"
	                            }, 
	                            "librarytype": "ampliseq", 
	                            "trimreads": true, 
	                            "tooltip": "Retrieved from external file", 
	                            "tvcargs": "tvc", 
	                            "built_in": false, 
	                            "configuration": "", 
	                            "compatibility": {}
	                        }, 
	                        "long_indel_assembler": {
	                            "min_indel_size": 4, 
	                            "short_suffix_match": 5, 
	                            "output_mnv": 0, 
	                            "min_var_count": 5, 
	                            "min_var_freq": "0.14999999999999999", 
	                            "kmer_len": 19, 
	                            "max_hp_length": 8, 
	                            "relative_strand_bias": "0.80000000000000004"
	                        }, 
	                        "freebayes": {
	                            "gen_min_coverage": 5, 
	                            "allow_mnps": 1, 
	                            "allow_complex": 0, 
	                            "read_max_mismatch_fraction": 1, 
	                            "read_mismatch_limit": 10, 
	                            "allow_indels": 1, 
	                            "min_mapping_qv": 4, 
	                            "gen_min_alt_allele_freq": "0.10000000000000001", 
	                            "allow_snps": 1, 
	                            "gen_min_indel_alt_allele_freq": "0.14999999999999999"
	                        }
	                    }, 
	                    "version": "4.1-r74477", 
	                    "features": [], 
	                    "name": "variantCaller", 
	                    "id": 698
	                }, 
	                "AmpliconStats": {
	                    "userInput": "", 
	                    "version": "0.4.5", 
	                    "features": [], 
	                    "name": "AmpliconStats", 
	                    "id": 774
	                }
	            }, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 520, 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "date": "2014-05-20T13:56:24.000114+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "flowsInOrder": "", 
	            "sampleGrouping": null, 
	            "base_recalibrate": true, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/ionchefplantemplate/100136/", 
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

