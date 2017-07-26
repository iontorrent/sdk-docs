Pluginresultjob Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/PluginResultJob/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/PluginResultJob/schema/``


.. include:: ../manual_api_ref_docs/PluginResultJob.rst

Fields table
------------

===================== ==================================================== ======= ======== ======== ===== ====== ======== 
field                 help text                                            default nullable readonly blank unique type     
===================== ==================================================== ======= ======== ======== ===== ====== ======== 
**grid_engine_jobid** Integer data. Ex: 2673                               n/a     true     false    false false  integer  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                Integer data. Ex: 2673                                       false    false    true  true   integer  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**state**             Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**starttime**         A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endtime**           A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**config**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**run_level**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**      Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
===================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/PluginResultJob/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/PluginResultJob/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	PluginResultJobs = ts_api_response["objects"]
	
	for PluginResultJob in PluginResultJobs:
	    print PluginResultJob
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 16, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/PluginResultJob/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "grid_engine_jobid": -1, 
	            "id": 8, 
	            "state": "Completed", 
	            "starttime": "2017-04-04T04:34:13.000969+00:00", 
	            "endtime": "2017-04-04T04:43:43.000541+00:00", 
	            "config": {}, 
	            "run_level": "default", 
	            "resource_uri": "/rundb/api/v1/PluginResultJob/8/"
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

