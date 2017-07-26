.. _api_reference_pluginresult:

Plugin Result  Resource
=======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/pluginresult/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/pluginresult/schema/``
| 

.. include:: ../references_manual_extras/pluginresult.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 28, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "major": false, 
	            "can_terminate": false, 
	            "resultName": "Auto_S5-540_WholeTranscriptomeRNA_91", 
	            "pluginVersion": "5.4.0.0", 
	            "result": "/rundb/api/v1/results/3/", 
	            "owner": "/rundb/api/v1/user/1/", 
	            "id": 32, 
	            "size": "32843", 
	            "state": "Completed", 
	            "store": {}, 
	            "files": [
	                "FilteredBam_block.html", 
	                "FilterDuplicates.html"
	            ], 
	            "URL": "/output/Home/Auto_S5-540_WholeTranscriptomeRNA_91_003/plugin_out/FilterDuplicates_out.32/", 
	            "plugin_result_jobs": [
	                {
	                    "grid_engine_jobid": -1, 
	                    "id": 32, 
	                    "state": "Completed", 
	                    "starttime": "2017-04-25T20:46:14.000002+00:00", 
	                    "endtime": "2017-04-25T20:46:16.000092+00:00", 
	                    "config": {}, 
	                    "run_level": "default", 
	                    "resource_uri": "/rundb/api/v1/PluginResultJob/32/"
	                }
	            ], 
	            "path": "/results/analysis/output/Home/Auto_S5-540_WholeTranscriptomeRNA_91_003/plugin_out/FilterDuplicates_out.32", 
	            "endtime": "2017-04-25T20:46:16.000092+00:00", 
	            "apikey": null, 
	            "plugin": "/rundb/api/v1/plugin/25/", 
	            "reportLink": "/output/Home/Auto_S5-540_WholeTranscriptomeRNA_91_003/", 
	            "pluginName": "FilterDuplicates", 
	            "starttime": "2017-04-25T20:46:14.000002+00:00", 
	            "inodes": "7", 
	            "resource_uri": "/rundb/api/v1/pluginresult/32/"
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

