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
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "libmetrics": {
	                "i100Q20_reads": 8091532, 
	                "aveKeyCounts": 115, 
	                "id": 2, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 99
	            }, 
	            "representative": false, 
	            "analysis_metrics": {
	                "ignored": 279237, 
	                "lib": 34331404, 
	                "total_wells": 40796160, 
	                "pinned": 439629, 
	                "live": 34628090, 
	                "excluded": 3236330, 
	                "bead": 34629257, 
	                "resource_uri": "", 
	                "id": 4, 
	                "empty": 2211707, 
	                "libFinal": 18674586
	            }, 
	            "timeStamp": "2017-03-17T20:46:52.000292+00:00", 
	            "analysismetrics": {
	                "ignored": 279237, 
	                "lib": 34331404, 
	                "total_wells": 40796160, 
	                "pinned": 439629, 
	                "live": 34628090, 
	                "excluded": 3236330, 
	                "bead": 34629257, 
	                "resource_uri": "", 
	                "id": 4, 
	                "empty": 2211707, 
	                "libFinal": 18674586
	            }, 
	            "reportLink": "/output/Home/S5-530_cfDNA_004/", 
	            "reportStatus": "Nothing", 
	            "quality_metrics": {
	                "q0_mean_read_length": 102.061659841641, 
	                "q0_reads": 18673191, 
	                "q0_bases": "1905816868", 
	                "q20_reads": 18673191, 
	                "q20_bases": "1807605660", 
	                "q20_mean_read_length": 102, 
	                "id": 2, 
	                "resource_uri": ""
	            }, 
	            "resultsName": "S5-530_cfDNA", 
	            "projects": [
	                {
	                    "resource_uri": "", 
	                    "id": 1, 
	                    "name": "demo", 
	                    "modified": "2017-04-04T01:58:32.000439+00:00"
	                }
	            ], 
	            "qualitymetrics": {
	                "q0_mean_read_length": 102.061659841641, 
	                "q0_reads": 18673191, 
	                "q0_bases": "1905816868", 
	                "q20_reads": 18673191, 
	                "q20_bases": "1807605660", 
	                "q20_mean_read_length": 102, 
	                "id": 2, 
	                "resource_uri": ""
	            }, 
	            "eas": {
	                "chipType": "530", 
	                "reference": "hg19", 
	                "isPQ": false, 
	                "references": "hg19", 
	                "barcodeKitName": "IonCode - TagSequencing", 
	                "resource_uri": ""
	            }, 
	            "resource_uri": "/rundb/api/v1/compositeresult/4/", 
	            "id": 4, 
	            "autoExempt": false, 
	            "isShowAllMetrics": true
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

