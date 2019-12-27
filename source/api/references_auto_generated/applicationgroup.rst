.. _api_reference_applicationgroup:

Application Group  Resource
===========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/applicationgroup/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/applicationgroup/schema/``
| 

.. include:: ../references_manual_extras/applicationgroup.rst

Resource Fields
---------------

================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                                          default nullable readonly blank unique type    
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
**applications** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/applicationgroup/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 12
	    },
	    "objects": [
	        {
	            "applications": [
	                {
	                    "alternate_name": "AmpliSeq HD - Fusions",
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/12/"
	                    ],
	                    "barcode": "",
	                    "description": "AmpliSeq HD - Fusions",
	                    "id": 13,
	                    "isActive": true,
	                    "meta": {},
	                    "nucleotideType": "rna",
	                    "resource_uri": "/rundb/api/v1/runtype/13/",
	                    "runType": "AMPS_HD_RNA"
	                }
	            ],
	            "description": "Fusions",
	            "id": 12,
	            "isActive": true,
	            "name": "Fusions",
	            "resource_uri": "/rundb/api/v1/applicationgroup/12/",
	            "uid": "APPLGROUP_0012"
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

