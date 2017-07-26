Pluginresult Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/schema/``


.. include:: ../manual_api_ref_docs/pluginresult.rst

Fields table
------------

====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                  help text                                                                                          default nullable readonly blank unique type     
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**major**              Boolean data. Ex: True                                                                             n/a     false    true     false false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**can_terminate**      Boolean data. Ex: True                                                                             n/a     false    true     false false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginVersion**      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**result**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**owner**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                 Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**size**               Unicode string data. Ex: "Hello World"                                                             -1      false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**state**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**store**              Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**files**              A list of data. Ex: ['abc', 26.73, 8]                                                              n/a     false    true     false false  list     
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**URL**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plugin_result_jobs** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**               Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endtime**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    true     false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**apikey**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plugin**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**starttime**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    true     false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**inodes**             Unicode string data. Ex: "Hello World"                                                             -1      false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/pluginresult/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	pluginresults = ts_api_response["objects"]
	
	for pluginresult in pluginresults:
	    print pluginresult
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 16, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "major": false, 
	            "can_terminate": false, 
	            "resultName": "Reanalyze", 
	            "pluginVersion": "5.4.0.1", 
	            "result": "/rundb/api/v1/results/6/", 
	            "owner": "/rundb/api/v1/user/1/", 
	            "id": 17, 
	            "size": "36446", 
	            "state": "Completed", 
	            "store": {
	                "barcoded": true, 
	                "barcodes": {}
	            }, 
	            "files": [], 
	            "URL": "/output/Home/Reanalyze_006/plugin_out/PGxAnalysis_out.17/", 
	            "plugin_result_jobs": [
	                {
	                    "grid_engine_jobid": -1, 
	                    "id": 17, 
	                    "state": "Completed", 
	                    "starttime": "2017-04-04T05:06:01.000922+00:00", 
	                    "endtime": "2017-04-04T05:06:06.000544+00:00", 
	                    "config": {}, 
	                    "run_level": "last", 
	                    "resource_uri": "/rundb/api/v1/PluginResultJob/17/"
	                }
	            ], 
	            "path": "/results/analysis/output/Home/Reanalyze_006/plugin_out/PGxAnalysis_out.17", 
	            "endtime": "2017-04-04T05:06:06.000544+00:00", 
	            "apikey": null, 
	            "plugin": "/rundb/api/v1/plugin/19/", 
	            "reportLink": "/output/Home/Reanalyze_006/", 
	            "pluginName": "PGxAnalysis", 
	            "starttime": "2017-04-04T05:06:01.000922+00:00", 
	            "inodes": "6", 
	            "resource_uri": "/rundb/api/v1/pluginresult/17/"
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

