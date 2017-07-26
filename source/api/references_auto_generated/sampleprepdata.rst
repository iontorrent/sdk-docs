.. _api_reference_sampleprepdata:

Sample Prep Data  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleprepdata/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleprepdata/schema/``
| 

.. include:: ../references_manual_extras/sampleprepdata.rst

Resource Fields
---------------

======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
field                   help text                                                                      default nullable readonly blank unique type     
======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
**instrumentName**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastUpdate**          A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**kitType**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**solutionsPart**       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reagentsPart**        Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepDataType**  Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**tipRackBarcode**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reagentsExpiration**  Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**logPath**             Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**packageVer**          Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**solutionsLot**        Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**instrumentStatus**    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**scriptVersion**       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reagentsLot**         Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**solutionsExpiration** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**progress**            Floating point numeric data. Ex: 26.73                                         0       false    false    true  false  float    
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**message**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                  Integer data. Ex: 2673                                                                 false    false    true  true   integer  
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
- post
- put
- delete
- patch

