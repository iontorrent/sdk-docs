.. _api_reference_eventlog:

Event Log  Resource
===================

| Resource URL ``http://mytorrentserver/rundb/api/v1/eventlog/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/eventlog/schema/``
| 

.. include:: ../references_manual_extras/eventlog.rst

Resource Fields
---------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**username**     Unicode string data. Ex: "Hello World"               ION     false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**text**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**object_pk**    Integer data. Ex: 2673                               n/a     false    false    false false  integer  
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
	        "total_count": 34, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/eventlog/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "system", 
	            "created": "2017-07-22T06:58:07.000662+00:00", 
	            "text": "Updated Planned Run from explog: CopyOfSystemDefault_S5-530_cfDNA (97).", 
	            "object_pk": 97, 
	            "id": 2, 
	            "resource_uri": "/rundb/api/v1/eventlog/2/"
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

