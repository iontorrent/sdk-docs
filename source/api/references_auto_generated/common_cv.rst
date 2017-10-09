.. _api_reference_common_cv:

Common Cv  Resource
===================

| Resource URL ``http://mytorrentserver/rundb/api/v1/common_cv/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/common_cv/schema/``
| 

.. include:: ../references_manual_extras/common_cv.rst

Resource Fields
---------------

============================= ====================================== ======= ======== ======== ===== ====== ======= 
field                         help text                              default nullable readonly blank unique type    
============================= ====================================== ======= ======== ======== ===== ====== ======= 
**displayedValue**            Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequencing_instrumentType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**               Unicode string data. Ex: "Hello World" n/a     true     false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**                Unicode string data. Ex: "Hello World"         true     false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**value**                     Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**cv_type**                   Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isVisible**                 Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                       Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                         false    false    true  true   integer 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**                  Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isDefault**                 Boolean data. Ex: True                 true    false    false    true  false  boolean 
============================= ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 10, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/common_cv/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "displayedValue": "Ion PGM Hi-Q Chef for STR", 
	            "sequencing_instrumentType": "", 
	            "description": "Use Ion Chef script protocol optimized for HID", 
	            "categories": "hidSamplePrep", 
	            "value": "anneal62no10xab", 
	            "samplePrep_instrumentType": "IC", 
	            "cv_type": "samplePrepProtocol", 
	            "isVisible": true, 
	            "uid": "CV0001", 
	            "resource_uri": "/rundb/api/v1/common_cv/1/", 
	            "id": 1, 
	            "isActive": true, 
	            "isDefault": false
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

