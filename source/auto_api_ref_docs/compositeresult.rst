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
	        "total_count": 43354, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Completed", 
	            "processedflows": 0, 
	            "analysis_metrics": {
	                "ignored": 3003404, 
	                "lib": 134282829, 
	                "total_wells": 164699136, 
	                "pinned": 472926, 
	                "live": 135574135, 
	                "excluded": 16095180, 
	                "bead": 135800957, 
	                "resource_uri": "", 
	                "id": 31763, 
	                "empty": 9326669, 
	                "libFinal": 91521301
	            }, 
	            "timeStamp": "2014-01-23T07:39:52.000803+00:00", 
	            "analysismetrics": {
	                "ignored": 3003404, 
	                "lib": 134282829, 
	                "total_wells": 164699136, 
	                "pinned": 472926, 
	                "live": 135574135, 
	                "excluded": 16095180, 
	                "bead": 135800957, 
	                "resource_uri": "", 
	                "id": 31763, 
	                "empty": 9326669, 
	                "libFinal": 91521301
	            }, 
	            "reportLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/", 
	            "id": 293943, 
	            "reportStatus": "Nothing", 
	            "quality_metrics": {
	                "q0_mean_read_length": 168.0, 
	                "q0_reads": 91521301, 
	                "q0_bases": "15380233572", 
	                "q20_reads": 91521301, 
	                "q20_bases": "12209924742", 
	                "q20_mean_read_length": 103, 
	                "id": 31678, 
	                "resource_uri": ""
	            }, 
	            "resultsName": "Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	            "projects": [
	                {
	                    "resource_uri": "", 
	                    "id": 1080, 
	                    "name": "chef_827_909_20min_ext", 
	                    "modified": "2014-01-22T18:50:10.000920+00:00"
	                }
	            ], 
	            "qualitymetrics": {
	                "q0_mean_read_length": 168.0, 
	                "q0_reads": 91521301, 
	                "q0_bases": "15380233572", 
	                "q20_reads": 91521301, 
	                "q20_bases": "12209924742", 
	                "q20_mean_read_length": 103, 
	                "id": 31678, 
	                "resource_uri": ""
	            }, 
	            "eas": {
	                "resource_uri": "", 
	                "reference": "hg19", 
	                "barcodeKitName": "IonXpress"
	            }, 
	            "resource_uri": "/rundb/api/v1/compositeresult/293943/", 
	            "libmetrics": {
	                "i100Q20_reads": 56284561, 
	                "aveKeyCounts": 71.0, 
	                "id": 32368, 
	                "resource_uri": "", 
	                "q20_mean_alignment_length": 142
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

