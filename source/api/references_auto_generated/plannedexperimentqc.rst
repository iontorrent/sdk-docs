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
**id**                Integer data. Ex: 2673                                                                 false    false    true  true   integer 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**plannedExperiment** A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**qcType**            A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**threshold**         Integer data. Ex: 2673                                                         0       false    false    false false  integer 
===================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plannedexperimentqc/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 390
	    },
	    "objects": [
	        {
	            "id": 489,
	            "plannedExperiment": "/rundb/api/v1/plannedexperiment/170/",
	            "qcType": {
	                "defaultThreshold": 30,
	                "description": "",
	                "id": 3,
	                "maxThreshold": 100,
	                "minThreshold": 0,
	                "qcName": "Usable Sequence (%)",
	                "resource_uri": "/rundb/api/v1/qctype/3/"
	            },
	            "resource_uri": "/rundb/api/v1/plannedexperimentqc/489/",
	            "threshold": 30
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

