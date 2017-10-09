.. _api_reference_compositedatamanagement:

Composite Data Management  Resource
===================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/compositedatamanagement/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/compositedatamanagement/schema/``
| 

.. include:: ../references_manual_extras/compositedatamanagement.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	            "misc_diskspace": 0, 
	            "expName": "S5-540_WholeTranscriptomeRNA", 
	            "basecall_state": "Local", 
	            "in_process": false, 
	            "misc_state": "Deleted", 
	            "timeStamp": "2017-07-22T13:15:56.000197+00:00", 
	            "basecall_keep": false, 
	            "misc_keep": null, 
	            "output_keep": false, 
	            "basecall_diskspace": 175694.536458969, 
	            "resultsName": "Auto_S5-540_WholeTranscriptomeRNA_91", 
	            "output_state": "Local", 
	            "sigproc_state": "Local", 
	            "sigproc_keep": false, 
	            "sigproc_diskspace": 0.0160617828369141, 
	            "diskusage": 229301, 
	            "resource_uri": "/rundb/api/v1/compositedatamanagement/3/", 
	            "expDir": "/results/S5_DemoData/S5-540_WholeTranscriptomeRNA", 
	            "id": 3, 
	            "output_diskspace": 53607.1456193924
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

