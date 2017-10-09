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
	            "defaultSeqKit": {
	                "isActive": true, 
	                "samplePrep_instrumentType": "", 
	                "templatingSize": "", 
	                "kitType": "SequencingKit", 
	                "description": "Precision ID S5 Sequencing Kit", 
	                "name": "precisionIDS5Kit", 
	                "nucleotideType": "", 
	                "instrumentType": "S5", 
	                "chipTypes": "", 
	                "runMode": "", 
	                "parts": [
	                    {
	                        "barcode": "100041073B", 
	                        "id": 20236, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20236/", 
	                        "kit": "/rundb/api/v1/kitinfo/20111/"
	                    }, 
	                    {
	                        "barcode": "100041074B", 
	                        "id": 20237, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20237/", 
	                        "kit": "/rundb/api/v1/kitinfo/20111/"
	                    }, 
	                    {
	                        "barcode": "A33208", 
	                        "id": 20260, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20260/", 
	                        "kit": "/rundb/api/v1/kitinfo/20111/"
	                    }, 
	                    {
	                        "barcode": "100049484", 
	                        "id": 20263, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20263/", 
	                        "kit": "/rundb/api/v1/kitinfo/20111/"
	                    }
	                ], 
	                "flowCount": 650, 
	                "applicationType": "AMPS", 
	                "uid": "SEQ0028", 
	                "libraryReadLength": 0, 
	                "resource_uri": "/rundb/api/v1/kitinfo/20111/", 
	                "id": 20111, 
	                "categories": "filter_s5HidKit", 
	                "defaultFlowOrder": null
	            }, 
	            "defaultBarcodeKitName": null, 
	            "isHotSpotBEDFileBySampleSupported": true, 
	            "id": 20024, 
	            "isTargetRegionBEDFileBySampleSupported": true, 
	            "isReferenceSelectionSupported": true, 
	            "productCode": "AMPS_HID_S5_530", 
	            "applicationGroup": {
	                "name": "HID", 
	                "description": "Human Identification", 
	                "applications": [
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
	                    }
	                ], 
	                "uid": "APPLGROUP_0008", 
	                "id": 8, 
	                "isActive": true, 
	                "resource_uri": "/rundb/api/v1/applicationgroup/8/"
	            }, 
	            "isControlSeqTypeBySampleSupported": false, 
	            "defaultChipType": "530", 
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
	            "instrumentType": "s5", 
	            "isDefault": false, 
	            "isTargetTechniqueSelectionSupported": true, 
	            "description": "", 
	            "isHotspotRegionBEDFileSuppported": true, 
	            "isVisible": false, 
	            "productName": "AMPS_HID_S5_530", 
	            "isBarcodeKitSelectionRequired": false, 
	            "isDefaultBarcoded": false, 
	            "isTargetRegionBEDFileSelectionRequiredForRefSelection": true, 
	            "defaultTargetRegionBedFileName": "", 
	            "isActive": false, 
	            "isReferenceBySampleSupported": true, 
	            "defaultFlowCount": 1000, 
	            "defaultLibKit": {
	                "isActive": true, 
	                "samplePrep_instrumentType": "IC", 
	                "templatingSize": "", 
	                "kitType": "LibraryPrepKit", 
	                "description": "Precision ID Chef DL8", 
	                "name": "Ion Chef HID Library V2", 
	                "nucleotideType": "", 
	                "instrumentType": "", 
	                "chipTypes": "", 
	                "runMode": "", 
	                "parts": [
	                    {
	                        "barcode": "A32926C", 
	                        "id": 20245, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20245/", 
	                        "kit": "/rundb/api/v1/kitinfo/20105/"
	                    }, 
	                    {
	                        "barcode": "A33212", 
	                        "id": 20261, 
	                        "resource_uri": "/rundb/api/v1/kitpart/20261/", 
	                        "kit": "/rundb/api/v1/kitinfo/20105/"
	                    }
	                ], 
	                "flowCount": 0, 
	                "applicationType": "AMPS", 
	                "uid": "LPREP0003", 
	                "libraryReadLength": 0, 
	                "resource_uri": "/rundb/api/v1/kitinfo/20105/", 
	                "id": 20105, 
	                "categories": "filter_s5HidKit", 
	                "defaultFlowOrder": null
	            }, 
	            "barcodeKitSelectableType": "all", 
	            "isDefaultForInstrumentType": false, 
	            "defaultGenomeRefName": "hg19", 
	            "defaultSamplePrepKit": null, 
	            "defaultControlSeqKit": null, 
	            "defaultIonChefPrepKit": "/rundb/api/v1/kitinfo/20106/", 
	            "resource_uri": "/rundb/api/v1/applproduct/20024/", 
	            "defaultIonChefSequencingKit": null, 
	            "defaultTemplateKit": "/rundb/api/v1/kitinfo/20106/"
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

