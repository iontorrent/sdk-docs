.. _api_reference_qctype:

Qc Type  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/qctype/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/qctype/schema/``
| 

.. include:: ../references_manual_extras/qctype.rst

Resource Fields
---------------

==================== ====================================== ======= ======== ======== ===== ====== ======= 
field                help text                              default nullable readonly blank unique type    
==================== ====================================== ======= ======== ======== ===== ====== ======= 
**description**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**minThreshold**     Integer data. Ex: 2673                 0       false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**maxThreshold**     Integer data. Ex: 2673                 100     false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultThreshold** Integer data. Ex: 2673                 0       false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**qcName**           Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**               Integer data. Ex: 2673                         false    false    true  true   integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**     Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
==================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 3, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/qctype/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "description": "", 
	            "minThreshold": 0, 
	            "maxThreshold": 100, 
	            "defaultThreshold": 30, 
	            "qcName": "Bead Loading (%)", 
	            "id": 1, 
	            "resource_uri": "/rundb/api/v1/qctype/1/"
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

