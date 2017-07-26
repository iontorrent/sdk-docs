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
**description**         Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
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
**sampleDisplayedName** Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
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
	        "total_count": 0, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": []
	}

Allowed HTTP methods
--------------------

- get

