.. _api_reference_template:

Template  Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/template/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/template/schema/``
| 

.. include:: ../references_manual_extras/template.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**comments**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**isofficial**   Boolean data. Ex: True                 true    false    false    true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**key**          Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/template/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 6
	    },
	    "objects": [
	        {
	            "comments": " ",
	            "id": 6,
	            "isofficial": true,
	            "key": "ATCG",
	            "name": "TF_1",
	            "resource_uri": "/rundb/api/v1/template/6/",
	            "sequence": "GAATAATCCAGCCCGCCAGGCATGGAAGAGCGTCGTAAAGTATTGCAGGTTCAGGCGGCGGAAAGCGTGATTGACTACTGGCAAATAAAGTACGTTCCACCTTTGACACCATTTTCCGTAGTGAACTGACGCTGCCAAACGCCGACCGCG"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

