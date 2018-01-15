.. _api_reference_torrentsuite:

Torrent Suite  Resource
=======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/torrentsuite/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/torrentsuite/schema/``
| 

.. include:: ../references_manual_extras/torrentsuite.rst

Resource Fields
---------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**meta_version** Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**locked**       Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**logs**         Unicode string data. Ex: "Hello World" n/a     true     true     true  false  boolean 
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**versions**     Unicode string data. Ex: "Hello World" n/a     true     true     true  false  string  
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta_version": "5.8.0", 
	    "locked": false, 
	    "logs": false, 
	    "versions": {
	        "ion-docs": "5.6.3", 
	        "ion-gpu": "5.8.1-1", 
	        "ion-torrentpy": "5.8.17-1", 
	        "ion-tsconfig": "5.8.4-1", 
	        "ion-dbreports": "5.8.53-1", 
	        "ion-rsmts": "5.6.1-1", 
	        "ion-sampledata": "1.2.0-1", 
	        "ion-publishers": "5.8.1-1", 
	        "ion-pipeline": "5.8.7-1", 
	        "ion-analysis": "5.8.17-1", 
	        "ion-torrentr": "5.8.17-1", 
	        "ion-referencelibrary": "2.2.0"
	    }
	}

Allowed list HTTP methods
-------------------------

- GET
- PUT


Allowed detail HTTP methods
---------------------------

None

