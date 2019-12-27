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
	    "locked": false,
	    "logs": false,
	    "meta_version": "5.12.1",
	    "versions": {
	        "ion-analysis": "5.12.27-1",
	        "ion-chefupdates": "5.12.3",
	        "ion-dbreports": "5.12.60-1",
	        "ion-docs": "5.12.1",
	        "ion-gpu": "5.12.1-1",
	        "ion-onetouchupdater": "5.0.2-1",
	        "ion-pipeline": "5.12.17-1",
	        "ion-plugins": "5.12.15-1",
	        "ion-publishers": "5.12.1-1",
	        "ion-referencelibrary": "2.2.0",
	        "ion-rsmts": "5.12.5-1",
	        "ion-sampledata": "1.2.0-1",
	        "ion-torrentpy": "5.12.21-1",
	        "ion-torrentr": "5.12.23-1",
	        "ion-tsconfig": "5.12.23-1"
	    }
	}

Allowed list HTTP methods
-------------------------

- GET
- PUT


Allowed detail HTTP methods
---------------------------

None

