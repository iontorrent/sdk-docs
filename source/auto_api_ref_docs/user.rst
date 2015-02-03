User Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/user/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/user/schema/``


.. include:: ../manual_api_ref_docs/user.rst

Fields table
------------

================ ===================================================================================================== ================================ ======== ======== ===== ====== ======== 
field            help text                                                                                             default                          nullable readonly blank unique type     
================ ===================================================================================================== ================================ ======== ======== ===== ====== ======== 
**profile**      A single related resource. Can be either a URI or set of nested resource data.                        n/a                              false    false    false false  related  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**username**     Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters                           n/a                              false    false    false true   string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**first_name**   Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**last_name**    Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**is_active**    Designates whether this user should be treated as active. Unselect this instead of deleting accounts. true                             false    false    true  false  boolean  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**email**        Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**last_login**   A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2015-02-03T02:29:47.000645+00:00 false    false    false false  datetime 
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**full_name**    Unicode string data. Ex: "Hello World"                                                                n/a                              false    false    false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                                n/a                              false    true     false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                                                                 false    false    true  true   integer  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**date_joined**  A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2015-02-03T02:29:47.000646+00:00 false    false    false false  datetime 
================ ===================================================================================================== ================================ ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/user/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/user/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	users = ts_api_response["objects"]
	
	for user in users:
	    print user
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 23, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/user/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "profile": {
	                "phone_number": "", 
	                "name": "", 
	                "title": "user", 
	                "last_read_news_post": "2013-09-12T14:03:31.000755+00:00", 
	                "note": "", 
	                "id": 8, 
	                "resource_uri": ""
	            }, 
	            "username": "bernpuc", 
	            "first_name": "", 
	            "last_name": "", 
	            "is_active": true, 
	            "email": "bernard.puc@lifetech.com", 
	            "last_login": "2013-09-17T13:58:41+00:00", 
	            "full_name": "", 
	            "resource_uri": "/rundb/api/v1/user/8/", 
	            "id": 8, 
	            "date_joined": "2013-05-13T13:50:03+00:00"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get

