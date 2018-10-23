.. _api_reference_compositeexperiment:

Composite Experiment  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/mesh/v1/compositeexperiment/``
| Schema URL ``http://mytorrentserver/rundb/api/mesh/v1/compositeexperiment/schema/``
| 

.. include:: ../references_manual_extras/compositeexperiment.rst

Resource Fields
---------------

========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                      help text                                                                                          default nullable readonly blank unique type     
========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**storage_options**        Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**               Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**                Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStartTime**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**_host**                  Host this resource is located on.                                                                  n/a     false    true     false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                     Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsSerialNum** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                   A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**ftpStatus**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayName**            Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**repResult**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsSerialNum**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 8, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/mesh/v1/compositeexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipDescription": "540", 
	            "chipType": "540", 
	            "results": [
	                {
	                    "status": "Completed", 
	                    "processedflows": 0, 
	                    "libmetrics": {
	                        "i100Q20_reads": 0, 
	                        "aveKeyCounts": 88, 
	                        "id": 1, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 0
	                    }, 
	                    "representative": false, 
	                    "analysis_metrics": {
	                        "ignored": 1042801, 
	                        "lib": 139085639, 
	                        "total_wells": 164699136, 
	                        "pinned": 2329, 
	                        "live": 140339912, 
	                        "excluded": 16543404, 
	                        "bead": 140400602, 
	                        "resource_uri": "", 
	                        "id": 1, 
	                        "empty": 6710000, 
	                        "libFinal": 93974105
	                    }, 
	                    "timeStamp": "2017-07-22T13:15:56.000197+00:00", 
	                    "analysismetrics": {
	                        "ignored": 1042801, 
	                        "lib": 139085639, 
	                        "total_wells": 164699136, 
	                        "pinned": 2329, 
	                        "live": 140339912, 
	                        "excluded": 16543404, 
	                        "bead": 140400602, 
	                        "resource_uri": "", 
	                        "id": 1, 
	                        "empty": 6710000, 
	                        "libFinal": 93974105
	                    }, 
	                    "reportLink": "/output/Home/Auto_S5-540_WholeTranscriptomeRNA_91_003/", 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 149.579903660696, 
	                        "q0_reads": 93969124, 
	                        "q0_bases": "14055892515", 
	                        "q20_reads": 93969124, 
	                        "q20_bases": "11916010889", 
	                        "q20_mean_read_length": 149, 
	                        "id": 1, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_S5-540_WholeTranscriptomeRNA_91", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 1, 
	                            "name": "demo", 
	                            "modified": "2018-02-28T17:32:01.000703+00:00"
	                        }
	                    ], 
	                    "status_display": "Completed", 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 149.579903660696, 
	                        "q0_reads": 93969124, 
	                        "q0_bases": "14055892515", 
	                        "q20_reads": 93969124, 
	                        "q20_bases": "11916010889", 
	                        "q20_mean_read_length": 149, 
	                        "id": 1, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "chipType": "540", 
	                        "reference": "", 
	                        "isPQ": false, 
	                        "references": "", 
	                        "barcodeKitName": "IonXpressRNA", 
	                        "resource_uri": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/3/", 
	                    "id": 3, 
	                    "autoExempt": false, 
	                    "isShowAllMetrics": true
	                }
	            ], 
	            "library": "", 
	            "sample": "", 
	            "runMode": "single", 
	            "storage_options": "A", 
	            "references": "", 
	            "chefStartTime": null, 
	            "repResult": "/rundb/api/v1/compositeresult/3/", 
	            "id": 91, 
	            "barcodedSamples": {}, 
	            "chefSolutionsSerialNum": "", 
	            "barcodeId": "IonXpressRNA", 
	            "sampleSetName": "", 
	            "platform": "S5", 
	            "status": "run", 
	            "applicationCategoryDisplayedName": "RNA Sequencing", 
	            "star": false, 
	            "sampleDisplayedName": "", 
	            "resultDate": "2017-07-22T13:15:56.000197+00:00", 
	            "flows": 500, 
	            "plan": {
	                "runType": "RNA", 
	                "sampleTubeLabel": null, 
	                "id": 99, 
	                "resource_uri": ""
	            }, 
	            "date": "2017-02-21T12:59:23+00:00", 
	            "ftpStatus": "0", 
	            "displayName": "S5-540 WholeTranscriptomeRNA", 
	            "notes": "", 
	            "chipInstrumentType": "S5", 
	            "pgmName": "S16", 
	            "keep": false, 
	            "expName": "S5-540_WholeTranscriptomeRNA", 
	            "chefReagentsSerialNum": "", 
	            "resource_uri": "/rundb/api/mesh/v1/compositeexperiment/91/"
	        }
	    ], 
	    "warnings": []
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

