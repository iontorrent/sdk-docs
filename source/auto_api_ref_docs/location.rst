Location Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/location/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/location/schema/``


.. include:: ../manual_api_ref_docs/location.rst

Fields table
------------

=================== ====================================== ======= ======== ======== ===== ====== ======= 
field               help text                              default nullable readonly blank unique type    
=================== ====================================== ======= ======== ======== ===== ====== ======= 
**name**            Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**    Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultlocation** Only one location can be the default   false   false    false    true  false  boolean 
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**comments**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**              Integer data. Ex: 2673                         false    false    true  true   integer 
=================== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/location/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/location/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	locations = ts_api_response["objects"]
	
	for location in locations:
	    print location
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 1, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": [
	        {
	            "name": "Home", 
	            "resource_uri": "/rundb/api/v1/location/1/", 
	            "defaultlocation": true, 
	            "comments": "", 
	            "id": 1
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

