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
**name**         Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creator**      A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**modified**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resultsCount** Integer data. Ex: 2673                                                         n/a     false    true     false false  integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**public**       Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/project/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "demo", 
	            "creator": "/rundb/api/v1/user/1/", 
	            "created": "2017-07-22T06:59:07.000475+00:00", 
	            "modified": "2017-08-14T18:58:52.000246+00:00", 
	            "id": 1, 
	            "resultsCount": 5, 
	            "public": true, 
	            "resource_uri": "/rundb/api/v1/project/1/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

