Samplesetiteminfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/samplesetiteminfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/samplesetiteminfo/schema/``


.. include:: ../manual_api_ref_docs/samplesetiteminfo.rst

Fields table
------------

======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
field                   help text                                                                      default nullable readonly blank unique type     
======================= ============================================================================== ======= ======== ======== ===== ====== ======== 
**sample**              A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSetPk**         Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleExternalId**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName** Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**gender**              Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipGroup**   Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cellularityPct**      Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcodeKit**       Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleDescription**   Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**relationshipRole**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cancerType**          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePk**            Integer data. Ex: 2673                                                         n/a     true     true     true  false  integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**    A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**dnabarcode**          A single related resource. Can be either a URI or set of nested resource data. n/a     true     true     true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet**           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**creationDate**        A date & time as a string. Ex: "2010-11-10T03:07:43"                           true    false    false    true  false  datetime 
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                  Integer data. Ex: 2673                                                                 false    false    true  true   integer  
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSetStatus**     Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
----------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**        Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
======================= ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/samplesetiteminfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/samplesetiteminfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	samplesetiteminfos = ts_api_response["objects"]
	
	for samplesetiteminfo in samplesetiteminfos:
	    print samplesetiteminfo
	
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

