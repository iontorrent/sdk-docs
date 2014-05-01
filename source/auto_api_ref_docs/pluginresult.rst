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
	        "total_count": 761214, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/pluginresult/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "size": "-1", 
	            "apikey": "13bcc5b989d73fe93947a676ba03f1342dac9870", 
	            "plugin": "/rundb/api/v1/plugin/490/", 
	            "resultName": "C1--479-fc-BC-reanal", 
	            "reportLink": "/output/Home/C1--479-fc-BC-reanal_56256/", 
	            "pluginVersion": "0.2.0", 
	            "jobid": 2810200, 
	            "owner": "/rundb/api/v1/user/2/", 
	            "pluginName": "BarcodeAlignStats", 
	            "state": "Started", 
	            "result": "/rundb/api/v1/results/56256/", 
	            "starttime": "2014-05-01T20:22:07.000235+00:00", 
	            "duration": "0:37:17.162974", 
	            "path": "/results/analysis/output/Home/C1--479-fc-BC-reanal_56256/plugin_out/BarcodeAlignStats_out.768624", 
	            "store": {}, 
	            "endtime": null, 
	            "config": {}, 
	            "id": 768624, 
	            "inodes": "-1", 
	            "resource_uri": "/rundb/api/v1/pluginresult/768624/"
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

