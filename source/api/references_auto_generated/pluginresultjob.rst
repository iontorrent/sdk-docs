.. _api_reference_pluginresultjob:

Plugin Result Job  Resource
===========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/PluginResultJob/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/PluginResultJob/schema/``
| 

.. include:: ../references_manual_extras/pluginresultjob.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 15, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/PluginResultJob/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "grid_engine_jobid": -1, 
	            "id": 19, 
	            "state": "Completed", 
	            "starttime": "2017-08-09T20:26:03.000549+00:00", 
	            "endtime": "2017-08-09T20:30:11.000942+00:00", 
	            "config": {
	                "compressedType": "zip", 
	                "bamCreate": "on", 
	                "xlsCreate": "off", 
	                "zipFASTQ": "off", 
	                "vcfCreate": "on", 
	                "zipXLS": "off", 
	                "delimiter_select": ".", 
	                "zipVCF": "on", 
	                "zipBAM": "on", 
	                "fastqCreate": "off", 
	                "select_dialog": [
	                    "run_name", 
	                    "samplename", 
	                    "instrument", 
	                    "", 
	                    "", 
	                    "", 
	                    ""
	                ]
	            }, 
	            "run_level": "last", 
	            "resource_uri": "/rundb/api/v1/PluginResultJob/19/"
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

