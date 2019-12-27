.. _api_reference_plannedexperimentdb:

Planned Experiment Db  Resource
===============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plannedexperimentdb/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plannedexperimentdb/schema/``
| 

.. include:: ../references_manual_extras/plannedexperimentdb.rst

Resource Fields
---------------

=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                                                                          default nullable readonly blank unique type     
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**adapter**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                  Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                  A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                          Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**           Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                    Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                      Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                  Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**          Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                  Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**               Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**             Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
=============================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plannedexperimentdb/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 135
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "applicationGroup": "/rundb/api/v1/applicationgroup/5/",
	            "autoName": null,
	            "categories": "Oncomine;onco_solidTumor;barcodes_8;p4o",
	            "childPlans": [],
	            "controlSequencekitname": null,
	            "cycles": null,
	            "date": "2019-10-03T20:53:08.000623+00:00",
	            "expName": "",
	            "experiment": "/rundb/api/v1/experiment/163/",
	            "id": 170,
	            "irworkflow": "",
	            "isCustom_kitSettings": false,
	            "isFavorite": false,
	            "isPlanGroup": false,
	            "isReusable": true,
	            "isReverseRun": false,
	            "isSystem": true,
	            "isSystemDefault": false,
	            "libkit": null,
	            "libraryReadLength": 200,
	            "metaData": {},
	            "origin": "|5.12.1",
	            "pairedEndLibraryAdapterName": null,
	            "parentPlan": null,
	            "planDisplayedName": "Oncomine Tumor Specific Fusions",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "planName": "Oncomine_Tumor_Specific_Fusions",
	            "planPGM": "",
	            "planShortID": "OZT4F",
	            "planStatus": "inactive",
	            "preAnalysis": true,
	            "project": "",
	            "projects": [],
	            "qcValues": [
	                {
	                    "id": 487,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 1,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Bead Loading (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/1/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/487/",
	                    "threshold": 30
	                },
	                {
	                    "id": 488,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 2,
	                        "maxThreshold": 100,
	                        "minThreshold": 1,
	                        "qcName": "Key Signal (1-100)",
	                        "resource_uri": "/rundb/api/v1/qctype/2/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/488/",
	                    "threshold": 30
	                },
	                {
	                    "id": 489,
	                    "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	                    "qcType": {
	                        "defaultThreshold": 30,
	                        "description": "",
	                        "id": 3,
	                        "maxThreshold": 100,
	                        "minThreshold": 0,
	                        "qcName": "Usable Sequence (%)",
	                        "resource_uri": "/rundb/api/v1/qctype/3/"
	                    },
	                    "resource_uri": "/rundb/api/v1/plannedexperimentqc/489/",
	                    "threshold": 30
	                }
	            ],
	            "resource_uri": "/rundb/api/v1/plannedexperimentdb/170/",
	            "reverse_primer": null,
	            "runMode": "single",
	            "runType": "AMPS_RNA",
	            "runname": null,
	            "sampleGrouping": "/rundb/api/v1/samplegrouptype_cv/7/",
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
	            "sampleSets": [],
	            "sampleTubeLabel": null,
	            "seqKitBarcode": null,
	            "storageHost": null,
	            "storage_options": "A",
	            "templatingKitBarcode": null,
	            "templatingKitName": "Ion Chef S530 V2",
	            "usePostBeadfind": false,
	            "usePreBeadfind": true,
	            "username": null
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

