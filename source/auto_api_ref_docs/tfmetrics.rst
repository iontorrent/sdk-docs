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
	        "total_count": 7320, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/tfmetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "corrHPSNR": "", 
	            "Q10Mean": 79.7, 
	            "SysSNR": 20.19, 
	            "HPAccuracy": "0 : 560244/582614, 1 : 356550/377171, 2 : 35115/45374, 3 : 0/0, 4 : 521/4373, 5 : 0/0, 6 : 0/0, 7 : 0/0", 
	            "Q17ReadCount": 3992.0, 
	            "sequence": "TTGCGCGCGCTGTGAATGCGCTGCTGTCGAATCGCGCTGCGCTGAACGTCGCGTGCGCGAACGATCTGAGACTGCCAAGGCACACAGGGGATAGG", 
	            "Q17Histo": "951 0 0 1 9 5 2 7 6 277 5 0 1 2 3 0 2 1 6 1 7 2 3 3 0 0 10 1 0 26 0 2 0 1 2 3 5 1 1 0 2 6 2 1 9 0 3 5 2 0 7 0 2 5 4 2 6 2 34 4 13 1 15 5 18 7 8 6 12 7 9 12 1 9 1 44 0 67 0 29 2 37 7 3 6 305 356 544 0 35 14 1116 1019 52 150 16 0 0 0 0 0", 
	            "name": "TF_D", 
	            "aveKeyCount": 71.0, 
	            "number": 4119.0, 
	            "id": 1, 
	            "keypass": 5368.0, 
	            "Q10ReadCount": 4586.0, 
	            "report": "/rundb/api/v1/results/89/", 
	            "resource_uri": "/rundb/api/v1/tfmetrics/1/", 
	            "Q17Mean": 66.56, 
	            "Q10Histo": "40 0 0 1 8 3 0 4 2 1 587 5 3 5 1 8 0 2 6 1 5 1 3 3 2 1 5 9 0 0 2 0 2 1 5 1 0 4 0 2 5 8 7 7 5 2 5 8 9 3 5 3 1 5 1 1 2 4 4 1 1 2 4 5 5 4 4 21 6 1 5 14 9 13 3 1 1 2 15 10 25 18 36 18 20 18 40 78 138 109 95 399 1340 1471 383 245 0 0 0 0 0"
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

