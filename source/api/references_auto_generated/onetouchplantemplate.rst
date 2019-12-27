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
**adapter**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationCategoryDisplayedName**  Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroup**                  A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName**     Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoAnalyze**                       Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodeId**                         Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**barcodedSamples**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**base_recalibration_mode**           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bedfile**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**categories**                        Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chefInfo**                          A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       {}      false    false    false false  dict     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**childPlans**                        A list of data. Ex: ['abc', 26.73, 8]                                                              []      false    false    false false  list     
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipBarcode**                       Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**chipType**                          Unicode string data. Ex: "Hello World"                                                                     false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**cycles**                            Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**date**                              A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**earlyDatFileDeletion**              Boolean data. Ex: True                                                                             false   false    true     false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**endBarcodeKitName**                 Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**expName**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**                        A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flows**                             Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**flowsInOrder**                      Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**forward3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**                                Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**irworkflow**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isCustom_kitSettings**              Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isDuplicateReads**                  Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isFavorite**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                       Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReusable**                        Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isReverseRun**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystem**                          Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**isSystemDefault**                   Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libkit**                            Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**library**                           Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryKey**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepType**                   Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryPrepTypeDisplayedName**      Unicode string data. Ex: "Hello World"                                                                     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libraryReadLength**                 Integer data. Ex: 2673                                                                             0       false    false    false false  integer  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**librarykitname**                    Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**                          Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_hotSpotRegionBedFile** Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_reference**            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**mixedTypeRNA_targetRegionBedFile**  Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**notes**                             Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**origin**                            Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentPlan**                        Unicode string data. Ex: "Hello World"                                                             None    false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planDisplayedName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecuted**                      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planExecutedDate**                  A date & time as a string. Ex: "2010-11-10T03:07:43"                                               n/a     true     false    false false  datetime 
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planGUID**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planName**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planPGM**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planStatus**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**platform**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**preAnalysis**                       Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**project**                           Unicode string data. Ex: "Hello World"                                                             n/a     false    true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qcValues**                          Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**realign**                           Boolean data. Ex: True                                                                             n/a     false    false    false false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**regionfile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**                      Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse3primeadapter**              Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverse_primer**                    Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reverselibrarykey**                 Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runMode**                           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runType**                           Unicode string data. Ex: "Hello World"                                                             GENS    false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runname**                           Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sample**                            Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleDisplayedName**               Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGrouping**                    A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleGroupingName**                Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**samplePrepProtocol**                Unicode string data. Ex: "Hello World"                                                                     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSetDisplayedName**            Unicode string data. Ex: "Hello World"                                                             n/a     true     true     true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleSets**                        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     true     false    true  false  related  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**                   Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**selectedPlugins**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                     Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sequencekitname**                   Unicode string data. Ex: "Hello World"                                                                     true     false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sseBedFile**                        Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storageHost**                       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**storage_options**                   Unicode string data. Ex: "Hello World"                                                             A       false    false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**              Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**templatingKitName**                 Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfKey**                             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**                   Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                    Boolean data. Ex: True                                                                             true    false    false    true  false  boolean  
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**username**                          Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**variantfrequency**                  Unicode string data. Ex: "Hello World"                                                                     false    true     false false  string   
===================================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/onetouchplantemplate/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 36
	    },
	    "objects": [
	        {
	            "adapter": null,
	            "alignmentargs": "",
	            "analysisargs": "",
	            "applicationCategoryDisplayedName": "",
	            "applicationGroup": "/rundb/api/v1/applicationgroup/6/",
	            "applicationGroupDisplayedName": "Pharmacogenomics",
	            "autoAnalyze": true,
	            "autoName": null,
	            "barcodeId": "IonXpress",
	            "barcodedSamples": {},
	            "base_recalibration_mode": "standard_recal",
	            "basecallerargs": "",
	            "beadfindargs": "",
	            "bedfile": "/results/uploads/BED/5/hg19/unmerged/detail/PGx.20150728.designed.bed",
	            "calibrateargs": "",
	            "categories": "",
	            "chefInfo": {},
	            "childPlans": [],
	            "chipBarcode": "",
	            "chipType": "",
	            "controlSequencekitname": "",
	            "custom_args": false,
	            "cycles": null,
	            "date": "2018-02-08T19:41:44.000698+00:00",
	            "earlyDatFileDeletion": false,
	            "endBarcodeKitName": "",
	            "expName": "",
	            "experiment": "/rundb/api/v1/experiment/122/",
	            "flows": 500,
	            "flowsInOrder": "",
	            "forward3primeadapter": "ATCACCGACTGCCCATAGAGAGGCTGAGAC",
	            "id": 130,
	            "ionstatsargs": "",
	            "irworkflow": "",
	            "isCustom_kitSettings": false,
	            "isDuplicateReads": false,
	            "isFavorite": false,
	            "isPlanGroup": false,
	            "isReusable": true,
	            "isReverseRun": false,
	            "isSystem": false,
	            "isSystemDefault": false,
	            "libkit": null,
	            "library": "hg19",
	            "libraryKey": "TCAG",
	            "libraryPrepType": "",
	            "libraryPrepTypeDisplayedName": "",
	            "libraryReadLength": 0,
	            "librarykitname": "Ion AmpliSeq 2.0 Library Kit",
	            "metaData": {},
	            "mixedTypeRNA_hotSpotRegionBedFile": null,
	            "mixedTypeRNA_reference": null,
	            "mixedTypeRNA_targetRegionBedFile": null,
	            "notes": "",
	            "origin": "ampliseq.com|5.8.0",
	            "pairedEndLibraryAdapterName": "",
	            "parentPlan": null,
	            "planDisplayedName": "PGx Research Panel",
	            "planExecuted": false,
	            "planExecutedDate": null,
	            "planGUID": "7489c32d-d3ed-4cc1-a7a2-e59b819ea395",
	            "planName": "PGx_Research_Panel",
	            "planPGM": null,
	            "planShortID": "OO9C5",
	            "planStatus": "planned",
	            "platform": "PGM",
	            "preAnalysis": true,
	            "prebasecallerargs": "",
	            "prethumbnailbasecallerargs": "",
	            "project": "",
	            "projects": [],
	            "qcValues": [],
	            "realign": false,
	            "regionfile": "/results/uploads/BED/15/hg19/unmerged/detail/PGx.20180131.hotspots.bed",
	            "resource_uri": "/rundb/api/v1/onetouchplantemplate/130/",
	            "reverse3primeadapter": "",
	            "reverse_primer": null,
	            "reverselibrarykey": "",
	            "runMode": "",
	            "runType": "AMPS",
	            "runname": null,
	            "sample": "",
	            "sampleDisplayedName": "",
	            "sampleGrouping": null,
	            "sampleGroupingName": "",
	            "samplePrepKitName": null,
	            "samplePrepProtocol": "",
	            "sampleSetDisplayedName": "",
	            "sampleSets": [],
	            "sampleTubeLabel": null,
	            "selectedPlugins": {
	                "variantCaller": {
	                    "ampliSeqVariantCallerConfig": {
	                        "freebayes": {
	                            "allow_complex": 0,
	                            "allow_indels": 1,
	                            "allow_mnps": 1,
	                            "allow_snps": 1,
	                            "gen_min_alt_allele_freq": "0.15",
	                            "gen_min_coverage": 10,
	                            "gen_min_indel_alt_allele_freq": "0.15",
	                            "min_mapping_qv": 4,
	                            "read_max_mismatch_fraction": 1,
	                            "read_snp_limit": 10
	                        },
	                        "long_indel_assembler": {
	                            "kmer_len": 19,
	                            "max_hp_length": 8,
	                            "min_indel_size": 4,
	                            "min_var_count": 5,
	                            "min_var_freq": "0.15",
	                            "output_mnv": 0,
	                            "relative_strand_bias": "0.8",
	                            "short_suffix_match": 5
	                        },
	                        "meta": {
	                            "built_in": true,
	                            "compatibility": {
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            },
	                            "configuration": "PGx_germline_low_stringency",
	                            "name": "PGx - Germ Line - Customized parameters",
	                            "repository_id": "",
	                            "tooltip": "Panel-optimized parameters from AmpliSeq.com",
	                            "ts_version": "5.0",
	                            "tvcargs": "tvc --use-input-allele-only",
	                            "user_selections": {
	                                "chip": "pgm",
	                                "frequency": "germline",
	                                "library": "ampliseq",
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }
	                        },
	                        "torrent_variant_caller": {
	                            "data_quality_stringency": "6.5",
	                            "do_mnp_realignment": 1,
	                            "do_snp_realignment": 1,
	                            "downsample_to_coverage": 4000,
	                            "filter_deletion_predictions": "0.2",
	                            "filter_insertion_predictions": "0.4",
	                            "filter_unusual_predictions": "0.7",
	                            "heavy_tailed": 3,
	                            "hotspot_min_allele_freq": "0.1",
	                            "hotspot_min_cov_each_strand": 3,
	                            "hotspot_min_coverage": 6,
	                            "hotspot_min_variant_score": 4,
	                            "hotspot_strand_bias": "0.98",
	                            "hotspot_strand_bias_pval": "0.01",
	                            "hp_max_length": 10,
	                            "indel_as_hpindel": 0,
	                            "indel_min_allele_freq": "0.1",
	                            "indel_min_cov_each_strand": 5,
	                            "indel_min_coverage": 15,
	                            "indel_min_variant_score": 10,
	                            "indel_strand_bias": "0.85",
	                            "indel_strand_bias_pval": 1,
	                            "mnp_min_allele_freq": "0.1",
	                            "mnp_min_cov_each_strand": 0,
	                            "mnp_min_coverage": 6,
	                            "mnp_min_variant_score": 10,
	                            "mnp_strand_bias": "0.95",
	                            "mnp_strand_bias_pval": 1,
	                            "outlier_probability": "0.01",
	                            "position_bias": "0.75",
	                            "position_bias_pval": "0.05",
	                            "position_bias_ref_fraction": "0.05",
	                            "prediction_precision": 1,
	                            "process_input_positions_only": 1,
	                            "realignment_threshold": 1,
	                            "snp_min_allele_freq": "0.1",
	                            "snp_min_cov_each_strand": 0,
	                            "snp_min_coverage": 6,
	                            "snp_min_variant_score": 10,
	                            "snp_strand_bias": "0.95",
	                            "snp_strand_bias_pval": 1,
	                            "suppress_recalibration": 0,
	                            "use_position_bias": 0
	                        }
	                    },
	                    "features": [],
	                    "id": 36,
	                    "name": "variantCaller",
	                    "userInput": {
	                        "freebayes": {
	                            "allow_complex": 0,
	                            "allow_indels": 1,
	                            "allow_mnps": 1,
	                            "allow_snps": 1,
	                            "gen_min_alt_allele_freq": "0.15",
	                            "gen_min_coverage": 10,
	                            "gen_min_indel_alt_allele_freq": "0.15",
	                            "min_mapping_qv": 4,
	                            "read_max_mismatch_fraction": 1,
	                            "read_snp_limit": 10
	                        },
	                        "long_indel_assembler": {
	                            "kmer_len": 19,
	                            "max_hp_length": 8,
	                            "min_indel_size": 4,
	                            "min_var_count": 5,
	                            "min_var_freq": "0.15",
	                            "output_mnv": 0,
	                            "relative_strand_bias": "0.8",
	                            "short_suffix_match": 5
	                        },
	                        "meta": {
	                            "built_in": true,
	                            "compatibility": {
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            },
	                            "configuration": "PGx_germline_low_stringency",
	                            "name": "PGx - Germ Line - Customized parameters",
	                            "repository_id": "",
	                            "tooltip": "Panel-optimized parameters from AmpliSeq.com",
	                            "ts_version": "5.0",
	                            "tvcargs": "tvc --use-input-allele-only",
	                            "user_selections": {
	                                "chip": "pgm",
	                                "frequency": "germline",
	                                "library": "ampliseq",
	                                "panel": "/rundb/api/v1/contentupload/15/"
	                            }
	                        },
	                        "torrent_variant_caller": {
	                            "data_quality_stringency": "6.5",
	                            "do_mnp_realignment": 1,
	                            "do_snp_realignment": 1,
	                            "downsample_to_coverage": 4000,
	                            "filter_deletion_predictions": "0.2",
	                            "filter_insertion_predictions": "0.4",
	                            "filter_unusual_predictions": "0.7",
	                            "heavy_tailed": 3,
	                            "hotspot_min_allele_freq": "0.1",
	                            "hotspot_min_cov_each_strand": 3,
	                            "hotspot_min_coverage": 6,
	                            "hotspot_min_variant_score": 4,
	                            "hotspot_strand_bias": "0.98",
	                            "hotspot_strand_bias_pval": "0.01",
	                            "hp_max_length": 10,
	                            "indel_as_hpindel": 0,
	                            "indel_min_allele_freq": "0.1",
	                            "indel_min_cov_each_strand": 5,
	                            "indel_min_coverage": 15,
	                            "indel_min_variant_score": 10,
	                            "indel_strand_bias": "0.85",
	                            "indel_strand_bias_pval": 1,
	                            "mnp_min_allele_freq": "0.1",
	                            "mnp_min_cov_each_strand": 0,
	                            "mnp_min_coverage": 6,
	                            "mnp_min_variant_score": 10,
	                            "mnp_strand_bias": "0.95",
	                            "mnp_strand_bias_pval": 1,
	                            "outlier_probability": "0.01",
	                            "position_bias": "0.75",
	                            "position_bias_pval": "0.05",
	                            "position_bias_ref_fraction": "0.05",
	                            "prediction_precision": 1,
	                            "process_input_positions_only": 1,
	                            "realignment_threshold": 1,
	                            "snp_min_allele_freq": "0.1",
	                            "snp_min_cov_each_strand": 0,
	                            "snp_min_coverage": 6,
	                            "snp_min_variant_score": 10,
	                            "snp_strand_bias": "0.95",
	                            "snp_strand_bias_pval": 1,
	                            "suppress_recalibration": 0,
	                            "use_position_bias": 0
	                        }
	                    },
	                    "version": "5.8.0.19"
	                }
	            },
	            "seqKitBarcode": null,
	            "sequencekitname": "IonPGMHiQ",
	            "sseBedFile": "",
	            "storageHost": null,
	            "storage_options": "A",
	            "templatingKitBarcode": null,
	            "templatingKitName": "Ion PGM Hi-Q OT2 Kit - 200",
	            "tfKey": "ATCG",
	            "thumbnailalignmentargs": "",
	            "thumbnailanalysisargs": "",
	            "thumbnailbasecallerargs": "",
	            "thumbnailbeadfindargs": "",
	            "thumbnailcalibrateargs": "",
	            "thumbnailionstatsargs": "",
	            "usePostBeadfind": true,
	            "usePreBeadfind": true,
	            "username": "ionuser",
	            "variantfrequency": ""
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

