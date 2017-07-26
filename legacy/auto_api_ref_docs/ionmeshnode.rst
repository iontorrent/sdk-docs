Ionmeshnode Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/ionmeshnode/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/ionmeshnode/schema/``


.. include:: ../manual_api_ref_docs/ionmeshnode.rst

Fields table
------------

==================== ====================================== ======= ======== ======== ===== ====== ======= 
field                help text                              default nullable readonly blank unique type    
==================== ====================================== ======= ======== ======== ===== ====== ======= 
**share_plans**      Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**share_monitoring** Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**hostname**         Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**share_data**       Boolean data. Ex: True                 true    false    false    true  false  boolean 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**               Integer data. Ex: 2673                         false    false    true  true   integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**     Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
==================== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/ionmeshnode/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/ionmeshnode/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	ionmeshnodes = ts_api_response["objects"]
	
	for ionmeshnode in ionmeshnodes:
	    print ionmeshnode
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 0, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": []
	}

Allowed HTTP methods
--------------------

- patch
- get
- delete

