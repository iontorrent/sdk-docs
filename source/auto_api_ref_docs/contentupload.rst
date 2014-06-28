Contentupload Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/contentupload/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/contentupload/schema/``


.. include:: ../manual_api_ref_docs/contentupload.rst

Fields table
------------

================ ====================================== ======= ======== ======== ===== ====== ======= 
field            help text                              default nullable readonly blank unique type    
================ ====================================== ======= ======== ======== ===== ====== ======= 
**status**       Unicode string data. Ex: "Hello World"         false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**meta**         Unicode string data. Ex: "Hello World" {}      false    false    true  false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**file_path**    Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri** Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
---------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**           Integer data. Ex: 2673                         false    false    true  true   integer 
================ ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/contentupload/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/contentupload/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	contentuploads = ts_api_response["objects"]
	
	for contentupload in contentuploads:
	    print contentupload
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 25, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/contentupload/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "status": "Successfully Completed", 
	            "meta": {
	                "upload_date": "2014-03-27T00:28:46", 
	                "description": "Comp Cancer Panel", 
	                "reference": "hg19", 
	                "is_ampliseq": true, 
	                "hotspot": true, 
	                "choice": "proton", 
	                "design": {
	                    "status": "ORDERABLE", 
	                    "pipeline": "DNA", 
	                    "min_number_amplicons_per_pool": 3991, 
	                    "type": "FIXED_PANEL", 
	                    "description": "<p>The Ion AmpliSeq&trade; Comprehensive Cancer Panel provides highly multiplexed target selection of genes implicated in cancer research. Encompassing over 50% of the Wellcome Trust Sanger Institute Cancer Gene Census, this is the most comprehensive cancer gene panel available. With all-exon coverage of 409 genes, the Ion AmpliSeq&trade; Comprehensive Cancer Panel delivers fast, FFPE-compatible, target selection for a broad survey of key genes for semiconductor sequencing.&nbsp; \r\n<a href=\"http://products.invitrogen.com/ivgn/product/4477685\" target=\"_blank\">Learn more<img src=\"/resources/images/linkout.png\" style=\"display:inline;margin:0\"/></a></p>\r\n\r\n<table class=\"design-template-info-wrapper-table\">\r\n    <tr class=\"design-template-statistics\">\r\n        <td><strong>COSMIC mutation targets</strong>\r\n            15,749</td>\r\n        <td><strong>Amplicon length</strong>\r\n            125&ndash;175 bp (average 155 bp)</td>\r\n        <td><strong>Primer pool size</strong>\r\n            ~16,000 primers in 4 tubes</td>\r\n        <td><strong>Input DNA required</strong>\r\n            10 ng per pool, 40 ng per DNA sample</td>\r\n        <td><strong>Read length</strong>\r\n            1 x 200</td>\r\n    </tr>\r\n</table>", 
	                    "order_number": 90, 
	                    "design_name": "Comp Cancer Panel", 
	                    "results_uri": "/ws/tmpldesign/14011153/download/results", 
	                    "pipeline_version": null, 
	                    "request_id_and_solution_ordering_id": "CCP", 
	                    "configuration_choices": [
	                        "pgm", 
	                        "proton"
	                    ], 
	                    "target_size": 1293547, 
	                    "genome": "HG19", 
	                    "solution_name": null, 
	                    "created_date": "2013-10-07T14:21:51.388+0000", 
	                    "plan": {
	                        "missed_bed": null, 
	                        "hotspot_bed": "CCP.20131001.hotspots.bed", 
	                        "coverage_summary": null, 
	                        "designed_bed": "CCP.20131001.designed.bed", 
	                        "target_mutations": null, 
	                        "primer_bed": null, 
	                        "selectedPlugins": {
	                            "variantCaller": {
	                                "features": [], 
	                                "ampliSeqVariantCallerConfig": {
	                                    "torrent_variant_caller": {
	                                        "snp_min_allele_freq": "0.02", 
	                                        "snp_strand_bias": "0.95", 
	                                        "hotspot_min_coverage": "6", 
	                                        "hotspot_min_cov_each_strand": "2", 
	                                        "hotspot_min_allele_freq": "0.01", 
	                                        "snp_min_variant_score": "6", 
	                                        "hotspot_strand_bias": "0.95", 
	                                        "hp_max_length": "8", 
	                                        "filter_insertion_predictions": "0.2", 
	                                        "indel_min_variant_score": "6", 
	                                        "indel_min_coverage": "15", 
	                                        "heavy_tailed": "3", 
	                                        "outlier_probability": "0.005", 
	                                        "data_quality_stringency": "6.5", 
	                                        "snp_min_cov_each_strand": "0", 
	                                        "hotspot_min_variant_score": "6", 
	                                        "indel_strand_bias": "0.9", 
	                                        "downsample_to_coverage": "2000", 
	                                        "filter_unusual_predictions": "0.3", 
	                                        "indel_min_allele_freq": "0.05", 
	                                        "do_snp_realignment": "1", 
	                                        "prediction_precision": "1.0", 
	                                        "indel_min_cov_each_strand": "2", 
	                                        "filter_deletion_predictions": "0.2", 
	                                        "suppress_recalibration": "0", 
	                                        "snp_min_coverage": "6"
	                                    }, 
	                                    "meta": {
	                                        "repository_id": "", 
	                                        "ts_version": "4.0", 
	                                        "name": "Panel-optimized - Comp Cancer Panel", 
	                                        "user_selections": {
	                                            "chip": "proton_p1", 
	                                            "frequency": "germline", 
	                                            "library": "ampliseq", 
	                                            "panel": "/rundb/api/v1/contentupload/48/"
	                                        }, 
	                                        "trimreads": true, 
	                                        "tooltip": "Panel-optimized parameters from AmpliSeq.com", 
	                                        "tvcargs": "tvc", 
	                                        "built_in": true, 
	                                        "configuration": "", 
	                                        "compatibility": {
	                                            "panel": "/rundb/api/v1/contentupload/48/"
	                                        }
	                                    }, 
	                                    "long_indel_assembler": {
	                                        "min_indel_size": "4", 
	                                        "short_suffix_match": "5", 
	                                        "output_mnv": "0", 
	                                        "min_var_count": "5", 
	                                        "min_var_freq": "0.15", 
	                                        "kmer_len": "19", 
	                                        "max_hp_length": "8", 
	                                        "relative_strand_bias": "0.8"
	                                    }, 
	                                    "freebayes": {
	                                        "gen_min_coverage": "6", 
	                                        "allow_mnps": "1", 
	                                        "allow_complex": "0", 
	                                        "read_max_mismatch_fraction": "1.0", 
	                                        "read_mismatch_limit": "10", 
	                                        "allow_indels": "1", 
	                                        "min_mapping_qv": "4", 
	                                        "gen_min_alt_allele_freq": "0.035", 
	                                        "allow_snps": "1", 
	                                        "gen_min_indel_alt_allele_freq": "0.1"
	                                    }
	                                }, 
	                                "userInput": {
	                                    "torrent_variant_caller": {
	                                        "snp_min_allele_freq": "0.02", 
	                                        "snp_strand_bias": "0.95", 
	                                        "hotspot_min_coverage": "6", 
	                                        "hotspot_min_cov_each_strand": "2", 
	                                        "hotspot_min_allele_freq": "0.01", 
	                                        "snp_min_variant_score": "6", 
	                                        "hotspot_strand_bias": "0.95", 
	                                        "hp_max_length": "8", 
	                                        "filter_insertion_predictions": "0.2", 
	                                        "indel_min_variant_score": "6", 
	                                        "indel_min_coverage": "15", 
	                                        "heavy_tailed": "3", 
	                                        "outlier_probability": "0.005", 
	                                        "data_quality_stringency": "6.5", 
	                                        "snp_min_cov_each_strand": "0", 
	                                        "hotspot_min_variant_score": "6", 
	                                        "indel_strand_bias": "0.9", 
	                                        "downsample_to_coverage": "2000", 
	                                        "filter_unusual_predictions": "0.3", 
	                                        "indel_min_allele_freq": "0.05", 
	                                        "do_snp_realignment": "1", 
	                                        "prediction_precision": "1.0", 
	                                        "indel_min_cov_each_strand": "2", 
	                                        "filter_deletion_predictions": "0.2", 
	                                        "suppress_recalibration": "0", 
	                                        "snp_min_coverage": "6"
	                                    }, 
	                                    "meta": {
	                                        "repository_id": "", 
	                                        "ts_version": "4.0", 
	                                        "name": "Panel-optimized - Comp Cancer Panel", 
	                                        "user_selections": {
	                                            "chip": "proton_p1", 
	                                            "frequency": "germline", 
	                                            "library": "ampliseq", 
	                                            "panel": "/rundb/api/v1/contentupload/48/"
	                                        }, 
	                                        "trimreads": true, 
	                                        "tooltip": "Panel-optimized parameters from AmpliSeq.com", 
	                                        "tvcargs": "tvc", 
	                                        "built_in": true, 
	                                        "configuration": "", 
	                                        "compatibility": {
	                                            "panel": "/rundb/api/v1/contentupload/48/"
	                                        }
	                                    }, 
	                                    "long_indel_assembler": {
	                                        "min_indel_size": "4", 
	                                        "short_suffix_match": "5", 
	                                        "output_mnv": "0", 
	                                        "min_var_count": "5", 
	                                        "min_var_freq": "0.15", 
	                                        "kmer_len": "19", 
	                                        "max_hp_length": "8", 
	                                        "relative_strand_bias": "0.8"
	                                    }, 
	                                    "freebayes": {
	                                        "gen_min_coverage": "6", 
	                                        "allow_mnps": "1", 
	                                        "allow_complex": "0", 
	                                        "read_max_mismatch_fraction": "1.0", 
	                                        "read_mismatch_limit": "10", 
	                                        "allow_indels": "1", 
	                                        "min_mapping_qv": "4", 
	                                        "gen_min_alt_allele_freq": "0.035", 
	                                        "allow_snps": "1", 
	                                        "gen_min_indel_alt_allele_freq": "0.1"
	                                    }
	                                }, 
	                                "version": "4.1-r74477", 
	                                "id": 698, 
	                                "name": "variantCaller"
	                            }
	                        }, 
	                        "coverage_detail": null, 
	                        "primer_sequences": "CCP.20131001.primerDataSheet.csv", 
	                        "runType": "AMPS", 
	                        "submitted_bed": null, 
	                        "well_plate_data": null
	                    }, 
	                    "design_id": "CCP", 
	                    "number_of_amplicons": 15992, 
	                    "id": 14011153, 
	                    "amplicons_coverage_summary": "95.349763093262169", 
	                    "number_of_amplicon_pools": 4
	                }
	            }, 
	            "file_path": "/results/uploads/BED/48/CCP.20131001.results.zip", 
	            "resource_uri": "/rundb/api/v1/contentupload/48/", 
	            "id": 48
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

