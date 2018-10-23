.. _api_reference_samplesetitem:

Sample Set Item  Resource
=========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/samplesetitem/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/samplesetitem/schema/``
| 

.. include:: ../references_manual_extras/samplesetitem.rst

Resource Fields
---------------

===================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                 help text                                                                      default nullable readonly blank unique type     
===================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**sample**            A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellNum**           Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**biopsyDays**        Integer data. Ex: 2673                                                         0       true     false    false false  integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**nucleotideType**    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**gender**            Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipGroup** Integer data. Ex: 2673                                                         n/a     false    false    false false  integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**coupleId**          Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellularityPct**    Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                Integer data. Ex: 2673                                                                 false    false    true  true   integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipRole**  Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateColumn**    Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cancerType**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlType**       Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**  A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcode**        A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateRow**       Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**embryoId**          Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**       Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
===================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 16, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/samplesetitem/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "sample": "/rundb/api/v1/sample/8/", 
	            "cellNum": "", 
	            "biopsyDays": 0, 
	            "resource_uri": "/rundb/api/v1/samplesetitem/3/", 
	            "nucleotideType": "", 
	            "gender": "", 
	            "relationshipGroup": 0, 
	            "coupleId": "", 
	            "cellularityPct": null, 
	            "id": 3, 
	            "relationshipRole": "", 
	            "pcrPlateColumn": "", 
	            "cancerType": "", 
	            "controlType": "", 
	            "sampleSet": "/rundb/api/v1/sampleset/1/", 
	            "lastModifiedDate": "2017-11-01T16:19:12.000420+00:00", 
	            "dnabarcode": null, 
	            "pcrPlateRow": "", 
	            "creationDate": "2017-11-01T16:19:12.000420+00:00", 
	            "embryoId": "", 
	            "description": ""
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

