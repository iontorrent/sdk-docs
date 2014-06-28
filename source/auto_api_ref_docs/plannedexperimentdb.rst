Plannedexperimentdb Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentdb/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentdb/schema/``


.. include:: ../manual_api_ref_docs/plannedexperimentdb.rst

Fields table
------------

=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                                                                          default nullable readonly blank unique type     
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**isReverseRun**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefLastUpdate**              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
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
**chefLogPath**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet_planTotal**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSet**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefProgress**                Floating point numeric data. Ex: 26.73                                                             0.0     false    false    true  false  float    
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                  Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefMessage**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                  Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                  A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
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
**usePostBeadfind**             Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                                                                                     false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentdb/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/plannedexperimentdb/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	plannedexperimentdbs = ts_api_response["objects"]
	
	for plannedexperimentdb in plannedexperimentdbs:
	    print plannedexperimentdb
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 18369, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperimentdb/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isReverseRun": false, 
	            "planDisplayedName": "CopyOfSystemDefault_R_2014_06_27_14_19_01_user_P19-606", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "isSystemDefault": false, 
	            "username": null, 
	            "planShortID": "G5B50", 
	            "planStatus": "run", 
	            "chefLastUpdate": null, 
	            "templatingKitBarcode": null, 
	            "sampleTubeLabel": null, 
	            "planExecutedDate": null, 
	            "chefStatus": "", 
	            "samplePrepKitName": null, 
	            "reverse_primer": null, 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "seqKitBarcode": null, 
	            "id": 102212, 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": false, 
	            "sampleSet_planIndex": 0, 
	            "qcValues": [
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/102212/", 
	                    "id": 266571, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Bead Loading (%)", 
	                        "id": 1, 
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/266571/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/102212/", 
	                    "id": 266570, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 1, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Key Signal (1-100)", 
	                        "id": 2, 
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/266570/"
	                }, 
	                {
	                    "threshold": 30, 
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/102212/", 
	                    "id": 266569, 
	                    "qcType": {
	                        "description": "", 
	                        "minThreshold": 0, 
	                        "maxThreshold": 100, 
	                        "defaultThreshold": 30, 
	                        "qcName": "Usable Sequence (%)", 
	                        "id": 3, 
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/266569/"
	                }
	            ], 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "sampleSet_planTotal": 0, 
	            "experiment": "/rundb/api/v1/experiment/23975/", 
	            "projects": [], 
	            "runType": "GENS", 
	            "sampleSet": null, 
	            "planPGM": null, 
	            "chefProgress": 0.0, 
	            "autoName": null, 
	            "isReusable": false, 
	            "controlSequencekitname": null, 
	            "date": "2014-06-27T23:36:06.000229+00:00", 
	            "isSystem": false, 
	            "libkit": null, 
	            "categories": "", 
	            "planName": "CopyOfSystemDefault_R_2014_06_27_14_19_01_user_P19-606", 
	            "chefMessage": "", 
	            "parentPlan": null, 
	            "childPlans": [], 
	            "templatingKitName": "Ion PI Template OT2 200 Kit v3", 
	            "pairedEndLibraryAdapterName": null, 
	            "runMode": "single", 
	            "adapter": null, 
	            "sampleGrouping": null, 
	            "irworkflow": "", 
	            "chipBarcode": null, 
	            "planExecuted": true, 
	            "project": "", 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "R_2014_06_27_14_19_01_user_P19-606", 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "80384c15-e0e2-4909-9d4c-950731bf1cf4", 
	            "cycles": null, 
	            "resource_uri": "/rundb/api/v1/plannedexperimentdb/102212/"
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

