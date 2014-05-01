Compositeexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/schema/``


.. include:: ../manual_api_ref_docs/compositeexperiment.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**ftpStatus**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options** Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**            Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**           Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**repResult**       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/compositeexperiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	compositeexperiments = ts_api_response["objects"]
	
	for compositeexperiment in compositeexperiments:
	    print compositeexperiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 16616, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipDescription": "PI", 
	            "chipType": "P1.1.17", 
	            "results": [], 
	            "sample": "", 
	            "runMode": "single", 
	            "storage_options": "D", 
	            "repResult": null, 
	            "id": 22493, 
	            "archived": false, 
	            "sampleSetName": "", 
	            "star": false, 
	            "resultDate": "2014-05-01T20:22:50.000059+00:00", 
	            "flows": 2, 
	            "plan": {
	                "runType": "GENS", 
	                "id": 104225, 
	                "resource_uri": ""
	            }, 
	            "date": "2014-05-01T23:02:42+00:00", 
	            "ftpStatus": "0", 
	            "notes": "", 
	            "chipInstrumentType": "proton", 
	            "pgmName": "FDR", 
	            "keep": false, 
	            "expName": "R_2014_05_01_16_00_58_user_FDR-92", 
	            "resource_uri": "/rundb/api/v1/compositeexperiment/22493/"
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

