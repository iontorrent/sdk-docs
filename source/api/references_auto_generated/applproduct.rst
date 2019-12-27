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
**appl**                                                  A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**applicationGroup**                                      A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**barcodeKitSelectableType**                              Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**categories**                                            Unicode string data. Ex: "Hello World"                                                 true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultBarcodeKitName**                                 Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultChipType**                                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultControlSeqKit**                                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultFlowCount**                                      Integer data. Ex: 2673                                                         0       false    false    false false  integer 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultGenomeRefName**                                  Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultHotSpotRegionBedFileName**                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultIonChefPrepKit**                                 A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultIonChefSequencingKit**                           A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultLibKit**                                         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultSamplePrepKit**                                  A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultSeqKit**                                         A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultTargetRegionBedFileName**                        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**defaultTemplateKit**                                    A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    false false  related 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**description**                                           Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**dualBarcodingRule**                                     Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                                                    Integer data. Ex: 2673                                                                 false    false    true  true   integer 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**instrumentType**                                        Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isActive**                                              Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isBarcodeKitSelectionRequired**                         Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isControlSeqTypeBySampleSupported**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefault**                                             Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefaultBarcoded**                                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDefaultForInstrumentType**                            Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDualBarcodingBySampleSupported**                      Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isDualNucleotideTypeBySampleSupported**                 Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isHotSpotBEDFileBySampleSupported**                     Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isHotspotRegionBEDFileSuppported**                      Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isReferenceBySampleSupported**                          Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isReferenceSelectionSupported**                         Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isSamplePrepKitSupported**                              Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileBySampleSupported**                Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileSelectionRequiredForRefSelection** Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetRegionBEDFileSupported**                        Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isTargetTechniqueSelectionSupported**                   Boolean data. Ex: True                                                         true    false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**isVisible**                                             Boolean data. Ex: True                                                         false   false    false    true  false  boolean 
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**productCode**                                           Unicode string data. Ex: "Hello World"                                         any     false    false    false true   string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**productName**                                           Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
--------------------------------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**                                          Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
========================================================= ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/applproduct/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 59
	    },
	    "objects": [
	        {
	            "appl": {
	                "alternate_name": "AmpliSeq HD - DNA and Fusions (Single Library)",
	                "applicationGroups": [
	                    "/rundb/api/v1/applicationgroup/11/"
	                ],
	                "barcode": "",
	                "description": "AmpliSeq HD - DNA and Fusions (Single Library)",
	                "id": 15,
	                "isActive": true,
	                "meta": {},
	                "nucleotideType": "dna",
	                "resource_uri": "/rundb/api/v1/runtype/15/",
	                "runType": "AMPS_HD_DNA_RNA_1"
	            },
	            "applicationGroup": {
	                "applications": [
	                    {
	                        "alternate_name": "AmpliSeq HD - DNA and Fusions (Single Library)",
	                        "applicationGroups": [
	                            "/rundb/api/v1/applicationgroup/11/"
	                        ],
	                        "barcode": "",
	                        "description": "AmpliSeq HD - DNA and Fusions (Single Library)",
	                        "id": 15,
	                        "isActive": true,
	                        "meta": {},
	                        "nucleotideType": "dna",
	                        "resource_uri": "/rundb/api/v1/runtype/15/",
	                        "runType": "AMPS_HD_DNA_RNA_1"
	                    }
	                ],
	                "description": "DNA and Fusions (Single Library)",
	                "id": 11,
	                "isActive": true,
	                "name": "DNA + RNA 1",
	                "resource_uri": "/rundb/api/v1/applicationgroup/11/",
	                "uid": "APPLGROUP_0011"
	            },
	            "barcodeKitSelectableType": "all",
	            "categories": "",
	            "defaultBarcodeKitName": null,
	            "defaultChipType": "540",
	            "defaultControlSeqKit": null,
	            "defaultFlowCount": 500,
	            "defaultGenomeRefName": "hg19",
	            "defaultHotSpotRegionBedFileName": "",
	            "defaultIonChefPrepKit": "/rundb/api/v1/kitinfo/20083/",
	            "defaultIonChefSequencingKit": null,
	            "defaultLibKit": {
	                "applicationType": "AMPS_HD_DNA;AMPS_HD_RNA;AMPS_HD_DNA_RNA;AMPS_HD_DNA_RNA_1",
	                "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	                "cartridgeExpirationDayLimit": null,
	                "categories": "",
	                "chipTypes": "",
	                "defaultCartridgeUsageCount": null,
	                "defaultFlowOrder": null,
	                "description": "Ion AmpliSeq HD Library Kit",
	                "flowCount": 0,
	                "id": 20114,
	                "instrumentType": "",
	                "isActive": true,
	                "kitType": "LibraryKit",
	                "libraryReadLength": 0,
	                "name": "Ion AmpliSeq HD Library Kit",
	                "nucleotideType": "",
	                "parts": [],
	                "resource_uri": "/rundb/api/v1/kitinfo/20114/",
	                "runMode": "",
	                "samplePrep_instrumentType": "",
	                "uid": "LIB0027"
	            },
	            "defaultSamplePrepKit": null,
	            "defaultSeqKit": {
	                "applicationType": "",
	                "cartridgeBetweenUsageAbsoluteMaxDayLimit": null,
	                "cartridgeExpirationDayLimit": null,
	                "categories": "s5v1Kit;flowOverridable;",
	                "chipTypes": "",
	                "defaultCartridgeUsageCount": null,
	                "defaultFlowOrder": null,
	                "description": "Ion S5 Sequencing Kit",
	                "flowCount": 500,
	                "id": 20088,
	                "instrumentType": "S5",
	                "isActive": true,
	                "kitType": "SequencingKit",
	                "libraryReadLength": 0,
	                "name": "Ion S5 Sequencing Kit",
	                "nucleotideType": "",
	                "parts": [
	                    {
	                        "barcode": "100031412",
	                        "id": 20173,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20173/"
	                    },
	                    {
	                        "barcode": "100031090",
	                        "id": 20174,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20174/"
	                    },
	                    {
	                        "barcode": "100031096",
	                        "id": 20175,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20175/"
	                    },
	                    {
	                        "barcode": "A27767",
	                        "id": 20195,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20195/"
	                    },
	                    {
	                        "barcode": "A27768",
	                        "id": 20196,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20196/"
	                    },
	                    {
	                        "barcode": "100033230",
	                        "id": 20202,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20202/"
	                    },
	                    {
	                        "barcode": "100031091B",
	                        "id": 20238,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20238/"
	                    },
	                    {
	                        "barcode": "INS1012841B",
	                        "id": 20239,
	                        "kit": "/rundb/api/v1/kitinfo/20088/",
	                        "resource_uri": "/rundb/api/v1/kitpart/20239/"
	                    }
	                ],
	                "resource_uri": "/rundb/api/v1/kitinfo/20088/",
	                "runMode": "",
	                "samplePrep_instrumentType": "",
	                "uid": "SEQ0023"
	            },
	            "defaultTargetRegionBedFileName": "",
	            "defaultTemplateKit": null,
	            "description": "",
	            "dualBarcodingRule": "",
	            "id": 20059,
	            "instrumentType": "s5",
	            "isActive": true,
	            "isBarcodeKitSelectionRequired": false,
	            "isControlSeqTypeBySampleSupported": false,
	            "isDefault": true,
	            "isDefaultBarcoded": false,
	            "isDefaultForInstrumentType": false,
	            "isDualBarcodingBySampleSupported": false,
	            "isDualNucleotideTypeBySampleSupported": false,
	            "isHotSpotBEDFileBySampleSupported": true,
	            "isHotspotRegionBEDFileSuppported": true,
	            "isReferenceBySampleSupported": true,
	            "isReferenceSelectionSupported": true,
	            "isSamplePrepKitSupported": true,
	            "isTargetRegionBEDFileBySampleSupported": true,
	            "isTargetRegionBEDFileSelectionRequiredForRefSelection": true,
	            "isTargetRegionBEDFileSupported": true,
	            "isTargetTechniqueSelectionSupported": true,
	            "isVisible": true,
	            "productCode": "AMPS_HD_DNA_RNA_1",
	            "productName": "AMPS_HD_DNA_RNA_1_default",
	            "resource_uri": "/rundb/api/v1/applproduct/20059/"
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

