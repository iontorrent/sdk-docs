.. _api_reference_log:

Log  Resource
=============

| Resource URL ``http://mytorrentserver/rundb/api/v1/log/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/log/schema/``
| 

.. include:: ../references_manual_extras/log.rst

Resource Fields
---------------

================ ============================================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                                                      default nullable readonly blank unique type     
================ ============================================================================== ======= ======== ======== ===== ====== ======== 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**text**         Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**timeStamp**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload**       A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

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

