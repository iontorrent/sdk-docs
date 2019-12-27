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
**iRAnnotationType**   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**iRValue**            Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                 Integer data. Ex: 2673                                                                 false    false    true  true   integer 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isActive**           Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isIRCompatible**     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sampleGroupType_CV** A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related 
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**uid**                Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string  
---------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**value**              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
====================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/sampleannotation_cv/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 90
	    },
	    "objects": [
	        {
	            "annotationType": "16s_markers",
	            "iRAnnotationType": "16S_Markers",
	            "iRValue": "Target Species",
	            "id": 90,
	            "isActive": true,
	            "isIRCompatible": true,
	            "resource_uri": "/rundb/api/v1/sampleannotation_cv/90/",
	            "sampleGroupType_CV": null,
	            "uid": "SAMPLEANNOTATE_CV_0090",
	            "value": "Target Species"
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

