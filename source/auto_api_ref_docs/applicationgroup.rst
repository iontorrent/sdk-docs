Applicationgroup Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/applicationgroup/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/applicationgroup/schema/``


.. include:: ../manual_api_ref_docs/applicationgroup.rst

Fields table
------------

================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                                          default nullable readonly blank unique type    
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 
**name**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applications** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    false false  related 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**     Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
---------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
================ ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/applicationgroup/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/applicationgroup/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	applicationgroups = ts_api_response["objects"]
	
	for applicationgroup in applicationgroups:
	    print applicationgroup
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 5, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/applicationgroup/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "DNA", 
	            "description": "DNA", 
	            "applications": [
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/", 
	                        "/rundb/api/v1/applicationgroup/3/", 
	                        "/rundb/api/v1/applicationgroup/4/"
	                    ], 
	                    "description": "Generic Sequencing", 
	                    "nucleotideType": "", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "runType": "GENS", 
	                    "id": 1, 
	                    "alternate_name": "Other", 
	                    "resource_uri": "/rundb/api/v1/runtype/1/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/"
	                    ], 
	                    "description": "AmpliSeq DNA", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "runType": "AMPS", 
	                    "id": 2, 
	                    "alternate_name": "AmpliSeq DNA", 
	                    "resource_uri": "/rundb/api/v1/runtype/2/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/"
	                    ], 
	                    "description": "TargetSeq", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "runType": "TARS", 
	                    "id": 3, 
	                    "alternate_name": "TargetSeq", 
	                    "resource_uri": "/rundb/api/v1/runtype/3/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/", 
	                        "/rundb/api/v1/applicationgroup/4/"
	                    ], 
	                    "description": "Whole Genome", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "runType": "WGNM", 
	                    "id": 4, 
	                    "alternate_name": "Whole Genome", 
	                    "resource_uri": "/rundb/api/v1/runtype/4/"
	                }, 
	                {
	                    "applicationGroups": [
	                        "/rundb/api/v1/applicationgroup/1/"
	                    ], 
	                    "description": "AmpliSeq Exome", 
	                    "nucleotideType": "dna", 
	                    "barcode": "", 
	                    "meta": {}, 
	                    "runType": "AMPS_EXOME", 
	                    "id": 7, 
	                    "alternate_name": "AmpliSeq Exome", 
	                    "resource_uri": "/rundb/api/v1/runtype/7/"
	                }
	            ], 
	            "uid": "APPLGROUP_0001", 
	            "id": 1, 
	            "isActive": true, 
	            "resource_uri": "/rundb/api/v1/applicationgroup/1/"
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

