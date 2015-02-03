Obsoletereferencegenome Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/obsoletereferencegenome/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/obsoletereferencegenome/schema/``


.. include:: ../manual_api_ref_docs/obsoletereferencegenome.rst

Fields table
------------

================== ==================================================== ================================ ======== ======== ===== ====== ======== 
field              help text                                            default                          nullable readonly blank unique type     
================== ==================================================== ================================ ======== ======== ===== ====== ======== 
**status**         Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**reference_path** Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**name**           Unicode string data. Ex: "Hello World"               n/a                              false    false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**short_name**     Unicode string data. Ex: "Hello World"               n/a                              false    false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**index_version**  Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**notes**          Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**enabled**        Boolean data. Ex: True                               true                             false    false    true  false  boolean  
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**species**        Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**identity_hash**  Unicode string data. Ex: "Hello World"               None                             true     false    false false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**source**         Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**version**        Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**celery_task_id** Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**date**           A date & time as a string. Ex: "2010-11-10T03:07:43" 2015-02-03T02:29:30.000916+00:00 false    false    false false  datetime 
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**verbose_error**  Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                                                false    false    true  true   integer  
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a                              false    true     false false  string   
================== ==================================================== ================================ ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/obsoletereferencegenome/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/obsoletereferencegenome/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	obsoletereferencegenomes = ts_api_response["objects"]
	
	for obsoletereferencegenome in obsoletereferencegenomes:
	    print obsoletereferencegenome
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 0, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": []
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

