.. _api_reference_plannedexperimentqc:

Planned Experiment Qc  Resource
===============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plannedexperimentqc/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plannedexperimentqc/schema/``
| 

.. include:: ../references_manual_extras/plannedexperimentqc.rst

Resource Fields
---------------

===================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                 help text                                                                      default nullable readonly blank unique type    
===================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**threshold**         Integer data. Ex: 2673                                                         0       false    false    false false  integer 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**plannedExperiment** A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                Integer data. Ex: 2673                                                                 false    false    true  true   integer 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**qcType**            A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
===================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 255, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperimentqc/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "threshold": 30, 
	            "plannedExperiment": "/rundb/api/v1/plannedexperiment/44/", 
	            "id": 130, 
	            "qcType": {
	                "description": "", 
	                "minThreshold": 0, 
	                "maxThreshold": 100, 
	                "defaultThreshold": 30, 
	                "qcName": "Bead Loading (%)", 
	                "id": 1, 
	                "resource_uri": "/rundb/api/v1/qctype/1/"
	            }, 
	            "resource_uri": "/rundb/api/v1/plannedexperimentqc/130/"
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

