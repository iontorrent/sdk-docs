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
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**kit**          A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
================ ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 261, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/kitpart/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "barcode": "100020580", 
	            "id": 20086, 
	            "resource_uri": "/rundb/api/v1/kitpart/20086/", 
	            "kit": "/rundb/api/v1/kitinfo/20042/"
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

