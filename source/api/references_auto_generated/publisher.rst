.. _api_reference_publisher:

Publisher Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/publisher/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/publisher/schema/``
| 

.. include:: ../references_manual_extras/publisher.rst

Resource Fields
---------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**name**         Unicode string data. Ex: "Hello World"               n/a     false    false    false true   string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**      Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**global_meta**  Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**         A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     false    false    false false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/publisher/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "refAnnot", 
	            "version": "1.0", 
	            "global_meta": {}, 
	            "date": "2017-07-22T21:17:12.000925+00:00", 
	            "path": "/results/publishers/refAnnot", 
	            "id": 1, 
	            "resource_uri": "/rundb/api/v1/publisher/refAnnot/"
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

