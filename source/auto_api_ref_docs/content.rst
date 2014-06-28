Content Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/content/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/content/schema/``


.. include:: ../manual_api_ref_docs/content.rst

Fields table
------------

================= ============================================================================== ======= ======== ======== ===== ====== ======= 
field             help text                                                                      default nullable readonly blank unique type    
================= ============================================================================== ======= ======== ======== ===== ====== ======= 
**publisher**     A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**contentupload** A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**meta**          Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**file**          Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**path**          Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**            Integer data. Ex: 2673                                                                 false    false    true  true   integer 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**  Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
================= ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/content/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/content/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	contents = ts_api_response["objects"]
	
	for content in contents:
	    print content
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 72, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/content/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "publisher": "/rundb/api/v1/publisher/BED/", 
	            "contentupload": "/rundb/api/v1/contentupload/16/", 
	            "meta": {
	                "is_ampliseq": false, 
	                "hotspot_bed": null, 
	                "reference": "hg19", 
	                "primary_bed": "/results/uploads/BED/16/testPanel30.bed", 
	                "hotspot": false
	            }, 
	            "file": "/results/uploads/BED/16/hg19/unmerged/plain/testPanel30.bed", 
	            "path": "/hg19/unmerged/plain/testPanel30.bed", 
	            "id": 53, 
	            "resource_uri": "/rundb/api/v1/content/53/"
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

