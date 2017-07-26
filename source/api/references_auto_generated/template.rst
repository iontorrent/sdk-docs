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

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/template/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isofficial": true, 
	            "name": "TF_1", 
	            "sequence": "GAATAATCCAGCCCGCCAGGCATGGAAGAGCGTCGTAAAGTATTGCAGGTTCAGGCGGCGGAAAGCGTGATTGACTACTGGCAAATAAAGTACGTTCCACCTTTGACACCATTTTCCGTAGTGAACTGACGCTGCCAAACGCCGACCGCG", 
	            "comments": " ", 
	            "key": "ATCG", 
	            "id": 5, 
	            "resource_uri": "/rundb/api/v1/template/5/"
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

