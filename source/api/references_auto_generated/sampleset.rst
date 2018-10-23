.. _api_reference_sampleset:

Sample Set  Resource
====================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleset/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleset/schema/``
| 

.. include:: ../references_manual_extras/sampleset.rst

Resource Fields
---------------

================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                            help text                                                                                          default nullable readonly blank unique type     
================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 
**status**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrument**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepPlateType**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                 Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleCount**                  Integer data. Ex: 2673                                                                             n/a     false    true     false false  integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**SampleGroupType_CV**           A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pcrPlateSerialNum**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrumentData**    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**                      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupTypeName**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**combinedLibraryTubeLabel**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**creationDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                           Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sampleset/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "readyForPlanning": true, 
	            "status": "created", 
	            "libraryPrepInstrument": "", 
	            "libraryPrepType": "", 
	            "libraryPrepPlateType": "", 
	            "description": "", 
	            "resource_uri": "/rundb/api/v1/sampleset/1/", 
	            "sampleCount": 8, 
	            "displayedName": "Ampliseq on Chef", 
	            "SampleGroupType_CV": null, 
	            "pcrPlateSerialNum": "", 
	            "libraryPrepInstrumentData": null, 
	            "libraryPrepKitName": "", 
	            "samples": [
	                "/rundb/api/v1/samplesetitem/3/", 
	                "/rundb/api/v1/samplesetitem/5/", 
	                "/rundb/api/v1/samplesetitem/7/", 
	                "/rundb/api/v1/samplesetitem/9/", 
	                "/rundb/api/v1/samplesetitem/11/", 
	                "/rundb/api/v1/samplesetitem/13/", 
	                "/rundb/api/v1/samplesetitem/15/", 
	                "/rundb/api/v1/samplesetitem/17/"
	            ], 
	            "lastModifiedDate": "2017-08-28T21:21:14.000027+00:00", 
	            "sampleGroupTypeName": "", 
	            "combinedLibraryTubeLabel": "", 
	            "creationDate": "2017-08-28T21:21:14.000027+00:00", 
	            "libraryPrepTypeDisplayedName": "", 
	            "id": 1, 
	            "libraryPrepKitDisplayedName": ""
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

