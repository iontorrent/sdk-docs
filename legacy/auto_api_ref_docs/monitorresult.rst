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
	        "total_count": 1, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "libmetrics": {
	                "i100Q20_reads": 8091532, 
	                "aveKeyCounts": 115, 
	                "id": 4, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 99
	            }, 
	            "timeStamp": "2017-04-04T04:29:06.000356+00:00", 
	            "analysismetrics": {
	                "ignored": 279237, 
	                "lib": 34331404, 
	                "total_wells": 40796160, 
	                "pinned": 439629, 
	                "live": 34628090, 
	                "excluded": 3236330, 
	                "bead": 34629257, 
	                "resource_uri": "", 
	                "id": 6, 
	                "empty": 2211707, 
	                "libFinal": 18674586
	            }, 
	            "reportLink": "/output/Home/Reanalyze_006/", 
	            "library": "hg19", 
	            "id": 6, 
	            "reportStatus": "Nothing", 
	            "experiment": {
	                "ftpStatus": "0", 
	                "chipInstrumentType": "S5", 
	                "displayName": "S5-530 cfDNA", 
	                "chipType": "530", 
	                "runMode": "single", 
	                "notes": "", 
	                "chipDescription": "530", 
	                "resultDate": "2017-04-04T04:29:06.000356+00:00", 
	                "flows": 500, 
	                "platform": "S5", 
	                "expName": "S5-530_cfDNA", 
	                "storage_options": "KI", 
	                "pgmName": "S16", 
	                "date": "2017-01-31T16:17:22+00:00", 
	                "star": false, 
	                "resource_uri": "", 
	                "qcThresholds": {
	                    "Key Signal (1-100)": 30, 
	                    "Usable Sequence (%)": 30, 
	                    "Bead Loading (%)": 30
	                }, 
	                "id": 89, 
	                "plan": {
	                    "runType": "TAG_SEQUENCING", 
	                    "id": 97, 
	                    "resource_uri": ""
	                }
	            }, 
	            "resultsName": "Reanalyze", 
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
	                "id": 4, 
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
	            "resource_uri": "/rundb/api/v1/monitorresult/6/", 
	            "barcodeId": "IonCode - TagSequencing", 
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

