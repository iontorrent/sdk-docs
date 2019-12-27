.. _api_reference_sampleattribute:

Sample Attribute  Resource
==========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/sampleattribute/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/sampleattribute/schema/``
| 

.. include:: ../references_manual_extras/sampleattribute.rst

Resource Fields
---------------

==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                help text                                                                      default nullable readonly blank unique type     
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**creationDate**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dataType**         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dataType_name**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**displayedName**    Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**               Integer data. Ex: 2673                                                                 false    false    true  true   integer  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isActive**         Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isMandatory**      Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate** A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleCount**      Integer data. Ex: 2673                                                         n/a     false    true     false false  integer  
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 1
	    },
	    "objects": [
	        {
	            "creationDate": "2019-02-21T20:37:39.000872+00:00",
	            "dataType": "/rundb/api/v1/sampleattributedatatype/1/",
	            "dataType_name": "Text",
	            "description": "",
	            "displayedName": "customattribute",
	            "id": 1,
	            "isActive": true,
	            "isMandatory": false,
	            "lastModifiedDate": "2019-02-21T20:38:36.000274+00:00",
	            "resource_uri": "/rundb/api/v1/sampleattribute/1/",
	            "sampleCount": 0
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

