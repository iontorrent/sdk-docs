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
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**object_pk**    Integer data. Ex: 2673                               n/a     false    false    false false  integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**  Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
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
	        "next": "/rundb/api/v1/datamanagementhistory/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 36
	    },
	    "objects": [
	        {
	            "created": "2018-05-29T17:32:06.000459+00:00",
	            "id": 59,
	            "object_pk": 7,
	            "resource_uri": "/rundb/api/v1/datamanagementhistory/59/",
	            "resultsName": "CA_Combined_demo_001",
	            "text": "Src Dir not found: /results/analysis/output/Home/CA_Combined_demo_001_007. Setting action_state to Deleted",
	            "username": "dm_agent"
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

