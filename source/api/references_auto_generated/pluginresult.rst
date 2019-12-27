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
**URL**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**apikey**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**can_terminate**      Boolean data. Ex: True                                                                             n/a     false    true     false false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endtime**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    true     false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**files**              A list of data. Ex: ['abc', 26.73, 8]                                                              n/a     false    true     false false  list     
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                 Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**inodes**             Unicode string data. Ex: "Hello World"                                                             -1      false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**major**              Boolean data. Ex: True                                                                             n/a     false    true     false false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**owner**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**               Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plugin**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginVersion**      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plugin_result_jobs** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**result**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**size**               Unicode string data. Ex: "Hello World"                                                             -1      false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**starttime**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    true     false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**state**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**store**              Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**validation_errors**  Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 18
	    },
	    "objects": [
	        {
	            "URL": "/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/plugin_out/PathogenomixRipseqNGS_out.25/",
	            "apikey": "7b20b457ab2701e26f93a9ca774338b5e33d779a",
	            "can_terminate": false,
	            "endtime": "2019-01-17T23:50:39.000550+00:00",
	            "files": [
	                "status_block.html"
	            ],
	            "id": 25,
	            "inodes": "7",
	            "major": false,
	            "owner": "/rundb/api/v1/user/1/",
	            "path": "/results/analysis/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/plugin_out/PathogenomixRipseqNGS_out.25",
	            "plugin": "/rundb/api/v1/plugin/64/",
	            "pluginName": "PathogenomixRipseqNGS",
	            "pluginVersion": "5.10.0.5",
	            "plugin_result_jobs": [
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
	            ],
	            "reportLink": "/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/",
	            "resource_uri": "/rundb/api/v1/pluginresult/25/",
	            "result": "/rundb/api/v1/results/6/",
	            "resultName": "Auto_user_CB1-42-r9723-314wfa-tl_94",
	            "size": "25475",
	            "starttime": "2019-01-17T23:50:33.000769+00:00",
	            "state": "Completed",
	            "store": {},
	            "validation_errors": {
	                "validation_errors": []
	            }
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

