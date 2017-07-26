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
**status**       Unicode string data. Ex: "Hello World"               unread  false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**level**        Integer data. Ex: 2673                               20      false    false    false false  integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**route**        Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expires**      Unicode string data. Ex: "Hello World"               read    false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**time**         A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tags**         Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/message/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "body": "All Data Management Auto Actions are disabled and /results/ is 38.38% full   <a href='/data/datamanagement/' >  Visit Data Management</a>", 
	            "status": "unread", 
	            "level": 40, 
	            "route": "_StaffOnly", 
	            "expires": "read", 
	            "time": "2017-04-05T23:01:38.000971+00:00", 
	            "id": 23, 
	            "tags": "Home_all_auto_actions_disabled", 
	            "resource_uri": "/rundb/api/v1/message/23/"
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

