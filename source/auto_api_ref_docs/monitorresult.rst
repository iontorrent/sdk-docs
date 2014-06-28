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
	        "total_count": 159, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/monitorresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "libmetrics": {
	                "i100Q20_reads": 61016174, 
	                "aveKeyCounts": 89.0, 
	                "id": 41874, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 159
	            }, 
	            "timeStamp": "2014-06-28T07:11:58.000789+00:00", 
	            "analysismetrics": {
	                "ignored": 1364892, 
	                "lib": 118063544, 
	                "total_wells": 164699136, 
	                "pinned": 463867, 
	                "live": 118074386, 
	                "excluded": 16095180, 
	                "bead": 118525043, 
	                "resource_uri": "", 
	                "id": 41726, 
	                "empty": 28250154, 
	                "libFinal": 85604279
	            }, 
	            "reportLink": "/output/Home/Auto_user_Z28-428--r65714-pou4_dbsa_23958_304393/", 
	            "library": "hg19", 
	            "id": 304393, 
	            "reportStatus": "Nothing", 
	            "experiment": {
	                "ftpStatus": "Complete", 
	                "chipInstrumentType": "proton", 
	                "displayName": "user Z28-428--r65714-pou4 dbsa", 
	                "chipType": "P1.1.17", 
	                "notes": "", 
	                "chipDescription": "PI", 
	                "resultDate": "2014-06-28T07:11:58.000789+00:00", 
	                "flows": 520, 
	                "runMode": "single", 
	                "expName": "R_2014_06_27_17_13_22_user_Z28-428--r65714-pou4_dbsa", 
	                "storage_options": "D", 
	                "pgmName": "Z28", 
	                "date": "2014-06-27T21:19:01+00:00", 
	                "star": false, 
	                "resource_uri": "", 
	                "qcThresholds": {
	                    "Key Signal (1-100)": 30, 
	                    "Usable Sequence (%)": 30, 
	                    "Bead Loading (%)": 30
	                }, 
	                "id": 23958, 
	                "plan": {
	                    "runType": "AMPS_EXOME", 
	                    "id": 102195, 
	                    "resource_uri": ""
	                }
	            }, 
	            "resultsName": "Auto_user_Z28-428--r65714-pou4_dbsa_23958", 
	            "projects": [
	                {
	                    "resource_uri": "", 
	                    "id": 1385, 
	                    "name": "auto_chip", 
	                    "modified": "2014-06-27T21:21:43.000081+00:00"
	                }
	            ], 
	            "qualitymetrics": {
	                "q0_mean_read_length": 178.362197969099, 
	                "q0_reads": 85604279, 
	                "q0_bases": "15268567358", 
	                "q20_reads": 85604279, 
	                "q20_bases": "13060288783", 
	                "q20_mean_read_length": 178, 
	                "id": 39683, 
	                "resource_uri": ""
	            }, 
	            "eas": {
	                "resource_uri": "", 
	                "reference": "hg19", 
	                "barcodeKitName": "IonXpress"
	            }, 
	            "resource_uri": "/rundb/api/v1/monitorresult/304393/", 
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

