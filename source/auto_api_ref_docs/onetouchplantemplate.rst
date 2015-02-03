Onetouchplantemplate Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/schema/``


.. include:: ../manual_api_ref_docs/onetouchplantemplate.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/onetouchplantemplate/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	onetouchplantemplates = ts_api_response["objects"]
	
	for onetouchplantemplate in onetouchplantemplates:
	    print onetouchplantemplate
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 111, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/onetouchplantemplate/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "Ceph_RnD_IC_PIv2", 
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
	            "projects": [], 
	            "notes": "", 
	            "sequencekitname": "IonProtonIHiQ", 
	            "base_recalibration_mode": "standard_recal", 
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
	            "barcodeId": "", 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/32900/", 
	            "bedfile": "", 
	            "isReusable": true, 
	            "isDuplicateReads": true, 
	            "thumbnailbeadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=100,100 --beadfind-thumbnail 1", 
	            "librarykitname": "Ion Xpress Plus Fragment Library Kit", 
	            "adapter": null, 
	            "basecallerargs": "BaseCaller --barcode-filter 0.01 --barcode-filter-minreads 10 --keypass-filter on --phasing-residual-filter=2.0 --num-unfiltered 1000 --barcode-filter-postpone 1", 
	            "tfKey": "ATCG", 
	            "parentPlan": null, 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "planned", 
	            "samplePrepKitName": "", 
	            "applicationGroupDisplayedName": "DNA", 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": false, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111137/", 
	                    "id": 289263, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289263/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111137/", 
	                    "id": 289262, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289262/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/111137/", 
	                    "id": 289261, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/289261/"
	                }
	            ], 
	            "analysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=216,224 --bkg-bfmask-update false --gpuWorkLoad 1 --total-timeout 600 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "thumbnailcalibrateargs": "calibrate --skipDroop", 
	            "templatingKitName": "Ion PI Hi-Q OT2 200 Kit", 
	            "runType": "WGNM", 
	            "username": "ionadmin", 
	            "planName": "Ceph_RnD_IC_PIv2", 
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
	            "project": "", 
	            "usePostBeadfind": false, 
	            "libraryReadLength": 0, 
	            "runname": null, 
	            "planGUID": "f35c5c0d-f01a-405c-9049-8139b2f26a13", 
	            "planShortID": "8SJUE", 
	            "sampleSetGroupType": null, 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 111137, 
	            "barcodedSamples": {}, 
	            "regionfile": "", 
	            "selectedPlugins": {
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
	                "duplicateReads_useZC": {
	                    "userInput": "", 
	                    "version": "1.0.0", 
	                    "features": [], 
	                    "name": "duplicateReads_useZC", 
	                    "id": 429
	                }
	            }, 
	            "beadfindargs": "justBeadFind --beadfind-minlivesnr 3 --region-size=216,224 --total-timeout 600", 
	            "sampleSet": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 520, 
	            "thumbnailanalysisargs": "Analysis --from-beadfind --clonal-filter-bkgmodel true --region-size=100,100 --bkg-bfmask-update false --gpuWorkLoad 1 --bkg-debug-param 1 --beadfind-thumbnail 1 --gopt /opt/ion/config/gopt_p1.1.17_ampliseq_exome.param.json", 
	            "date": "2015-01-28T18:37:09.000403+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "sampleSetDisplayedName": "", 
	            "calibrateargs": "calibrate --skipDroop", 
	            "flowsInOrder": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": null, 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/onetouchplantemplate/111137/", 
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

