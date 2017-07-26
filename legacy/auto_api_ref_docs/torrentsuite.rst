Torrentsuite Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/torrentsuite/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/torrentsuite/schema/``


.. include:: ../manual_api_ref_docs/torrentsuite.rst

Fields table
------------

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

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/torrentsuite/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/torrentsuite/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	torrentsuites = ts_api_response["objects"]
	
	for torrentsuite in torrentsuites:
	    print torrentsuite
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta_version": "5.4.0.RC2", 
	    "locked": false, 
	    "logs": false, 
	    "versions": {
	        "ion-docs": "5.2.12", 
	        "ion-gpu": "5.4.0-1", 
	        "ion-pipeline": "5.4.4-1", 
	        "ion-torrentpy": "5.4.2-1", 
	        "ion-tsconfig": "5.4.2-1", 
	        "ion-chefupdates": "5.4.0", 
	        "ion-rsmts": "5.4.0-1", 
	        "ion-sampledata": "1.2.0-1", 
	        "ion-publishers": "5.4.1-1", 
	        "ion-dbreports": "5.4.15-1", 
	        "ion-analysis": "5.4.3-1", 
	        "ion-onetouchupdater": "5.0.2-1", 
	        "ion-torrentr": "5.4.2-1", 
	        "ion-plugins": "5.4.7-1", 
	        "ion-referencelibrary": "2.2.0"
	    }
	}

Allowed HTTP methods
--------------------


