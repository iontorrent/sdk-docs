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
	        "total_count": 84, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/monitorresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "libmetrics": {
	                "i100Q20_reads": 25649023, 
	                "aveKeyCounts": 64.0, 
	                "id": 35097, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 115
	            }, 
	            "timeStamp": "2014-05-01T20:06:49.000663+00:00", 
	            "analysismetrics": {
	                "ignored": 3514741, 
	                "lib": 138786910, 
	                "total_wells": 164699136, 
	                "pinned": 1352977, 
	                "live": 138797327, 
	                "excluded": 16095180, 
	                "bead": 138900214, 
	                "resource_uri": "", 
	                "id": 34888, 
	                "empty": 4836024, 
	                "libFinal": 84929565
	            }, 
	            "reportLink": "/output/Home/C1--479-fc-BC-reanal_56256/", 
	            "library": "hg19", 
	            "id": 56256, 
	            "reportStatus": "Nothing", 
	            "experiment": {
	                "ftpStatus": "Complete", 
	                "chipInstrumentType": "proton", 
	                "displayName": "user C1--479-r61824-", 
	                "chipType": "P1.1.17", 
	                "notes": "", 
	                "chipDescription": "PI", 
	                "resultDate": "2014-05-01T20:06:49.000663+00:00", 
	                "flows": 520, 
	                "runMode": "single", 
	                "expName": "R_2014_04_30_17_19_55_user_C1--479-r61824-", 
	                "storage_options": "D", 
	                "pgmName": "c1", 
	                "date": "2014-05-01T00:23:00+00:00", 
	                "star": false, 
	                "resource_uri": "", 
	                "qcThresholds": {
	                    "Key Signal (1-100)": 30, 
	                    "Usable Sequence (%)": 30, 
	                    "Bead Loading (%)": 30
	                }, 
	                "id": 22484, 
	                "plan": {
	                    "runType": "WGNM", 
	                    "id": 104216, 
	                    "resource_uri": ""
	                }
	            }, 
	            "resultsName": "C1--479-fc-BC-reanal", 
	            "projects": [
	                {
	                    "resource_uri": "", 
	                    "id": 169, 
	                    "name": "loading", 
	                    "modified": "2014-05-01T17:53:34.000096+00:00"
	                }
	            ], 
	            "qualitymetrics": {
	                "q0_mean_read_length": 126.203182797703, 
	                "q0_reads": 84917681, 
	                "q0_bases": "10716881618", 
	                "q20_reads": 84917681, 
	                "q20_bases": "6381479613", 
	                "q20_mean_read_length": 126, 
	                "id": 34118, 
	                "resource_uri": ""
	            }, 
	            "eas": {
	                "resource_uri": "", 
	                "reference": "hg19", 
	                "barcodeKitName": "IonXpress"
	            }, 
	            "resource_uri": "/rundb/api/v1/monitorresult/56256/", 
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

