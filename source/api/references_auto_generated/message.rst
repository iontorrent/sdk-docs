.. _api_reference_message:

Message Resource
================

| Resource URL ``http://mytorrentserver/rundb/api/v1/message/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/message/schema/``
| 

.. include:: ../references_manual_extras/message.rst

Resource Fields
---------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**body**         Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expires**      Unicode string data. Ex: "Hello World"               read    false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**level**        Integer data. Ex: 2673                               20      false    false    false false  integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**route**        Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**       Unicode string data. Ex: "Hello World"               unread  false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tags**         Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**time**         A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
================ ==================================================== ======= ======== ======== ===== ====== ======== 

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

