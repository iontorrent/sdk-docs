.. _api_reference_onetouchplantemplatesummary:

Onetouch Plan Template Summary  Resource
========================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplatesummary/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplatesummary/schema/``
| 

.. include:: ../references_manual_extras/onetouchplantemplatesummary.rst

Resource Fields
---------------

=============================== ==================================================== ======= ======== ======== ===== ====== ======== 
field                           help text                                            default nullable readonly blank unique type     
=============================== ==================================================== ======= ======== ======== ===== ====== ======== 
**origin**                      Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**             Unicode string data. Ex: "Hello World"               A       false    false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                 Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                 Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**        Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**             Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**            A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**              Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**               Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                          Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                    Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                  Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**          Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                 Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**           Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                     Unicode string data. Ex: "Hello World"               GENS    false    false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**             Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                  Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**      Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                        A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                    Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                      Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                  Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName** Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**             Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                 Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**           Integer data. Ex: 2673                               0       false    false    false false  integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                     Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**              Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                    Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                      Integer data. Ex: 2673                               n/a     true     false    false false  integer  
------------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
=============================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 37, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/onetouchplantemplatesummary/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "origin": "ampliseq.com|5.8.0", 
	            "isReverseRun": false, 
	            "planDisplayedName": "PGx Research Panel", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "planShortID": "OO9C5", 
	            "planStatus": "planned", 
	            "runMode": "", 
	            "isCustom_kitSettings": false, 
	            "sampleTubeLabel": null, 
	            "planExecutedDate": null, 
	            "samplePrepKitName": null, 
	            "reverse_primer": null, 
	            "seqKitBarcode": null, 
	            "id": 130, 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "samplePrepProtocol": "", 
	            "isPlanGroup": false, 
	            "templatingKitName": "Ion PGM Hi-Q OT2 Kit - 200", 
	            "runType": "AMPS", 
	            "templatingKitBarcode": null, 
	            "planPGM": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": "", 
	            "date": "2018-02-08T19:41:44.000698+00:00", 
	            "isSystem": false, 
	            "libkit": null, 
	            "categories": "", 
	            "planName": "PGx_Research_Panel", 
	            "pairedEndLibraryAdapterName": "", 
	            "adapter": null, 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "username": "ionuser", 
	            "usePostBeadfind": true, 
	            "storageHost": null, 
	            "expName": "", 
	            "libraryReadLength": 0, 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "7489c32d-d3ed-4cc1-a7a2-e59b819ea395", 
	            "cycles": null, 
	            "resource_uri": "/rundb/api/v1/onetouchplantemplatesummary/130/"
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

