Results Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/results/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/results/schema/``


.. include:: ../manual_api_ref_docs/results.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**reference**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportstorage**   A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysisVersion** Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runid**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**filesystempath**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**        Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedCycles** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bamLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginState**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**       Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginStore**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsType**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfmetrics**       Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentIDs**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysismetrics** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeToComplete**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginresults**   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**framesProcessed** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/results/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/results/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	resultss = ts_api_response["objects"]
	
	for results in resultss:
	    print results
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/results/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "reference": "hg19", 
	            "processedflows": 0, 
	            "reportStatus": "Nothing", 
	            "reportstorage": {
	                "name": "Home", 
	                "default": true, 
	                "webServerPath": "/output", 
	                "dirPath": "/results/analysis/output", 
	                "id": 1, 
	                "resource_uri": ""
	            }, 
	            "analysisVersion": "db:5.4.7-1,an:5.4.2-1,", 
	            "runid": "J500K", 
	            "id": 5, 
	            "filesystempath": "/results/analysis/output/Home/S5-540_AmpliSeqExome_005", 
	            "metaData": {}, 
	            "log": "/output/Home/S5-540_AmpliSeqExome_005/log.html", 
	            "timeStamp": "2017-03-18T06:39:37.000203+00:00", 
	            "libmetrics": [
	                "/rundb/api/v1/libmetrics/3/"
	            ], 
	            "experiment": "/rundb/api/v1/experiment/90/", 
	            "resultsName": "S5-540_AmpliSeqExome", 
	            "status": "Completed", 
	            "planShortID": "GXEYK", 
	            "processedCycles": 0, 
	            "bamLink": "/output/Home/S5-540_AmpliSeqExome_005/download_links/S5-540_AmpliSeqExome_S5-540_AmpliSeqExome.bam", 
	            "representative": false, 
	            "qualitymetrics": [
	                "/rundb/api/v1/qualitymetrics/3/"
	            ], 
	            "diskusage": 371907, 
	            "eas": "/rundb/api/v1/experimentanalysissettings/89/", 
	            "projects": [
	                "/rundb/api/v1/project/1/"
	            ], 
	            "resultsType": "", 
	            "tfmetrics": [
	                "/rundb/api/v1/tfmetrics/6/", 
	                "/rundb/api/v1/tfmetrics/5/"
	            ], 
	            "parentIDs": "", 
	            "analysismetrics": [
	                "/rundb/api/v1/analysismetrics/5/"
	            ], 
	            "timeToComplete": "0", 
	            "reportLink": "/output/Home/S5-540_AmpliSeqExome_005/", 
	            "pluginresults": [
	                "/rundb/api/v1/pluginresult/6/", 
	                "/rundb/api/v1/pluginresult/3/", 
	                "/rundb/api/v1/pluginresult/2/", 
	                "/rundb/api/v1/pluginresult/1/"
	            ], 
	            "framesProcessed": 0, 
	            "autoExempt": false, 
	            "resource_uri": "/rundb/api/v1/results/5/"
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

