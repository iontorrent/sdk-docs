Compositedatamanagement Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/compositedatamanagement/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/compositedatamanagement/schema/``


.. include:: ../manual_api_ref_docs/compositedatamanagement.rst

Fields table
------------

================== ==================================================== ======= ======== ======== ===== ====== ======== 
field              help text                                            default nullable readonly blank unique type     
================== ==================================================== ======= ======== ======== ===== ====== ======== 
**basecall_state** Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**in_process**     Boolean data. Ex: True                               false   false    false    false false  boolean  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**misc_state**     Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**basecall_keep**  Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**misc_keep**      Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**output_keep**    Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**        Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**    Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**output_state**   Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sigproc_state**  Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sigproc_keep**   Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**      Integer data. Ex: 2673                               n/a     true     false    false false  integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expDir**         Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/compositedatamanagement/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/compositedatamanagement/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	compositedatamanagements = ts_api_response["objects"]
	
	for compositedatamanagement in compositedatamanagements:
	    print compositedatamanagement
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositedatamanagement/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "misc_diskspace": 135791.989539146, 
	            "expName": "S5-540_AmpliSeqExome", 
	            "basecall_state": "Local", 
	            "in_process": false, 
	            "misc_state": "Local", 
	            "timeStamp": "2017-03-18T06:39:37.000203+00:00", 
	            "basecall_keep": false, 
	            "misc_keep": false, 
	            "output_keep": false, 
	            "basecall_diskspace": 175688.613199234, 
	            "resultsName": "S5-540_AmpliSeqExome", 
	            "output_state": "Local", 
	            "sigproc_state": "Local", 
	            "sigproc_keep": true, 
	            "sigproc_diskspace": 0.0158777236938477, 
	            "diskusage": 371907, 
	            "resource_uri": "/rundb/api/v1/compositedatamanagement/5/", 
	            "expDir": "/results/S5_DemoData/S5-540_AmpliSeqExome", 
	            "id": 5, 
	            "output_diskspace": 60428.8543195724
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

