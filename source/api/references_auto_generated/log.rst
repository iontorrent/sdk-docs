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
**text**         Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**timeStamp**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload**       A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

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

