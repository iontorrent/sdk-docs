Plugin Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plugin/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plugin/schema/``


.. include:: ../manual_api_ref_docs/plugin.rst

Fields table
------------

=================== ==================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                            default nullable readonly blank unique type     
=================== ==================================================== ======= ======== ======== ===== ====== ======== 
**active**          Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                       false    false    true  true   integer  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanConfig**    Boolean data. Ex: True                               n/a     false    true     false false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autorunMutable**  Boolean data. Ex: True                               true    false    false    true  false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**script**          Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selected**        Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**         Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hasAbout**        Boolean data. Ex: True                               n/a     false    true     false false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**input**           Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**majorBlock**      Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**     Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autorun**         Boolean data. Ex: True                               false   false    false    true  false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginsettings**  Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**            A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isConfig**        Boolean data. Ex: True                               n/a     false    true     false false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**            Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**userinputfields** Unicode string data. Ex: "Hello World"               {}      true     false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**             Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**config**          Unicode string data. Ex: "Hello World"                       true     false    false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**versionedName**   Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isInstance**      Boolean data. Ex: True                               n/a     false    true     false false  boolean  
------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
=================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/plugin/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/plugin/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	plugins = ts_api_response["objects"]
	
	for plugin in plugins:
	    print plugin
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 102, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plugin/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "active": true, 
	            "id": 493, 
	            "isPlanConfig": false, 
	            "autorunMutable": true, 
	            "script": "launch.sh", 
	            "selected": true, 
	            "version": "0.2.0", 
	            "hasAbout": false, 
	            "input": "False", 
	            "majorBlock": false, 
	            "status": {}, 
	            "description": "Ion Torrent Plugin - 'BarcodeAlignStats' v0.2.0", 
	            "autorun": false, 
	            "pluginsettings": {
	                "runtype": [
	                    "wholechip", 
	                    "thumbnail"
	                ], 
	                "depends": [], 
	                "features": [], 
	                "runlevel": []
	            }, 
	            "date": "2013-05-30T21:32:15.000437+00:00", 
	            "path": "/results/plugins/BarcodeAlignStats", 
	            "isConfig": false, 
	            "name": "BarcodeAlignStats", 
	            "userinputfields": {}, 
	            "url": "", 
	            "config": {}, 
	            "versionedName": "BarcodeAlignStats--v0.2.0", 
	            "isInstance": false, 
	            "resource_uri": "/rundb/api/v1/plugin/493/"
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

