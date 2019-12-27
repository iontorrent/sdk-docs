.. _api_reference_rig:

Rig Resource
============

| Resource URL ``http://mytorrentserver/rundb/api/v1/rig/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/rig/schema/``
| 

.. include:: ../references_manual_extras/rig.rst

Resource Fields
---------------

=================== ============================================================================== ============= ======== ======== ===== ====== ======= 
field               help text                                                                      default       nullable readonly blank unique type    
=================== ============================================================================== ============= ======== ======== ===== ====== ======= 
**alarms**          Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**comments**        Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**display_state**   Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftppassword**     Unicode string data. Ex: "Hello World"                                         ionguest      false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftprootdir**      Unicode string data. Ex: "Hello World"                                         results       false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftpserver**       Unicode string data. Ex: "Hello World"                                         192.168.201.1 false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftpusername**     Unicode string data. Ex: "Hello World"                                         ionguest      false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**host_address**    Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_clean_date** Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_experiment** Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_init_date**  Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**location**        A single related resource. Can be either a URI or set of nested resource data. n/a           true     false    true  false  related 
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**name**            Unicode string data. Ex: "Hello World"                                         n/a           false    false    false true   string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                         n/a           false    true     false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**serial**          Unicode string data. Ex: "Hello World"                                         n/a           true     false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**state**           Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**type**            Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updateCommand**   Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updateflag**      Boolean data. Ex: True                                                         false         false    false    true  false  boolean 
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updatehome**      Unicode string data. Ex: "Hello World"                                         192.168.201.1 false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**version**         Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
=================== ============================================================================== ============= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/rig/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 4
	    },
	    "objects": [
	        {
	            "alarms": {},
	            "comments": "",
	            "display_state": "",
	            "ftppassword": "ionguest",
	            "ftprootdir": "results",
	            "ftpserver": "192.168.201.1",
	            "ftpusername": "ionguest",
	            "host_address": "",
	            "last_clean_date": "",
	            "last_experiment": "",
	            "last_init_date": "",
	            "location": {
	                "comments": "",
	                "defaultlocation": true,
	                "id": 1,
	                "name": "Home",
	                "resource_uri": "/rundb/api/v1/location/1/"
	            },
	            "name": "S5_DemoData",
	            "resource_uri": "/rundb/api/v1/rig/S5_DemoData/",
	            "serial": "",
	            "state": "",
	            "type": "",
	            "updateCommand": {},
	            "updateflag": false,
	            "updatehome": "192.168.201.1",
	            "version": {}
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

