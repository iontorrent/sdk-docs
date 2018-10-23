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
**validation_errors**  Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
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
	        "total_count": 17, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "major": true, 
	            "can_terminate": false, 
	            "resultName": "Auto_user_CB1-42-r9723-314wfa-tl_94", 
	            "pluginVersion": "5.8.0.0", 
	            "result": "/rundb/api/v1/results/6/", 
	            "owner": "/rundb/api/v1/user/2/", 
	            "id": 24, 
	            "size": "344884433", 
	            "validation_errors": {
	                "validation_errors": []
	            }, 
	            "state": "Error", 
	            "store": {
	                "reference": "/results/referenceLibrary/tmap-f3/hg19/hg19.fasta", 
	                "barcoded": false, 
	                "Error": "Failed running run_rnaseqanalysis.py.", 
	                "genome": "hg19", 
	                "launch_mode": "Manual", 
	                "fpkm_thres": "0.3", 
	                "cutadapt": "None", 
	                "fraction_of_reads": "1"
	            }, 
	            "files": [
	                "RNASeqAnalysis.html"
	            ], 
	            "URL": "/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/plugin_out/RNASeqAnalysis_out.24/", 
	            "plugin_result_jobs": [
	                {
	                    "grid_engine_jobid": 517, 
	                    "id": 24, 
	                    "state": "Error", 
	                    "starttime": "2018-04-25T22:22:52.000576+00:00", 
	                    "endtime": "2018-04-25T22:28:47.000816+00:00", 
	                    "config": {
	                        "cutadapt": "None", 
	                        "fraction_of_reads": "1", 
	                        "reference": "/results/referenceLibrary/tmap-f3/hg19/hg19.fasta", 
	                        "genome": "hg19", 
	                        "launch_mode": "Manual"
	                    }, 
	                    "run_level": "default", 
	                    "resource_uri": "/rundb/api/v1/PluginResultJob/24/"
	                }
	            ], 
	            "path": "/results/analysis/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/plugin_out/RNASeqAnalysis_out.24", 
	            "endtime": "2018-04-25T22:28:47.000816+00:00", 
	            "apikey": "5a4f5fb12ef3d6c5490b3a41501097a506cd8d85", 
	            "plugin": "/rundb/api/v1/plugin/29/", 
	            "reportLink": "/output/Home/Auto_user_CB1-42-r9723-314wfa-tl_94_006/", 
	            "pluginName": "RNASeqAnalysis", 
	            "starttime": "2018-04-25T22:22:52.000576+00:00", 
	            "inodes": "33", 
	            "resource_uri": "/rundb/api/v1/pluginresult/24/"
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

