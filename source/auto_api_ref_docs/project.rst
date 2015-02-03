Project Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/project/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/project/schema/``


.. include:: ../manual_api_ref_docs/project.rst

Fields table
------------

================ ============================================================================== ======= ======== ======== ===== ====== ======== 
field            help text                                                                      default nullable readonly blank unique type     
================ ============================================================================== ======= ======== ======== ===== ====== ======== 
**name**         Unicode string data. Ex: "Hello World"                                         n/a     false    false    false true   string   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creator**      A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**created**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**modified**     A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resultsCount** Integer data. Ex: 2673                                                         n/a     false    true     false false  integer  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**public**       Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================ ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/project/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/project/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	projects = ts_api_response["objects"]
	
	for project in projects:
	    print project
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 1684, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/project/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "name": "3gb_snapps", 
	            "creator": "/rundb/api/v1/user/2/", 
	            "created": "2012-07-03T15:14:33.000509+00:00", 
	            "modified": "2012-07-03T15:14:33.000509+00:00", 
	            "id": 1, 
	            "resultsCount": 24, 
	            "public": true, 
	            "resource_uri": "/rundb/api/v1/project/1/"
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

