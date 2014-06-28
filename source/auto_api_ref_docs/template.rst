Template Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/template/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/template/schema/``


.. include:: ../manual_api_ref_docs/template.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**isofficial**   Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**comments**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**key**          Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/template/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/template/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	templates = ts_api_response["objects"]
	
	for template in templates:
	    print template
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 9, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/template/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isofficial": true, 
	            "name": "TF1.2(tA-tB30') Hyb extend", 
	            "sequence": "GTTTTAGGGTCCCCGGGGTTAAAAGGTTTCGAACACGATGTCGGAGACACGCAGGGATGAGATGG", 
	            "comments": "", 
	            "key": "ATCGT", 
	            "id": 7, 
	            "resource_uri": "/rundb/api/v1/template/7/"
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

