.. _api_reference_ionchefplantemplatesummary:

Ion Chef Plan Template Summary  Resource
========================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/ionchefplantemplatesummary/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/ionchefplantemplatesummary/schema/``
| 

.. include:: ../references_manual_extras/ionchefplantemplatesummary.rst

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
**templatingKitBarcode**        Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
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
**templatingSize**              Unicode string data. Ex: "Hello World"                       true     false    false false  string   
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
	        "total_count": 46, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/ionchefplantemplatesummary/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "origin": "|5.4.0.RC3", 
	            "isReverseRun": false, 
	            "planDisplayedName": "Oncomine TagSeq Liquid Biopsy", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "planShortID": "9HMOG", 
	            "planStatus": "inactive", 
	            "runMode": "single", 
	            "templatingKitBarcode": null, 
	            "sampleTubeLabel": null, 
	            "planExecutedDate": null, 
	            "samplePrepKitName": null, 
	            "reverse_primer": null, 
	            "seqKitBarcode": null, 
	            "id": 102, 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "samplePrepProtocol": "", 
	            "isPlanGroup": false, 
	            "templatingKitName": "Ion Chef S530 V1", 
	            "runType": "TAG_SEQUENCING", 
	            "planPGM": "", 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": null, 
	            "date": "2017-04-10T04:56:32.000003+00:00", 
	            "isSystem": true, 
	            "libkit": null, 
	            "categories": "", 
	            "planName": "Oncomine_TagSeq_Liquid_Biopsy", 
	            "templatingSize": "", 
	            "pairedEndLibraryAdapterName": null, 
	            "adapter": null, 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "username": null, 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "", 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "f71a0fd1-88a1-4943-88f4-cbf997afe25d", 
	            "cycles": null, 
	            "resource_uri": "/rundb/api/v1/ionchefplantemplatesummary/102/"
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

