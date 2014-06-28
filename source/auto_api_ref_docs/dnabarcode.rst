Dnabarcode Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/dnabarcode/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/dnabarcode/schema/``


.. include:: ../manual_api_ref_docs/dnabarcode.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**index**        Integer data. Ex: 2673                 n/a     false    false    false false  integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_cutoff** Floating point numeric data. Ex: 26.73 0       false    false    false false  float   
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**floworder**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**adapter**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**length**       Integer data. Ex: 2673                 0       false    false    true  false  integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id_str**       Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_mode**   Integer data. Ex: 2673                 0       false    false    true  false  integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**type**         Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**annotation**   Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/dnabarcode/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/dnabarcode/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	dnabarcodes = ts_api_response["objects"]
	
	for dnabarcode in dnabarcodes:
	    print dnabarcode
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 9387, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/dnabarcode/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "index": 9, 
	            "name": "IonXpress", 
	            "score_cutoff": 2.0, 
	            "sequence": "TGAGCGGAAC", 
	            "floworder": "", 
	            "adapter": "GAT", 
	            "id": 761, 
	            "length": 10, 
	            "id_str": "IonXpress_009", 
	            "score_mode": 1, 
	            "type": "", 
	            "annotation": "", 
	            "resource_uri": "/rundb/api/v1/dnabarcode/761/"
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

