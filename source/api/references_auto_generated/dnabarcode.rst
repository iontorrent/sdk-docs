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
**active**         Boolean data. Ex: True                 true    false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**adapter**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**annotation**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**end_adapter**    Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**end_sequence**   Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**             Integer data. Ex: 2673                         false    false    true  true   integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id_str**         Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**index**          Integer data. Ex: 2673                 n/a     false    false    false false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**is_end_barcode** Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**length**         Integer data. Ex: 2673                 0       false    false    true  false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**           Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**   Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_cutoff**   Floating point numeric data. Ex: 26.73 0       false    false    false false  float   
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**score_mode**     Integer data. Ex: 2673                 0       false    false    true  false  integer 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**sequence**       Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**system**         Boolean data. Ex: True                 false   false    false    true  false  boolean 
------------------ -------------------------------------- ------- -------- -------- ----- ------ ------- 
**type**           Unicode string data. Ex: "Hello World"         false    false    true  false  string  
================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/dnabarcode/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 2090
	    },
	    "objects": [
	        {
	            "active": true,
	            "adapter": "GGTGAT",
	            "annotation": "IonCode_0196--IonOmega_444A",
	            "end_adapter": "CTGAG",
	            "end_sequence": "TATTCACAGCGC",
	            "id": 4043,
	            "id_str": "IonDual_H12_0196",
	            "index": 96,
	            "is_end_barcode": false,
	            "length": 12,
	            "name": "Ion Dual Barcode Kit 1-96",
	            "resource_uri": "/rundb/api/v1/dnabarcode/4043/",
	            "score_cutoff": 0,
	            "score_mode": 0,
	            "sequence": "CTAACAATTCAC",
	            "system": true,
	            "type": ""
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

