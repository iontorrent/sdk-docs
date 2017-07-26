.. _api_reference_applproduct:

Appl Product  Resource
======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/applproduct/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/applproduct/schema/``
| 

.. include:: ../references_manual_extras/applproduct.rst

Resource Fields
---------------

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

Example Response
^^^^^^^^^^^^^^^^

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
	            "defaultSeqKit": null, 
	            "defaultBarcodeKitName": "RNA_Barcode_None", 
	            "isHotSpotBEDFileBySampleSupported": true, 
	            "id": 20021, 
	            "isTargetRegionBEDFileBySampleSupported": true, 
	            "isReferenceSelectionSupported": true, 
	            "productCode": "AMPS_RNA_2", 
	            "applicationGroup": {
	                "name": "RNA", 
	                "description": "RNA", 
	                "applications": [
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/2/"
	                        ], 
	                        "description": "RNA Sequencing", 
	                        "nucleotideType": "rna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "RNA Sequencing", 
	                        "runType": "RNA", 
	                        "id": 5, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/5/"
	                    }, 
	                    {
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/2/", 
	                            "/rundb/api/v1/applicationgroup/5/", 
	                            "/rundb/api/v1/applicationgroup/9/"
	                        ], 
	                        "description": "AmpliSeq RNA", 
	                        "nucleotideType": "rna", 
	                        "barcode": "", 
	                        "meta": {}, 
	                        "alternate_name": "AmpliSeq RNA", 
	                        "runType": "AMPS_RNA", 
	                        "id": 6, 
	                        "isActive": true, 
	                        "resource_uri": "/rundb/api/v1/runtype/6/"
	                    }
	                ], 
	                "uid": "APPLGROUP_0002", 
	                "id": 2, 
	                "isActive": true, 
	                "resource_uri": "/rundb/api/v1/applicationgroup/2/"
	            }, 
	            "isControlSeqTypeBySampleSupported": false, 
	            "defaultChipType": null, 
	            "appl": {
	                "applicationGroups": [
	                    "/rundb/api/v1/applicationgroup/2/", 
	                    "/rundb/api/v1/applicationgroup/5/", 
	                    "/rundb/api/v1/applicationgroup/9/"
	                ], 
	                "description": "AmpliSeq RNA", 
	                "nucleotideType": "rna", 
	                "barcode": "", 
	                "meta": {}, 
	                "alternate_name": "AmpliSeq RNA", 
	                "runType": "AMPS_RNA", 
	                "id": 6, 
	                "isActive": true, 
	                "resource_uri": "/rundb/api/v1/runtype/6/"
	            }, 
	            "categories": "", 
	            "instrumentType": "s5", 
	            "isDefault": true, 
	            "isTargetTechniqueSelectionSupported": true, 
	            "description": "", 
	            "isHotspotRegionBEDFileSuppported": false, 
	            "isVisible": false, 
	            "productName": "AMPS_RNA_S5_S5XL_default", 
	            "isBarcodeKitSelectionRequired": false, 
	            "isDefaultBarcoded": true, 
	            "isTargetRegionBEDFileSelectionRequiredForRefSelection": true, 
	            "defaultTargetRegionBedFileName": "", 
	            "isActive": true, 
	            "isReferenceBySampleSupported": true, 
	            "defaultFlowCount": 500, 
	            "defaultLibKit": null, 
	            "barcodeKitSelectableType": "rna", 
	            "isDefaultForInstrumentType": true, 
	            "defaultGenomeRefName": "", 
	            "defaultSamplePrepKit": null, 
	            "defaultControlSeqKit": null, 
	            "defaultIonChefPrepKit": null, 
	            "resource_uri": "/rundb/api/v1/applproduct/20021/", 
	            "defaultIonChefSequencingKit": null, 
	            "defaultTemplateKit": null
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

