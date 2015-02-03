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
	        "total_count": 11, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/template/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isofficial": false, 
	            "name": "DxTF-1", 
	            "sequence": "GAATAATCCAGCCCGCCAGGCATGGAAGAGCGTCGTAAAGTATTGCAGGTTCAGGCGGCGGAAAGCGTGATTGACTACTGGCAAATAAAGTACGTTCCACCTTTGACACCATTTTCCGTAGTGAACTGACGCTGCCAAACGCCGACCGCG", 
	            "comments": "Disabled J.Sabina, 12/7/2014; Same as TF_1.", 
	            "key": "ATCG", 
	            "id": 10, 
	            "resource_uri": "/rundb/api/v1/template/10/"
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

