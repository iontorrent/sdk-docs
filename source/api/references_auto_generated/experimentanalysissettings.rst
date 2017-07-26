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
**ionstatsargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isEditable**                        Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**              Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**results**                           Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a            true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**               Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailalignmentargs**            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailanalysisargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                            false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                             {}             true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                             standard_recal false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**reference**                         Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isOneTimeOverride**                 Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**analysisargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailcalibrateargs**            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                             {}             true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a            true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**barcodeKitName**                    Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**beadfindargs**                      Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**threePrimeAdapter**                 Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailbasecallerargs**           Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**status**                            Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**prebasecallerargs**                 Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailionstatsargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**prethumbnailbasecallerargs**        Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**alignmentargs**                     Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a            true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKitName**                    Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**thumbnailbeadfindargs**             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**calibrateargs**                     Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**libraryKitBarcode**                 Unicode string data. Ex: "Hello World"                                                             n/a            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                            true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**basecallerargs**                    Unicode string data. Ex: "Hello World"                                                                            false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**custom_args**                       Boolean data. Ex: True                                                                             false          false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- -------------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a            false    true     false false  string   
===================================== ================================================================================================== ============== ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 86, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/experimentanalysissettings/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "ionstatsargs": "", 
	            "isEditable": true, 
	            "hotSpotRegionBedFile": "", 
	            "results": [], 
	            "mixedTypeRNA_reference": null, 
	            "mixedTypeRNA_targetRegionBedFile": null, 
	            "targetRegionBedFile": "", 
	            "thumbnailalignmentargs": "", 
	            "thumbnailanalysisargs": "", 
	            "id": 2, 
	            "barcodedSamples": {}, 
	            "base_recalibration_mode": "standard_recal", 
	            "reference": "", 
	            "isOneTimeOverride": false, 
	            "mixedTypeRNA_hotSpotRegionBedFile": null, 
	            "analysisargs": "", 
	            "thumbnailcalibrateargs": "", 
	            "realign": false, 
	            "selectedPlugins": {}, 
	            "experiment": "/rundb/api/v1/experiment/2/", 
	            "barcodeKitName": "", 
	            "beadfindargs": "", 
	            "threePrimeAdapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "thumbnailbasecallerargs": "", 
	            "status": "planned", 
	            "prebasecallerargs": "", 
	            "thumbnailionstatsargs": "", 
	            "prethumbnailbasecallerargs": "", 
	            "alignmentargs": "", 
	            "isDuplicateReads": false, 
	            "libraryKey": "TCAG", 
	            "date": "2017-03-08T16:27:32.000442+00:00", 
	            "libraryKitName": "Ion Xpress Plus Fragment Library Kit", 
	            "thumbnailbeadfindargs": "", 
	            "calibrateargs": "", 
	            "tfKey": "ATCG", 
	            "libraryKitBarcode": null, 
	            "sseBedFile": "", 
	            "basecallerargs": "", 
	            "custom_args": false, 
	            "resource_uri": "/rundb/api/v1/experimentanalysissettings/2/"
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

