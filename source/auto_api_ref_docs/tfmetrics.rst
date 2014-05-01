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
	        "total_count": 12499, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/tfmetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "corrHPSNR": "", 
	            "Q10Mean": 81.8, 
	            "SysSNR": 19.41, 
	            "HPAccuracy": "0 : 257730/269219, 1 : 165695/174283, 2 : 18132/21031, 3 : 0/0, 4 : 1574/2067, 5 : 0/0, 6 : 0/0, 7 : 0/0", 
	            "Q17ReadCount": 2037.0, 
	            "sequence": "TTGCGCGCGCTGTGAATGCGCTGCTGTCGAATCGCGCTGCGCTGAACGTCGCGTGCGCGAACGATCTGAGACTGCCAAGGCACACAGGGGATAGG", 
	            "Q17Histo": "31 0 0 2 0 1 1 3 4 261 5 4 1 3 8 0 4 1 1 0 3 2 3 2 3 2 5 3 3 11 0 1 0 0 3 4 4 0 1 3 2 3 2 2 23 0 2 2 2 0 2 4 2 1 3 2 1 2 9 1 3 1 8 1 3 4 5 2 5 10 7 7 5 12 6 59 0 10 0 9 2 3 5 4 5 47 30 28 0 5 17 25 133 1 413 1135 0 0 0 0 0", 
	            "name": "TF_D", 
	            "aveKeyCount": 70.0, 
	            "number": 2458.0, 
	            "id": 1, 
	            "keypass": 2458.0, 
	            "Q10ReadCount": 2097.0, 
	            "report": "/rundb/api/v1/results/591/", 
	            "resource_uri": "/rundb/api/v1/tfmetrics/1/", 
	            "Q17Mean": 78.34, 
	            "Q10Histo": "5 0 0 0 0 1 0 1 0 0 274 6 3 5 2 3 3 2 1 2 2 2 0 6 1 1 3 5 4 1 0 1 2 0 2 4 0 0 0 1 1 4 3 0 1 1 1 4 3 0 2 4 2 1 1 2 1 3 0 1 0 3 0 2 2 2 2 1 2 2 2 3 5 5 3 7 0 3 1 0 7 2 5 2 3 2 3 1 9 6 6 10 57 135 355 1432 0 0 0 0 0"
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

