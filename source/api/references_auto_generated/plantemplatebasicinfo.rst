.. _api_reference_plantemplatebasicinfo:

Plan Template Basic Info  Resource
==================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/schema/``
| 

.. include:: ../references_manual_extras/plantemplatebasicinfo.rst

Resource Fields
---------------

==================================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                                help text                                                                      default nullable readonly blank unique type     
==================================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**origin**                           Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isReverseRun**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planDisplayedName**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**storage_options**                  Unicode string data. Ex: "Hello World"                                         A       false    false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**preAnalysis**                      Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reference**                        Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planShortID**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**             Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planStatus**                       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runMode**                          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**             Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                  Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reverse_primer**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applicationGroup**                 A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                               Integer data. Ex: 2673                                                                 false    false    true  true   integer  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**metaData**                         Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isFavorite**                       Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                    Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**               Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                      Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleGroupName**                  Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingKitName**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**barcodeKitName**                   Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runType**                          Unicode string data. Ex: "Hello World"                                         GENS    false    false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planPGM**                          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                  Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName** Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**autoName**                         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isReusable**                       Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**           Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sequencingInstrumentType**         Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**date**                             A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**eas**                              A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystem**                         Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libkit**                           Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**categories**                       Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planName**                         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**irAccountName**                    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatePrepInstrumentType**       Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**              Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**adapter**                          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**irworkflow**                       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingSize**                   Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planExecuted**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**username**                         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                  Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**storageHost**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**expName**                          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                Integer data. Ex: 2673                                                         0       false    false    false false  integer  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runname**                          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                   Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planGUID**                         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cycles**                           Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**notes**                            Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
------------------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**                     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
==================================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 68, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plantemplatebasicinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "origin": "|5.4.0.RC2", 
	            "isReverseRun": false, 
	            "planDisplayedName": "Oncomine Mutation Load", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "reference": "hg19", 
	            "planShortID": "1J3FB", 
	            "hotSpotRegionBedFile": "", 
	            "planStatus": "planned", 
	            "runMode": "single", 
	            "templatingKitBarcode": null, 
	            "sampleTubeLabel": null, 
	            "planExecutedDate": null, 
	            "samplePrepKitName": null, 
	            "reverse_primer": null, 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "applicationGroupDisplayedName": "DNA", 
	            "id": 100, 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "seqKitBarcode": null, 
	            "samplePrepProtocol": "", 
	            "isPlanGroup": false, 
	            "sampleGroupName": "Self", 
	            "templatingKitName": "Ion Chef S540 V1", 
	            "barcodeKitName": "IonCode Barcodes 1-32", 
	            "runType": "AMPS", 
	            "planPGM": "", 
	            "isSystemDefault": false, 
	            "applicationCategoryDisplayedName": "Oncology - ImmunoOncology", 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": null, 
	            "sequencingInstrumentType": "S5", 
	            "date": "2017-03-28T05:00:31.000988+00:00", 
	            "eas": "/rundb/api/v1/experimentanalysissettings/91/", 
	            "isSystem": true, 
	            "libkit": null, 
	            "categories": "onco_immune", 
	            "planName": "Oncomine_Mutation_Load", 
	            "irAccountName": "", 
	            "templatePrepInstrumentType": "IonChef", 
	            "pairedEndLibraryAdapterName": null, 
	            "targetRegionBedFile": "", 
	            "adapter": null, 
	            "irworkflow": "", 
	            "templatingSize": "", 
	            "planExecuted": false, 
	            "username": null, 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "", 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "9a591f4f-8d75-4744-ab53-0e404976abe8", 
	            "cycles": null, 
	            "notes": "", 
	            "resource_uri": "/rundb/api/v1/plantemplatebasicinfo/100/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get

