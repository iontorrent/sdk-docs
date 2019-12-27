.. _api_reference_sample:

Sample  Resource
================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sample/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sample/schema/``
| 

.. include:: ../references_manual_extras/sample.rst

Resource Fields
---------------

================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
field             help text                                                                                          default nullable readonly blank unique type     
================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
**date**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiments**   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**externalId**    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**            Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**  Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
================= ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/sample/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 23
	    },
	    "objects": [
	        {
	            "date": "2018-04-13T22:17:13.000114+00:00",
	            "description": "",
	            "displayedName": "Sample 9",
	            "experiments": [
	                "/rundb/api/v1/experiment/136/"
	            ],
	            "externalId": "",
	            "id": 26,
	            "name": "Sample_9",
	            "resource_uri": "/rundb/api/v1/sample/26/",
	            "sampleSets": [],
	            "status": "planned"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT

