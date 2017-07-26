.. _api_reference_sampleattributedatatype:

Sample Attribute Data Type  Resource
====================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleattributedatatype/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleattributedatatype/schema/``
| 

.. include:: ../references_manual_extras/sampleattributedatatype.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**dataType**     Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sampleattributedatatype/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "dataType": "Text", 
	            "resource_uri": "/rundb/api/v1/sampleattributedatatype/1/", 
	            "description": "Up to 1024 characters", 
	            "isActive": true, 
	            "id": 1
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

