.. _api_reference_datamanagementhistory:

Data Management History  Resource
=================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/datamanagementhistory/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/datamanagementhistory/schema/``
| 

.. include:: ../references_manual_extras/datamanagementhistory.rst

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
**resultsName**  Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
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
	        "total_count": 40, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/datamanagementhistory/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "ionadmin", 
	            "created": "2017-04-21T21:21:03.000286+00:00", 
	            "text": "Export Pending for Signal Processing Input to /mnt/results.<br>User Comment: ", 
	            "object_pk": 3, 
	            "resultsName": "Auto_S5-540_WholeTranscriptomeRNA_91", 
	            "id": 46, 
	            "resource_uri": "/rundb/api/v1/datamanagementhistory/46/"
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

