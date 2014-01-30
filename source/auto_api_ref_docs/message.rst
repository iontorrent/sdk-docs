Message Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/message/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/message/schema/``


.. include:: ../manual_api_ref_docs/message.rst

Fields table
------------

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

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/message/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/message/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	messages = ts_api_response["objects"]
	
	for message in messages:
	    print message
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/message/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "body": "All ion packages failed to download!", 
	            "status": "unread", 
	            "level": 40, 
	            "route": "updates", 
	            "expires": "read", 
	            "time": "2012-04-17T16:56:08.000874+00:00", 
	            "id": 7, 
	            "tags": "", 
	            "resource_uri": "/rundb/api/v1/message/7/"
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

