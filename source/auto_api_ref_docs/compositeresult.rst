Compositeresult Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/compositeresult/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/compositeresult/schema/``


.. include:: ../manual_api_ref_docs/compositeresult.rst

Fields table
------------

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

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/compositeresult/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/compositeresult/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	compositeresults = ts_api_response["objects"]
	
	for compositeresult in compositeresults:
	    print compositeresult
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 13696, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "analysis_metrics": {
	                "ignored": 0, 
	                "lib": 255561, 
	                "total_wells": 1474560, 
	                "pinned": 70346, 
	                "live": 283253, 
	                "excluded": 222544, 
	                "bead": 803436, 
	                "resource_uri": "", 
	                "id": 988, 
	                "empty": 378234, 
	                "libFinal": 230854
	            }, 
	            "timeStamp": "2010-07-30T21:05:37.000219+00:00", 
	            "analysismetrics": {
	                "ignored": 0, 
	                "lib": 255561, 
	                "total_wells": 1474560, 
	                "pinned": 70346, 
	                "live": 283253, 
	                "excluded": 222544, 
	                "bead": 803436, 
	                "resource_uri": "", 
	                "id": 988, 
	                "empty": 378234, 
	                "libFinal": 230854
	            }, 
	            "reportLink": "/output/IonEast/v5_1145/Detailed_Report.php", 
	            "id": 1145, 
	            "reportStatus": "Pruned", 
	            "quality_metrics": null, 
	            "resultsName": "v5", 
	            "projects": [], 
	            "qualitymetrics": null, 
	            "eas": {
	                "resource_uri": "", 
	                "reference": "e_coli_dh10b", 
	                "barcodeKitName": ""
	            }, 
	            "resource_uri": "/rundb/api/v1/compositeresult/1145/", 
	            "libmetrics": {
	                "i100Q20_reads": 96, 
	                "aveKeyCounts": 50.0, 
	                "id": 1019, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 37
	            }, 
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

