Qualitymetrics Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/qualitymetrics/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/qualitymetrics/schema/``


.. include:: ../manual_api_ref_docs/qualitymetrics.rst

Fields table
------------

======================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                    help text                                                                      default nullable readonly blank unique type    
======================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**q0_reads**             Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_max_read_length**  Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_reads**            Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**               A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mean_read_length** Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_100bp_reads**      Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_max_read_length**   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_100bp_reads**      Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                   Integer data. Ex: 2673                                                                 false    false    true  true   integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mean_read_length** Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_bases**            Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_bases**             Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_150bp_reads**      Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_reads**            Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_50bp_reads**       Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_50bp_reads**       Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_50bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_150bp_reads**      Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_150bp_reads**       Integer data. Ex: 2673                                                         0       false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mean_read_length**  Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_max_read_length**  Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**         Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_100bp_reads**       Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------ ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_bases**            Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
======================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/qualitymetrics/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/qualitymetrics/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	qualitymetricss = ts_api_response["objects"]
	
	for qualitymetrics in qualitymetricss:
	    print qualitymetrics
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 9946, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/qualitymetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "q0_reads": 4521648, 
	            "q17_max_read_length": 391, 
	            "q20_reads": 4521648, 
	            "report": "/rundb/api/v1/results/16213/", 
	            "q17_mean_read_length": 245.0, 
	            "q17_100bp_reads": 4366653, 
	            "q0_max_read_length": 393, 
	            "q20_100bp_reads": 4241622, 
	            "id": 10134, 
	            "q20_mean_read_length": 236, 
	            "q17_bases": "1063712172", 
	            "q0_bases": "1119261439", 
	            "q20_150bp_reads": 4092396, 
	            "q17_reads": 4521648, 
	            "q17_50bp_reads": 4430265, 
	            "q20_50bp_reads": 4337983, 
	            "q0_50bp_reads": 4469162, 
	            "q17_150bp_reads": 4252340, 
	            "q0_150bp_reads": 4283032, 
	            "q0_mean_read_length": 247.0, 
	            "q20_max_read_length": 389.0, 
	            "resource_uri": "/rundb/api/v1/qualitymetrics/10134/", 
	            "q0_100bp_reads": 4401251, 
	            "q20_bases": "1034146239"
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

