.. _api_reference_sampleprepdata:

Sample Prep Data  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleprepdata/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleprepdata/schema/``
| 

.. include:: ../references_manual_extras/sampleprepdata.rst

Resource Fields
---------------

======================= ==================================================== ======= ======== ======== ===== ====== ======== 
field                   help text                                            default nullable readonly blank unique type     
======================= ==================================================== ======= ======== ======== ===== ====== ======== 
**endTime**             A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                  Integer data. Ex: 2673                                       false    false    true  true   integer  
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**instrumentName**      Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**instrumentStatus**    Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**kitType**             Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**lastUpdate**          A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**logPath**             Unicode string data. Ex: "Hello World"               n/a     true     false    false false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**message**             Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**operationMode**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**packageVer**          Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**progress**            Floating point numeric data. Ex: 26.73               0       false    false    true  false  float    
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentsExpiration**  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentsLot**         Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentsPart**        Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**remainingSeconds**    Integer data. Ex: 2673                               n/a     true     false    false false  integer  
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**        Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepDataType**  Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**scriptVersion**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**solutionsExpiration** Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**solutionsLot**        Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**solutionsPart**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**startTime**           A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     true     false    false false  datetime 
----------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tipRackBarcode**      Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
======================= ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 0
	    },
	    "objects": []
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

