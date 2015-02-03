Monitorresult Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/monitorresult/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/monitorresult/schema/``


.. include:: ../manual_api_ref_docs/monitorresult.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysismetrics** A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**         Unicode string data. Ex: "Hello World"                                                             n/a     true     true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
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
**barcodeId**       Unicode string data. Ex: "Hello World"                                                             n/a     true     true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/monitorresult/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/monitorresult/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	monitorresults = ts_api_response["objects"]
	
	for monitorresult in monitorresults:
	    print monitorresult
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 49, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/monitorresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "libmetrics": {
	                "i100Q20_reads": 63353502, 
	                "aveKeyCounts": 84, 
	                "id": 52457, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 180
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
	            "library": "hg19", 
	            "id": 317423, 
	            "reportStatus": "Nothing", 
	            "experiment": {
	                "ftpStatus": "Complete", 
	                "chipInstrumentType": "proton", 
	                "displayName": "user F3--909--R78811-mosaic1tru4 1xot2 na12878 1400Mmol 4chips-co", 
	                "chipType": "P1.1.17", 
	                "notes": "mosaic 1 ot 4 chips 1400M molecules", 
	                "chipDescription": "PI", 
	                "resultDate": "2015-02-03T02:21:07.000963+00:00", 
	                "flows": 520, 
	                "runMode": "single", 
	                "expName": "R_2015_02_02_13_18_20_user_F3--909--R78811-mosaic1tru4_1xot2_na12878_1400Mmol_4chips-co", 
	                "storage_options": "D", 
	                "pgmName": "f3", 
	                "date": "2015-02-02T18:23:59+00:00", 
	                "star": false, 
	                "resource_uri": "", 
	                "qcThresholds": {
	                    "Key Signal (1-100)": 30, 
	                    "Usable Sequence (%)": 30, 
	                    "Bead Loading (%)": 30
	                }, 
	                "id": 33084, 
	                "plan": {
	                    "runType": "WGNM", 
	                    "id": 111321, 
	                    "resource_uri": ""
	                }
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
	            "resource_uri": "/rundb/api/v1/monitorresult/317423/", 
	            "barcodeId": "IonXpress", 
	            "autoExempt": false, 
	            "representative": false
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

