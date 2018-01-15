.. _api_reference_content:

Content  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/content/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/content/schema/``
| 

.. include:: ../references_manual_extras/content.rst

Resource Fields
---------------

================= ============================================================================== ======= ======== ======== ===== ====== ======= 
field             help text                                                                      default nullable readonly blank unique type    
================= ============================================================================== ======= ======== ======== ===== ====== ======= 
**publisher**     A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**contentupload** A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**meta**          Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**file**          Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**path**          Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**            Integer data. Ex: 2673                                                                 false    false    true  true   integer 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**  Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
================= ============================================================================== ======= ======== ======== ===== ====== ======= 

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

