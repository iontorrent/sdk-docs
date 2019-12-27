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
**date_joined**  A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2019-11-19T06:33:10.000022+00:00 false    false    false false  datetime 
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**email**        Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**first_name**   Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**full_name**    Unicode string data. Ex: "Hello World"                                                                n/a                              false    false    false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                                                                 false    false    true  true   integer  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**is_active**    Designates whether this user should be treated as active. Unselect this instead of deleting accounts. true                             false    false    true  false  boolean  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**last_login**   A date & time as a string. Ex: "2010-11-10T03:07:43"                                                  2019-11-19T06:33:10.000022+00:00 false    false    false false  datetime 
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**last_name**    Unicode string data. Ex: "Hello World"                                                                                                 false    false    true  false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**profile**      A single related resource. Can be either a URI or set of nested resource data.                        n/a                              false    false    false false  related  
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                                n/a                              false    true     false false  string   
---------------- ----------------------------------------------------------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**username**     Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters                           n/a                              false    false    false true   string   
================ ===================================================================================================== ================================ ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/user/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 6
	    },
	    "objects": [
	        {
	            "date_joined": "2017-07-24T18:11:45.000735+00:00",
	            "email": "yourname@mail.com",
	            "first_name": "",
	            "full_name": "",
	            "id": 6,
	            "is_active": true,
	            "last_login": "2017-07-24T18:11:45.000735+00:00",
	            "last_name": "",
	            "profile": {
	                "id": 6,
	                "last_read_news_post": "1984-11-06T00:00:00+00:00",
	                "name": "",
	                "needs_activation": false,
	                "note": "",
	                "phone_number": "",
	                "resource_uri": "",
	                "title": "user"
	            },
	            "resource_uri": "/rundb/api/v1/user/6/",
	            "username": "dm_contact"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

- GET

