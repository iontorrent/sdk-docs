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
	        "total_count": 32, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/datamanagementhistory/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "username": "ionadmin", 
	            "created": "2017-07-22T06:59:07.000501+00:00", 
	            "text": "Started from Local Basecalling Input /results/S5_DemoData/S5-530_cfDNA.", 
	            "object_pk": 1, 
	            "resultsName": "Auto_S5-530_cfDNA_89", 
	            "id": 8, 
	            "resource_uri": "/rundb/api/v1/datamanagementhistory/8/"
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

