Plannedexperimentqc Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentqc/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentqc/schema/``


.. include:: ../manual_api_ref_docs/plannedexperimentqc.rst

Fields table
------------

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

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/plannedexperimentqc/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/plannedexperimentqc/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	plannedexperimentqcs = ts_api_response["objects"]
	
	for plannedexperimentqc in plannedexperimentqcs:
	    print plannedexperimentqc
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 28134, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plannedexperimentqc/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "threshold": 30, 
	            "plannedExperiment": "/rundb/api/v1/plannedexperiment/89091/", 
	            "id": 259834, 
	            "qcType": {
	                "description": "", 
	                "minThreshold": 0, 
	                "maxThreshold": 100, 
	                "defaultThreshold": 30, 
	                "qcName": "Usable Sequence (%)", 
	                "id": 3, 
	                "resource_uri": "/rundb/api/v1/qctype/3/"
	            }, 
	            "resource_uri": "/rundb/api/v1/plannedexperimentqc/259834/"
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

