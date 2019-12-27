.. _api_reference_plantemplatesummary:

Plan Template Summary  Resource
===============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plantemplatesummary/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plantemplatesummary/schema/``
| 

.. include:: ../references_manual_extras/plantemplatesummary.rst

Resource Fields
---------------

=============================== ==================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                            default nullable readonly blank unique type     
=============================== ==================================================== ======= ======== ======== ===== ====== ======== 
**adapter**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                  Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                               n/a     true     false    false false  integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                          Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**        Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                  Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**           Integer data. Ex: 2673                               0       false    false    false false  integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                    Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                      Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**              Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"               GENS    false    false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**          Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**               Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"               A       false    false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**             Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
=============================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plantemplatesummary/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 126
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "autoName": null,
	            "categories": "Oncomine;onco_solidTumor;barcodes_8;p4o",
	            "controlSequencekitname": null,
	            "cycles": null,
	            "date": "2019-10-03T20:53:08.000623+00:00",
	            "expName": "",
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
	            "planDisplayedName": "Oncomine Tumor Specific Fusions",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "aa9309c5-5922-49f3-b901-987383b03e57",
	            "planName": "Oncomine_Tumor_Specific_Fusions",
	            "planPGM": "",
	            "planShortID": "OZT4F",
	            "planStatus": "inactive",
	            "preAnalysis": true,
	            "resource_uri": "/rundb/api/v1/plantemplatesummary/170/",
	            "reverse_primer": null,
	            "runMode": "single",
	            "runType": "AMPS_RNA",
	            "runname": null,
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
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

