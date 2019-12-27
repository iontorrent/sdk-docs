.. _api_reference_experimentanalysissettings:

Experiment Analysis Settings  Resource
======================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/experimentanalysissettings/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/experimentanalysissettings/schema/``
| 

.. include:: ../references_manual_extras/experimentanalysissettings.rst

Resource Fields
---------------

===================================== ================================================================================================== ============== ======== ======== ===== ====== ======== 
field                                 help text                                                                                          default        nullable readonly blank unique type     
===================================== ================================================================================================== ============== ======== ======== ===== ====== ======== 
**alignmentargs**                     Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**analysisargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**barcodeKitName**                    Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                             {}             true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                             standard_recal false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**basecallerargs**                    Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**beadfindargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**calibrateargs**                     Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**custom_args**                       Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a            true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**endBarcodeKitName**                 Unicode string data. Ex: "Hello World"                                                                            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a            true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**              Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                            false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**ionstatsargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isEditable**                        Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isOneTimeOverride**                 Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKitBarcode**                 Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKitName**                    Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**prebasecallerargs**                 Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**prethumbnailbasecallerargs**        Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**reference**                         Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a            false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**results**                           Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a            true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                             {}             true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**status**                            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**               Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**threePrimeAdapter**                 Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailalignmentargs**            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailanalysisargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailbasecallerargs**           Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailbeadfindargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailcalibrateargs**            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailionstatsargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
===================================== ================================================================================================== ============== ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/experimentanalysissettings/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 136
	    },
	    "objects": [
	        {
	            "alignmentargs": "",
	            "analysisargs": "",
	            "barcodeKitName": "Ion Dual Barcode Kit 1-96",
	            "barcodedSamples": {},
	            "base_recalibration_mode": "standard_recal",
	            "basecallerargs": "",
	            "beadfindargs": "",
	            "calibrateargs": "",
	            "custom_args": false,
	            "date": "2019-10-03T20:53:08.000599+00:00",
	            "endBarcodeKitName": "",
	            "experiment": "/rundb/api/v1/experiment/163/",
	            "hotSpotRegionBedFile": "",
	            "id": 162,
	            "ionstatsargs": "",
	            "isDuplicateReads": false,
	            "isEditable": true,
	            "isOneTimeOverride": false,
	            "libraryKey": "TCAG",
	            "libraryKitBarcode": null,
	            "libraryKitName": "Ion AmpliSeq Library Kit Plus",
	            "mixedTypeRNA_hotSpotRegionBedFile": null,
	            "mixedTypeRNA_reference": null,
	            "mixedTypeRNA_targetRegionBedFile": null,
	            "prebasecallerargs": "",
	            "prethumbnailbasecallerargs": "",
	            "realign": false,
	            "reference": "",
	            "resource_uri": "/rundb/api/v1/experimentanalysissettings/162/",
	            "results": [],
	            "selectedPlugins": {},
	            "sseBedFile": "",
	            "status": "inactive",
	            "targetRegionBedFile": "",
	            "tfKey": "ATCG",
	            "threePrimeAdapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC",
	            "thumbnailalignmentargs": "",
	            "thumbnailanalysisargs": "",
	            "thumbnailbasecallerargs": "",
	            "thumbnailbeadfindargs": "",
	            "thumbnailcalibrateargs": "",
	            "thumbnailionstatsargs": ""
	        }
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

