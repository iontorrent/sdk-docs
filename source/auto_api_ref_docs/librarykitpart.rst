Librarykitpart Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/librarykitpart/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/librarykitpart/schema/``


.. include:: ../manual_api_ref_docs/librarykitpart.rst

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

Request URL: ``http://mytorrentserver/rundb/api/v1/librarykitpart/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/librarykitpart/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	librarykitparts = ts_api_response["objects"]
	
	for librarykitpart in librarykitparts:
	    print librarykitpart
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 17, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/librarykitpart/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "barcode": "A25908", 
	            "id": 20140, 
	            "resource_uri": "/rundb/api/v1/librarykitpart/20140/", 
	            "kit": "/rundb/api/v1/kitinfo/20065/"
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

