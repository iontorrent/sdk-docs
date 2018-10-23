.. _api_reference_onetouchplantemplate:

Onetouch Plan Template  Resource
================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/onetouchplantemplate/schema/``
| 

.. include:: ../references_manual_extras/onetouchplantemplate.rst

Resource Fields
---------------

===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field                                 help text                                                                                          default nullable readonly blank unique type     
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**planDisplayedName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                       Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endBarcodeKitName**                 Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                       Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                        Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                            Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                   Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                          Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**                 Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                    Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**adapter**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**earlyDatFileDeletion**              Boolean data. Ex: True                                                                             false   false    true     false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                        Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**     Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                          Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                           Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                        A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                 Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInfo**                          A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       {}      false    false    false false  dict     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                  A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                             Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                          Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**                  Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**                   Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                       Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                    Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName**      Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 37, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/onetouchplantemplate/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "planDisplayedName": "PGx Research Panel", 
	            "autoAnalyze": true, 
	            "endBarcodeKitName": "", 
	            "templatingKitBarcode": null, 
	            "preAnalysis": true, 
	            "thumbnailanalysisargs": "", 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/6/", 
	            "mixedTypeRNA_hotSpotRegionBedFile": null, 
	            "mixedTypeRNA_targetRegionBedFile": null, 
	            "platform": "PGM", 
	            "categories": "", 
	            "planPGM": null, 
	            "prebasecallerargs": "", 
	            "alignmentargs": "", 
	            "thumbnailbasecallerargs": "", 
	            "libkit": null, 
	            "projects": [], 
	            "notes": "", 
	            "sequencekitname": "IonPGMHiQ", 
	            "base_recalibration_mode": "standard_recal", 
	            "storageHost": null, 
	            "expName": "", 
	            "thumbnailionstatsargs": "", 
	            "cycles": null, 
	            "isReverseRun": false, 
	            "storage_options": "A", 
	            "thumbnailalignmentargs": "", 
	            "chipType": "", 
	            "library": "hg19", 
	            "runMode": "", 
	            "sampleTubeLabel": null, 
	            "seqKitBarcode": null, 
	            "barcodeId": "IonXpress", 
	            "isPlanGroup": false, 
	            "realign": false, 
	            "sampleGroupingName": "", 
	            "experiment": "/rundb/api/v1/experiment/122/", 
	            "bedfile": "/results/uploads/BED/5/hg19/unmerged/detail/PGx.20150728.designed.bed", 
	            "applicationCategoryDisplayedName": "", 
	            "isReusable": true, 
	            "isDuplicateReads": false, 
	            "sampleSets": [], 
	            "thumbnailbeadfindargs": "", 
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit", 
	            "sseBedFile": "", 
	            "adapter": null, 
	            "basecallerargs": "", 
	            "earlyDatFileDeletion": false, 
	            "parentPlan": null, 
	            "origin": "ampliseq.com|5.8.0", 
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC", 
	            "planStatus": "planned", 
	            "isCustom_kitSettings": false, 
	            "samplePrepKitName": null, 
	            "applicationGroupDisplayedName": "Pharmacogenomics", 
	            "metaData": {}, 
	            "isFavorite": false, 
	            "qcValues": [], 
	            "analysisargs": "", 
	            "thumbnailcalibrateargs": "", 
	            "templatingKitName": "Ion PGM Hi-Q OT2 Kit - 200", 
	            "runType": "AMPS", 
	            "username": "ionuser", 
	            "planShortID": "OO9C5", 
	            "sampleDisplayedName": "", 
	            "prethumbnailbasecallerargs": "", 
	            "controlSequencekitname": "", 
	            "tfKey": "ATCG", 
	            "mixedTypeRNA_reference": null, 
	            "childPlans": [], 
	            "pairedEndLibraryAdapterName": "", 
	            "reverselibrarykey": "", 
	            "irworkflow": "", 
	            "planExecuted": false, 
	            "project": "", 
	            "usePostBeadfind": true, 
	            "libraryReadLength": 0, 
	            "runname": null, 
	            "chefInfo": {}, 
	            "planGUID": "7489c32d-d3ed-4cc1-a7a2-e59b819ea395", 
	            "ionstatsargs": "", 
	            "samplePrepProtocol": "", 
	            "sample": "", 
	            "planExecutedDate": null, 
	            "reverse_primer": null, 
	            "id": 130, 
	            "barcodedSamples": {}, 
	            "custom_args": false, 
	            "regionfile": "/results/uploads/BED/15/hg19/unmerged/detail/PGx.20180131.hotspots.bed", 
	            "selectedPlugins": {
	                "variantCaller": {
	                    "features": [], 
	                    "ampliSeqVariantCallerConfig": {
	                        "torrent_variant_caller": {
	                            "snp_min_allele_freq": "0.1", 
	                            "snp_strand_bias": "0.95", 
	                            "hotspot_min_coverage": 6, 
	                            "hotspot_min_cov_each_strand": 3, 
	                            "position_bias": "0.75", 
	                            "hotspot_min_allele_freq": "0.1", 
	                            "snp_min_variant_score": 10, 
	                            "mnp_min_variant_score": 10, 
	                            "hotspot_strand_bias": "0.98", 
	                            "hp_max_length": 10, 
	                            "filter_insertion_predictions": "0.4", 
	                            "indel_min_variant_score": 10, 
	                            "indel_min_coverage": 15, 
	                            "heavy_tailed": 3, 
	                            "outlier_probability": "0.01", 
	                            "position_bias_ref_fraction": "0.05", 
	                            "indel_strand_bias_pval": 1, 
	                            "data_quality_stringency": "6.5", 
	                            "snp_min_cov_each_strand": 0, 
	                            "indel_as_hpindel": 0, 
	                            "snp_strand_bias_pval": 1, 
	                            "mnp_strand_bias": "0.95", 
	                            "mnp_strand_bias_pval": 1, 
	                            "process_input_positions_only": 1, 
	                            "hotspot_strand_bias_pval": "0.01", 
	                            "hotspot_min_variant_score": 4, 
	                            "do_mnp_realignment": 1, 
	                            "indel_strand_bias": "0.85", 
	                            "downsample_to_coverage": 4000, 
	                            "filter_unusual_predictions": "0.7", 
	                            "indel_min_allele_freq": "0.1", 
	                            "mnp_min_allele_freq": "0.1", 
	                            "mnp_min_coverage": 6, 
	                            "do_snp_realignment": 1, 
	                            "mnp_min_cov_each_strand": 0, 
	                            "snp_min_coverage": 6, 
	                            "prediction_precision": 1, 
	                            "indel_min_cov_each_strand": 5, 
	                            "filter_deletion_predictions": "0.2", 
	                            "realignment_threshold": 1, 
	                            "suppress_recalibration": 0, 
	                            "position_bias_pval": "0.05", 
	                            "use_position_bias": 0
	                        }, 
	                        "meta": {
	                            "repository_id": "", 
	                            "ts_version": "5.0", 
	                            "name": "PGx - Germ Line - Customized parameters", 
	                            "user_selections": {
	                                "chip": "pgm", 
	                                "frequency": "germline", 
	                                "library": "ampliseq", 
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }, 
	                            "tooltip": "Panel-optimized parameters from AmpliSeq.com", 
	                            "tvcargs": "tvc --use-input-allele-only", 
	                            "built_in": true, 
	                            "configuration": "PGx_germline_low_stringency", 
	                            "compatibility": {
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }
	                        }, 
	                        "long_indel_assembler": {
	                            "min_indel_size": 4, 
	                            "short_suffix_match": 5, 
	                            "output_mnv": 0, 
	                            "min_var_count": 5, 
	                            "min_var_freq": "0.15", 
	                            "kmer_len": 19, 
	                            "max_hp_length": 8, 
	                            "relative_strand_bias": "0.8"
	                        }, 
	                        "freebayes": {
	                            "gen_min_coverage": 10, 
	                            "allow_mnps": 1, 
	                            "allow_complex": 0, 
	                            "read_snp_limit": 10, 
	                            "read_max_mismatch_fraction": 1, 
	                            "allow_indels": 1, 
	                            "min_mapping_qv": 4, 
	                            "gen_min_alt_allele_freq": "0.15", 
	                            "allow_snps": 1, 
	                            "gen_min_indel_alt_allele_freq": "0.15"
	                        }
	                    }, 
	                    "userInput": {
	                        "torrent_variant_caller": {
	                            "snp_min_allele_freq": "0.1", 
	                            "snp_strand_bias": "0.95", 
	                            "hotspot_min_coverage": 6, 
	                            "hotspot_min_cov_each_strand": 3, 
	                            "position_bias": "0.75", 
	                            "hotspot_min_allele_freq": "0.1", 
	                            "snp_min_variant_score": 10, 
	                            "mnp_min_variant_score": 10, 
	                            "hotspot_strand_bias": "0.98", 
	                            "hp_max_length": 10, 
	                            "filter_insertion_predictions": "0.4", 
	                            "indel_min_variant_score": 10, 
	                            "indel_min_coverage": 15, 
	                            "heavy_tailed": 3, 
	                            "outlier_probability": "0.01", 
	                            "position_bias_ref_fraction": "0.05", 
	                            "indel_strand_bias_pval": 1, 
	                            "data_quality_stringency": "6.5", 
	                            "snp_min_cov_each_strand": 0, 
	                            "indel_as_hpindel": 0, 
	                            "snp_strand_bias_pval": 1, 
	                            "mnp_strand_bias": "0.95", 
	                            "mnp_strand_bias_pval": 1, 
	                            "process_input_positions_only": 1, 
	                            "hotspot_strand_bias_pval": "0.01", 
	                            "hotspot_min_variant_score": 4, 
	                            "do_mnp_realignment": 1, 
	                            "indel_strand_bias": "0.85", 
	                            "downsample_to_coverage": 4000, 
	                            "filter_unusual_predictions": "0.7", 
	                            "indel_min_allele_freq": "0.1", 
	                            "mnp_min_allele_freq": "0.1", 
	                            "mnp_min_coverage": 6, 
	                            "do_snp_realignment": 1, 
	                            "mnp_min_cov_each_strand": 0, 
	                            "snp_min_coverage": 6, 
	                            "prediction_precision": 1, 
	                            "indel_min_cov_each_strand": 5, 
	                            "filter_deletion_predictions": "0.2", 
	                            "realignment_threshold": 1, 
	                            "suppress_recalibration": 0, 
	                            "position_bias_pval": "0.05", 
	                            "use_position_bias": 0
	                        }, 
	                        "meta": {
	                            "repository_id": "", 
	                            "ts_version": "5.0", 
	                            "name": "PGx - Germ Line - Customized parameters", 
	                            "user_selections": {
	                                "chip": "pgm", 
	                                "frequency": "germline", 
	                                "library": "ampliseq", 
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }, 
	                            "tooltip": "Panel-optimized parameters from AmpliSeq.com", 
	                            "tvcargs": "tvc --use-input-allele-only", 
	                            "built_in": true, 
	                            "configuration": "PGx_germline_low_stringency", 
	                            "compatibility": {
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }
	                        }, 
	                        "long_indel_assembler": {
	                            "min_indel_size": 4, 
	                            "short_suffix_match": 5, 
	                            "output_mnv": 0, 
	                            "min_var_count": 5, 
	                            "min_var_freq": "0.15", 
	                            "kmer_len": 19, 
	                            "max_hp_length": 8, 
	                            "relative_strand_bias": "0.8"
	                        }, 
	                        "freebayes": {
	                            "gen_min_coverage": 10, 
	                            "allow_mnps": 1, 
	                            "allow_complex": 0, 
	                            "read_snp_limit": 10, 
	                            "read_max_mismatch_fraction": 1, 
	                            "allow_indels": 1, 
	                            "min_mapping_qv": 4, 
	                            "gen_min_alt_allele_freq": "0.15", 
	                            "allow_snps": 1, 
	                            "gen_min_indel_alt_allele_freq": "0.15"
	                        }
	                    }, 
	                    "version": "5.8.0.19", 
	                    "id": 36, 
	                    "name": "variantCaller"
	                }
	            }, 
	            "beadfindargs": "", 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "libraryKey": "TCAG", 
	            "flows": 500, 
	            "date": "2018-02-08T19:41:44.000698+00:00", 
	            "isSystem": false, 
	            "variantfrequency": "", 
	            "planName": "PGx_Research_Panel", 
	            "calibrateargs": "", 
	            "flowsInOrder": "", 
	            "libraryPrepType": "", 
	            "sampleGrouping": null, 
	            "chipBarcode": "", 
	            "sampleSetDisplayedName": "", 
	            "usePreBeadfind": true, 
	            "resource_uri": "/rundb/api/v1/onetouchplantemplate/130/", 
	            "libraryPrepTypeDisplayedName": "", 
	            "reverse3primeadapter": ""
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

