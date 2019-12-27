.. _api_reference_supportupload:

Support Upload  Resource
========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/supportupload/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/supportupload/schema/``
| 

.. include:: ../references_manual_extras/supportupload.rst

Resource Fields
---------------

================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field              help text                                                                      default nullable readonly blank unique type     
================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**celery_task_id** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**contact_email**  Unicode string data. Ex: "Hello World"                                                 false    false    false false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**created**        A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**    Unicode string data. Ex: "Hello World"                                                 false    false    false false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**file**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related  
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                                                 false    false    true  true   integer  
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**local_message**  Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**local_status**   Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**result**         A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**ticket_id**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**ticket_message** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**ticket_status**  Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**updated**        A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 0
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

