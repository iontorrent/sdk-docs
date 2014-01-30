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
**sffLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
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
**tfSffLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginStore**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsType**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfFastq**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
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
**fastqLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
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
	        "total_count": 13696, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/results/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "reference": "e_coli_dh10b", 
	            "processedflows": 0, 
	            "reportStatus": "Pruned", 
	            "reportstorage": {
	                "name": "old_runs", 
	                "default": false, 
	                "webServerPath": "/output", 
	                "dirPath": "/results/analysis/output", 
	                "id": 2, 
	                "resource_uri": ""
	            }, 
	            "analysisVersion": "bf:0.6.4d.1-1,db:1.58-0,al:1.10-1,an:1.3-0,", 
	            "runid": "", 
	            "id": 1145, 
	            "filesystempath": "/results/analysis/output/IonEast/v5_1145", 
	            "metaData": {
	                "Comment": "0 files deleted", 
	                "Date": "2012-10-10 06:22:53.713707", 
	                "Info": "Pruning completed.  No valid files to remove", 
	                "Log": [
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-09-26 11:29:35.780010", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-09-26 11:29:36.025898", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-03 06:54:24.752362", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-03 06:54:24.968882", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-04 06:47:41.909293", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-04 06:47:42.118817", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-05 06:21:38.085571", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-05 06:21:38.373808", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-06 09:56:51.825991", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-06 09:56:52.097357", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-07 10:04:01.791019", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-07 10:04:02.064161", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-08 07:58:50.538874", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-08 07:58:50.802054", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-09 08:15:38.632490", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-09 08:15:38.948509", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }, 
	                    {
	                        "Comment": "v5 Pruned via auto-action", 
	                        "Date": "2012-10-10 06:22:53.372094", 
	                        "Info": "Pruning using prune group No-op: []", 
	                        "Status": "Pruning"
	                    }, 
	                    {
	                        "Comment": "0 files deleted", 
	                        "Date": "2012-10-10 06:22:53.713707", 
	                        "Info": "Pruning completed.  No valid files to remove", 
	                        "Status": "Pruned"
	                    }
	                ], 
	                "Status": "Pruned"
	            }, 
	            "log": "/output/IonEast/v5_1145/log.html", 
	            "timeStamp": "2010-07-30T21:05:37.000219+00:00", 
	            "libmetrics": [
	                "/rundb/api/v1/libmetrics/1019/"
	            ], 
	            "experiment": "/rundb/api/v1/experiment/816/", 
	            "resultsName": "v5", 
	            "status": "Completed", 
	            "planShortID": "", 
	            "processedCycles": 55, 
	            "bamLink": "/output/IonEast/v5_1145/R_2010_07_30_13_49_32_user_WOL-64-lib36-ion-bst-notopo-BR_v5.bam", 
	            "sffLink": null, 
	            "representative": false, 
	            "pluginState": {}, 
	            "qualitymetrics": [], 
	            "diskusage": 1304, 
	            "eas": "/rundb/api/v1/experimentanalysissettings/10093/", 
	            "tfSffLink": null, 
	            "projects": [], 
	            "pluginStore": {}, 
	            "resultsType": "", 
	            "tfFastq": "_", 
	            "tfmetrics": [], 
	            "parentIDs": "", 
	            "analysismetrics": [
	                "/rundb/api/v1/analysismetrics/988/"
	            ], 
	            "timeToComplete": "0", 
	            "reportLink": "/output/IonEast/v5_1145/Detailed_Report.php", 
	            "fastqLink": "/output/IonEast/v5_1145/keypass_R_2010_07_30_13_49_32_user_WOL-64-lib36-ion-bst-notopo-BR_v5.fastq", 
	            "pluginresults": [], 
	            "framesProcessed": 162, 
	            "autoExempt": false, 
	            "resource_uri": "/rundb/api/v1/results/1145/"
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

