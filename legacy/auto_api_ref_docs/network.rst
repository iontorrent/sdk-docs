Network Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/network/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/network/schema/``


.. include:: ../manual_api_ref_docs/network.rst

Fields table
------------

=============== ====================================== ======= ======== ======== ===== ====== ======= 
field           help text                              default nullable readonly blank unique type    
=============== ====================================== ======= ======== ======== ===== ====== ======= 
**eth_device**  Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**external_ip** Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**internal_ip** Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**route**       Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
=============== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/network/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/network/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	networks = ts_api_response["objects"]
	
	for network in networks:
	    print network
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "eth_device": true, 
	    "external_ip": "12.27.71.34", 
	    "internal_ip": "192.168.122.135", 
	    "route": true
	}

Allowed HTTP methods
--------------------


