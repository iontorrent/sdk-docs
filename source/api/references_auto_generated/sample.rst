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
**status**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**    Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiments**   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**externalId**    Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**  Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**            Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
----------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
================= ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 13, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sample/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "run", 
	            "sampleSets": [], 
	            "description": null, 
	            "displayedName": "e5272-wfa-l165", 
	            "experiments": [
	                "/rundb/api/v1/experiment/94/"
	            ], 
	            "externalId": "", 
	            "date": "2017-08-23T21:42:01.000299+00:00", 
	            "resource_uri": "/rundb/api/v1/sample/4/", 
	            "id": 4, 
	            "name": "e5272-wfa-l165"
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

