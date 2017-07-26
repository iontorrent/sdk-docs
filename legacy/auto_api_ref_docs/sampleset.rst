Sampleset Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/sampleset/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/sampleset/schema/``


.. include:: ../manual_api_ref_docs/sampleset.rst

Fields table
------------

================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                            help text                                                                                          default nullable readonly blank unique type     
================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 
**status**                       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrument**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepPlateType**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**description**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                 Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleCount**                  Integer data. Ex: 2673                                                                             n/a     false    true     false false  integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayedName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**SampleGroupType_CV**           A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pcrPlateSerialNum**            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepInstrumentData**    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitName**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**                      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**lastModifiedDate**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupTypeName**          Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**combinedLibraryTubeLabel**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**creationDate**                 A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName** Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                           Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
-------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepKitDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
================================ ================================================================================================== ======= ======== ======== ===== ====== ======== 

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

