Plugin Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plugin/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plugin/schema/``


.. include:: ../manual_api_ref_docs/plugin.rst

Fields table
------------

===================== ==================================================== ======= ======== ======== ===== ====== ======== 
field                 help text                                            default nullable readonly blank unique type     
===================== ==================================================== ======= ======== ======== ===== ====== ======== 
**active**            Boolean data. Ex: True                               true    false    false    true  false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**availableVersions** A list of data. Ex: ['abc', 26.73, 8]                []      false    true     false false  list     
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                Integer data. Ex: 2673                                       false    false    true  true   integer  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanConfig**      Boolean data. Ex: True                               n/a     false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSupported**       Boolean data. Ex: True                               n/a     false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**script**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selected**          Boolean data. Ex: True                               false   false    false    true  false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**           Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hasAbout**          Boolean data. Ex: True                               n/a     false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**input**             Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**majorBlock**        Boolean data. Ex: True                               false   false    false    true  false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**            Unicode string data. Ex: "Hello World"                       true     false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**defaultSelected**   Boolean data. Ex: True                               false   false    false    true  false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginsettings**    Unicode string data. Ex: "Hello World"                       true     false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**              A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**              Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isConfig**          Boolean data. Ex: True                               n/a     false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isInstance**        Boolean data. Ex: True                               n/a     false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**              Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**userinputfields**   Unicode string data. Ex: "Hello World"               {}      true     false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**               Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**config**            Unicode string data. Ex: "Hello World"                       true     false    false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**packageName**       Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**versionedName**     Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isUpgradable**      Boolean data. Ex: True                               false   false    true     false false  boolean  
--------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**      Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
===================== ==================================================== ======= ======== ======== ===== ====== ======== 

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
	        "total_count": 16, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plugin/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "active": true, 
	            "availableVersions": [
	                "5.4.0.1", 
	                "5.4.0.4", 
	                "5.4.0.5"
	            ], 
	            "id": 20, 
	            "isPlanConfig": false, 
	            "isSupported": true, 
	            "script": "RunTransfer.py", 
	            "selected": true, 
	            "version": "5.4.0.5", 
	            "hasAbout": true, 
	            "input": "/configure/plugins/plugin/20/configure/report/", 
	            "majorBlock": false, 
	            "status": {}, 
	            "description": "Main class definition for this plugin", 
	            "defaultSelected": true, 
	            "pluginsettings": {
	                "depends": [], 
	                "features": [], 
	                "runtypes": [], 
	                "runlevels": []
	            }, 
	            "date": "2017-03-28T05:03:48.000450+00:00", 
	            "path": "/results/plugins/RunTransfer", 
	            "isConfig": true, 
	            "isInstance": true, 
	            "name": "RunTransfer", 
	            "userinputfields": {}, 
	            "url": "", 
	            "config": {
	                "upload_path": "/results/uploads/", 
	                "ip": "blackbird.itw", 
	                "user_password": "ionadmin", 
	                "user_name": "ionadmin", 
	                "thumbnailonly": "off"
	            }, 
	            "packageName": "ion-plugin-runtransfer", 
	            "versionedName": "RunTransfer--v5.4.0.5", 
	            "isUpgradable": false, 
	            "resource_uri": "/rundb/api/v1/plugin/20/"
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

