Publisher Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/publisher/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/publisher/schema/``


.. include:: ../manual_api_ref_docs/publisher.rst

Fields table
------------

================ ==================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                            default nullable readonly blank unique type     
================ ==================================================== ======= ======== ======== ===== ====== ======== 
**name**         Unicode string data. Ex: "Hello World"               n/a     false    false    false true   string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**      Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**global_meta**  Unicode string data. Ex: "Hello World"               {}      false    false    true  false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**         A date & time as a string. Ex: "2010-11-10T03:07:43" n/a     false    false    false false  datetime 
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                       false    false    true  true   integer  
---------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================ ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/publisher/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/publisher/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	publishers = ts_api_response["objects"]
	
	for publisher in publishers:
	    print publisher
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/publisher/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "BED", 
	            "version": "1.0", 
	            "global_meta": {}, 
	            "date": "2017-03-13T19:18:24.000648+00:00", 
	            "path": "/results/publishers/BED", 
	            "id": 1, 
	            "resource_uri": "/rundb/api/v1/publisher/BED/"
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

