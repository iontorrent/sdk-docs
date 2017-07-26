Rig Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/rig/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/rig/schema/``


.. include:: ../manual_api_ref_docs/rig.rst

Fields table
------------

=================== ============================================================================== ============= ======== ======== ===== ====== ======= 
field               help text                                                                      default       nullable readonly blank unique type    
=================== ============================================================================== ============= ======== ======== ===== ====== ======= 
**version**         Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**name**            Unicode string data. Ex: "Hello World"                                         n/a           false    false    false true   string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**state**           Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftprootdir**      Unicode string data. Ex: "Hello World"                                         results       false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_clean_date** Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updatehome**      Unicode string data. Ex: "Hello World"                                         192.168.201.1 false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftpserver**       Unicode string data. Ex: "Hello World"                                         192.168.201.1 false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**comments**        Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_experiment** Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftppassword**     Unicode string data. Ex: "Hello World"                                         ionguest      false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updateflag**      Boolean data. Ex: True                                                         false         false    false    true  false  boolean 
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**location**        A single related resource. Can be either a URI or set of nested resource data. n/a           false    false    false false  related 
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**last_init_date**  Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**updateCommand**   Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**alarms**          Unicode string data. Ex: "Hello World"                                         {}            false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**serial**          Unicode string data. Ex: "Hello World"                                         n/a           true     false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**host_address**    Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**type**            Unicode string data. Ex: "Hello World"                                                       false    false    true  false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**ftpusername**     Unicode string data. Ex: "Hello World"                                         ionguest      false    false    false false  string  
------------------- ------------------------------------------------------------------------------ ------------- -------- -------- ----- ------ ------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                         n/a           false    true     false false  string  
=================== ============================================================================== ============= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/rig/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/rig/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	rigs = ts_api_response["objects"]
	
	for rig in rigs:
	    print rig
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/rig/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "version": {}, 
	            "name": "default", 
	            "state": "", 
	            "ftprootdir": "results", 
	            "last_clean_date": "", 
	            "updatehome": "192.168.201.1", 
	            "ftpserver": "192.168.201.1", 
	            "comments": "This is a model PGM.  Do not delete.", 
	            "last_experiment": "", 
	            "ftppassword": "ionguest", 
	            "updateflag": false, 
	            "location": {
	                "name": "Home", 
	                "resource_uri": "/rundb/api/v1/location/1/", 
	                "defaultlocation": true, 
	                "comments": "", 
	                "id": 1
	            }, 
	            "last_init_date": "", 
	            "updateCommand": {}, 
	            "alarms": {}, 
	            "serial": null, 
	            "host_address": "", 
	            "type": "", 
	            "ftpusername": "ionguest", 
	            "resource_uri": "/rundb/api/v1/rig/default/"
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

