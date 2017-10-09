.. _api_reference_plugin:

Plugin  Resource
================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plugin/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plugin/schema/``
| 

.. include:: ../references_manual_extras/plugin.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	                "5.6.0.0"
	            ], 
	            "id": 16, 
	            "isPlanConfig": true, 
	            "isSupported": true, 
	            "script": "smallRNA.py", 
	            "selected": true, 
	            "version": "5.6.0.0", 
	            "hasAbout": false, 
	            "input": "/configure/plugins/plugin/16/configure/report/", 
	            "majorBlock": true, 
	            "status": {}, 
	            "description": "Run the small RNA pipeline.", 
	            "defaultSelected": false, 
	            "pluginsettings": {
	                "depends": [], 
	                "features": [], 
	                "runtypes": [
	                    "wholechip", 
	                    "thumbnail", 
	                    "composite"
	                ], 
	                "runlevels": [
	                    "default"
	                ]
	            }, 
	            "date": "2017-08-01T20:08:28.000127+00:00", 
	            "path": "/results/plugins/smallRNA", 
	            "isConfig": true, 
	            "isInstance": true, 
	            "name": "smallRNA", 
	            "userinputfields": {}, 
	            "url": "", 
	            "config": {}, 
	            "packageName": "ion-plugin-smallrna", 
	            "versionedName": "smallRNA--v5.6.0.0", 
	            "isUpgradable": false, 
	            "resource_uri": "/rundb/api/v1/plugin/16/"
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

