Sampleattribute Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/sampleattribute/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/sampleattribute/schema/``


.. include:: ../manual_api_ref_docs/sampleattribute.rst

Fields table
------------

==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                help text                                                                      default nullable readonly blank unique type     
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**description**      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dataType_name**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dataType**         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**displayedName**    Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isMandatory**      Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleCount**      Integer data. Ex: 2673                                                         n/a     false    true     false false  integer  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate** A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**               Integer data. Ex: 2673                                                                 false    false    true  true   integer  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isActive**         Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/sampleattribute/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/sampleattribute/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	sampleattributes = ts_api_response["objects"]
	
	for sampleattribute in sampleattributes:
	    print sampleattribute
	
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

