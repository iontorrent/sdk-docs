Samplesetitem Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/samplesetitem/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/samplesetitem/schema/``


.. include:: ../manual_api_ref_docs/samplesetitem.rst

Fields table
------------

===================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                 help text                                                                      default nullable readonly blank unique type     
===================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**sample**            A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**gender**            Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipGroup** Integer data. Ex: 2673                                                         n/a     false    false    false false  integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellularityPct**    Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipRole**  Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cancerType**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**  A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcode**        A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                Integer data. Ex: 2673                                                                 false    false    true  true   integer  
--------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**      Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
===================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/samplesetitem/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/samplesetitem/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	samplesetitems = ts_api_response["objects"]
	
	for samplesetitem in samplesetitems:
	    print samplesetitem
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 4, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/samplesetitem/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "sample": "/rundb/api/v1/sample/4877/", 
	            "gender": "Female", 
	            "relationshipGroup": 1, 
	            "cellularityPct": null, 
	            "relationshipRole": "Self", 
	            "cancerType": null, 
	            "sampleSet": "/rundb/api/v1/sampleset/5/", 
	            "lastModifiedDate": "2013-10-07T12:04:51.000440+00:00", 
	            "dnabarcode": null, 
	            "creationDate": "2013-10-07T12:04:51.000440+00:00", 
	            "id": 14, 
	            "resource_uri": "/rundb/api/v1/samplesetitem/14/"
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

