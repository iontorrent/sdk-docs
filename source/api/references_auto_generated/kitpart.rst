.. _api_reference_kitpart:

Kit Part Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/kitpart/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/kitpart/schema/``
| 

.. include:: ../references_manual_extras/kitpart.rst

Resource Fields
---------------

================ ============================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                      default nullable readonly blank unique type    
================ ============================================================================== ======= ======== ======== ===== ====== ======= 
**barcode**      Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**kit**          A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
================ ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/kitpart/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 253
	    },
	    "objects": [
	        {
	            "barcode": "A43587",
	            "id": 20269,
	            "kit": "/rundb/api/v1/kitinfo/20118/",
	            "resource_uri": "/rundb/api/v1/kitpart/20269/"
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

