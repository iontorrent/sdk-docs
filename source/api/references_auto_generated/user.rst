.. _api_reference_user:

User Resource
=============

| Resource URL ``http://mytorrentserver/rundb/api/v1/user/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/user/schema/``
| 

.. include:: ../references_manual_extras/user.rst

Resource Fields
---------------

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
**last_login**   A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2017-12-19T21:15:15.000681+00:00 false    false    false false  datetime 
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**full_name**    Unicode string data. Ex: "Hello World"                                                                n/a                              false    false    false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                                n/a                              false    true     false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                                                                 false    false    true  true   integer  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**date_joined**  A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2017-12-19T21:15:15.000681+00:00 false    false    false false  datetime 
================ ===================================================================================================== ================================ ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
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
	                "last_read_news_post": "1984-11-06T00:00:00+00:00", 
	                "note": "", 
	                "id": 1, 
	                "resource_uri": ""
	            }, 
	            "username": "ionuser", 
	            "first_name": "", 
	            "last_name": "", 
	            "is_active": true, 
	            "email": "ionuser@iontorrent.com", 
	            "last_login": "2017-07-22T06:43:37.000152+00:00", 
	            "full_name": "", 
	            "resource_uri": "/rundb/api/v1/user/2/", 
	            "id": 2, 
	            "date_joined": "2017-07-22T06:43:37.000152+00:00"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

- GET

