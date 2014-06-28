Compositeexperiment Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/schema/``


.. include:: ../manual_api_ref_docs/compositeexperiment.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**ftpStatus**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options** Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**            Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**        Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**           Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**repResult**       A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**         Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**            A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**            A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/compositeexperiment/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/compositeexperiment/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	compositeexperiments = ts_api_response["objects"]
	
	for compositeexperiment in compositeexperiments:
	    print compositeexperiment
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 20366, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipInstrumentType": "proton", 
	            "chipType": "P1.1.17", 
	            "results": [
	                {
	                    "status": "Completed", 
	                    "processedflows": 0, 
	                    "analysis_metrics": {
	                        "ignored": 1364892, 
	                        "lib": 118063544, 
	                        "total_wells": 164699136, 
	                        "pinned": 463867, 
	                        "live": 118074386, 
	                        "excluded": 16095180, 
	                        "bead": 118525043, 
	                        "resource_uri": "", 
	                        "id": 41726, 
	                        "empty": 28250154, 
	                        "libFinal": 85604279
	                    }, 
	                    "timeStamp": "2014-06-28T07:11:58.000789+00:00", 
	                    "analysismetrics": {
	                        "ignored": 1364892, 
	                        "lib": 118063544, 
	                        "total_wells": 164699136, 
	                        "pinned": 463867, 
	                        "live": 118074386, 
	                        "excluded": 16095180, 
	                        "bead": 118525043, 
	                        "resource_uri": "", 
	                        "id": 41726, 
	                        "empty": 28250154, 
	                        "libFinal": 85604279
	                    }, 
	                    "reportLink": "/output/Home/Auto_user_Z28-428--r65714-pou4_dbsa_23958_304393/", 
	                    "id": 304393, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 178.362197969099, 
	                        "q0_reads": 85604279, 
	                        "q0_bases": "15268567358", 
	                        "q20_reads": 85604279, 
	                        "q20_bases": "13060288783", 
	                        "q20_mean_read_length": 178, 
	                        "id": 39683, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_user_Z28-428--r65714-pou4_dbsa_23958", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 1385, 
	                            "name": "auto_chip", 
	                            "modified": "2014-06-27T21:21:43.000081+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 178.362197969099, 
	                        "q0_reads": 85604279, 
	                        "q0_bases": "15268567358", 
	                        "q20_reads": 85604279, 
	                        "q20_bases": "13060288783", 
	                        "q20_mean_read_length": 178, 
	                        "id": 39683, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "hg19", 
	                        "barcodeKitName": "IonXpress"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/304393/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 61016174, 
	                        "aveKeyCounts": 89.0, 
	                        "id": 41874, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 159
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 9939, 
	                        "lib": 726685, 
	                        "total_wells": 960000, 
	                        "pinned": 44080, 
	                        "live": 726723, 
	                        "excluded": 0, 
	                        "bead": 738396, 
	                        "resource_uri": "", 
	                        "id": 41695, 
	                        "empty": 167585, 
	                        "libFinal": 517179
	                    }, 
	                    "timeStamp": "2014-06-28T00:18:42.000351+00:00", 
	                    "analysismetrics": {
	                        "ignored": 9939, 
	                        "lib": 726685, 
	                        "total_wells": 960000, 
	                        "pinned": 44080, 
	                        "live": 726723, 
	                        "excluded": 0, 
	                        "bead": 738396, 
	                        "resource_uri": "", 
	                        "id": 41695, 
	                        "empty": 167585, 
	                        "libFinal": 517179
	                    }, 
	                    "reportLink": "/output/Home/Auto_user_Z28-428--r65714-pou4_dbsa_23958_tn_304394/", 
	                    "id": 304394, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 176.041268110267, 
	                        "q0_reads": 517179, 
	                        "q0_bases": "91044847", 
	                        "q20_reads": 517179, 
	                        "q20_bases": "77321419", 
	                        "q20_mean_read_length": 176, 
	                        "id": 39658, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_user_Z28-428--r65714-pou4_dbsa_23958_tn", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 1385, 
	                            "name": "auto_chip", 
	                            "modified": "2014-06-27T21:21:43.000081+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 176.041268110267, 
	                        "q0_reads": 517179, 
	                        "q0_bases": "91044847", 
	                        "q20_reads": 517179, 
	                        "q20_bases": "77321419", 
	                        "q20_mean_read_length": 176, 
	                        "id": 39658, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "hg19", 
	                        "barcodeKitName": "IonXpress"
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/304394/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 358815, 
	                        "aveKeyCounts": 88.0, 
	                        "id": 41849, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 155
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }
	            ], 
	            "library": "hg19", 
	            "sample": "148541", 
	            "runMode": "single", 
	            "storage_options": "D", 
	            "repResult": "/rundb/api/v1/compositeresult/304394/", 
	            "id": 23958, 
	            "archived": false, 
	            "barcodeId": "IonXpress", 
	            "sampleSetName": "", 
	            "star": false, 
	            "resultDate": "2014-06-28T07:11:58.000789+00:00", 
	            "flows": 520, 
	            "plan": {
	                "runType": "AMPS_EXOME", 
	                "id": 102195, 
	                "resource_uri": ""
	            }, 
	            "date": "2014-06-27T21:19:01+00:00", 
	            "ftpStatus": "Complete", 
	            "notes": "", 
	            "chipDescription": "PI", 
	            "pgmName": "Z28", 
	            "keep": false, 
	            "expName": "R_2014_06_27_17_13_22_user_Z28-428--r65714-pou4_dbsa", 
	            "resource_uri": "/rundb/api/v1/compositeexperiment/23958/"
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

