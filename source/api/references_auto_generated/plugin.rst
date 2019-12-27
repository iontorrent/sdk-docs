.. _api_reference_plugin:

Plugin  Resource
================

| Resource URL ``http://mytorrentserver/rundb/api/v1/plugin/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/plugin/schema/``
| 

.. include:: ../references_manual_extras/plugin.rst

Resource Fields
---------------

========================== ==================================================== ======= ======== ======== ===== ====== ======== 
field                      help text                                            default nullable readonly blank unique type     
========================== ==================================================== ======= ======== ======== ===== ====== ======== 
**active**                 Boolean data. Ex: True                               true    false    false    true  false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**availableVersions**      A list of data. Ex: ['abc', 26.73, 8]                []      false    true     false false  list     
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**config**                 Unicode string data. Ex: "Hello World"                       true     false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                   A date & time as a string. Ex: "2010-11-10T03:07:43" true    false    false    true  false  datetime 
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**defaultSelected**        Boolean data. Ex: True                               false   false    false    true  false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**hasAbout**               Boolean data. Ex: True                               n/a     false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                     Integer data. Ex: 2673                                       false    false    true  true   integer  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**input**                  Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isConfig**               Boolean data. Ex: True                               n/a     false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isInstance**             Boolean data. Ex: True                               n/a     false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanConfig**           Boolean data. Ex: True                               n/a     false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSupported**            Boolean data. Ex: True                               n/a     false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isUpgradable**           Boolean data. Ex: True                               false   false    true     false false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**majorBlock**             Boolean data. Ex: True                               false   false    false    true  false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**name**                   Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**packageName**            Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**path**                   Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginsettings**         Unicode string data. Ex: "Hello World"                       true     false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**requires_configuration** Boolean data. Ex: True                               false   false    false    true  false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**           Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**script**                 Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selected**               Boolean data. Ex: True                               false   false    false    true  false  boolean  
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                 Unicode string data. Ex: "Hello World"                       true     false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**url**                    Unicode string data. Ex: "Hello World"                       false    false    true  false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**userinputfields**        Unicode string data. Ex: "Hello World"               {}      true     false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**version**                Unicode string data. Ex: "Hello World"               n/a     false    false    false false  string   
-------------------------- ---------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**versionedName**          Unicode string data. Ex: "Hello World"               n/a     false    true     false false  string   
========================== ==================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/plugin/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 16
	    },
	    "objects": [
	        {
	            "active": true,
	            "availableVersions": [
	                "5.12.0.1"
	            ],
	            "config": {},
	            "date": "2019-11-08T21:45:21.000653+00:00",
	            "defaultSelected": false,
	            "description": "Whole Transciptome AmpliSeq-RNA Analysis. (Ion supprted)",
	            "hasAbout": true,
	            "id": 90,
	            "input": "/configure/plugins/plugin/90/configure/report/",
	            "isConfig": false,
	            "isInstance": true,
	            "isPlanConfig": true,
	            "isSupported": true,
	            "isUpgradable": false,
	            "majorBlock": true,
	            "name": "immuneResponseRNA",
	            "packageName": "ion-plugin-immuneresponserna",
	            "path": "/results/plugins/immuneResponseRNA",
	            "pluginsettings": {
	                "depends": [],
	                "features": [],
	                "runlevels": [
	                    "default"
	                ],
	                "runtypes": [
	                    "wholechip",
	                    "thumbnail",
	                    "composite"
	                ]
	            },
	            "requires_configuration": false,
	            "resource_uri": "/rundb/api/v1/plugin/90/",
	            "script": "immuneResponseRNA.py",
	            "selected": true,
	            "status": {},
	            "url": "",
	            "userinputfields": {},
	            "version": "5.12.0.1",
	            "versionedName": "immuneResponseRNA--v5.12.0.1"
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

