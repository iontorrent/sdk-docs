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
**analysisVersion** Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysismetrics** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bamLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**       Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**filesystempath**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**framesProcessed** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**i18nstatus**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**        Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentIDs**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginState**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginStore**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginresults**   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedCycles** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reference**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportstorage**   A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsType**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runid**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfmetrics**       Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeToComplete**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/results/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 7
	    },
	    "objects": [
	        {
	            "analysisVersion": "_",
	            "analysismetrics": [],
	            "autoExempt": false,
	            "bamLink": "/output/Home/CA_Combined_demo_001_007/download_links/NONE_ReportOnly_NONE_CA_Combined_demo_001.bam",
	            "diskusage": 0,
	            "eas": "/rundb/api/v1/experimentanalysissettings/123/",
	            "experiment": "/rundb/api/v1/experiment/124/",
	            "filesystempath": "/results/analysis/output/Home/CA_Combined_demo_001_007",
	            "framesProcessed": 0,
	            "i18nstatus": {
	                "i18n": "Pending",
	                "state": "Other"
	            },
	            "id": 7,
	            "libmetrics": [],
	            "log": "/output/Home/CA_Combined_demo_001_007/log.html",
	            "metaData": {},
	            "parentIDs": ":4:2:",
	            "planShortID": "",
	            "pluginresults": [],
	            "processedCycles": 0,
	            "processedflows": 0,
	            "projects": [
	                "/rundb/api/v1/project/1/"
	            ],
	            "qualitymetrics": [],
	            "reference": "hg19",
	            "reportLink": "/output/Home/CA_Combined_demo_001_007/",
	            "reportStatus": "Nothing",
	            "reportstorage": {
	                "default": true,
	                "dirPath": "/results/analysis/output",
	                "id": 1,
	                "name": "Home",
	                "resource_uri": "",
	                "webServerPath": "/output"
	            },
	            "representative": false,
	            "resource_uri": "/rundb/api/v1/results/7/",
	            "resultsName": "CA_Combined_demo_001",
	            "resultsType": "CombinedAlignments",
	            "runid": "GOAMS",
	            "status": "Pending",
	            "tfmetrics": [],
	            "timeStamp": "2018-02-28T17:32:01.000577+00:00",
	            "timeToComplete": "0"
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

