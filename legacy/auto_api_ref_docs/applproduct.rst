Applproduct Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/applproduct/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/applproduct/schema/``


.. include:: ../manual_api_ref_docs/applproduct.rst

Fields table
------------

========================================================= ============================================================================== ======= ======== ======== ===== ====== ======= 
field                                                     help text                                                                      default nullable readonly blank unique type    
========================================================= ============================================================================== ======= ======== ======== ===== ====== ======= 
**isDualNucleotideTypeBySampleSupported**                 Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultHotSpotRegionBedFileName**                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileSupported**                        Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isSamplePrepKitSupported**                              Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultSeqKit**                                         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultBarcodeKitName**                                 Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isHotSpotBEDFileBySampleSupported**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                                                    Integer data. Ex: 2673                                                                 false    false    true  true   integer 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileBySampleSupported**                Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isReferenceSelectionSupported**                         Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**productCode**                                           Unicode string data. Ex: "Hello World"                                         any     false    false    false true   string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**applicationGroup**                                      A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isControlSeqTypeBySampleSupported**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultChipType**                                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**appl**                                                  A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**categories**                                            Unicode string data. Ex: "Hello World"                                                 true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**instrumentType**                                        Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefault**                                             Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetTechniqueSelectionSupported**                   Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**description**                                           Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isHotspotRegionBEDFileSuppported**                      Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isVisible**                                             Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**productName**                                           Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isBarcodeKitSelectionRequired**                         Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefaultBarcoded**                                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileSelectionRequiredForRefSelection** Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultTargetRegionBedFileName**                        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isActive**                                              Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isReferenceBySampleSupported**                          Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultFlowCount**                                      Integer data. Ex: 2673                                                         0       false    false    false false  integer 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultLibKit**                                         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**barcodeKitSelectableType**                              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefaultForInstrumentType**                            Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultGenomeRefName**                                  Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultSamplePrepKit**                                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultControlSeqKit**                                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultIonChefPrepKit**                                 A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**                                          Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultIonChefSequencingKit**                           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultTemplateKit**                                    A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
========================================================= ============================================================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/applproduct/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/applproduct/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	applproducts = ts_api_response["objects"]
	
	for applproduct in applproducts:
	    print applproduct
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 49, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/applproduct/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isDualNucleotideTypeBySampleSupported": false, 
	            "defaultHotSpotRegionBedFileName": "", 
	            "isTargetRegionBEDFileSupported": true, 
	            "isSamplePrepKitSupported": true, 
	            "defaultSeqKit": {
	                "isActive": true, 
	                "samplePrep_instrumentType": "", 
	                "templatingSize": "", 
	                "kitType": "SequencingKit", 
	                "description": "Ion PGM Sequencing 200 Kit v2", 
	                "name": "IonPGM200Kit-v2", 
	                "nucleotideType": "", 
	                "instrumentType": "pgm", 
	                "chipTypes": "", 
	                "runMode": "", 
	                "parts": [
	                    {
	                        "barcode": "4482006", 
	                        "id": 20054, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20054/", 
	                        "kit": "/rundb/api/v1/kitinfo/20033/"
	                    }, 
	                    {
	                        "barcode": "4482007", 
	                        "id": 20055, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20055/", 
	                        "kit": "/rundb/api/v1/kitinfo/20033/"
	                    }, 
	                    {
	                        "barcode": "4482008", 
	                        "id": 20056, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20056/", 
	                        "kit": "/rundb/api/v1/kitinfo/20033/"
	                    }, 
	                    {
	                        "barcode": "4482009", 
	                        "id": 20057, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20057/", 
	                        "kit": "/rundb/api/v1/kitinfo/20033/"
	                    }
	                ], 
	                "flowCount": 500, 
	                "applicationType": "", 
	                "uid": "SEQ0009", 
	                "libraryReadLength": 0, 
	                "resource_uri": "/rundb/api/v1/kitinfo/20033/", 
	                "id": 20033, 
	                "categories": "readLengthDerivableFromFlows;", 
	                "defaultFlowOrder": null
	            }, 
	            "defaultBarcodeKitName": null, 
	            "isHotSpotBEDFileBySampleSupported": true, 
	            "id": 20001, 
	            "isTargetRegionBEDFileBySampleSupported": true, 
	            "isReferenceSelectionSupported": true, 
	            "productCode": "AMPS_0", 
	            "applicationGroup": {
	                "name": "DNA", 
	                "description": "DNA", 
	                "applications": [
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/1/", 
	                            "/rundb/api/v1/applicationgroup/3/", 
	                            "/rundb/api/v1/applicationgroup/4/"
	                        ], 
	                        "description": "Generic Sequencing", 
	                        "nucleotideType": "", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "Other", 
	                        "runType": "GENS", 
	                        "id": 1, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/1/"
	                    }, 
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/1/", 
	                            "/rundb/api/v1/applicationgroup/6/", 
	                            "/rundb/api/v1/applicationgroup/8/"
	                        ], 
	                        "description": "AmpliSeq DNA", 
	                        "nucleotideType": "dna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "AmpliSeq DNA", 
	                        "runType": "AMPS", 
	                        "id": 2, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/2/"
	                    }, 
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/1/"
	                        ], 
	                        "description": "TargetSeq", 
	                        "nucleotideType": "dna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "TargetSeq", 
	                        "runType": "TARS", 
	                        "id": 3, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/3/"
	                    }, 
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/1/", 
	                            "/rundb/api/v1/applicationgroup/4/"
	                        ], 
	                        "description": "Whole Genome", 
	                        "nucleotideType": "dna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "Whole Genome", 
	                        "runType": "WGNM", 
	                        "id": 4, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/4/"
	                    }, 
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/1/"
	                        ], 
	                        "description": "AmpliSeq Exome", 
	                        "nucleotideType": "dna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "AmpliSeq Exome", 
	                        "runType": "AMPS_EXOME", 
	                        "id": 7, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/7/"
	                    }
	                ], 
	                "uid": "APPLGROUP_0001", 
	                "id": 1, 
	                "isActive": true, 
	                "resource_uri": "/rundb/api/v1/applicationgroup/1/"
	            }, 
	            "isControlSeqTypeBySampleSupported": false, 
	            "defaultChipType": null, 
	            "appl": {
	                "applicationGroups": [
	                    "/rundb/api/v1/applicationgroup/1/", 
	                    "/rundb/api/v1/applicationgroup/6/", 
	                    "/rundb/api/v1/applicationgroup/8/"
	                ], 
	                "description": "AmpliSeq DNA", 
	                "nucleotideType": "dna", 
	                "barcode": "", 
	                "meta": {}, 
	                "alternate_name": "AmpliSeq DNA", 
	                "runType": "AMPS", 
	                "id": 2, 
	                "isActive": true, 
	                "resource_uri": "/rundb/api/v1/runtype/2/"
	            }, 
	            "categories": "", 
	            "instrumentType": "pgm", 
	            "isDefault": true, 
	            "isTargetTechniqueSelectionSupported": true, 
	            "description": "", 
	            "isHotspotRegionBEDFileSuppported": true, 
	            "isVisible": true, 
	            "productName": "AMPS_default", 
	            "isBarcodeKitSelectionRequired": false, 
	            "isDefaultBarcoded": false, 
	            "isTargetRegionBEDFileSelectionRequiredForRefSelection": true, 
	            "defaultTargetRegionBedFileName": "", 
	            "isActive": true, 
	            "isReferenceBySampleSupported": true, 
	            "defaultFlowCount": 500, 
	            "defaultLibKit": {
	                "isActive": true, 
	                "samplePrep_instrumentType": "", 
	                "templatingSize": "", 
	                "kitType": "LibraryKit", 
	                "description": "Ion AmpliSeq 2.0 Library Kit", 
	                "name": "Ion AmpliSeq 2.0 Library Kit", 
	                "nucleotideType": "dna", 
	                "instrumentType": "", 
	                "chipTypes": "", 
	                "runMode": "", 
	                "parts": [
	                    {
	                        "barcode": "4475345", 
	                        "id": 20034, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20034/", 
	                        "kit": "/rundb/api/v1/kitinfo/20012/"
	                    }
	                ], 
	                "flowCount": 0, 
	                "applicationType": "AMPS_ANY", 
	                "uid": "LIB0008", 
	                "libraryReadLength": 0, 
	                "resource_uri": "/rundb/api/v1/kitinfo/20012/", 
	                "id": 20012, 
	                "categories": "", 
	                "defaultFlowOrder": null
	            }, 
	            "barcodeKitSelectableType": "all", 
	            "isDefaultForInstrumentType": true, 
	            "defaultGenomeRefName": "hg19", 
	            "defaultSamplePrepKit": null, 
	            "defaultControlSeqKit": null, 
	            "defaultIonChefPrepKit": "/rundb/api/v1/kitinfo/20042/", 
	            "resource_uri": "/rundb/api/v1/applproduct/20001/", 
	            "defaultIonChefSequencingKit": "/rundb/api/v1/kitinfo/20033/", 
	            "defaultTemplateKit": "/rundb/api/v1/kitinfo/20034/"
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

