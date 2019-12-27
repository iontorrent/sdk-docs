.. _api_reference_monitorresult:

Monitor Result  Resource
========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/monitorresult/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/monitorresult/schema/``
| 

.. include:: ../references_manual_extras/monitorresult.rst

Resource Fields
---------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**analysismetrics** A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**       Unicode string data. Ex: "Hello World"                                                             n/a     true     true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**i18nstatus**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**         Unicode string data. Ex: "Hello World"                                                             n/a     true     true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

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

