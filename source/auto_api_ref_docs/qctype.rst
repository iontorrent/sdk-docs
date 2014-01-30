Qctype Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/qctype/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/qctype/schema/``


.. include:: ../manual_api_ref_docs/qctype.rst

Fields table
------------

==================== ====================================== ======= ======== ======== ===== ====== ======= 
field                help text                              default nullable readonly blank unique type    
==================== ====================================== ======= ======== ======== ===== ====== ======= 
**description**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**minThreshold**     Integer data. Ex: 2673                 0       false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**maxThreshold**     Integer data. Ex: 2673                 100     false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**defaultThreshold** Integer data. Ex: 2673                 0       false    false    false false  integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**qcName**           Unicode string data. Ex: "Hello World" n/a     false    false    false true   string  
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**               Integer data. Ex: 2673                         false    false    true  true   integer 
-------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**     Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
==================== ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/qctype/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/qctype/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	qctypes = ts_api_response["objects"]
	
	for qctype in qctypes:
	    print qctype
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 3, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/qctype/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "description": "", 
	            "minThreshold": 0, 
	            "maxThreshold": 100, 
	            "defaultThreshold": 30, 
	            "qcName": "Bead Loading (%)", 
	            "id": 1, 
	            "resource_uri": "/rundb/api/v1/qctype/1/"
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

