Experiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/experiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/experiment/schema/``


.. include:: ../manual_api_ref_docs/experiment.rst

Fields table
------------

====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                  help text                                                                                          default nullable readonly blank unique type     
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**isReverseRun**       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**    Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**           Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**user_ack**           Unicode string data. Ex: "Hello World"                                                             U       false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**             Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**            Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**      Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                 Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**           Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**                Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitbarcode** Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**       Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas_set**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runtype**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samples**            Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pinnedRepResult**    Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reagentBarcode**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**               Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isProton**           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expCompInfo**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**         A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**              Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**               A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**               A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**          Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**unique**             Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false true   string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expDir**             Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**ftpStatus**          Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**baselineRun**        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayName**        Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**        Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**            Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**     Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**             Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
---------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**rawdatastyle**       Unicode string data. Ex: "Hello World"                                                             single  true     false    false false  string   
====================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/experiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/experiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	experiments = ts_api_response["objects"]
	
	for experiment in experiments:
	    print experiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 11450, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/experiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isReverseRun": false, 
	            "storage_options": "KI", 
	            "chipType": "314R", 
	            "user_ack": "U", 
	            "results": [], 
	            "sample": "xb2s8", 
	            "runMode": "", 
	            "reverse_primer": null, 
	            "seqKitBarcode": "", 
	            "id": 2241, 
	            "metaData": {}, 
	            "log": {
	                "postbeadfind": "Yes", 
	                "num_frames": 162, 
	                "image_map": "4 0 r4 1 r3 2 r2 3 r1", 
	                "oversample": 8, 
	                "seqbarcode": "", 
	                "library": "Library:none", 
	                "sample": "xb2s8", 
	                "driver_version": 29, 
	                "frequency": 53333333, 
	                "board_version": null, 
	                "firmware_version": 99, 
	                "cal_chip_high_low_inrange": [
	                    61, 
	                    2576, 
	                    1471923
	                ], 
	                "fpga_version": 70, 
	                "script_version": [
	                    16, 
	                    1, 
	                    2
	                ], 
	                "board_serial": "000048", 
	                "librarykeysequence": "TCAG", 
	                "frame_time": "0.0084779999999999994", 
	                "liveview_version": 239, 
	                "calibratepassed": "Yes", 
	                "wetload": "yes", 
	                "datacollect_version": 160, 
	                "serial_number": "sn08p0714008", 
	                "pgmtemperature": "30.00 - 30.00", 
	                "user_name": "johnB", 
	                "pgmpressure": "10.72 - 10.72", 
	                "autoanalyze": false, 
	                "cal_chip_hist": [
	                    51, 
	                    134, 
	                    125, 
	                    125, 
	                    146, 
	                    135, 
	                    157, 
	                    144, 
	                    152, 
	                    149, 
	                    155, 
	                    190, 
	                    258, 
	                    594, 
	                    1906, 
	                    5012, 
	                    12092, 
	                    22057, 
	                    33487, 
	                    40239, 
	                    40380, 
	                    36162, 
	                    37166, 
	                    50038, 
	                    76028, 
	                    109995, 
	                    142645, 
	                    162980, 
	                    167182, 
	                    152288, 
	                    126247, 
	                    94724, 
	                    63635, 
	                    39832, 
	                    22213, 
	                    12091, 
	                    6046, 
	                    3425, 
	                    2028, 
	                    1596, 
	                    1354, 
	                    1259, 
	                    1213, 
	                    1063, 
	                    879, 
	                    701, 
	                    518, 
	                    385, 
	                    268, 
	                    164, 
	                    108, 
	                    53
	                ], 
	                "dac": [
	                    32970, 
	                    32943, 
	                    32812, 
	                    32812, 
	                    33062, 
	                    33035, 
	                    32903, 
	                    32903
	                ], 
	                "start_time": "Mon Nov 15 19:51:15 2010", 
	                "autosettlecalibrate": "Yes", 
	                "chipbarcode": "AA0006923", 
	                "ref_electrode": "1.576999999999999957367 V", 
	                "analyzeearly": false, 
	                "runtype": "GNMS", 
	                "kernel_build": "#50 PREEMPT Fri Nov 5 10:13:40 EDT 2010", 
	                "prerun": true, 
	                "chiptype": "\"314R\"", 
	                "autoanalysisname": "", 
	                "prebeadfind": true, 
	                "chiptemperature": "50 - 50", 
	                "project": "BF2S8", 
	                "experiment_name": "R_2010_11_15_19_51_15_johnB_SUR-412_2S8", 
	                "end_time": "Mon Nov 15 20:13:58 2010", 
	                "user_notes": "", 
	                "vrefs": "23442 25490", 
	                "cycles": 2, 
	                "gain": "0.63100000000000001"
	            }, 
	            "sequencekitbarcode": null, 
	            "resource_uri": "/rundb/api/v1/experiment/2241/", 
	            "eas_set": [
	                {
	                    "isEditable": false, 
	                    "hotSpotRegionBedFile": "", 
	                    "results": [], 
	                    "targetRegionBedFile": "", 
	                    "thumbnailalignmentargs": "", 
	                    "thumbnailanalysisargs": "", 
	                    "id": 3427, 
	                    "barcodedSamples": {}, 
	                    "reference": "Library:none", 
	                    "isOneTimeOverride": false, 
	                    "analysisargs": "", 
	                    "selectedPlugins": {}, 
	                    "experiment": "/rundb/api/v1/experiment/2241/", 
	                    "barcodeKitName": "", 
	                    "beadfindargs": "", 
	                    "threePrimeAdapter": "", 
	                    "thumbnailbasecallerargs": "", 
	                    "status": "run", 
	                    "prebasecallerargs": "", 
	                    "prethumbnailbasecallerargs": "", 
	                    "alignmentargs": "", 
	                    "isDuplicateReads": false, 
	                    "libraryKey": "TCAG", 
	                    "date": "2013-01-29T14:27:54.000618+00:00", 
	                    "libraryKitName": "", 
	                    "thumbnailbeadfindargs": "", 
	                    "tfKey": "", 
	                    "libraryKitBarcode": null, 
	                    "basecallerargs": "", 
	                    "resource_uri": "/rundb/api/v1/experimentanalysissettings/3427/"
	                }
	            ], 
	            "runtype": "GNMS", 
	            "samples": [
	                {
	                    "status": "run", 
	                    "sampleSets": [], 
	                    "description": null, 
	                    "displayedName": "xb2s8", 
	                    "experiments": [
	                        "/rundb/api/v1/experiment/2197/", 
	                        "/rundb/api/v1/experiment/2229/", 
	                        "/rundb/api/v1/experiment/2220/", 
	                        "/rundb/api/v1/experiment/2241/", 
	                        "/rundb/api/v1/experiment/2232/", 
	                        "/rundb/api/v1/experiment/2235/", 
	                        "/rundb/api/v1/experiment/2219/", 
	                        "/rundb/api/v1/experiment/2216/", 
	                        "/rundb/api/v1/experiment/2200/", 
	                        "/rundb/api/v1/experiment/2203/"
	                    ], 
	                    "externalId": "", 
	                    "date": "2013-01-29T14:27:54.000158+00:00", 
	                    "resource_uri": "/rundb/api/v1/sample/1312/", 
	                    "id": 1312, 
	                    "name": "xb2s8"
	                }
	            ], 
	            "pinnedRepResult": false, 
	            "reagentBarcode": "", 
	            "star": false, 
	            "isProton": "False", 
	            "expCompInfo": "", 
	            "resultDate": "2010-11-16T00:51:15+00:00", 
	            "flows": 0, 
	            "plan": null, 
	            "date": "2010-11-16T00:51:15+00:00", 
	            "diskusage": 5639, 
	            "unique": "/results2/Surge/R_2010_11_15_19_51_15_johnB_SUR-412_2S8", 
	            "expDir": "/results2/Surge/R_2010_11_15_19_51_15_johnB_SUR-412_2S8", 
	            "autoAnalyze": false, 
	            "ftpStatus": "Complete", 
	            "flowsInOrder": "0", 
	            "baselineRun": false, 
	            "displayName": "johnB SUR-412 2S8", 
	            "notes": "", 
	            "sequencekitname": null, 
	            "chipBarcode": "AA0006923", 
	            "pgmName": "Surge", 
	            "storageHost": null, 
	            "expName": "R_2010_11_15_19_51_15_johnB_SUR-412_2S8", 
	            "status": "run", 
	            "usePreBeadfind": true, 
	            "cycles": 2, 
	            "rawdatastyle": "single"
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

