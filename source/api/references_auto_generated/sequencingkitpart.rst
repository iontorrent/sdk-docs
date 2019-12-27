.. _api_reference_sequencingkitpart:

Sequencing Kit Part Resource
============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sequencingkitpart/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sequencingkitpart/schema/``
| 

.. include:: ../references_manual_extras/sequencingkitpart.rst

Resource Fields
---------------

==================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                help text                                                                      default nullable readonly blank unique type    
==================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**barcode**          Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultFlowOrder** A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**               Integer data. Ex: 2673                                                                 false    false    true  true   integer 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**kit**              A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
==================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/sequencingkitpart/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 99
	    },
	    "objects": [
	        {
	            "barcode": "100049484",
	            "defaultFlowOrder": null,
	            "id": 20263,
	            "kit": "/rundb/api/v1/kitinfo/20111/",
	            "resource_uri": "/rundb/api/v1/sequencingkitpart/20263/"
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

