.. _api_reference_results:

Results  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/results/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/results/schema/``
| 

.. include:: ../references_manual_extras/results.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	            "analysisVersion": "db:5.4.15-1,an:5.4.3-1,", 
	            "runid": "Z6MPC", 
	            "id": 6, 
	            "filesystempath": "/results/analysis/output/Home/Reanalyze_006", 
	            "metaData": {}, 
	            "log": "/output/Home/Reanalyze_006/log.html", 
	            "timeStamp": "2017-04-04T04:29:06.000356+00:00", 
	            "libmetrics": [
	                "/rundb/api/v1/libmetrics/4/"
	            ], 
	            "experiment": "/rundb/api/v1/experiment/89/", 
	            "resultsName": "Reanalyze", 
	            "status": "Completed", 
	            "planShortID": "1BFQJ", 
	            "processedCycles": 0, 
	            "bamLink": "/output/Home/Reanalyze_006/download_links/S5-530_cfDNA_Reanalyze.bam", 
	            "representative": false, 
	            "qualitymetrics": [
	                "/rundb/api/v1/qualitymetrics/4/"
	            ], 
	            "diskusage": 73494, 
	            "eas": "/rundb/api/v1/experimentanalysissettings/92/", 
	            "projects": [
	                "/rundb/api/v1/project/1/"
	            ], 
	            "resultsType": "", 
	            "tfmetrics": [
	                "/rundb/api/v1/tfmetrics/8/", 
	                "/rundb/api/v1/tfmetrics/7/"
	            ], 
	            "parentIDs": "", 
	            "analysismetrics": [
	                "/rundb/api/v1/analysismetrics/6/"
	            ], 
	            "timeToComplete": "0", 
	            "reportLink": "/output/Home/Reanalyze_006/", 
	            "pluginresults": [
	                "/rundb/api/v1/pluginresult/30/", 
	                "/rundb/api/v1/pluginresult/17/", 
	                "/rundb/api/v1/pluginresult/16/", 
	                "/rundb/api/v1/pluginresult/15/", 
	                "/rundb/api/v1/pluginresult/14/", 
	                "/rundb/api/v1/pluginresult/13/", 
	                "/rundb/api/v1/pluginresult/12/", 
	                "/rundb/api/v1/pluginresult/11/", 
	                "/rundb/api/v1/pluginresult/10/", 
	                "/rundb/api/v1/pluginresult/9/", 
	                "/rundb/api/v1/pluginresult/8/"
	            ], 
	            "framesProcessed": 0, 
	            "autoExempt": false, 
	            "resource_uri": "/rundb/api/v1/results/6/"
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

