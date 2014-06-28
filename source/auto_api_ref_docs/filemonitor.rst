Filemonitor Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/filemonitor/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/filemonitor/schema/``


.. include:: ../manual_api_ref_docs/filemonitor.rst

Fields table
------------

================== ==================================================== ======= ======== ======== ===== ====== ======== 
field              help text                                            default nullable readonly blank unique type     
================== ==================================================== ======= ======== ======== ===== ====== ======== 
**status**         Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**updated**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**created**        A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**            Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**md5sum**         Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**celery_task_id** Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**local_dir**      Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**progress**       Unicode string data. Ex: "Hello World"               0       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**size**           Unicode string data. Ex: "Hello World"               None    true     false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tags**           Unicode string data. Ex: "Hello World"                       false    false    false false  string   
------------------ ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/filemonitor/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/filemonitor/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	filemonitors = ts_api_response["objects"]
	
	for filemonitor in filemonitors:
	    print filemonitor
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 8, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/filemonitor/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Complete", 
	            "updated": "2014-05-08T19:25:27.000843+00:00", 
	            "name": "AmpliSeqExome.20131001.Results.zip", 
	            "created": "2014-05-08T19:25:01.000513+00:00", 
	            "url": "https://ampliseq.com/ws/tmpldesign/14035495/download/results", 
	            "md5sum": null, 
	            "celery_task_id": "63a36c6f-ccc2-4ce3-8539-18335039f128", 
	            "local_dir": "/tmp/tmpubvTKY", 
	            "progress": "24174499", 
	            "size": "24174499", 
	            "id": 9, 
	            "tags": "ampliseq_template", 
	            "resource_uri": "/rundb/api/v1/filemonitor/9/"
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

