Analysismetrics Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/analysismetrics/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/analysismetrics/schema/``


.. include:: ../manual_api_ref_docs/analysismetrics.rst

Fields table
------------

========================= ============================================================================== ======= ======== ======== ===== ====== ======= 
field                     help text                                                                      default nullable readonly blank unique type    
========================= ============================================================================== ======= ======== ======== ===== ====== ======= 
**libLive**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**ignored**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout_ambiguous**     Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sysIE**                 Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**bead**                  Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**tfKp**                  Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout_live**          Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                    Integer data. Ex: 2673                                                                 false    false    true  true   integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**libFinal**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**lib**                   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**keypass_all_beads**     Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**dud**                   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sysCF**                 Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**pinned**                Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**live**                  Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**excluded**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**tf**                    Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**empty**                 Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**tfFinal**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**amb**                   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**lib_pass_basecaller**   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**lib_pass_cafie**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout_dud**           Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**libMix**                Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**                A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**libKp**                 Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**tfLive**                Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**sysDR**                 Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout_test_fragment** Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout_library**       Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**washout**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**tfMix**                 Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**          Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
========================= ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/analysismetrics/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/analysismetrics/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	analysismetricss = ts_api_response["objects"]
	
	for analysismetrics in analysismetricss:
	    print analysismetrics
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11924, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/analysismetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "libLive": 3060, 
	            "ignored": 682, 
	            "washout_ambiguous": 0, 
	            "sysIE": 0.00814, 
	            "bead": 3062, 
	            "tfKp": 0, 
	            "washout_live": 0, 
	            "id": 1, 
	            "libFinal": 3028, 
	            "lib": 3042, 
	            "keypass_all_beads": 3028, 
	            "dud": 1, 
	            "sysCF": 0.01348, 
	            "pinned": 23, 
	            "live": 3044, 
	            "excluded": 0, 
	            "tf": 2, 
	            "empty": 6915, 
	            "tfFinal": 0, 
	            "amb": 17, 
	            "lib_pass_basecaller": 3042, 
	            "lib_pass_cafie": 3042, 
	            "washout_dud": 0, 
	            "libMix": 0, 
	            "report": "/rundb/api/v1/results/2/", 
	            "libKp": 3028, 
	            "tfLive": 2, 
	            "sysDR": 0.00127, 
	            "washout_test_fragment": 0, 
	            "washout_library": 0, 
	            "washout": 0, 
	            "tfMix": 0, 
	            "resource_uri": "/rundb/api/v1/analysismetrics/1/"
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

