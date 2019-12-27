.. _api_reference_compositeresult:

Composite Result  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/compositeresult/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/compositeresult/schema/``
| 

.. include:: ../references_manual_extras/compositeresult.rst

Resource Fields
---------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**analysismetrics** A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**i18nstatus**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/compositeresult/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 7
	    },
	    "objects": [
	        {
	            "analysis_metrics": null,
	            "analysismetrics": null,
	            "autoExempt": false,
	            "eas": {
	                "barcodeKitName": "IonXpress",
	                "chipType": "",
	                "isPQ": false,
	                "reference": "hg19",
	                "references": "hg19",
	                "resource_uri": ""
	            },
	            "i18nstatus": {
	                "i18n": "Pending",
	                "state": "Other"
	            },
	            "id": 7,
	            "isShowAllMetrics": true,
	            "libmetrics": null,
	            "processedflows": 0,
	            "projects": [
	                {
	                    "id": 1,
	                    "modified": "2018-02-28T17:32:01.000703+00:00",
	                    "name": "demo",
	                    "resource_uri": ""
	                }
	            ],
	            "quality_metrics": null,
	            "qualitymetrics": null,
	            "reportLink": "/output/Home/CA_Combined_demo_001_007/",
	            "reportStatus": "Nothing",
	            "representative": false,
	            "resource_uri": "/rundb/api/v1/compositeresult/7/",
	            "resultsName": "CA_Combined_demo_001",
	            "status": "Pending",
	            "timeStamp": "2018-02-28T17:32:01.000577+00:00"
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

