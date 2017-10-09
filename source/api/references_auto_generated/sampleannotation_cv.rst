.. _api_reference_sampleannotation_cv:

Sample Annotation Cv  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleannotation_cv/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleannotation_cv/schema/``
| 

.. include:: ../references_manual_extras/sampleannotation_cv.rst

Resource Fields
---------------

====================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                  help text                                                                      default nullable readonly blank unique type    
====================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**annotationType**     Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**uid**                Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isIRCompatible**     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sampleGroupType_CV** A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**value**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**iRValue**            Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**iRAnnotationType**   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                 Integer data. Ex: 2673                                                                 false    false    true  true   integer 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isActive**           Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
====================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 43, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sampleannotation_cv/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "annotationType": "cancerType", 
	            "uid": "SAMPLEANNOTATE_CV_0016", 
	            "isIRCompatible": true, 
	            "sampleGroupType_CV": null, 
	            "value": "Esophageal Cancer", 
	            "iRValue": "Esophageal Cancer", 
	            "iRAnnotationType": "CancerType", 
	            "id": 16, 
	            "isActive": true, 
	            "resource_uri": "/rundb/api/v1/sampleannotation_cv/16/"
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

