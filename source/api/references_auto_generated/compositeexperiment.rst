.. _api_reference_compositeexperiment:

Composite Experiment  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/mesh/v1/compositeexperiment/``
| Schema URL ``http://mytorrentserver/rundb/api/mesh/v1/compositeexperiment/schema/``
| 

.. include:: ../references_manual_extras/compositeexperiment.rst

Resource Fields
---------------

========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                      help text                                                                                          default nullable readonly blank unique type     
========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**_host**                  Host this resource is located on.                                                                  n/a     false    true     false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefReagentsSerialNum**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefSolutionsSerialNum** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefStartTime**          A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**               Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                   A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     false    false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**displayName**            Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**ftpStatus**              Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                     Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                  Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pgmName**                Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**plan**                   A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**               Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**repResult**              A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultDate**             A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    true     false    false false  datetime 
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**results**                Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**star**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**                 Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
-------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**        Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
========================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/mesh/v1/compositeexperiment/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 146
	    },
	    "objects": [
	        {
	            "_host": "hawk.itw",
	            "applicationCategoryDisplayedName": "AmpliSeq DNA and Fusions",
	            "barcodeId": "IonCode Barcodes 1-32",
	            "barcodedSamples": {},
	            "chefReagentsSerialNum": "",
	            "chefSolutionsSerialNum": "",
	            "chefStartTime": null,
	            "chipDescription": "540",
	            "chipInstrumentType": "S5",
	            "chipType": "540",
	            "date": "2019-10-03T22:24:50+00:00",
	            "displayName": "user S16-754-R153458-540 DNA33-RNA18 OCAv3 AO-1002",
	            "expName": "R_2019_10_03_15_23_03_user_S16-754-R153458-540_DNA33-RNA18_OCAv3_AO-1002",
	            "flows": 400,
	            "ftpStatus": "Complete",
	            "id": 1800,
	            "keep": false,
	            "library": "hg19",
	            "notes": "",
	            "pgmName": "S16",
	            "plan": {
	                "id": 1808,
	                "resource_uri": "",
	                "runType": "AMPS_DNA_RNA",
	                "sampleTubeLabel": null
	            },
	            "platform": "S5",
	            "references": "hg19",
	            "repResult": "/rundb/api/v1/compositeresult/1921/",
	            "resource_uri": "/rundb/api/mesh/v1/compositeexperiment/1800/",
	            "resultDate": "2019-10-04T02:55:43.000359+00:00",
	            "results": [
	                {
	                    "analysis_metrics": {
	                        "bead": 144205030,
	                        "empty": 5365643,
	                        "excluded": 13159848,
	                        "id": 1785,
	                        "ignored": 1554120,
	                        "lib": 143117241,
	                        "libFinal": 72109222,
	                        "live": 144191568,
	                        "pinned": 414495,
	                        "resource_uri": "",
	                        "total_wells": 164699136
	                    },
	                    "analysismetrics": {
	                        "bead": 144205030,
	                        "empty": 5365643,
	                        "excluded": 13159848,
	                        "id": 1785,
	                        "ignored": 1554120,
	                        "lib": 143117241,
	                        "libFinal": 72109222,
	                        "live": 144191568,
	                        "pinned": 414495,
	                        "resource_uri": "",
	                        "total_wells": 164699136
	                    },
	                    "autoExempt": false,
	                    "eas": {
	                        "barcodeKitName": "IonCode Barcodes 1-32",
	                        "chipType": "540",
	                        "isPQ": false,
	                        "reference": "hg19",
	                        "references": "hg19",
	                        "resource_uri": ""
	                    },
	                    "i18nstatus": {
	                        "i18n": "Completed",
	                        "state": "Completed"
	                    },
	                    "id": 1920,
	                    "isShowAllMetrics": true,
	                    "libmetrics": {
	                        "aveKeyCounts": 100,
	                        "i100Q20_reads": 32512585,
	                        "id": 1632,
	                        "q20_mean_alignment_length": 98,
	                        "resource_uri": ""
	                    },
	                    "processedflows": 0,
	                    "projects": [
	                        {
	                            "id": 179,
	                            "modified": "2019-10-04T22:30:21.000322+00:00",
	                            "name": "Valkyrie",
	                            "resource_uri": ""
	                        }
	                    ],
	                    "quality_metrics": {
	                        "id": 1633,
	                        "q0_bases": "8055445299",
	                        "q0_mean_read_length": 111.714116247485,
	                        "q0_reads": 72107676,
	                        "q20_bases": "7144330852",
	                        "q20_mean_read_length": 111,
	                        "q20_reads": 72107676,
	                        "resource_uri": ""
	                    },
	                    "qualitymetrics": {
	                        "id": 1633,
	                        "q0_bases": "8055445299",
	                        "q0_mean_read_length": 111.714116247485,
	                        "q0_reads": 72107676,
	                        "q20_bases": "7144330852",
	                        "q20_mean_read_length": 111,
	                        "q20_reads": 72107676,
	                        "resource_uri": ""
	                    },
	                    "reportLink": "/output/Home/Auto_user_S16-754-R153458-540_DNA33-RNA18_OCAv3_AO-1002_1800_1920/",
	                    "reportStatus": "Nothing",
	                    "representative": false,
	                    "resource_uri": "/rundb/api/v1/compositeresult/1920/",
	                    "resultsName": "Auto_user_S16-754-R153458-540_DNA33-RNA18_OCAv3_AO-1002_1800",
	                    "status": "Completed",
	                    "status_display": "Completed",
	                    "timeStamp": "2019-10-04T02:55:43.000359+00:00"
	                },
	                {
	                    "analysis_metrics": {
	                        "bead": 882703,
	                        "empty": 30634,
	                        "excluded": 39760,
	                        "id": 1784,
	                        "ignored": 6104,
	                        "lib": 876208,
	                        "libFinal": 440446,
	                        "live": 882647,
	                        "pinned": 799,
	                        "resource_uri": "",
	                        "total_wells": 960000
	                    },
	                    "analysismetrics": {
	                        "bead": 882703,
	                        "empty": 30634,
	                        "excluded": 39760,
	                        "id": 1784,
	                        "ignored": 6104,
	                        "lib": 876208,
	                        "libFinal": 440446,
	                        "live": 882647,
	                        "pinned": 799,
	                        "resource_uri": "",
	                        "total_wells": 960000
	                    },
	                    "autoExempt": false,
	                    "eas": {
	                        "barcodeKitName": "IonCode Barcodes 1-32",
	                        "chipType": "540",
	                        "isPQ": false,
	                        "reference": "hg19",
	                        "references": "hg19",
	                        "resource_uri": ""
	                    },
	                    "i18nstatus": {
	                        "i18n": "Completed",
	                        "state": "Completed"
	                    },
	                    "id": 1921,
	                    "isShowAllMetrics": true,
	                    "libmetrics": {
	                        "aveKeyCounts": 104,
	                        "i100Q20_reads": 195606,
	                        "id": 1631,
	                        "q20_mean_alignment_length": 98,
	                        "resource_uri": ""
	                    },
	                    "processedflows": 400,
	                    "projects": [
	                        {
	                            "id": 179,
	                            "modified": "2019-10-04T22:30:21.000322+00:00",
	                            "name": "Valkyrie",
	                            "resource_uri": ""
	                        }
	                    ],
	                    "quality_metrics": {
	                        "id": 1632,
	                        "q0_bases": "49082942",
	                        "q0_mean_read_length": 111.441965329731,
	                        "q0_reads": 440435,
	                        "q20_bases": "43452424",
	                        "q20_mean_read_length": 111,
	                        "q20_reads": 440435,
	                        "resource_uri": ""
	                    },
	                    "qualitymetrics": {
	                        "id": 1632,
	                        "q0_bases": "49082942",
	                        "q0_mean_read_length": 111.441965329731,
	                        "q0_reads": 440435,
	                        "q20_bases": "43452424",
	                        "q20_mean_read_length": 111,
	                        "q20_reads": 440435,
	                        "resource_uri": ""
	                    },
	                    "reportLink": "/output/Home/Auto_user_S16-754-R153458-540_DNA33-RNA18_OCAv3_AO-1002_1800_tn_1921/",
	                    "reportStatus": "Nothing",
	                    "representative": false,
	                    "resource_uri": "/rundb/api/v1/compositeresult/1921/",
	                    "resultsName": "Auto_user_S16-754-R153458-540_DNA33-RNA18_OCAv3_AO-1002_1800_tn",
	                    "status": "Completed",
	                    "status_display": "Completed",
	                    "timeStamp": "2019-10-04T00:39:45.000429+00:00"
	                }
	            ],
	            "runMode": "single",
	            "sample": "",
	            "sampleDisplayedName": "",
	            "sampleSetName": "",
	            "star": false,
	            "status": "run",
	            "storage_options": "A"
	        }
	    ],
	    "warnings": [
	        "The Torrent Server(s) phuket.itw,hawk.itw have too many results to display. Only experiments newer than 2018-10-26 are displayed. Try searching or adding additional filters.",
	        "Could not fetch runs from Torrent Server(s) tsautotest17.itw!"
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

