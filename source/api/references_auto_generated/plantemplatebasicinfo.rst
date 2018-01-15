.. _api_reference_plantemplatebasicinfo:

Plan Template Basic Info  Resource
==================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/schema/``
| 

.. include:: ../references_manual_extras/plantemplatebasicinfo.rst

Resource Fields
---------------

==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                                help text                                                                                          default nullable readonly blank unique type     
==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**origin**                           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                  Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                      Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reference**                        Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**             Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                 A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**    Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                               Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                         Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**               Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupName**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeKitName**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                          Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencingInstrumentType**         Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**                              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                         Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                       Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irAccountName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatePrepInstrumentType**       Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**              Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingSize**                   Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                           Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                            Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 84, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plantemplatebasicinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "origin": "|5.8.0", 
	            "isReverseRun": false, 
	            "planDisplayedName": "Oncomine Comprehensive v3 Fusions for 550", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "reference": "", 
	            "planShortID": "Y2E01", 
	            "hotSpotRegionBedFile": "", 
	            "planStatus": "planned", 
	            "runMode": "single", 
	            "isCustom_kitSettings": false, 
	            "sampleTubeLabel": null, 
	            "planExecutedDate": null, 
	            "samplePrepKitName": null, 
	            "reverse_primer": null, 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/5/", 
	            "applicationGroupDisplayedName": "DNA and Fusions", 
	            "id": 123, 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "seqKitBarcode": null, 
	            "samplePrepProtocol": "", 
	            "isPlanGroup": false, 
	            "sampleGroupName": "Single Fusions", 
	            "experiment": "/rundb/api/v1/experiment/115/", 
	            "projects": "", 
	            "barcodeKitName": "IonXpress", 
	            "runType": "AMPS_RNA", 
	            "templatingKitBarcode": null, 
	            "templatingKitName": "Ion Chef S550 V1", 
	            "planPGM": "", 
	            "isSystemDefault": false, 
	            "applicationCategoryDisplayedName": "Oncology - Solid Tumor", 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": null, 
	            "sequencingInstrumentType": "s5", 
	            "date": "2017-12-05T00:10:38.000438+00:00", 
	            "eas": "/rundb/api/v1/experimentanalysissettings/114/", 
	            "isSystem": true, 
	            "libkit": null, 
	            "categories": "Oncomine;onco_solidTumor", 
	            "planName": "Oncomine_Comprehensive_v3_Fusions_for_550", 
	            "irAccountName": "", 
	            "templatePrepInstrumentType": "IonChef", 
	            "pairedEndLibraryAdapterName": null, 
	            "targetRegionBedFile": "", 
	            "adapter": null, 
	            "irworkflow": "", 
	            "templatingSize": "200", 
	            "planExecuted": false, 
	            "username": null, 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "", 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "5de7dbc0-17db-441c-abfb-ec6c060d988c", 
	            "cycles": null, 
	            "notes": "", 
	            "resource_uri": "/rundb/api/v1/plantemplatebasicinfo/123/"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

- GET

