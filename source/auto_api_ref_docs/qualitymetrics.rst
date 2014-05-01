Qualitymetrics Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/qualitymetrics/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/qualitymetrics/schema/``


.. include:: ../manual_api_ref_docs/qualitymetrics.rst

Fields table
------------

========================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                      help text                                                                      default nullable readonly blank unique type    
========================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**q0_reads**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_max_read_length**    Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**                 A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mean_read_length**   Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**           Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_max_read_length**     Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                     Integer data. Ex: 2673                                                                 false    false    true  true   integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mean_read_length**   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_bases**               Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_50bp_reads**          Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_150bp_reads**         Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mean_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mode_read_length**    Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_max_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_median_read_length**  Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_100bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
========================== ============================================================================== ======= ======== ======== ===== ====== ======= 

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
	        "total_count": 33268, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/qualitymetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "q0_reads": 129603, 
	            "q17_max_read_length": 234, 
	            "q20_median_read_length": 0, 
	            "q20_reads": 129603, 
	            "report": "/rundb/api/v1/results/32184/", 
	            "q17_mean_read_length": 71.0, 
	            "q17_100bp_reads": 31746, 
	            "resource_uri": "/rundb/api/v1/qualitymetrics/12796/", 
	            "q0_max_read_length": 238, 
	            "q20_100bp_reads": 13368, 
	            "id": 12796, 
	            "q20_mean_read_length": 47, 
	            "q20_150bp_reads": 602, 
	            "q0_bases": "10399984", 
	            "q20_50bp_reads": 61279, 
	            "q17_reads": 129603, 
	            "q17_50bp_reads": 91864, 
	            "q17_median_read_length": 0, 
	            "q0_50bp_reads": 102392, 
	            "q17_150bp_reads": 4052, 
	            "q0_150bp_reads": 5379, 
	            "q0_mean_read_length": 80.0, 
	            "q17_bases": "8642783", 
	            "q0_mode_read_length": 0, 
	            "q20_mode_read_length": 0, 
	            "q20_max_read_length": 213.0, 
	            "q20_bases": "7315545", 
	            "q0_median_read_length": 0, 
	            "q0_100bp_reads": 36699, 
	            "q17_mode_read_length": 0
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

