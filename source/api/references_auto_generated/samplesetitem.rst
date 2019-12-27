.. _api_reference_samplesetitem:

Sample Set Item  Resource
=========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/samplesetitem/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/samplesetitem/schema/``
| 

.. include:: ../references_manual_extras/samplesetitem.rst

Resource Fields
---------------

======================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                    help text                                                                      default nullable readonly blank unique type     
======================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**assayGroup**           Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**biopsyDays**           Integer data. Ex: 2673                                                         0       true     false    false false  integer  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cancerType**           Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellNum**              Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellularityPct**       Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlType**          Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**coupleId**             Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**         A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**          Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcode**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**embryoId**             Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**gender**               Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                   Integer data. Ex: 2673                                                                 false    false    true  true   integer  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**mouseStrains**         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**nucleotideType**       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**panelPoolType**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateColumn**       Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pcrPlateRow**          Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**population**           Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipGroup**    Integer data. Ex: 2673                                                         n/a     false    false    false false  integer  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipRole**     Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**         Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sample**               A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleCollectionDate** A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleReceiptDate**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**            A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSource**         Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**tubePosition**         Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
======================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/samplesetitem/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 16
	    },
	    "objects": [
	        {
	            "assayGroup": null,
	            "biopsyDays": 0,
	            "cancerType": "",
	            "cellNum": "",
	            "cellularityPct": null,
	            "controlType": "",
	            "coupleId": "",
	            "creationDate": "2017-11-01T18:48:24.000678+00:00",
	            "description": "",
	            "dnabarcode": null,
	            "embryoId": "",
	            "gender": "",
	            "id": 19,
	            "lastModifiedDate": "2017-11-01T18:48:24.000678+00:00",
	            "mouseStrains": null,
	            "nucleotideType": "",
	            "panelPoolType": null,
	            "pcrPlateColumn": "",
	            "pcrPlateRow": "",
	            "population": null,
	            "relationshipGroup": 0,
	            "relationshipRole": "",
	            "resource_uri": "/rundb/api/v1/samplesetitem/19/",
	            "sample": "/rundb/api/v1/sample/16/",
	            "sampleCollectionDate": null,
	            "sampleReceiptDate": null,
	            "sampleSet": "/rundb/api/v1/sampleset/2/",
	            "sampleSource": null,
	            "tubePosition": ""
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

