.. _api_reference_location:

Location  Resource
==================

| Resource URL ``http://mytorrentserver/rundb/api/v1/location/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/location/schema/``
| 

.. include:: ../references_manual_extras/location.rst

Resource Fields
---------------

=================== ====================================== ======= ======== ======== ===== ====== ======= 
field               help text                              default nullable readonly blank unique type    
=================== ====================================== ======= ======== ======== ===== ====== ======= 
**name**            Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**    Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultlocation** Only one location can be the default   false   false    false    true  false  boolean 
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**comments**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**              Integer data. Ex: 2673                         false    false    true  true   integer 
=================== ====================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/location/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "Disabled", 
	            "resource_uri": "/rundb/api/v1/location/2/", 
	            "defaultlocation": false, 
	            "comments": "A location which will not be assigned to any File Servers so that Rigs assigned to this location will not be treated as valid Rigs when ionCrawler attempts to find new raw data directories. This is so that we do not have to delete a Rig from the Rigs table but still want to prevent new Experiments from appearing associated with the Rig.", 
	            "id": 2
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

