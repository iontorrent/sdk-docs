Compositeexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/schema/``


.. include:: ../manual_api_ref_docs/compositeexperiment.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**ftpStatus**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options** Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**            Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**           Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**repResult**       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/compositeexperiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	compositeexperiments = ts_api_response["objects"]
	
	for compositeexperiment in compositeexperiments:
	    print compositeexperiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 26763, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipInstrumentType": "proton", 
	            "chipType": "P1.1.17", 
	            "results": [
	                {
	                    "status": "Completed", 
	                    "processedflows": 0, 
	                    "analysis_metrics": {
	                        "ignored": 1416707, 
	                        "lib": 122792563, 
	                        "total_wells": 164699136, 
	                        "pinned": 345310, 
	                        "live": 122796187, 
	                        "excluded": 16095180, 
	                        "bead": 123099544, 
	                        "resource_uri": "", 
	                        "id": 54528, 
	                        "empty": 23742395, 
	                        "libFinal": 85173747
	                    }, 
	                    "timeStamp": "2015-02-03T02:21:07.000963+00:00", 
	                    "analysismetrics": {
	                        "ignored": 1416707, 
	                        "lib": 122792563, 
	                        "total_wells": 164699136, 
	                        "pinned": 345310, 
	                        "live": 122796187, 
	                        "excluded": 16095180, 
	                        "bead": 123099544, 
	                        "resource_uri": "", 
	                        "id": 54528, 
	                        "empty": 23742395, 
	                        "libFinal": 85173747
	                    }, 
	                    "reportLink": "/output/Home/Auto_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co_33084_317423/", 
	                    "id": 317423, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 203.07748070541, 
	                        "q0_reads": 85173747, 
	                        "q0_bases": "17296869963", 
	                        "q20_reads": 85173747, 
	                        "q20_bases": "15168226464", 
	                        "q20_mean_read_length": 203, 
	                        "id": 50272, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co_33084", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 1622, 
	                            "name": "mosaic_enterprise", 
	                            "modified": "2015-02-02T18:26:29.000916+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 203.07748070541, 
	                        "q0_reads": 85173747, 
	                        "q0_bases": "17296869963", 
	                        "q20_reads": 85173747, 
	                        "q20_bases": "15168226464", 
	                        "q20_mean_read_length": 203, 
	                        "id": 50272, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "hg19", 
	                        "barcodeKitName": "IonXpress"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/317423/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 63353502, 
	                        "aveKeyCounts": 84, 
	                        "id": 52457, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 180
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 6676, 
	                        "lib": 754498, 
	                        "total_wells": 960000, 
	                        "pinned": 40056, 
	                        "live": 754506, 
	                        "excluded": 0, 
	                        "bead": 756432, 
	                        "resource_uri": "", 
	                        "id": 54510, 
	                        "empty": 156836, 
	                        "libFinal": 502627
	                    }, 
	                    "timeStamp": "2015-02-02T21:18:01.000809+00:00", 
	                    "analysismetrics": {
	                        "ignored": 6676, 
	                        "lib": 754498, 
	                        "total_wells": 960000, 
	                        "pinned": 40056, 
	                        "live": 754506, 
	                        "excluded": 0, 
	                        "bead": 756432, 
	                        "resource_uri": "", 
	                        "id": 54510, 
	                        "empty": 156836, 
	                        "libFinal": 502627
	                    }, 
	                    "reportLink": "/output/Home/Auto_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co_33084_tn_317424/", 
	                    "id": 317424, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 202.425096542764, 
	                        "q0_reads": 502627, 
	                        "q0_bases": "101744319", 
	                        "q20_reads": 502627, 
	                        "q20_bases": "88430873", 
	                        "q20_mean_read_length": 202, 
	                        "id": 50259, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co_33084_tn", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 1622, 
	                            "name": "mosaic_enterprise", 
	                            "modified": "2015-02-02T18:26:29.000916+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 202.425096542764, 
	                        "q0_reads": 502627, 
	                        "q0_bases": "101744319", 
	                        "q20_reads": 502627, 
	                        "q20_bases": "88430873", 
	                        "q20_mean_read_length": 202, 
	                        "id": 50259, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "hg19", 
	                        "barcodeKitName": "IonXpress"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/317424/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 364623, 
	                        "aveKeyCounts": 84, 
	                        "id": 52444, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 177
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }
	            ], 
	            "library": "hg19", 
	            "sample": "609600", 
	            "runMode": "single", 
	            "storage_options": "D", 
	            "repResult": "/rundb/api/v1/compositeresult/317424/", 
	            "id": 33084, 
	            "archived": false, 
	            "barcodeId": "IonXpress", 
	            "sampleSetName": "", 
	            "star": false, 
	            "resultDate": "2015-02-03T02:21:07.000963+00:00", 
	            "flows": 520, 
	            "plan": {
	                "runType": "WGNM", 
	                "id": 111321, 
	                "resource_uri": ""
	            }, 
	            "date": "2015-02-02T18:23:59+00:00", 
	            "ftpStatus": "Complete", 
	            "notes": "mosaic 1 ot 4 chips 1400M molecules", 
	            "chipDescription": "PI", 
	            "pgmName": "f3", 
	            "keep": false, 
	            "expName": "R_2015_02_02_13_18_20_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co", 
	            "resource_uri": "/rundb/api/v1/compositeexperiment/33084/"
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

