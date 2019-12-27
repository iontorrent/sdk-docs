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
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**object_pk**    Integer data. Ex: 2673                               n/a     false    false    false false  integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**text**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**     Unicode string data. Ex: "Hello World"               ION     false    false    true  false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/eventlog/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 57
	    },
	    "objects": [
	        {
	            "created": "2018-08-02T18:54:44.000330+00:00",
	            "id": 60,
	            "object_pk": 144,
	            "resource_uri": "/rundb/api/v1/eventlog/60/",
	            "text": "Created Planned Run: Ion_AmpliSeq_Transcriptome_Mouse_Gene_Expression (144)",
	            "username": "ionadmin"
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

