Contentupload Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/contentupload/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/contentupload/schema/``


.. include:: ../manual_api_ref_docs/contentupload.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**status**       Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**meta**         Unicode string data. Ex: "Hello World" {}      false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**file_path**    Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/contentupload/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/contentupload/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	contentuploads = ts_api_response["objects"]
	
	for contentupload in contentuploads:
	    print contentupload
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 106, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/contentupload/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Successfully Completed", 
	            "meta": {
	                "reference": "hg19", 
	                "hotspot": false
	            }, 
	            "file_path": "/results/uploads/BED/88/IAD34929_Amplicons.bed", 
	            "resource_uri": "/rundb/api/v1/contentupload/88/", 
	            "id": 88
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

