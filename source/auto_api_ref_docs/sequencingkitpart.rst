Sequencingkitpart Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitpart/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitpart/schema/``


.. include:: ../manual_api_ref_docs/sequencingkitpart.rst

Fields table
------------

================ ============================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                      default nullable readonly blank unique type    
================ ============================================================================== ======= ======== ======== ===== ====== ======= 
**barcode**      Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**kit**          A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
================ ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/sequencingkitpart/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/sequencingkitpart/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	sequencingkitparts = ts_api_response["objects"]
	
	for sequencingkitpart in sequencingkitparts:
	    print sequencingkitpart
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 64, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sequencingkitpart/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "barcode": "A25592", 
	            "id": 20132, 
	            "resource_uri": "/rundb/api/v1/sequencingkitpart/20132/", 
	            "kit": "/rundb/api/v1/kitinfo/20063/"
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

