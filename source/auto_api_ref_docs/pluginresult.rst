Pluginresult Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/schema/``


.. include:: ../manual_api_ref_docs/pluginresult.rst

Fields table
------------

================= ============================================================================== ======= ======== ======== ===== ====== ======== 
field             help text                                                                      default nullable readonly blank unique type     
================= ============================================================================== ======= ======== ======== ===== ====== ======== 
**size**          Unicode string data. Ex: "Hello World"                                         -1      false    false    false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**apikey**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**plugin**        A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resultName**    Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reportLink**    Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pluginVersion** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**jobid**         Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**owner**         A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pluginName**    Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**state**         Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**result**        A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**starttime**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**duration**      Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**path**          Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**store**         Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**endtime**       A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**config**        Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**            Integer data. Ex: 2673                                                                 false    false    true  true   integer  
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**inodes**        Unicode string data. Ex: "Hello World"                                         -1      false    false    false false  string   
----------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**  Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================= ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/pluginresult/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/pluginresult/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	pluginresults = ts_api_response["objects"]
	
	for pluginresult in pluginresults:
	    print pluginresult
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 788680, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "size": "3484344", 
	            "apikey": null, 
	            "plugin": "/rundb/api/v1/plugin/823/", 
	            "resultName": "Auto_user_Z28-428--r65714-pou4_dbsa_23958", 
	            "reportLink": "/output/Home/Auto_user_Z28-428--r65714-pou4_dbsa_23958_304393/", 
	            "pluginVersion": "4.2-r88266", 
	            "jobid": 3145172, 
	            "owner": "/rundb/api/v1/user/1/", 
	            "pluginName": "AssemblerSPAdes", 
	            "state": "Completed", 
	            "result": "/rundb/api/v1/results/304393/", 
	            "starttime": "2014-06-28T13:49:00.000133+00:00", 
	            "duration": "0:01:54.098431", 
	            "path": "/results/analysis/output/Home/Auto_user_Z28-428--r65714-pou4_dbsa_23958_304393/plugin_out/AssemblerSPAdes_out.815369", 
	            "store": {}, 
	            "endtime": "2014-06-28T13:50:54.000232+00:00", 
	            "config": {
	                "only_barcodes": "", 
	                "spadesOptions": "-k 21,33,55,77,99", 
	                "spadesversion": "3.1.0", 
	                "RAM": "32G", 
	                "min_reads": "500", 
	                "bgenome": "None", 
	                "runSpades": "1", 
	                "fraction_of_reads": "1"
	            }, 
	            "id": 815369, 
	            "inodes": "396", 
	            "resource_uri": "/rundb/api/v1/pluginresult/815369/"
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

