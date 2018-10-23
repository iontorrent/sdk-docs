.. _api_reference_compositeresult:

Composite Result  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/compositeresult/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/compositeresult/schema/``
| 

.. include:: ../references_manual_extras/compositeresult.rst

Resource Fields
---------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysismetrics** A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
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

