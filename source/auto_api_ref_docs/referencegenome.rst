Referencegenome Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/referencegenome/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/referencegenome/schema/``


.. include:: ../manual_api_ref_docs/referencegenome.rst

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
**date**           A date & time as a string. Ex: "2010-11-10T03:07:43" 2015-02-03T02:30:36.000120+00:00 false    false    false false  datetime 
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**verbose_error**  Unicode string data. Ex: "Hello World"                                                false    false    true  false  string   
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**id**             Integer data. Ex: 2673                                                                false    false    true  true   integer  
------------------ ---------------------------------------------------- -------------------------------- -------- -------- ----- ------ -------- 
**resource_uri**   Unicode string data. Ex: "Hello World"               n/a                              false    true     false false  string   
================== ==================================================== ================================ ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/referencegenome/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/referencegenome/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	referencegenomes = ts_api_response["objects"]
	
	for referencegenome in referencegenomes:
	    print referencegenome
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 23, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/referencegenome/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "complete", 
	            "reference_path": "/results/referenceLibrary/tmap-f3/CFTR_38amp_v2", 
	            "name": "CFTR_38amp_v2", 
	            "short_name": "CFTR_38amp_v2", 
	            "index_version": "tmap-f3", 
	            "notes": "", 
	            "enabled": true, 
	            "species": "", 
	            "identity_hash": null, 
	            "source": "", 
	            "version": "CFTR_38amp_v2", 
	            "celery_task_id": "", 
	            "date": "2012-03-21T12:32:00.000382+00:00", 
	            "verbose_error": "[\"\", \"\\nSequence name 'CFTR.13.120s' contains a non-alphanumeric character at line 1 !\\n\\n/usr/local/bin/build_genome_index.pl: /results/referenceLibrary/tmap-f2/CFTR_38amp_v2/CFTR_38amp_v2.fasta is fixed and the original is kept as /results/referenceLibrary/tmap-f2/CFTR_38amp_v2/CFTR_38amp_v2.fasta.orig \\n\\n/usr/local/bin/build_genome_index.pl: output directory CFTR_38amp_v2 already exits, aborting.\\n\", 9]", 
	            "id": 7, 
	            "resource_uri": "/rundb/api/v1/referencegenome/7/"
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

