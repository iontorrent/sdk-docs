Fileserver Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/fileserver/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/fileserver/schema/``


.. include:: ../manual_api_ref_docs/fileserver.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**percentfull**  Floating point numeric data. Ex: 26.73 0.0     true     false    false false  float   
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**filesPrefix**  Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**comments**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/fileserver/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/fileserver/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	fileservers = ts_api_response["objects"]
	
	for fileserver in fileservers:
	    print fileserver
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/fileserver/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "percentfull": 89.7534648330382, 
	            "name": "gs1-nfs", 
	            "filesPrefix": "/ion-data/results/", 
	            "comments": "gs1-nfs:/gs1/ion-data", 
	            "id": 2, 
	            "resource_uri": "/rundb/api/v1/fileserver/2/"
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

