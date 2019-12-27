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
**adapter**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                 A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**    Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeKitName**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                       Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                           Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**                              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**             Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                               Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irAccountName**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**             Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                         Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                         Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                            Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                      Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reference**                        Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                     Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                          Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupName**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**               Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencingInstrumentType**         Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                      Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                  Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**              Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatePrepInstrumentType**       Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
==================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plantemplatebasicinfo/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 103
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "applicationCategoryDisplayedName": "Oncology - ImmunoOncology",
	            "applicationGroup": "/rundb/api/v1/applicationgroup/9/",
	            "applicationGroupDisplayedName": "Immune Repertoire",
	            "autoName": null,
	            "barcodeKitName": "Ion Dual Barcode Kit 1-96",
	            "categories": "onco_immune;immunology",
	            "controlSequencekitname": null,
	            "cycles": null,
	            "date": "2019-10-03T20:53:08.000426+00:00",
	            "eas": "/rundb/api/v1/experimentanalysissettings/159/",
	            "expName": "",
	            "experiment": "/rundb/api/v1/experiment/160/",
	            "hotSpotRegionBedFile": "",
	            "id": 167,
	            "irAccountName": "",
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
	            "notes": "",
	            "origin": "|5.12.1",
	            "pairedEndLibraryAdapterName": null,
	            "planDisplayedName": "Ion Ampliseq Mouse TCRB-SR for S5",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "18b7b769-c7b9-4df9-9c70-3fe1794f4868",
	            "planName": "Ion_Ampliseq_Mouse_TCRB-SR_for_S5",
	            "planPGM": "",
	            "planShortID": "MX7ER",
	            "planStatus": "planned",
	            "preAnalysis": true,
	            "projects": "",
	            "reference": "",
	            "resource_uri": "/rundb/api/v1/plantemplatebasicinfo/167/",
	            "reverse_primer": null,
	            "runMode": "single",
	            "runType": "MIXED",
	            "runname": null,
	            "sampleGroupName": "Self",
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
	            "sampleTubeLabel": null,
	            "seqKitBarcode": null,
	            "sequencingInstrumentType": "s5",
	            "storageHost": null,
	            "storage_options": "A",
	            "targetRegionBedFile": "",
	            "templatePrepInstrumentType": "IonChef",
	            "templatingKitBarcode": null,
	            "templatingKitName": "Ion Chef S540 V1",
	            "usePostBeadfind": false,
	            "usePreBeadfind": true,
	            "username": null
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

- GET

