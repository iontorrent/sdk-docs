.. _api_reference_dnabarcode:

Dna Barcode Resource
====================

| Resource URL ``http://mytorrentserver/rundb/api/v1/dnabarcode/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/dnabarcode/schema/``
| 

.. include:: ../references_manual_extras/dnabarcode.rst

Resource Fields
---------------

================== ====================================== ======= ======== ======== ===== ====== ======= 
field              help text                              default nullable readonly blank unique type    
================== ====================================== ======= ======== ======== ===== ====== ======= 
**index**          Integer data. Ex: 2673                 n/a     false    false    false false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**end_adapter**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**           Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_cutoff**   Floating point numeric data. Ex: 26.73 0       false    false    false false  float   
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**       Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**is_end_barcode** Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**adapter**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**system**         Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**             Integer data. Ex: 2673                         false    false    true  true   integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**length**         Integer data. Ex: 2673                 0       false    false    true  false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id_str**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**active**         Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**end_sequence**   Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_mode**     Integer data. Ex: 2673                 0       false    false    true  false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**type**           Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**annotation**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**   Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2090, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/dnabarcode/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "index": 1, 
	            "end_adapter": "", 
	            "name": "MuSeek_5prime_tag", 
	            "score_cutoff": 2, 
	            "sequence": "TTCA", 
	            "is_end_barcode": false, 
	            "adapter": "", 
	            "system": false, 
	            "id": 1, 
	            "length": 4, 
	            "id_str": "MuSeek_5prime_tag_001", 
	            "active": true, 
	            "end_sequence": "", 
	            "score_mode": 1, 
	            "type": "none", 
	            "annotation": "", 
	            "resource_uri": "/rundb/api/v1/dnabarcode/1/"
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

