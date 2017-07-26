.. _api_reference_activeionchefprepkitinfo:

Active Ion Chef Prep Kit Info  Resource
=======================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/activeionchefprepkitinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/activeionchefprepkitinfo/schema/``
| 

.. include:: ../references_manual_extras/activeionchefprepkitinfo.rst

Resource Fields
---------------

============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
field                         help text                                                                                          default nullable readonly blank unique type    
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 
**isActive**                  Boolean data. Ex: True                                                                             true    false    false    true  false  boolean 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**samplePrep_instrumentType** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**templatingSize**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**kitType**                   Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**description**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**nucleotideType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**instrumentType**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**chipTypes**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**runMode**                   Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**parts**                     Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**flowCount**                 Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**applicationType**           Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**uid**                       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**libraryReadLength**         Integer data. Ex: 2673                                                                             0       false    false    false false  integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                                                                                     false    false    true  true   integer 
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**categories**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string  
----------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string  
============================= ================================================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/activeionchefprepkitinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isActive": true, 
	            "samplePrep_instrumentType": "IC", 
	            "templatingSize": "", 
	            "kitType": "IonChefPrepKit", 
	            "description": "ION PGM IC 200 KIT", 
	            "nucleotideType": "", 
	            "instrumentType": "pgm", 
	            "chipTypes": "", 
	            "runMode": "", 
	            "parts": [
	                {
	                    "barcode": "100020580", 
	                    "id": 20086, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20086/", 
	                    "kit": "/rundb/api/v1/kitinfo/20042/"
	                }, 
	                {
	                    "barcode": "01", 
	                    "id": 20123, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20123/", 
	                    "kit": "/rundb/api/v1/kitinfo/20042/"
	                }, 
	                {
	                    "barcode": "100020579", 
	                    "id": 20085, 
	                    "resource_uri": "/rundb/api/v1/kitpart/20085/", 
	                    "kit": "/rundb/api/v1/kitinfo/20042/"
	                }
	            ], 
	            "flowCount": 0, 
	            "applicationType": "", 
	            "uid": "ICPREP0001", 
	            "libraryReadLength": 0, 
	            "resource_uri": "/rundb/api/v1/activeionchefprepkitinfo/20042/", 
	            "id": 20042, 
	            "categories": "", 
	            "name": "ION PGM IC 200 KIT"
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
