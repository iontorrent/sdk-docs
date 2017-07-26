Samplegrouptype_Cv Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/schema/``


.. include:: ../manual_api_ref_docs/samplegrouptype_cv.rst

Fields table
------------

======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                    help text                                                                                          default nullable readonly blank unique type    
======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 
**isIRCompatible**       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**sampleAnnotation_set** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**displayedName**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**iRValue**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**iRAnnotationType**     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**sampleSets**           Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                   Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**isActive**             Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
------------------------ -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**         Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
======================== ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/samplegrouptype_cv/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	samplegrouptype_cvs = ts_api_response["objects"]
	
	for samplegrouptype_cv in samplegrouptype_cvs:
	    print samplegrouptype_cv
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 7, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/samplegrouptype_cv/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isIRCompatible": true, 
	            "description": "", 
	            "sampleAnnotation_set": [
	                "/rundb/api/v1/sampleannotation_cv/1/", 
	                "/rundb/api/v1/sampleannotation_cv/2/"
	            ], 
	            "displayedName": "Sample_Control", 
	            "iRValue": "Paired_Sample|Sample_Control", 
	            "iRAnnotationType": "RelationshipType", 
	            "uid": "SAMPLEGROUP_CV_0001", 
	            "sampleSets": [], 
	            "id": 1, 
	            "isActive": true, 
	            "resource_uri": "/rundb/api/v1/samplegrouptype_cv/1/"
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

