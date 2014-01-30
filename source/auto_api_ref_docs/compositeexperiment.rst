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
**resultDate**      A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**           Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**         Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
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
	        "total_count": 11335, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/compositeexperiment/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "chipInstrumentType": "pgm", 
	            "chipType": "318C", 
	            "results": [
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12134, 
	                        "empty": 2735423, 
	                        "libFinal": 4521648
	                    }, 
	                    "timeStamp": "2014-01-28T22:05:05.000864+00:00", 
	                    "analysismetrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12134, 
	                        "empty": 2735423, 
	                        "libFinal": 4521648
	                    }, 
	                    "reportLink": "/output17/IonEast/reanalyze_bpp_16215/", 
	                    "id": 16215, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521648, 
	                        "q0_bases": "1119261439", 
	                        "q20_reads": 4521648, 
	                        "q20_bases": "1034146239", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10135, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "reanalyze_bpp", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521648, 
	                        "q0_bases": "1119261439", 
	                        "q20_reads": 4521648, 
	                        "q20_bases": "1034146239", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10135, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16215/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 4244729, 
	                        "aveKeyCounts": 62.0, 
	                        "id": 12935, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 239
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Create Download Links", 
	                    "processedflows": 0, 
	                    "analysis_metrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12133, 
	                        "empty": 2735423, 
	                        "libFinal": 0
	                    }, 
	                    "timeStamp": "2014-01-28T14:36:48.000875+00:00", 
	                    "analysismetrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12133, 
	                        "empty": 2735423, 
	                        "libFinal": 0
	                    }, 
	                    "reportLink": "/output17/IonEast/reanalysis_bpp_16214/", 
	                    "id": 16214, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": null, 
	                    "resultsName": "reanalysis_bpp", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": null, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16214/", 
	                    "libmetrics": null, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12132, 
	                        "empty": 2735423, 
	                        "libFinal": 4521648
	                    }, 
	                    "timeStamp": "2014-01-21T20:02:18.000604+00:00", 
	                    "analysismetrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12132, 
	                        "empty": 2735423, 
	                        "libFinal": 4521648
	                    }, 
	                    "reportLink": "/output17/IonEast/reanalysis_bpp_deleteme_16213/", 
	                    "id": 16213, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521648, 
	                        "q0_bases": "1119261439", 
	                        "q20_reads": 4521648, 
	                        "q20_bases": "1034146239", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10134, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "reanalysis_bpp_deleteme", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521648, 
	                        "q0_bases": "1119261439", 
	                        "q20_reads": 4521648, 
	                        "q20_bases": "1034146239", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10134, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16213/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 4244636, 
	                        "aveKeyCounts": 62.0, 
	                        "id": 12934, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 239
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12131, 
	                        "empty": 2735423, 
	                        "libFinal": 4521442
	                    }, 
	                    "timeStamp": "2013-12-31T20:38:54.000878+00:00", 
	                    "analysismetrics": {
	                        "ignored": 655129, 
	                        "lib": 7752120, 
	                        "total_wells": 12862464, 
	                        "pinned": 88232, 
	                        "live": 7802979, 
	                        "excluded": 1575189, 
	                        "bead": 7808491, 
	                        "resource_uri": "", 
	                        "id": 12131, 
	                        "empty": 2735423, 
	                        "libFinal": 4521442
	                    }, 
	                    "reportLink": "/output17/IonEast/reanalysis_bpp_deleteme_16212/", 
	                    "id": 16212, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521442, 
	                        "q0_bases": "1118703994", 
	                        "q20_reads": 4521442, 
	                        "q20_bases": "1033639926", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10133, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "reanalysis_bpp_deleteme", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 247.0, 
	                        "q0_reads": 4521442, 
	                        "q0_bases": "1118703994", 
	                        "q20_reads": 4521442, 
	                        "q20_bases": "1033639926", 
	                        "q20_mean_read_length": 236, 
	                        "id": 10133, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16212/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 4243892, 
	                        "aveKeyCounts": 62.0, 
	                        "id": 12933, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 239
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 675500, 
	                        "lib": 7825432, 
	                        "total_wells": 12862464, 
	                        "pinned": 148930, 
	                        "live": 7876394, 
	                        "excluded": 1559456, 
	                        "bead": 7883235, 
	                        "resource_uri": "", 
	                        "id": 12130, 
	                        "empty": 2595343, 
	                        "libFinal": 4445264
	                    }, 
	                    "timeStamp": "2013-12-26T18:37:39.000738+00:00", 
	                    "analysismetrics": {
	                        "ignored": 675500, 
	                        "lib": 7825432, 
	                        "total_wells": 12862464, 
	                        "pinned": 148930, 
	                        "live": 7876394, 
	                        "excluded": 1559456, 
	                        "bead": 7883235, 
	                        "resource_uri": "", 
	                        "id": 12130, 
	                        "empty": 2595343, 
	                        "libFinal": 4445264
	                    }, 
	                    "reportLink": "/output17/IonEast/reanalysis_bpp_16211/", 
	                    "id": 16211, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 248.0, 
	                        "q0_reads": 4445264, 
	                        "q0_bases": "1103257610", 
	                        "q20_reads": 4445264, 
	                        "q20_bases": "1020939246", 
	                        "q20_mean_read_length": 238, 
	                        "id": 10132, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "reanalysis_bpp", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 248.0, 
	                        "q0_reads": 4445264, 
	                        "q0_bases": "1103257610", 
	                        "q20_reads": 4445264, 
	                        "q20_bases": "1020939246", 
	                        "q20_mean_read_length": 238, 
	                        "id": 10132, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16211/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 4176098, 
	                        "aveKeyCounts": 61.0, 
	                        "id": 12932, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 240
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }, 
	                {
	                    "status": "Completed", 
	                    "processedflows": 520, 
	                    "analysis_metrics": {
	                        "ignored": 675500, 
	                        "lib": 7825432, 
	                        "total_wells": 12862464, 
	                        "pinned": 148930, 
	                        "live": 7876394, 
	                        "excluded": 1559456, 
	                        "bead": 7883235, 
	                        "resource_uri": "", 
	                        "id": 12096, 
	                        "empty": 2595343, 
	                        "libFinal": 4445247
	                    }, 
	                    "timeStamp": "2013-11-12T22:47:52.000328+00:00", 
	                    "analysismetrics": {
	                        "ignored": 675500, 
	                        "lib": 7825432, 
	                        "total_wells": 12862464, 
	                        "pinned": 148930, 
	                        "live": 7876394, 
	                        "excluded": 1559456, 
	                        "bead": 7883235, 
	                        "resource_uri": "", 
	                        "id": 12096, 
	                        "empty": 2595343, 
	                        "libFinal": 4445247
	                    }, 
	                    "reportLink": "/output17/IonEast/Auto_user_ZIR-84--R181550-chef_Pi10_s1_kit_lot-mlm_12451_16176/", 
	                    "id": 16176, 
	                    "reportStatus": "Nothing", 
	                    "quality_metrics": {
	                        "q0_mean_read_length": 248.0, 
	                        "q0_reads": 4445247, 
	                        "q0_bases": "1103120511", 
	                        "q20_reads": 4445247, 
	                        "q20_bases": "1020893630", 
	                        "q20_mean_read_length": 238, 
	                        "id": 10104, 
	                        "resource_uri": ""
	                    }, 
	                    "resultsName": "Auto_user_ZIR-84--R181550-chef_Pi10_s1_kit_lot-mlm_12451", 
	                    "projects": [
	                        {
	                            "resource_uri": "", 
	                            "id": 162, 
	                            "name": "Chef_kit_AOO", 
	                            "modified": "2013-11-08T15:20:20.000568+00:00"
	                        }
	                    ], 
	                    "qualitymetrics": {
	                        "q0_mean_read_length": 248.0, 
	                        "q0_reads": 4445247, 
	                        "q0_bases": "1103120511", 
	                        "q20_reads": 4445247, 
	                        "q20_bases": "1020893630", 
	                        "q20_mean_read_length": 238, 
	                        "id": 10104, 
	                        "resource_uri": ""
	                    }, 
	                    "eas": {
	                        "resource_uri": "", 
	                        "reference": "e_coli_dh10b", 
	                        "barcodeKitName": ""
	                    }, 
	                    "resource_uri": "/rundb/api/v1/compositeresult/16176/", 
	                    "libmetrics": {
	                        "i100Q20_reads": 4176859, 
	                        "aveKeyCounts": 61.0, 
	                        "id": 12899, 
	                        "resource_uri": "", 
	                        "q20_mean_alignment_length": 240
	                    }, 
	                    "autoExempt": false, 
	                    "representative": false
	                }
	            ], 
	            "library": "e_coli_dh10b", 
	            "sample": "E134809-build_2-L2899", 
	            "runMode": "", 
	            "storage_options": "D", 
	            "id": 12451, 
	            "archived": false, 
	            "barcodeId": "", 
	            "sampleSetName": "", 
	            "star": false, 
	            "resultDate": "2014-01-28T22:05:05.000864+00:00", 
	            "flows": 520, 
	            "plan": {
	                "runType": "WGNM", 
	                "id": 44360, 
	                "resource_uri": ""
	            }, 
	            "date": "2013-11-12T16:47:58+00:00", 
	            "ftpStatus": "Complete", 
	            "notes": "1T build 2 Lib2899 255bp lr3_lot1434687 Pi10 s1 chef kit reagent lot 2", 
	            "chipDescription": "318", 
	            "pgmName": "Zirm", 
	            "keep": false, 
	            "expName": "R_2013_11_12_11_47_58_user_ZIR-84--R181550-chef_Pi10_s1_kit_lot-mlm", 
	            "resource_uri": "/rundb/api/v1/compositeexperiment/12451/"
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

