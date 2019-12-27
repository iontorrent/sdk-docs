.. _api_reference_project:

Project  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/project/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/project/schema/``
| 

.. include:: ../references_manual_extras/project.rst

Resource Fields
---------------

================ ============================================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                                                      default nullable readonly blank unique type     
================ ============================================================================== ======= ======== ======== ===== ====== ======== 
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creator**      A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**modified**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**name**         Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**public**       Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resultsCount** Integer data. Ex: 2673                                                         n/a     false    true     false false  integer  
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/project/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2
	    },
	    "objects": [
	        {
	            "created": "2017-08-23T21:43:01.000074+00:00",
	            "creator": "/rundb/api/v1/user/1/",
	            "id": 2,
	            "modified": "2018-04-27T18:59:37.000779+00:00",
	            "name": "SampleData",
	            "public": true,
	            "resource_uri": "/rundb/api/v1/project/2/",
	            "resultsCount": 0
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

