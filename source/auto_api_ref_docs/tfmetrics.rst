Tfmetrics Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/tfmetrics/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/tfmetrics/schema/``


.. include:: ../manual_api_ref_docs/tfmetrics.rst

Fields table
------------

================ ============================================================================== ======= ======== ======== ===== ====== ======= 
field            help text                                                                      default nullable readonly blank unique type    
================ ============================================================================== ======= ======== ======== ===== ====== ======= 
**corrHPSNR**    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q10Mean**      Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**SysSNR**       Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**HPAccuracy**   Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q17ReadCount** Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sequence**     Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q17Histo**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**name**         Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**aveKeyCount**  Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**number**       Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                                                                 false    false    true  true   integer 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**keypass**      Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q10ReadCount** Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**       A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q17Mean**      Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
---------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**Q10Histo**     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
================ ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/tfmetrics/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/tfmetrics/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	tfmetricss = ts_api_response["objects"]
	
	for tfmetrics in tfmetricss:
	    print tfmetrics
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 20435, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/tfmetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "corrHPSNR": "", 
	            "Q10Mean": 41.6, 
	            "SysSNR": 3.46, 
	            "HPAccuracy": "0 : 137931/168077, 1 : 135718/167266, 2 : 2833/7002, 3 : 199/2918, 4 : 0/0, 5 : 0/0, 6 : 0/0, 7 : 0/0", 
	            "Q17ReadCount": 450.0, 
	            "sequence": "TAGCGTACATCGCGCATCTATATATCGTCAACTACGCTGAGTCGGAGACACGCAGGGATGAGATGG", 
	            "Q17Histo": "71 30 30 12 56 15 13 0 9 38 19 21 16 9 85 28 110 6 34 15 118 27 79 22 57 45 97 23 224 560 0 41 11 72 103 3 62 6 21 13 19 4 50 216 0 54 16 12 1 4 67 95 71 142 20 17 10 3 5 2 4 5 1 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", 
	            "name": "TF5", 
	            "aveKeyCount": 0.0, 
	            "number": 3024.0, 
	            "id": 1, 
	            "keypass": 3027.0, 
	            "Q10ReadCount": 1285.0, 
	            "report": "/rundb/api/v1/results/2/", 
	            "resource_uri": "/rundb/api/v1/tfmetrics/1/", 
	            "Q17Mean": 29.95, 
	            "Q10Histo": "33 16 20 7 1 0 10 0 4 0 2 1 5 20 21 85 18 6 73 0 9 9 37 35 144 28 20 29 88 14 84 14 147 38 6 70 39 20 77 11 34 33 34 64 42 45 74 65 72 38 134 122 110 106 118 126 101 94 17 11 25 38 51 45 55 38 94 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
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

