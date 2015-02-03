Sampleset Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/sampleset/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/sampleset/schema/``


.. include:: ../manual_api_ref_docs/sampleset.rst

Fields table
------------

======================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                   help text                                                                                          default nullable readonly blank unique type     
======================= ================================================================================================== ======= ======== ======== ===== ====== ======== 
**status**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleCount**         Integer data. Ex: 2673                                                                             n/a     false    true     false false  integer  
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**SampleGroupType_CV**  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**             Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**    A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupTypeName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**creationDate**        A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                  Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
----------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**        Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
======================= ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/sampleset/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/sampleset/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	samplesets = ts_api_response["objects"]
	
	for sampleset in samplesets:
	    print sampleset
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 2, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/sampleset/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "planned", 
	            "description": "", 
	            "sampleCount": 2, 
	            "displayedName": "Test", 
	            "SampleGroupType_CV": null, 
	            "samples": [
	                "/rundb/api/v1/samplesetitem/18/", 
	                "/rundb/api/v1/samplesetitem/19/"
	            ], 
	            "lastModifiedDate": "2014-11-14T06:28:07.000121+00:00", 
	            "sampleGroupTypeName": "", 
	            "creationDate": "2014-11-14T01:04:50.000223+00:00", 
	            "id": 7, 
	            "resource_uri": "/rundb/api/v1/sampleset/7/"
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

