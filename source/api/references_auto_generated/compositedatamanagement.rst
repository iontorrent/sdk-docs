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
**basecall_keep**  Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**basecall_state** Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**      Integer data. Ex: 2673                               n/a     true     false    false false  integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expDir**         Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**        Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**in_process**     Boolean data. Ex: True                               false   false    false    false false  boolean  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**misc_keep**      Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**misc_state**     Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**output_keep**    Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**output_state**   Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**    Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sigproc_keep**   Unicode string data. Ex: "Hello World"               n/a     true     true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sigproc_state**  Unicode string data. Ex: "Hello World"               Unknown false    true     false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**      A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/compositedatamanagement/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 6
	    },
	    "objects": [
	        {
	            "basecall_diskspace": 5.99083232879639,
	            "basecall_keep": false,
	            "basecall_state": "Local",
	            "diskusage": 393,
	            "expDir": "/results/PGM_test/cropped_CB1-42",
	            "expName": "R_2011_04_07_12_44_38_user_CB1-42-r9723-314wfa-tl",
	            "id": 6,
	            "in_process": false,
	            "misc_diskspace": 0,
	            "misc_keep": null,
	            "misc_state": "Deleted",
	            "output_diskspace": 4.13351440429688,
	            "output_keep": false,
	            "output_state": "Error",
	            "resource_uri": "/rundb/api/v1/compositedatamanagement/6/",
	            "resultsName": "Auto_user_CB1-42-r9723-314wfa-tl_94",
	            "sigproc_diskspace": 384.02961730957,
	            "sigproc_keep": false,
	            "sigproc_state": "Local",
	            "timeStamp": "2017-08-23T21:46:24.000391+00:00"
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

