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
**config**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endtime**           A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**grid_engine_jobid** Integer data. Ex: 2673                               n/a     true     false    false false  integer  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                Integer data. Ex: 2673                                       false    false    true  true   integer  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**      Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**run_level**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**starttime**         A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**state**             Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
===================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/PluginResultJob/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 18
	    },
	    "objects": [
	        {
	            "config": {
	                "copyNumberThreshold": "20",
	                "email": "osaebo",
	                "generateAllPrimerCombinations": true,
	                "generateReversedPrimerSets": false,
	                "isNC": false,
	                "maxClusterVariation": "1.0",
	                "ncCT": "33",
	                "password": "xl3eple",
	                "primerCheckLength": "12",
	                "primerCheckMaxErrors": "3",
	                "primers": ">V1_2_A_F\nGTGCCTAAYACATGCAWGT\n>V1_2_A_R\nCTGGDCCGTRTCTCAGT",
	                "readLengthThreshold": "100",
	                "safetyMarginCT": "3",
	                "sampleCT": "16",
	                "trimEndsWithNoPrimer": "21",
	                "useCT": false,
	                "useFullPrimerCoverageReadsOnly": false,
	                "useReadsWithNoPrimer": false,
	                "useWalkingInsDel": false
	            },
	            "endtime": "2019-01-17T23:50:39.000550+00:00",
	            "grid_engine_jobid": 518,
	            "id": 25,
	            "resource_uri": "/rundb/api/v1/PluginResultJob/25/",
	            "run_level": "last",
	            "starttime": "2019-01-17T23:50:33.000769+00:00",
	            "state": "Completed"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

