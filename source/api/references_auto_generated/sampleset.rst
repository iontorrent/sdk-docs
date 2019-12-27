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
**SampleGroupType_CV**           A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**additionalCycles**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**combinedLibraryTubeLabel**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**creationDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cyclingProtocols**             Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                           Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrument**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrumentData**    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepPlateType**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pcrPlateSerialNum**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                 Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleCount**                  Integer data. Ex: 2673                                                                             n/a     false    true     false false  integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupTypeName**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**                      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/sampleset/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "SampleGroupType_CV": null,
	            "additionalCycles": null,
	            "combinedLibraryTubeLabel": "",
	            "creationDate": "2017-11-01T16:19:12.000371+00:00",
	            "cyclingProtocols": null,
	            "description": "",
	            "displayedName": "Sample Set 1",
	            "id": 2,
	            "lastModifiedDate": "2017-11-01T16:19:12.000371+00:00",
	            "libraryPrepInstrument": "",
	            "libraryPrepInstrumentData": null,
	            "libraryPrepKitDisplayedName": "",
	            "libraryPrepKitName": "",
	            "libraryPrepPlateType": "",
	            "libraryPrepType": "",
	            "libraryPrepTypeDisplayedName": "",
	            "pcrPlateSerialNum": "",
	            "readyForPlanning": true,
	            "resource_uri": "/rundb/api/v1/sampleset/2/",
	            "sampleCount": 8,
	            "sampleGroupTypeName": "",
	            "samples": [
	                "/rundb/api/v1/samplesetitem/6/",
	                "/rundb/api/v1/samplesetitem/8/",
	                "/rundb/api/v1/samplesetitem/10/",
	                "/rundb/api/v1/samplesetitem/12/",
	                "/rundb/api/v1/samplesetitem/14/",
	                "/rundb/api/v1/samplesetitem/16/",
	                "/rundb/api/v1/samplesetitem/18/",
	                "/rundb/api/v1/samplesetitem/19/"
	            ],
	            "status": "created"
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

