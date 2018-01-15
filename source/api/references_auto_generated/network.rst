.. _api_reference_network:

Network Resource
================

| Resource URL ``http://mytorrentserver/rundb/api/v1/network/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/network/schema/``
| 

.. include:: ../references_manual_extras/network.rst

Resource Fields
---------------

=============== ====================================== ======= ======== ======== ===== ====== ======= 
field           help text                              default nullable readonly blank unique type    
=============== ====================================== ======= ======== ======== ===== ====== ======= 
**eth_device**  Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**external_ip** Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**internal_ip** Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
--------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**route**       Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
=============== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "eth_device": true, 
	    "external_ip": "12.27.71.34", 
	    "internal_ip": "10.45.2.119", 
	    "route": true
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

None

