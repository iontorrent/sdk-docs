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
	        "total_count": 37659, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "analysis_metrics": {
	                "ignored": 4938030, 
	                "lib": 104318813, 
	                "total_wells": 164699136, 
	                "pinned": 416177, 
	                "live": 104333175, 
	                "excluded": 16095180, 
	                "bead": 111451410, 
	                "resource_uri": "", 
	                "id": 30862, 
	                "empty": 31798339, 
	                "libFinal": 59559295
	            }, 
	            "timeStamp": "2014-01-30T07:52:22.000647+00:00", 
	            "analysismetrics": {
	                "ignored": 4938030, 
	                "lib": 104318813, 
	                "total_wells": 164699136, 
	                "pinned": 416177, 
	                "live": 104333175, 
	                "excluded": 16095180, 
	                "bead": 111451410, 
	                "resource_uri": "", 
	                "id": 30862, 
	                "empty": 31798339, 
	                "libFinal": 59559295
	            }, 
	            "reportLink": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/", 
	            "id": 52046, 
	            "reportStatus": "Nothing", 
	            "quality_metrics": {
	                "q0_mean_read_length": 142.0, 
	                "q0_reads": 59559295, 
	                "q0_bases": "8485928995", 
	                "q20_reads": 59559295, 
	                "q20_bases": "6280960963", 
	                "q20_mean_read_length": 69, 
	                "id": 30474, 
	                "resource_uri": ""
	            }, 
	            "resultsName": "Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	            "projects": [
	                {
	                    "resource_uri": "", 
	                    "id": 169, 
	                    "name": "loading", 
	                    "modified": "2014-05-01T17:53:34.000096+00:00"
	                }
	            ], 
	            "qualitymetrics": {
	                "q0_mean_read_length": 142.0, 
	                "q0_reads": 59559295, 
	                "q0_bases": "8485928995", 
	                "q20_reads": 59559295, 
	                "q20_bases": "6280960963", 
	                "q20_mean_read_length": 69, 
	                "id": 30474, 
	                "resource_uri": ""
	            }, 
	            "eas": {
	                "resource_uri": "", 
	                "reference": "hg19", 
	                "barcodeKitName": "IonXpress"
	            }, 
	            "resource_uri": "/rundb/api/v1/compositeresult/52046/", 
	            "libmetrics": {
	                "i100Q20_reads": 26629976, 
	                "aveKeyCounts": 59.0, 
	                "id": 31090, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 109
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

