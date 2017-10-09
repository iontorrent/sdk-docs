.. _api_reference_samplesetiteminfo:

Sample Set Item Info  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/samplesetiteminfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/samplesetiteminfo/schema/``
| 

.. include:: ../references_manual_extras/samplesetiteminfo.rst

Resource Fields
---------------

======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
field                   help text                                                                      default nullable readonly blank unique type     
======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
**relationshipGroup**   Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleDescription**   Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcodeKit**       Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sample**              A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateColumn**      Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cancerType**          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                  Integer data. Ex: 2673                                                                 false    false    true  true   integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName** Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellNum**             Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleExternalId**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**coupleId**            Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateRow**         Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSetPk**         Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSetStatus**     Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**embryoId**            Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**         Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipRole**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePk**            Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcode**          A single related resource. Can be either a URI or set of nested resource data. n/a     true     true     true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**        A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**biopsyDays**          Integer data. Ex: 2673                                                         0       true     false    false false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**nucleotideType**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**gender**              Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellularityPct**      Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlType**         Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**        Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
======================= ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/samplesetiteminfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "relationshipGroup": 0, 
	            "sampleDescription": "", 
	            "dnabarcodeKit": "IonCode Barcodes 1-32", 
	            "sample": "/rundb/api/v1/sample/6/", 
	            "pcrPlateColumn": "1", 
	            "cancerType": "", 
	            "attribute_dict": {}, 
	            "id": 1, 
	            "sampleDisplayedName": "sample 1", 
	            "cellNum": "", 
	            "sampleExternalId": "", 
	            "coupleId": "", 
	            "pcrPlateRow": "A", 
	            "sampleSetPk": 1, 
	            "sampleSetStatus": "created", 
	            "embryoId": "", 
	            "sampleSet": "/rundb/api/v1/sampleset/1/", 
	            "description": "", 
	            "lastModifiedDate": "2017-08-28T21:21:14.000040+00:00", 
	            "sampleSetGroupType": "", 
	            "relationshipRole": "", 
	            "samplePk": 6, 
	            "dnabarcode": "IonCode_0125", 
	            "creationDate": "2017-08-28T21:21:14.000040+00:00", 
	            "biopsyDays": 0, 
	            "nucleotideType": "", 
	            "gender": "", 
	            "cellularityPct": null, 
	            "controlType": "", 
	            "resource_uri": "/rundb/api/v1/samplesetiteminfo/1/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get

