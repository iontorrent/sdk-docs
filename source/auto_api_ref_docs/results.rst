Results Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/results/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/results/schema/``


.. include:: ../manual_api_ref_docs/results.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**reference**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportstorage**   A single related resource. Can be either a URI or set of nested resource data.                     n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysisVersion** Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runid**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**filesystempath**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**        Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**libmetrics**      Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**experiment**      A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**planShortID**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedCycles** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**bamLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sffLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginState**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**qualitymetrics**  Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**       Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**eas**             A single related resource. Can be either a URI or set of nested resource data.                     n/a     true     false    true  false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfSffLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginStore**     A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}                                       n/a     false    true     false false  dict     
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsType**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfFastq**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfmetrics**       Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentIDs**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysismetrics** Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeToComplete**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**fastqLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**pluginresults**   Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**framesProcessed** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/results/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/results/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	resultss = ts_api_response["objects"]
	
	for results in resultss:
	    print results
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 37659, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/results/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "reference": "hg19", 
	            "processedflows": 0, 
	            "reportStatus": "Nothing", 
	            "reportstorage": {
	                "name": "Home", 
	                "default": true, 
	                "webServerPath": "/output", 
	                "dirPath": "/results/analysis/output", 
	                "id": 1, 
	                "resource_uri": ""
	            }, 
	            "analysisVersion": "db:4.1.22+1-1,an:4.1.25+1-1,", 
	            "runid": "D3GNK", 
	            "id": 52046, 
	            "filesystempath": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046", 
	            "metaData": {}, 
	            "log": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/log.html", 
	            "timeStamp": "2014-01-30T07:52:22.000647+00:00", 
	            "libmetrics": [
	                "/rundb/api/v1/libmetrics/31090/"
	            ], 
	            "experiment": "/rundb/api/v1/experiment/19558/", 
	            "resultsName": "Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	            "status": "Completed", 
	            "planShortID": "WC3JH", 
	            "processedCycles": 0, 
	            "bamLink": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558.bam", 
	            "sffLink": null, 
	            "representative": false, 
	            "pluginState": {
	                "coverageAnalysisLite": "Completed", 
	                "SystematicErrorAnalysis": "Completed", 
	                "1_Torrent_Accuracy": "Completed", 
	                "duplicateReads_useZC": "Completed", 
	                "autoCal": "Completed", 
	                "variantCaller": "Completed", 
	                "ConversionRate": "Completed", 
	                "validateVariantCaller": "Completed", 
	                "timingPerformance": "Completed", 
	                "coverageAnalysis": "Completed", 
	                "VariantQC": "Completed"
	            }, 
	            "qualitymetrics": [
	                "/rundb/api/v1/qualitymetrics/30474/"
	            ], 
	            "diskusage": 34288, 
	            "eas": "/rundb/api/v1/experimentanalysissettings/22034/", 
	            "tfSffLink": null, 
	            "projects": [
	                "/rundb/api/v1/project/169/"
	            ], 
	            "pluginStore": {
	                "coverageAnalysisLite": {
	                    "Non-duplicate": "", 
	                    "barcoded": "true", 
	                    "Uniquely mapped": "No", 
	                    "Targetted regions": "/results/uploads/BED/46/hg19/merged/plain/AmpliSeqExome.20131001.designed.bed", 
	                    "Target padding": "0", 
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "Bases in target regions": "57742646", 
	                            "Number of mapped reads": "25272862", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Percent reads on target": "92.46%", 
	                            "Average base coverage depth": "58.13", 
	                            "Reference (File)": "hg19", 
	                            "Coverage Analysis Lite Report": "N/A", 
	                            "Target base coverage at 100x": "15.12%", 
	                            "Target base coverage at 20x": "83.15%", 
	                            "Uniformity of base coverage": "91.28%", 
	                            "Target base coverage at 1x": "98.50%", 
	                            "Using": "All Mapped Reads", 
	                            "Target base coverage at 500x": "0.01%", 
	                            "Alignments": "IonXpress_002_R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	                            "Total base reads on target": "3356512633"
	                        }, 
	                        "IonXpress_001": {
	                            "Bases in target regions": "57742646", 
	                            "Number of mapped reads": "31765405", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Percent reads on target": "89.94%", 
	                            "Average base coverage depth": "69.79", 
	                            "Reference (File)": "hg19", 
	                            "Coverage Analysis Lite Report": "N/A", 
	                            "Target base coverage at 100x": "22.98%", 
	                            "Target base coverage at 20x": "86.67%", 
	                            "Uniformity of base coverage": "91.27%", 
	                            "Target base coverage at 1x": "98.68%", 
	                            "Using": "All Mapped Reads", 
	                            "Target base coverage at 500x": "0.02%", 
	                            "Alignments": "IonXpress_001_R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	                            "Total base reads on target": "4029869840"
	                        }
	                    }
	                }, 
	                "SystematicErrorAnalysis": {
	                    "qts_peak": "NaN", 
	                    "indel-5-per-mb": "13476.5", 
	                    "positions-with-sse": "0.011488", 
	                    "qts_base": "NaN", 
	                    "barcoded": "true", 
	                    "positions-with-sse-d15": "0.011488", 
	                    "Target-regions_file": "/results/uploads/BED/46/hg19/merged/plain/AmpliSeqExome.20131001.designed.bed", 
	                    "stb-95-per-mb": "116389.1", 
	                    "positions-with-sse-i5": "0.007905", 
	                    "positions-with-sse-d5": "0.035763", 
	                    "positions-with-sse-i15": "0.001691", 
	                    "indel-15-per-mb": "3651.4", 
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "indel-5-per-mb": "12747.1", 
	                            "positions-with-sse": "0.011331", 
	                            "positions-with-sse-d15": "0.011331", 
	                            "stb-95-per-mb": "117377.0", 
	                            "positions-with-sse-i5": "0.007448", 
	                            "positions-with-sse-d5": "0.033942", 
	                            "positions-with-sse-i15": "0.001637", 
	                            "indel-15-per-mb": "3576.5"
	                        }, 
	                        "IonXpress_001": {
	                            "indel-5-per-mb": "14205.8", 
	                            "positions-with-sse": "0.011644", 
	                            "positions-with-sse-d15": "0.011644", 
	                            "stb-95-per-mb": "115401.2", 
	                            "positions-with-sse-i5": "0.008361", 
	                            "positions-with-sse-d5": "0.037584", 
	                            "positions-with-sse-i15": "0.001746", 
	                            "indel-15-per-mb": "3726.3"
	                        }
	                    }
	                }, 
	                "1_Torrent_Accuracy": {
	                    "accuracyStats": {
	                        "Raw_Accuracy_Stats": {
	                            "Average_Read_Accuracy": "97.87901"
	                        }, 
	                        "Raw_Accuracy_per_base": {
	                            "100": "2.326"
	                        }
	                    }, 
	                    "alignFlowSignals": {
	                        "accuracy_by_true_len": {
	                            "1": {
	                                "All": "98.9324"
	                            }, 
	                            "0": {
	                                "All": "99.5156"
	                            }, 
	                            "3": {
	                                "All": "91.99"
	                            }, 
	                            "2": {
	                                "All": "96.4887"
	                            }, 
	                            "5": {
	                                "All": "79.804"
	                            }, 
	                            "4": {
	                                "All": "87.4236"
	                            }, 
	                            "6": {
	                                "All": "72.3437"
	                            }
	                        }
	                    }, 
	                    "pooled": {
	                        "kmer_indel_rates": {}, 
	                        "accuracyStats": {}, 
	                        "alignFlowSignals": {}, 
	                        "Error_vs_Coverage": {}, 
	                        "errorQV": {
	                            "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/./errorQV.png", 
	                            "data": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/./errorQV.png", 
	                            "MismatchQV23+": ""
	                        }
	                    }, 
	                    "xbenchmark": {
	                        "url_root": "http://10.33.106.11/output/Home/C11-131--R133279-reanalysis_fromWells-YF_57778", 
	                        "errorQV": {
	                            "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/errorQV.png", 
	                            "data": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/errorQV.png", 
	                            "MismatchQV23+": "0.0204726112301496"
	                        }, 
	                        "kmer_indel_rates": {
	                            "del_2_in_5_mean_1_10": {
	                                "ATAAC": "0.14286", 
	                                "TAGGC": "5.99603", 
	                                "ACAAG": "0.17857", 
	                                "ATAAG": "0.27367", 
	                                "TCTTA": "0.15625", 
	                                "AAGGC": "1.90477", 
	                                "CGTTC": "0.37231", 
	                                "AGCCA": "1.12003", 
	                                "GGCCT": "0.13333", 
	                                "AGTTC": "0.18928", 
	                                "GAGGC": "6.36439", 
	                                "CGTTA": "0.15811", 
	                                "ATAAT": "0.398", 
	                                "ACAAT": 0, 
	                                "CCTTC": "0.18733", 
	                                "CGCCT": "0.08475", 
	                                "AGCCT": "0.57224", 
	                                "TGCCT": "0.29185", 
	                                "TCGGC": "3.51575", 
	                                "ATGGC": "2.01818"
	                            }, 
	                            "pct_genome_w_err_rate_ge": {
	                                "1": "0.7689", 
	                                "10": "0.7534", 
	                                "5": "0.7689", 
	                                "20": "0.4723"
	                            }, 
	                            "detailed_report": "/results/analysis/output/Home/C11-131--R133279-reanalysis_fromWells-YF_57778/plugin_out/1_Torrent_Accuracy_out/kmer_indel_rates/complete.html", 
	                            "del_2_in_5_mean_all": {
	                                "ATAAC": "0.365256", 
	                                "TAGGC": "6.051335", 
	                                "ACAAG": "0.342822", 
	                                "ATAAG": "0.3646025", 
	                                "TCTTA": "0.188922", 
	                                "AAGGC": "3.6024785", 
	                                "CGTTC": "0.461842", 
	                                "AGCCA": "1.1749565", 
	                                "GGCCT": "0.919791", 
	                                "AGTTC": "0.7084275", 
	                                "GAGGC": "6.0490545", 
	                                "CGTTA": "0.453094", 
	                                "ATAAT": "0.4345975", 
	                                "ACAAT": "0.3509975", 
	                                "CCTTC": "0.5503275", 
	                                "CGCCT": "1.0767715", 
	                                "AGCCT": "0.9995835", 
	                                "TGCCT": "0.845587", 
	                                "TCGGC": "2.684257", 
	                                "ATGGC": "2.8624605"
	                            }, 
	                            "formatted": {
	                                "worst2mer_rate": {
	                                    "1": " 6.1", 
	                                    "3": " 3.6", 
	                                    "2": " 6.0", 
	                                    "5": " 2.7", 
	                                    "4": " 2.9"
	                                }, 
	                                "worst2mer_slope": {
	                                    "1": " 0.0", 
	                                    "3": " 0.0", 
	                                    "2": " 0.0", 
	                                    "5": " 0.0", 
	                                    "4": " 0.0"
	                                }, 
	                                "worst2mer": {
	                                    "1": "TAGGC", 
	                                    "3": "AAGGC", 
	                                    "2": "GAGGC", 
	                                    "5": "TCGGC", 
	                                    "4": "ATGGC"
	                                }
	                            }, 
	                            "plots": {
	                                "fig_2": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/kmer_indel_rates/deletions_pentamers_strand_0_start_1_end_null_characterized_norm_current_max.png", 
	                                "fig_3": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/kmer_indel_rates/errors_strand_0_start_1_end_null_hist.png", 
	                                "fig_1": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/kmer_indel_rates/deletions_pentamers_strand_0_start_1_end_null_characterized_norm_classic_max.png", 
	                                "title_1": "Classic: sequence motifs with the highest deletion rates for the previous runs", 
	                                "title_2": "Current: sequence motifs with the highest  deletion rates for the current run", 
	                                "title_3": "Effective accuracy"
	                            }, 
	                            "del_2_in_5_slope": {
	                                "ATAAC": "0.0017", 
	                                "TAGGC": "0.0222", 
	                                "ACAAG": "0.0079", 
	                                "ATAAG": "-0.0011", 
	                                "TCTTA": "-0.0000", 
	                                "AAGGC": "0.0051", 
	                                "CGTTC": "0.0036", 
	                                "AGCCA": "0.0072", 
	                                "GGCCT": "0.0090", 
	                                "AGTTC": "0.0028", 
	                                "GAGGC": "0.0324", 
	                                "CGTTA": "0.0049", 
	                                "ATAAT": "0.0034", 
	                                "ACAAT": "0.0045", 
	                                "CCTTC": "0.0013", 
	                                "CGCCT": "0.0079", 
	                                "AGCCT": "0.0006", 
	                                "TGCCT": "0.0189", 
	                                "TCGGC": "0.0115", 
	                                "ATGGC": "0.0047"
	                            }
	                        }, 
	                        "accuracyStats": {
	                            "Raw_Insertion_Error_per_base": {
	                                "150": "0.235", 
	                                "10": "0.234", 
	                                "200": "0.350", 
	                                "300": "0.000", 
	                                "50": "0.130", 
	                                "1": "0.006", 
	                                "5": "0.177", 
	                                "100": "0.165", 
	                                "250": "2.842"
	                            }, 
	                            "Mapping_Stats": {
	                                "Perc_Mapped": "99.83", 
	                                "Total_Reads": "2911232", 
	                                "Reads_Mapped": "2906170"
	                            }, 
	                            "Raw_Accuracy_per_base": {
	                                "150": "0.589", 
	                                "10": "0.381", 
	                                "200": "0.902", 
	                                "300": "0.000", 
	                                "50": "0.322", 
	                                "1": "0.416", 
	                                "5": "0.290", 
	                                "100": "0.416", 
	                                "250": "4.191"
	                            }, 
	                            "Raw_Accuracy_Stats": {
	                                "Deletions": " 1456878", 
	                                "Total_Errors": " 3415775", 
	                                "Mismatches": " 554495", 
	                                "Insertions": " 1404402", 
	                                "Average_Read_Accuracy": "99.46725", 
	                                "Total_bases_called": " 641153143"
	                            }, 
	                            "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/accuracyStats/position_error.png", 
	                            "chip_error_plots": {
	                                "total": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/chip-error-total.png", 
	                                "mismatch": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/chip-error-mismatch.png", 
	                                "insertion": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/chip-error-insertion.png", 
	                                "deletion": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/chip-error-deletion.png"
	                            }
	                        }, 
	                        "Error_vs_Coverage": {
	                            "Default": {
	                                "insertion": "3", 
	                                "detailed_report": "/mnt/ddn/ion-archive/reports/C11-131--R133279-reanalysis_fromWells-YF_57778/plugin_out/1_Torrent_Accuracy_out/Error_vs_Coverage/Error_vs_Coverage.html", 
	                                "hp": {
	                                    "10": "99", 
	                                    "1": "51", 
	                                    "3": "32.66", 
	                                    "2": "41", 
	                                    "5": "43.64", 
	                                    "4": "43.9", 
	                                    "7": "38.46", 
	                                    "6": "40.92", 
	                                    "9": "99", 
	                                    "8": "99"
	                                }, 
	                                "transition": "5", 
	                                "accuracy_percent": "0.01", 
	                                "uncovered": "74", 
	                                "transversion": "12", 
	                                "mean_coverage": "144.460", 
	                                "deletion": "389", 
	                                "bases_covered": "4639601", 
	                                "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/Error_vs_Coverage/Default.png", 
	                                "accuracy_q_score": "40.55", 
	                                "sd_coverage": "15.080", 
	                                "match": "4639195", 
	                                "percent_covered": "99.998"
	                            }
	                        }, 
	                        "alignFlowSignals": {
	                            "plots": {
	                                "posterior": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/alignFlowSignals/plot_flow_signal_accuracy_all_smooth5.png", 
	                                "likelihood": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/alignFlowSignals/plot_flow_signals_per_hp_length_all_smooth5.png", 
	                                "summary": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/benchmark/alignFlowSignals/results.png"
	                            }, 
	                            "Ratio": {
	                                "11": {
	                                    "A": "", 
	                                    "All": "", 
	                                    "C": "", 
	                                    "G": "", 
	                                    "T": ""
	                                }, 
	                                "10": {
	                                    "A": "", 
	                                    "All": "36.5306", 
	                                    "C": "70.3125", 
	                                    "G": "39.4330", 
	                                    "T": ""
	                                }, 
	                                "1": {
	                                    "A": "49.9597", 
	                                    "All": "50.0104", 
	                                    "C": "50.0138", 
	                                    "G": "50.1304", 
	                                    "T": "49.9299"
	                                }, 
	                                "0": {
	                                    "A": "0.0000", 
	                                    "All": "0.0000", 
	                                    "C": "0.0000", 
	                                    "G": "0.0000", 
	                                    "T": "0.0000"
	                                }, 
	                                "3": {
	                                    "A": "49.7233", 
	                                    "All": "49.8810", 
	                                    "C": "49.8157", 
	                                    "G": "49.8697", 
	                                    "T": "50.1239"
	                                }, 
	                                "2": {
	                                    "A": "49.7491", 
	                                    "All": "49.9373", 
	                                    "C": "49.9713", 
	                                    "G": "50.0785", 
	                                    "T": "49.8549"
	                                }, 
	                                "5": {
	                                    "A": "48.2549", 
	                                    "All": "48.5931", 
	                                    "C": "46.8858", 
	                                    "G": "46.4814", 
	                                    "T": "49.5405"
	                                }, 
	                                "4": {
	                                    "A": "49.2833", 
	                                    "All": "49.6598", 
	                                    "C": "49.2925", 
	                                    "G": "49.1938", 
	                                    "T": "50.3516"
	                                }, 
	                                "7": {
	                                    "A": "32.1035", 
	                                    "All": "34.3504", 
	                                    "C": "36.6014", 
	                                    "G": "34.0248", 
	                                    "T": "36.4671"
	                                }, 
	                                "6": {
	                                    "A": "43.2306", 
	                                    "All": "43.8991", 
	                                    "C": "41.1068", 
	                                    "G": "39.1248", 
	                                    "T": "45.2629"
	                                }, 
	                                "9": {
	                                    "A": "17.8777", 
	                                    "All": "24.5513", 
	                                    "C": "42.4779", 
	                                    "G": "19.3156", 
	                                    "T": "30.2669"
	                                }, 
	                                "8": {
	                                    "A": "23.7597", 
	                                    "All": "27.5729", 
	                                    "C": "33.0423", 
	                                    "G": "26.6166", 
	                                    "T": "31.6226"
	                                }
	                            }, 
	                            "Accuracy": {
	                                "11": {
	                                    "A": "", 
	                                    "All": "", 
	                                    "C": "", 
	                                    "G": "", 
	                                    "T": ""
	                                }, 
	                                "10": {
	                                    "A": "", 
	                                    "All": "2.3516", 
	                                    "C": "11.7647", 
	                                    "G": "70.3704", 
	                                    "T": ""
	                                }, 
	                                "1": {
	                                    "A": "99.6812", 
	                                    "All": "99.6198", 
	                                    "C": "99.6466", 
	                                    "G": "99.5257", 
	                                    "T": "99.6386"
	                                }, 
	                                "0": {
	                                    "A": "99.9590", 
	                                    "All": "99.9509", 
	                                    "C": "99.9382", 
	                                    "G": "99.9287", 
	                                    "T": "99.9747"
	                                }, 
	                                "3": {
	                                    "A": "98.5934", 
	                                    "All": "98.3423", 
	                                    "C": "97.6956", 
	                                    "G": "98.9670", 
	                                    "T": "98.1011"
	                                }, 
	                                "2": {
	                                    "A": "99.0068", 
	                                    "All": "98.9610", 
	                                    "C": "98.7072", 
	                                    "G": "99.2648", 
	                                    "T": "98.8613"
	                                }, 
	                                "5": {
	                                    "A": "94.7598", 
	                                    "All": "94.6701", 
	                                    "C": "91.4867", 
	                                    "G": "92.8750", 
	                                    "T": "95.5184"
	                                }, 
	                                "4": {
	                                    "A": "96.8685", 
	                                    "All": "96.9889", 
	                                    "C": "96.6729", 
	                                    "G": "97.5183", 
	                                    "T": "97.0222"
	                                }, 
	                                "7": {
	                                    "A": "66.9598", 
	                                    "All": "66.2874", 
	                                    "C": "63.1816", 
	                                    "G": "70.8675", 
	                                    "T": "65.4888"
	                                }, 
	                                "6": {
	                                    "A": "87.1194", 
	                                    "All": "86.4746", 
	                                    "C": "76.5840", 
	                                    "G": "78.8010", 
	                                    "T": "87.4140"
	                                }, 
	                                "9": {
	                                    "A": "13.9823", 
	                                    "All": "13.4130", 
	                                    "C": "22.3022", 
	                                    "G": "21.3198", 
	                                    "T": "12.4131"
	                                }, 
	                                "8": {
	                                    "A": "45.0883", 
	                                    "All": "44.8508", 
	                                    "C": "44.4444", 
	                                    "G": "52.0833", 
	                                    "T": "44.2733"
	                                }
	                            }
	                        }
	                    }, 
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "kmer_indel_rates": {}, 
	                            "accuracyStats": {
	                                "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/accuracyStats/position_error.png", 
	                                "Raw_Accuracy_per_base": {
	                                    "150": "2.999", 
	                                    "10": "1.228", 
	                                    "200": "3.935", 
	                                    "300": "0.000", 
	                                    "50": "1.641", 
	                                    "1": "2.888", 
	                                    "5": "1.432", 
	                                    "100": "2.289", 
	                                    "250": "6.178"
	                                }, 
	                                "Raw_Accuracy_Stats": {
	                                    "Deletions": " 26440544", 
	                                    "Total_Errors": " 70325174", 
	                                    "Mismatches": " 13319169", 
	                                    "Insertions": " 30565461", 
	                                    "Average_Read_Accuracy": "97.90875", 
	                                    "Total_bases_called": " 3362828330.0"
	                                }, 
	                                "Raw_Insertion_Error_per_base": {
	                                    "150": "1.299", 
	                                    "10": "0.588", 
	                                    "200": "1.786", 
	                                    "300": "0.000", 
	                                    "50": "0.720", 
	                                    "1": "0.028", 
	                                    "5": "0.567", 
	                                    "100": "1.006", 
	                                    "250": "2.471"
	                                }, 
	                                "Mapping_Stats": {
	                                    "Perc_Mapped": "98.16", 
	                                    "Total_Reads": "25747781", 
	                                    "Reads_Mapped": "25272862"
	                                }
	                            }, 
	                            "alignFlowSignals": {
	                                "over_signal_pct_by_true_len": {
	                                    "comment": "Over flow signal percentage as a function of true HP length", 
	                                    "10": {
	                                        "A": "25.7449", 
	                                        "All": "33.6235", 
	                                        "C": "1.3089", 
	                                        "G": "26.5836", 
	                                        "T": "41.7176"
	                                    }, 
	                                    "1": {
	                                        "A": "56.5766", 
	                                        "All": "55.1418", 
	                                        "C": "65.8831", 
	                                        "G": "48.0436", 
	                                        "T": "53.2670"
	                                    }, 
	                                    "0": {
	                                        "A": "100.0000", 
	                                        "All": "100.0000", 
	                                        "C": "100.0000", 
	                                        "G": "100.0000", 
	                                        "T": "100.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "55.3483", 
	                                        "All": "33.0502", 
	                                        "C": "23.3713", 
	                                        "G": "26.8518", 
	                                        "T": "31.1935"
	                                    }, 
	                                    "2": {
	                                        "A": "35.1311", 
	                                        "All": "32.5375", 
	                                        "C": "38.8617", 
	                                        "G": "27.1029", 
	                                        "T": "30.1486"
	                                    }, 
	                                    "5": {
	                                        "A": "45.1254", 
	                                        "All": "34.2567", 
	                                        "C": "24.8941", 
	                                        "G": "30.4924", 
	                                        "T": "38.7186"
	                                    }, 
	                                    "4": {
	                                        "A": "51.4038", 
	                                        "All": "32.5959", 
	                                        "C": "20.9998", 
	                                        "G": "32.4411", 
	                                        "T": "34.0107"
	                                    }, 
	                                    "7": {
	                                        "A": "44.0708", 
	                                        "All": "38.5105", 
	                                        "C": "12.7423", 
	                                        "G": "31.4226", 
	                                        "T": "42.3173"
	                                    }, 
	                                    "6": {
	                                        "A": "44.8184", 
	                                        "All": "35.0215", 
	                                        "C": "20.8977", 
	                                        "G": "30.5796", 
	                                        "T": "40.5679"
	                                    }, 
	                                    "9": {
	                                        "A": "38.3270", 
	                                        "All": "42.7790", 
	                                        "C": "8.0943", 
	                                        "G": "40.4817", 
	                                        "T": "47.8340"
	                                    }, 
	                                    "8": {
	                                        "A": "43.0150", 
	                                        "All": "41.6788", 
	                                        "C": "10.2239", 
	                                        "G": "34.5133", 
	                                        "T": "44.3568"
	                                    }
	                                }, 
	                                "Ratio": {
	                                    "comment": "Over call percentage as a function of called HP length", 
	                                    "10": {
	                                        "A": "58.5954", 
	                                        "All": "66.6929", 
	                                        "C": "97.0857", 
	                                        "G": "86.7561", 
	                                        "T": "69.5104"
	                                    }, 
	                                    "1": {
	                                        "A": "63.4958", 
	                                        "All": "57.1624", 
	                                        "C": "64.7164", 
	                                        "G": "51.6141", 
	                                        "T": "46.9964"
	                                    }, 
	                                    "0": {
	                                        "A": "0.0000", 
	                                        "All": "0.0000", 
	                                        "C": "0.0000", 
	                                        "G": "0.0000", 
	                                        "T": "0.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "68.1315", 
	                                        "All": "59.2990", 
	                                        "C": "53.6865", 
	                                        "G": "58.8350", 
	                                        "T": "61.5061"
	                                    }, 
	                                    "2": {
	                                        "A": "69.0308", 
	                                        "All": "58.4908", 
	                                        "C": "49.6215", 
	                                        "G": "58.5403", 
	                                        "T": "61.0299"
	                                    }, 
	                                    "5": {
	                                        "A": "81.1984", 
	                                        "All": "77.6843", 
	                                        "C": "73.3960", 
	                                        "G": "79.2822", 
	                                        "T": "75.8085"
	                                    }, 
	                                    "4": {
	                                        "A": "79.9656", 
	                                        "All": "68.4701", 
	                                        "C": "61.7122", 
	                                        "G": "60.8706", 
	                                        "T": "67.3059"
	                                    }, 
	                                    "7": {
	                                        "A": "81.2525", 
	                                        "All": "84.3374", 
	                                        "C": "93.1884", 
	                                        "G": "94.8314", 
	                                        "T": "78.7119"
	                                    }, 
	                                    "6": {
	                                        "A": "82.6672", 
	                                        "All": "84.8207", 
	                                        "C": "88.6862", 
	                                        "G": "91.8440", 
	                                        "T": "78.5978"
	                                    }, 
	                                    "9": {
	                                        "A": "63.4363", 
	                                        "All": "67.4439", 
	                                        "C": "93.7398", 
	                                        "G": "87.1106", 
	                                        "T": "66.8347"
	                                    }, 
	                                    "8": {
	                                        "A": "75.9216", 
	                                        "All": "77.8859", 
	                                        "C": "91.5543", 
	                                        "G": "93.3872", 
	                                        "T": "74.9427"
	                                    }
	                                }, 
	                                "over_call_pct_by_true_len": {
	                                    "comment": "Over call percentage as a function of true HP length", 
	                                    "10": {
	                                        "A": "25.7449", 
	                                        "All": "33.6235", 
	                                        "C": "1.3089", 
	                                        "G": "26.5836", 
	                                        "T": "41.7176"
	                                    }, 
	                                    "1": {
	                                        "A": "56.5766", 
	                                        "All": "55.1418", 
	                                        "C": "65.8831", 
	                                        "G": "48.0436", 
	                                        "T": "53.2670"
	                                    }, 
	                                    "0": {
	                                        "A": "100.0000", 
	                                        "All": "100.0000", 
	                                        "C": "100.0000", 
	                                        "G": "100.0000", 
	                                        "T": "100.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "55.3483", 
	                                        "All": "33.0502", 
	                                        "C": "23.3713", 
	                                        "G": "26.8518", 
	                                        "T": "31.1935"
	                                    }, 
	                                    "2": {
	                                        "A": "35.1311", 
	                                        "All": "32.5375", 
	                                        "C": "38.8617", 
	                                        "G": "27.1029", 
	                                        "T": "30.1486"
	                                    }, 
	                                    "5": {
	                                        "A": "45.1254", 
	                                        "All": "34.2567", 
	                                        "C": "24.8941", 
	                                        "G": "30.4924", 
	                                        "T": "38.7186"
	                                    }, 
	                                    "4": {
	                                        "A": "51.4038", 
	                                        "All": "32.5959", 
	                                        "C": "20.9998", 
	                                        "G": "32.4411", 
	                                        "T": "34.0107"
	                                    }, 
	                                    "7": {
	                                        "A": "44.0708", 
	                                        "All": "38.5105", 
	                                        "C": "12.7423", 
	                                        "G": "31.4226", 
	                                        "T": "42.3173"
	                                    }, 
	                                    "6": {
	                                        "A": "44.8184", 
	                                        "All": "35.0215", 
	                                        "C": "20.8977", 
	                                        "G": "30.5796", 
	                                        "T": "40.5679"
	                                    }, 
	                                    "9": {
	                                        "A": "38.3270", 
	                                        "All": "42.7790", 
	                                        "C": "8.0943", 
	                                        "G": "40.4817", 
	                                        "T": "47.8340"
	                                    }, 
	                                    "8": {
	                                        "A": "43.0150", 
	                                        "All": "41.6788", 
	                                        "C": "10.2239", 
	                                        "G": "34.5133", 
	                                        "T": "44.3568"
	                                    }
	                                }, 
	                                "accuracy_by_true_len": {
	                                    "comment": "Accuracy as a function of true HP length", 
	                                    "10": {
	                                        "A": "41.8341", 
	                                        "All": "43.9815", 
	                                        "C": "14.7321", 
	                                        "G": "35.8855", 
	                                        "T": "46.4496"
	                                    }, 
	                                    "1": {
	                                        "A": "99.0711", 
	                                        "All": "98.9508", 
	                                        "C": "99.0513", 
	                                        "G": "98.6233", 
	                                        "T": "99.0372"
	                                    }, 
	                                    "0": {
	                                        "A": "99.5409", 
	                                        "All": "99.5231", 
	                                        "C": "99.3625", 
	                                        "G": "99.5093", 
	                                        "T": "99.6807"
	                                    }, 
	                                    "3": {
	                                        "A": "91.9808", 
	                                        "All": "92.0370", 
	                                        "C": "90.3074", 
	                                        "G": "92.9382", 
	                                        "T": "93.0059"
	                                    }, 
	                                    "2": {
	                                        "A": "96.8683", 
	                                        "All": "96.5282", 
	                                        "C": "96.7565", 
	                                        "G": "96.4467", 
	                                        "T": "95.9883"
	                                    }, 
	                                    "5": {
	                                        "A": "79.8068", 
	                                        "All": "80.0131", 
	                                        "C": "76.6714", 
	                                        "G": "80.0142", 
	                                        "T": "83.2864"
	                                    }, 
	                                    "4": {
	                                        "A": "88.9350", 
	                                        "All": "87.5250", 
	                                        "C": "83.4252", 
	                                        "G": "89.2348", 
	                                        "T": "88.6056"
	                                    }, 
	                                    "7": {
	                                        "A": "64.6629", 
	                                        "All": "65.9415", 
	                                        "C": "51.4129", 
	                                        "G": "65.9777", 
	                                        "T": "69.7377"
	                                    }, 
	                                    "6": {
	                                        "A": "72.2757", 
	                                        "All": "72.5613", 
	                                        "C": "64.9864", 
	                                        "G": "73.5550", 
	                                        "T": "76.6386"
	                                    }, 
	                                    "9": {
	                                        "A": "50.0371", 
	                                        "All": "50.9835", 
	                                        "C": "30.2857", 
	                                        "G": "42.8197", 
	                                        "T": "52.5882"
	                                    }, 
	                                    "8": {
	                                        "A": "55.8116", 
	                                        "All": "57.9695", 
	                                        "C": "37.3312", 
	                                        "G": "54.6840", 
	                                        "T": "61.4635"
	                                    }
	                                }, 
	                                "plots": {
	                                    "posterior": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/alignFlowSignals/plot_flow_signal_accuracy_all_smooth5.png", 
	                                    "likelihood": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/alignFlowSignals/plot_flow_signals_per_hp_length_all_smooth5.png", 
	                                    "summary": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/alignFlowSignals/results.png"
	                                }, 
	                                "Accuracy": {
	                                    "comment": "Accuracy as a function of called HP length", 
	                                    "10": {
	                                        "A": "39.0351", 
	                                        "All": "39.7030", 
	                                        "C": "3.6344", 
	                                        "G": "18.4274", 
	                                        "T": "43.4669"
	                                    }, 
	                                    "1": {
	                                        "A": "98.7782", 
	                                        "All": "98.5272", 
	                                        "C": "98.1800", 
	                                        "G": "98.2642", 
	                                        "T": "98.8394"
	                                    }, 
	                                    "0": {
	                                        "A": "99.7620", 
	                                        "All": "99.7341", 
	                                        "C": "99.8244", 
	                                        "G": "99.6104", 
	                                        "T": "99.7373"
	                                    }, 
	                                    "3": {
	                                        "A": "94.5008", 
	                                        "All": "93.2728", 
	                                        "C": "91.1659", 
	                                        "G": "94.0661", 
	                                        "T": "93.5693"
	                                    }, 
	                                    "2": {
	                                        "A": "96.5379", 
	                                        "All": "96.3348", 
	                                        "C": "96.1027", 
	                                        "G": "96.5265", 
	                                        "T": "96.1832"
	                                    }, 
	                                    "5": {
	                                        "A": "78.1628", 
	                                        "All": "81.5754", 
	                                        "C": "80.9277", 
	                                        "G": "83.0677", 
	                                        "T": "83.9135"
	                                    }, 
	                                    "4": {
	                                        "A": "83.6840", 
	                                        "All": "87.9603", 
	                                        "C": "87.5248", 
	                                        "G": "90.3304", 
	                                        "T": "89.9048"
	                                    }, 
	                                    "7": {
	                                        "A": "59.5403", 
	                                        "All": "59.5157", 
	                                        "C": "39.9491", 
	                                        "G": "49.1067", 
	                                        "T": "67.4511"
	                                    }, 
	                                    "6": {
	                                        "A": "64.2752", 
	                                        "All": "67.3581", 
	                                        "C": "63.9607", 
	                                        "G": "67.3484", 
	                                        "T": "72.3033"
	                                    }, 
	                                    "9": {
	                                        "A": "41.7837", 
	                                        "All": "44.3257", 
	                                        "C": "12.2014", 
	                                        "G": "22.7685", 
	                                        "T": "50.1655"
	                                    }, 
	                                    "8": {
	                                        "A": "45.7875", 
	                                        "All": "47.9357", 
	                                        "C": "25.1718", 
	                                        "G": "33.1550", 
	                                        "T": "53.9539"
	                                    }
	                                }
	                            }, 
	                            "Error_vs_Coverage": {}, 
	                            "errorQV": {
	                                "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/errorQV.png", 
	                                "data": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_2/errorQV.png", 
	                                "MismatchQV23+": "0.0994332028060197"
	                            }
	                        }, 
	                        "IonXpress_001": {
	                            "kmer_indel_rates": {}, 
	                            "accuracyStats": {
	                                "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/accuracyStats/position_error.png", 
	                                "Raw_Accuracy_per_base": {
	                                    "150": "3.081", 
	                                    "10": "1.302", 
	                                    "200": "4.014", 
	                                    "50": "1.695", 
	                                    "1": "2.996", 
	                                    "5": "1.571", 
	                                    "100": "2.355", 
	                                    "250": "6.493"
	                                }, 
	                                "Raw_Accuracy_Stats": {
	                                    "Deletions": " 32903743", 
	                                    "Total_Errors": " 88038076", 
	                                    "Mismatches": " 16892524", 
	                                    "Insertions": " 38241809", 
	                                    "Average_Read_Accuracy": "97.85534", 
	                                    "Total_bases_called": " 4104981040.0"
	                                }, 
	                                "Raw_Insertion_Error_per_base": {
	                                    "150": "1.345", 
	                                    "10": "0.597", 
	                                    "200": "1.807", 
	                                    "50": "0.749", 
	                                    "1": "0.030", 
	                                    "5": "0.595", 
	                                    "100": "1.039", 
	                                    "250": "2.783"
	                                }, 
	                                "Mapping_Stats": {
	                                    "Perc_Mapped": "97.78", 
	                                    "Total_Reads": "32486797", 
	                                    "Reads_Mapped": "31765405"
	                                }
	                            }, 
	                            "alignFlowSignals": {
	                                "over_signal_pct_by_true_len": {
	                                    "comment": "Over flow signal percentage as a function of true HP length", 
	                                    "10": {
	                                        "A": "27.1093", 
	                                        "All": "34.0605", 
	                                        "C": "3.4483", 
	                                        "G": "27.4194", 
	                                        "T": "41.3754"
	                                    }, 
	                                    "1": {
	                                        "A": "55.8561", 
	                                        "All": "55.2460", 
	                                        "C": "65.8952", 
	                                        "G": "48.8686", 
	                                        "T": "53.2421"
	                                    }, 
	                                    "0": {
	                                        "A": "100.0000", 
	                                        "All": "100.0000", 
	                                        "C": "100.0000", 
	                                        "G": "100.0000", 
	                                        "T": "100.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "54.2681", 
	                                        "All": "32.8487", 
	                                        "C": "23.4800", 
	                                        "G": "27.1247", 
	                                        "T": "31.5567"
	                                    }, 
	                                    "2": {
	                                        "A": "34.4576", 
	                                        "All": "32.7728", 
	                                        "C": "39.0225", 
	                                        "G": "27.8312", 
	                                        "T": "30.4933"
	                                    }, 
	                                    "5": {
	                                        "A": "45.0366", 
	                                        "All": "33.6654", 
	                                        "C": "24.4558", 
	                                        "G": "29.2440", 
	                                        "T": "38.9730"
	                                    }, 
	                                    "4": {
	                                        "A": "50.4426", 
	                                        "All": "31.9697", 
	                                        "C": "20.7566", 
	                                        "G": "31.2901", 
	                                        "T": "34.3497"
	                                    }, 
	                                    "7": {
	                                        "A": "44.9842", 
	                                        "All": "38.8307", 
	                                        "C": "13.1938", 
	                                        "G": "30.4411", 
	                                        "T": "42.7497"
	                                    }, 
	                                    "6": {
	                                        "A": "45.3469", 
	                                        "All": "34.7165", 
	                                        "C": "20.7481", 
	                                        "G": "29.1752", 
	                                        "T": "40.8741"
	                                    }, 
	                                    "9": {
	                                        "A": "39.4752", 
	                                        "All": "43.1353", 
	                                        "C": "8.4652", 
	                                        "G": "38.7140", 
	                                        "T": "47.8186"
	                                    }, 
	                                    "8": {
	                                        "A": "43.8470", 
	                                        "All": "41.8695", 
	                                        "C": "10.4321", 
	                                        "G": "32.2863", 
	                                        "T": "44.5139"
	                                    }
	                                }, 
	                                "Ratio": {
	                                    "comment": "Over call percentage as a function of called HP length", 
	                                    "10": {
	                                        "A": "58.3516", 
	                                        "All": "66.4060", 
	                                        "C": "97.7358", 
	                                        "G": "87.4528", 
	                                        "T": "68.8664"
	                                    }, 
	                                    "1": {
	                                        "A": "63.0128", 
	                                        "All": "57.4199", 
	                                        "C": "64.8307", 
	                                        "G": "52.2884", 
	                                        "T": "47.5518"
	                                    }, 
	                                    "0": {
	                                        "A": "0.0000", 
	                                        "All": "0.0000", 
	                                        "C": "0.0000", 
	                                        "G": "0.0000", 
	                                        "T": "0.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "67.9789", 
	                                        "All": "59.4218", 
	                                        "C": "53.8992", 
	                                        "G": "58.5761", 
	                                        "T": "62.4075"
	                                    }, 
	                                    "2": {
	                                        "A": "68.9782", 
	                                        "All": "58.9831", 
	                                        "C": "50.1370", 
	                                        "G": "59.1653", 
	                                        "T": "61.9949"
	                                    }, 
	                                    "5": {
	                                        "A": "81.0627", 
	                                        "All": "77.3571", 
	                                        "C": "73.0601", 
	                                        "G": "78.1900", 
	                                        "T": "76.2418"
	                                    }, 
	                                    "4": {
	                                        "A": "79.6316", 
	                                        "All": "68.0070", 
	                                        "C": "61.4215", 
	                                        "G": "60.1943", 
	                                        "T": "67.7954"
	                                    }, 
	                                    "7": {
	                                        "A": "81.8206", 
	                                        "All": "84.5626", 
	                                        "C": "93.0313", 
	                                        "G": "94.3845", 
	                                        "T": "78.8215"
	                                    }, 
	                                    "6": {
	                                        "A": "82.8854", 
	                                        "All": "84.8836", 
	                                        "C": "88.5126", 
	                                        "G": "91.4321", 
	                                        "T": "78.8966"
	                                    }, 
	                                    "9": {
	                                        "A": "63.9242", 
	                                        "All": "67.7810", 
	                                        "C": "93.3816", 
	                                        "G": "87.5111", 
	                                        "T": "66.8482"
	                                    }, 
	                                    "8": {
	                                        "A": "76.3008", 
	                                        "All": "78.2095", 
	                                        "C": "91.7554", 
	                                        "G": "93.2344", 
	                                        "T": "75.1640"
	                                    }
	                                }, 
	                                "over_call_pct_by_true_len": {
	                                    "comment": "Over call percentage as a function of true HP length", 
	                                    "10": {
	                                        "A": "27.1093", 
	                                        "All": "34.0605", 
	                                        "C": "3.4483", 
	                                        "G": "27.4194", 
	                                        "T": "41.3754"
	                                    }, 
	                                    "1": {
	                                        "A": "55.8561", 
	                                        "All": "55.2460", 
	                                        "C": "65.8952", 
	                                        "G": "48.8686", 
	                                        "T": "53.2421"
	                                    }, 
	                                    "0": {
	                                        "A": "100.0000", 
	                                        "All": "100.0000", 
	                                        "C": "100.0000", 
	                                        "G": "100.0000", 
	                                        "T": "100.0000"
	                                    }, 
	                                    "3": {
	                                        "A": "54.2681", 
	                                        "All": "32.8487", 
	                                        "C": "23.4800", 
	                                        "G": "27.1247", 
	                                        "T": "31.5567"
	                                    }, 
	                                    "2": {
	                                        "A": "34.4576", 
	                                        "All": "32.7728", 
	                                        "C": "39.0225", 
	                                        "G": "27.8312", 
	                                        "T": "30.4933"
	                                    }, 
	                                    "5": {
	                                        "A": "45.0366", 
	                                        "All": "33.6654", 
	                                        "C": "24.4558", 
	                                        "G": "29.2440", 
	                                        "T": "38.9730"
	                                    }, 
	                                    "4": {
	                                        "A": "50.4426", 
	                                        "All": "31.9697", 
	                                        "C": "20.7566", 
	                                        "G": "31.2901", 
	                                        "T": "34.3497"
	                                    }, 
	                                    "7": {
	                                        "A": "44.9842", 
	                                        "All": "38.8307", 
	                                        "C": "13.1938", 
	                                        "G": "30.4411", 
	                                        "T": "42.7497"
	                                    }, 
	                                    "6": {
	                                        "A": "45.3469", 
	                                        "All": "34.7165", 
	                                        "C": "20.7481", 
	                                        "G": "29.1752", 
	                                        "T": "40.8741"
	                                    }, 
	                                    "9": {
	                                        "A": "39.4752", 
	                                        "All": "43.1353", 
	                                        "C": "8.4652", 
	                                        "G": "38.7140", 
	                                        "T": "47.8186"
	                                    }, 
	                                    "8": {
	                                        "A": "43.8470", 
	                                        "All": "41.8695", 
	                                        "C": "10.4321", 
	                                        "G": "32.2863", 
	                                        "T": "44.5139"
	                                    }
	                                }, 
	                                "accuracy_by_true_len": {
	                                    "comment": "Accuracy as a function of true HP length", 
	                                    "10": {
	                                        "A": "42.4237", 
	                                        "All": "44.2679", 
	                                        "C": "20.0000", 
	                                        "G": "35.0105", 
	                                        "T": "46.5472"
	                                    }, 
	                                    "1": {
	                                        "A": "99.0462", 
	                                        "All": "98.9177", 
	                                        "C": "99.0161", 
	                                        "G": "98.5824", 
	                                        "T": "99.0052"
	                                    }, 
	                                    "0": {
	                                        "A": "99.5369", 
	                                        "All": "99.5096", 
	                                        "C": "99.3396", 
	                                        "G": "99.4881", 
	                                        "T": "99.6736"
	                                    }, 
	                                    "3": {
	                                        "A": "91.8745", 
	                                        "All": "91.9526", 
	                                        "C": "90.2716", 
	                                        "G": "92.8922", 
	                                        "T": "92.8680"
	                                    }, 
	                                    "2": {
	                                        "A": "96.7626", 
	                                        "All": "96.4573", 
	                                        "C": "96.6882", 
	                                        "G": "96.4100", 
	                                        "T": "95.8964"
	                                    }, 
	                                    "5": {
	                                        "A": "79.4818", 
	                                        "All": "79.6377", 
	                                        "C": "76.3840", 
	                                        "G": "79.5868", 
	                                        "T": "82.9864"
	                                    }, 
	                                    "4": {
	                                        "A": "88.7474", 
	                                        "All": "87.3430", 
	                                        "C": "83.3759", 
	                                        "G": "89.0479", 
	                                        "T": "88.3902"
	                                    }, 
	                                    "7": {
	                                        "A": "64.1909", 
	                                        "All": "65.4620", 
	                                        "C": "51.0615", 
	                                        "G": "65.2301", 
	                                        "T": "69.4236"
	                                    }, 
	                                    "6": {
	                                        "A": "71.9567", 
	                                        "All": "72.1705", 
	                                        "C": "64.8077", 
	                                        "G": "72.9177", 
	                                        "T": "76.4244"
	                                    }, 
	                                    "9": {
	                                        "A": "49.8059", 
	                                        "All": "50.7525", 
	                                        "C": "31.0420", 
	                                        "G": "42.1053", 
	                                        "T": "52.4449"
	                                    }, 
	                                    "8": {
	                                        "A": "56.1438", 
	                                        "All": "57.9210", 
	                                        "C": "37.3379", 
	                                        "G": "53.8044", 
	                                        "T": "61.2961"
	                                    }
	                                }, 
	                                "plots": {
	                                    "posterior": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/alignFlowSignals/plot_flow_signal_accuracy_all_smooth5.png", 
	                                    "likelihood": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/alignFlowSignals/plot_flow_signals_per_hp_length_all_smooth5.png", 
	                                    "summary": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/alignFlowSignals/results.png"
	                                }, 
	                                "Accuracy": {
	                                    "comment": "Accuracy as a function of called HP length", 
	                                    "10": {
	                                        "A": "38.4073", 
	                                        "All": "39.0858", 
	                                        "C": "4.6381", 
	                                        "G": "17.3597", 
	                                        "T": "43.1942"
	                                    }, 
	                                    "1": {
	                                        "A": "98.7564", 
	                                        "All": "98.4948", 
	                                        "C": "98.1287", 
	                                        "G": "98.2248", 
	                                        "T": "98.8214"
	                                    }, 
	                                    "0": {
	                                        "A": "99.7521", 
	                                        "All": "99.7260", 
	                                        "C": "99.8169", 
	                                        "G": "99.6028", 
	                                        "T": "99.7297"
	                                    }, 
	                                    "3": {
	                                        "A": "94.3642", 
	                                        "All": "93.1075", 
	                                        "C": "91.0569", 
	                                        "G": "93.8881", 
	                                        "T": "93.3773"
	                                    }, 
	                                    "2": {
	                                        "A": "96.4412", 
	                                        "All": "96.2377", 
	                                        "C": "96.0203", 
	                                        "G": "96.4261", 
	                                        "T": "96.0703"
	                                    }, 
	                                    "5": {
	                                        "A": "78.1645", 
	                                        "All": "81.5104", 
	                                        "C": "80.9379", 
	                                        "G": "83.0739", 
	                                        "T": "83.5930"
	                                    }, 
	                                    "4": {
	                                        "A": "83.5831", 
	                                        "All": "87.8010", 
	                                        "C": "87.4036", 
	                                        "G": "90.1057", 
	                                        "T": "89.5950"
	                                    }, 
	                                    "7": {
	                                        "A": "59.0066", 
	                                        "All": "59.0329", 
	                                        "C": "39.7469", 
	                                        "G": "48.9051", 
	                                        "T": "67.1505"
	                                    }, 
	                                    "6": {
	                                        "A": "63.9412", 
	                                        "All": "67.1469", 
	                                        "C": "64.0409", 
	                                        "G": "67.5572", 
	                                        "T": "71.8184"
	                                    }, 
	                                    "9": {
	                                        "A": "41.7973", 
	                                        "All": "44.0733", 
	                                        "C": "12.8240", 
	                                        "G": "22.5368", 
	                                        "T": "49.8560"
	                                    }, 
	                                    "8": {
	                                        "A": "45.3278", 
	                                        "All": "47.4086", 
	                                        "C": "25.2982", 
	                                        "G": "33.0838", 
	                                        "T": "53.4764"
	                                    }
	                                }
	                            }, 
	                            "Error_vs_Coverage": {}, 
	                            "errorQV": {
	                                "plots": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/errorQV.png", 
	                                "data": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/1_Torrent_Accuracy_out.661368/barcode_1/errorQV.png", 
	                                "MismatchQV23+": "0.102152843762131"
	                            }
	                        }
	                    }
	                }, 
	                "duplicateReads_useZC": {
	                    "adapter_found_rate_chr1": "0.869", 
	                    "duplicate_reads_chr1": 507578, 
	                    "total_reads_chr1": 607744, 
	                    "duplicate_rate_chr1": "0.835", 
	                    "duprate_at_500k_chr1": 0
	                }, 
	                "autoCal": {
	                    "dc_range": 0
	                }, 
	                "variantCaller": {
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "hotspots": {}, 
	                            "variants": {
	                                "no_call": 704, 
	                                "homo_snps": 17138, 
	                                "het_snps": 29003, 
	                                "other": 712, 
	                                "variants": 49934, 
	                                "het_indels": 2181, 
	                                "homo_indels": 900
	                            }
	                        }, 
	                        "IonXpress_001": {
	                            "hotspots": {}, 
	                            "variants": {
	                                "no_call": 777, 
	                                "homo_snps": 17362, 
	                                "het_snps": 29564, 
	                                "other": 764, 
	                                "variants": 50981, 
	                                "het_indels": 2325, 
	                                "homo_indels": 966
	                            }
	                        }
	                    }, 
	                    "barcoded": "true", 
	                    "targets_bed": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	                    "Target Regions": "AmpliSeqExome.20131001.designed", 
	                    "Trim Reads": true, 
	                    "Target Loci": "Not using", 
	                    "Configuration": "Custom", 
	                    "Aligned Reads": "R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading", 
	                    "Library Type": "AmpliSeq"
	                }, 
	                "ConversionRate": {}, 
	                "validateVariantCaller": {
	                    "SNP_FP-ConfidentPos": "2690.0", 
	                    "InDel_AmbPos-AllPos": "0.0", 
	                    "SNP_PPV>=30x": "98.087030277327599", 
	                    "InDel_FN>=100x": "230.0", 
	                    "SNP_FN>=100x": "422.0", 
	                    "InDel_TP-AllPos": "2103.0", 
	                    "InDel_FP>=30x": "1036.0", 
	                    "SNP_FN>=30x": "3344.0", 
	                    "SNP_FP>=1000x": "0.0", 
	                    "SNP_ConsensusAccuracy-AllPos": "0.9998953201391525", 
	                    "InDel_NoCalls-AllPos": "1115911.0", 
	                    "InDel_FP-AllPos": "2177.0", 
	                    "InDel_FP_50x-100x": "422.0", 
	                    "InDel_Sensitivity>=20x": "43.526170798898072", 
	                    "SNP_TP>=500x": "9.0", 
	                    "SNP_Sensitivity>=100x": "97.507236103727337", 
	                    "SNP_Sensitivity>=500x": "100.0", 
	                    "InDel_ConsensusAccuracy-AllPos": "0.99995004368748053", 
	                    "SNP_ConsensusAccuracy>=50x": "0.99997740130899992", 
	                    "InDel_FN>=20x": "2460.0", 
	                    "SNP_FP>=50x": "723.0", 
	                    "InDel_PPV-AllPos": "49.135514018691588", 
	                    "InDel_ConsensusAccuracy>=30x": "0.99997613890509252", 
	                    "InDel_FP-ncRNA": "12.0", 
	                    "InDel_ReferenceCalls-AllPos": "0.0", 
	                    "Target-regions_file": "/results/analysis/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/plugin_out/validateVariantCaller_out.661373/../variantCaller_out.661371/AmpliSeqExome.20131001.designed.bed", 
	                    "SNP_TP-AllPos": "82067.0", 
	                    "InDel_Sensitivity>=30x": "47.738264580369844", 
	                    "InDel_FN>=500x": "0.0", 
	                    "InDel_FP_20x-50x": "869.0", 
	                    "InDel_FP-ConfidentPos": "2177.0", 
	                    "InDel_FN-AllPos": "3838.0", 
	                    "SNP_HP11-AllPos": "0.0", 
	                    "InDel_FN>=50x": "997.0", 
	                    "SNP_Sensitivity-AllPos": "89.221687087550691", 
	                    "Truth-major_SNP_file": "NA12878_NIST_NoChrY_SNP.bed", 
	                    "InDel_Sensitivity-AllAnnotations": "70.797081280000995", 
	                    "SNP_FP_200x-300x": "15.0", 
	                    "InDel_FP>=20x": "1410.0", 
	                    "SNP_FN>=500x": "0.0", 
	                    "Combined Variant Positive Predictive Value for All Bases at >=20x": "96.112150000000014", 
	                    "SNP_Sensitivity>=1000x": 0, 
	                    "InDel_FP_700x-1000x": "0.0", 
	                    "SNP_FP>=30x": "1263.0", 
	                    "SNP_FP_700x-1000x": "0.0", 
	                    "SNP_ConsensusAccuracy>=20x": "0.99995073302645598", 
	                    "InDel_TP>=30x": "1678.0", 
	                    "SNP_AmbPos-AllPos": "0.0", 
	                    "Truth-minor_InDel_file": "None", 
	                    "SNP_FP_500x-700x": "0.0", 
	                    "SNP_FP_50x-100x": "537.0", 
	                    "InDel_ConsensusAccuracy>=20x": "0.99996785853209447", 
	                    "InDel_FP-Exons": "839.0", 
	                    "SNP_TP>=30x": "64760.0", 
	                    "SNP_ReferenceCalls-AllPos": "0.0", 
	                    "InDel_FP_500x-700x": "0.0", 
	                    "InDel_FP_200x-300x": "6.0", 
	                    "barcoded": "true", 
	                    "SNP_FP_20x-50x": "912.0", 
	                    "SNP_FP>=100x": "186.0", 
	                    "SNP_Sensitivity>=20x": "94.457915237186256", 
	                    "InDel_FP_300x-400x": "0.0", 
	                    "SNP_FP_100x-200x": "170.0", 
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "SNP_FP-ConfidentPos": "1282", 
	                            "InDel_AmbPos-AllPos": "0", 
	                            "SNP_PPV>=30x": "98.2273993416055", 
	                            "InDel_FN>=100x": "95", 
	                            "SNP_FN>=100x": "150", 
	                            "InDel_TP-AllPos": "1025", 
	                            "InDel_FP>=30x": "443", 
	                            "SNP_FN>=30x": "1580", 
	                            "SNP_FP>=1000x": "0", 
	                            "SNP_ConsensusAccuracy-AllPos": "0.999891483095697", 
	                            "InDel_NoCalls-AllPos": "565166", 
	                            "InDel_FP-AllPos": "1021", 
	                            "InDel_FP_50x-100x": "184", 
	                            "InDel_Sensitivity>=20x": "43.4907010014306", 
	                            "SNP_TP>=500x": "4", 
	                            "SNP_Sensitivity>=100x": "97.7430033102618", 
	                            "SNP_Sensitivity>=500x": "100", 
	                            "InDel_ConsensusAccuracy-AllPos": "0.999950699805301", 
	                            "SNP_ConsensusAccuracy>=50x": "0.999980449350013", 
	                            "InDel_FN>=20x": "1185", 
	                            "SNP_FP>=50x": "308", 
	                            "InDel_PPV-AllPos": "50.0977517106549", 
	                            "InDel_ConsensusAccuracy>=30x": "0.999978273364331", 
	                            "InDel_FP-ncRNA": "5", 
	                            "InDel_ReferenceCalls-AllPos": "0", 
	                            "SNP_TP-AllPos": "40739", 
	                            "InDel_Sensitivity>=30x": "48.0792316926771", 
	                            "InDel_FN>=500x": "0", 
	                            "InDel_FP_20x-50x": "409", 
	                            "InDel_FP-ConfidentPos": "1021", 
	                            "InDel_FN-AllPos": "1947", 
	                            "SNP_HP11-AllPos": "0", 
	                            "InDel_FN>=50x": "427", 
	                            "SNP_Sensitivity-AllPos": "88.5823005001087", 
	                            "InDel_Sensitivity-AllAnnotations": "34.4885598923284", 
	                            "SNP_FP_200x-300x": "5", 
	                            "InDel_FP>=20x": "634", 
	                            "SNP_FN>=500x": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at >=20x": "96.388900", 
	                            "SNP_Sensitivity>=1000x": "0", 
	                            "InDel_FP_700x-1000x": "0", 
	                            "SNP_FP>=30x": "560", 
	                            "SNP_FP_700x-1000x": "0", 
	                            "SNP_ConsensusAccuracy>=20x": "0.999952394084229", 
	                            "InDel_TP>=30x": "801", 
	                            "SNP_AmbPos-AllPos": "0", 
	                            "SNP_FP_500x-700x": "0", 
	                            "SNP_FP_50x-100x": "244", 
	                            "InDel_ConsensusAccuracy>=20x": "0.999969785359111", 
	                            "InDel_FP-Exons": "395", 
	                            "SNP_TP>=30x": "31032", 
	                            "SNP_ReferenceCalls-AllPos": "0", 
	                            "InDel_FP_500x-700x": "0", 
	                            "InDel_FP_200x-300x": "1", 
	                            "SNP_FP_20x-50x": "433", 
	                            "SNP_FP>=100x": "64", 
	                            "SNP_Sensitivity>=20x": "94.395505855048", 
	                            "InDel_FP_300x-400x": "0", 
	                            "SNP_FP_100x-200x": "59", 
	                            "SNP_Sensitivity-AllAnnotations": "88.5823005001087", 
	                            "InDel_FP_400x-500x": "0", 
	                            "InDel_FP>=50x": "225", 
	                            "SNP_FN-AllAnnotations": "5251", 
	                            "SNP_FP-AllPos": "1282", 
	                            "SNP_PPV-AllPos": "96.9491444753814", 
	                            "SNP_FP>=20x": "741", 
	                            "InDel_Sensitivity>=1000x": "0", 
	                            "InDel_ConsensusAccuracy>=50x": "0.999989169903321", 
	                            "InDel_TP>=100x": "148", 
	                            "SNP_TP>=50x": "21224", 
	                            "SNP_ConsensusAccuracy>=30x": "0.99996445336366", 
	                            "InDel_Sensitivity-AllPos": "34.4885598923284", 
	                            "InDel_TP>=20x": "912", 
	                            "InDel_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP>=500x": "0", 
	                            "% Callable Bases": "98.957700", 
	                            "SNP_FN>=20x": "2125", 
	                            "InDel_FP>=1000x": "0", 
	                            "SNP_Sensitivity>=30x": "95.1551576106955", 
	                            "InDel_FN>=1000x": "0", 
	                            "InDel_FP>=500x": "0", 
	                            "SNP_FP_400x-500x": "0", 
	                            "InDel_HP11-AllPos": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at all coverages": "94.773800", 
	                            "SNP_FN>=1000x": "0", 
	                            "SNP_FN>=50x": "869", 
	                            "InDel_TP>=500x": "0", 
	                            "InDel_PPV>=30x": "64.3890675241157", 
	                            "InDel_TP>=1000x": "0", 
	                            "SNP_FP_300x-400x": "0", 
	                            "SNP_Sensitivity>=50x": "96.0666274385552", 
	                            "Combined Variant Sensitivity for All Bases at >= 20x": "91.727600", 
	                            "SNP_TP>=100x": "6496", 
	                            "InDel_FP>=100x": "41", 
	                            "SNP_NoCalls-AllPos": "65424", 
	                            "InDel_Sensitivity>=500x": "0", 
	                            "SNP_TP>=20x": "35791", 
	                            "InDel_Sensitivity>=50x": "54.2826552462527", 
	                            "InDel_FN-AllAnnotations": "1947", 
	                            "InDel_TP>=50x": "507", 
	                            "SNP_TP>=1000x": "0", 
	                            "InDel_FN>=30x": "865", 
	                            "SNP_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP-ncRNA": "12", 
	                            "SNP_FN-AllPos": "5251", 
	                            "InDel_Sensitivity>=100x": "60.9053497942387", 
	                            "InDel_FP_100x-200x": "40", 
	                            "SNP_FP-Exons": "501", 
	                            "Combined Variant Sensitivity for All Bases at all coverages": "85.298800"
	                        }, 
	                        "IonXpress_001": {
	                            "SNP_FP-ConfidentPos": "1408", 
	                            "InDel_AmbPos-AllPos": "0", 
	                            "SNP_PPV>=30x": "97.9582353112021", 
	                            "InDel_FN>=100x": "135", 
	                            "SNP_FN>=100x": "272", 
	                            "InDel_TP-AllPos": "1078", 
	                            "InDel_FP>=30x": "593", 
	                            "SNP_FN>=30x": "1764", 
	                            "SNP_FP>=1000x": "0", 
	                            "SNP_ConsensusAccuracy-AllPos": "0.999899157182608", 
	                            "InDel_NoCalls-AllPos": "550745", 
	                            "InDel_FP-AllPos": "1156", 
	                            "InDel_FP_50x-100x": "238", 
	                            "InDel_Sensitivity>=20x": "43.5590969455511", 
	                            "SNP_TP>=500x": "5", 
	                            "SNP_Sensitivity>=100x": "97.3548575318487", 
	                            "SNP_Sensitivity>=500x": "100", 
	                            "InDel_ConsensusAccuracy-AllPos": "0.99994938756966", 
	                            "SNP_ConsensusAccuracy>=50x": "0.999974353267987", 
	                            "InDel_FN>=20x": "1275", 
	                            "SNP_FP>=50x": "415", 
	                            "InDel_PPV-AllPos": "48.2542524619517", 
	                            "InDel_ConsensusAccuracy>=30x": "0.999974004445854", 
	                            "InDel_FP-ncRNA": "7", 
	                            "InDel_ReferenceCalls-AllPos": "0", 
	                            "SNP_TP-AllPos": "41328", 
	                            "InDel_Sensitivity>=30x": "47.4310438074635", 
	                            "InDel_FN>=500x": "0", 
	                            "InDel_FP_20x-50x": "460", 
	                            "InDel_FP-ConfidentPos": "1156", 
	                            "InDel_FN-AllPos": "1891", 
	                            "SNP_HP11-AllPos": "0", 
	                            "InDel_FN>=50x": "570", 
	                            "SNP_Sensitivity-AllPos": "89.8610597725642", 
	                            "InDel_Sensitivity-AllAnnotations": "36.3085213876726", 
	                            "SNP_FP_200x-300x": "10", 
	                            "InDel_FP>=20x": "776", 
	                            "SNP_FN>=500x": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at >=20x": "95.835400", 
	                            "SNP_Sensitivity>=1000x": "0", 
	                            "InDel_FP_700x-1000x": "0", 
	                            "SNP_FP>=30x": "703", 
	                            "SNP_FP_700x-1000x": "0", 
	                            "SNP_ConsensusAccuracy>=20x": "0.999949071968683", 
	                            "InDel_TP>=30x": "877", 
	                            "SNP_AmbPos-AllPos": "0", 
	                            "SNP_FP_500x-700x": "0", 
	                            "SNP_FP_50x-100x": "293", 
	                            "InDel_ConsensusAccuracy>=20x": "0.999965931705078", 
	                            "InDel_FP-Exons": "444", 
	                            "SNP_TP>=30x": "33728", 
	                            "SNP_ReferenceCalls-AllPos": "0", 
	                            "InDel_FP_500x-700x": "0", 
	                            "InDel_FP_200x-300x": "5", 
	                            "SNP_FP_20x-50x": "479", 
	                            "SNP_FP>=100x": "122", 
	                            "SNP_Sensitivity>=20x": "94.5176434953809", 
	                            "InDel_FP_300x-400x": "0", 
	                            "SNP_FP_100x-200x": "111", 
	                            "SNP_Sensitivity-AllAnnotations": "89.8610597725642", 
	                            "InDel_FP_400x-500x": "0", 
	                            "InDel_FP>=50x": "316", 
	                            "SNP_FN-AllAnnotations": "4663", 
	                            "SNP_FP-AllPos": "1408", 
	                            "SNP_PPV-AllPos": "96.7053538000749", 
	                            "SNP_FP>=20x": "894", 
	                            "InDel_Sensitivity>=1000x": "0", 
	                            "InDel_ConsensusAccuracy>=50x": "0.999985283028132", 
	                            "InDel_TP>=100x": "221", 
	                            "SNP_TP>=50x": "25572", 
	                            "SNP_ConsensusAccuracy>=30x": "0.999959021704743", 
	                            "InDel_Sensitivity-AllPos": "36.3085213876726", 
	                            "InDel_TP>=20x": "984", 
	                            "InDel_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP>=500x": "0", 
	                            "% Callable Bases": "98.984300", 
	                            "SNP_FN>=20x": "2172", 
	                            "InDel_FP>=1000x": "0", 
	                            "SNP_Sensitivity>=30x": "95.0298658852699", 
	                            "InDel_FN>=1000x": "0", 
	                            "InDel_FP>=500x": "0", 
	                            "SNP_FP_400x-500x": "0", 
	                            "InDel_HP11-AllPos": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at all coverages": "94.298400", 
	                            "SNP_FN>=1000x": "0", 
	                            "SNP_FN>=50x": "1129", 
	                            "InDel_TP>=500x": "0", 
	                            "InDel_PPV>=30x": "59.6598639455782", 
	                            "InDel_TP>=1000x": "0", 
	                            "SNP_FP_300x-400x": "1", 
	                            "SNP_Sensitivity>=50x": "95.771693944047", 
	                            "Combined Variant Sensitivity for All Bases at >= 20x": "91.768700", 
	                            "SNP_TP>=100x": "10011", 
	                            "InDel_FP>=100x": "78", 
	                            "SNP_NoCalls-AllPos": "63770", 
	                            "InDel_Sensitivity>=500x": "0", 
	                            "SNP_TP>=20x": "37446", 
	                            "InDel_Sensitivity>=50x": "53.3169533169533", 
	                            "InDel_FN-AllAnnotations": "1891", 
	                            "InDel_TP>=50x": "651", 
	                            "SNP_TP>=1000x": "0", 
	                            "InDel_FN>=30x": "972", 
	                            "SNP_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP-ncRNA": "12", 
	                            "SNP_FN-AllPos": "4663", 
	                            "InDel_Sensitivity>=100x": "62.0786516853933", 
	                            "InDel_FP_100x-200x": "73", 
	                            "SNP_FP-Exons": "568", 
	                            "Combined Variant Sensitivity for All Bases at all coverages": "86.613500"
	                        }
	                    }, 
	                    "SNP_Sensitivity-AllAnnotations": "178.44336027267292", 
	                    "InDel_FP_400x-500x": "0.0", 
	                    "InDel_FP>=50x": "541.0", 
	                    "SNP_FN-AllAnnotations": "9914.0", 
	                    "SNP_FP-AllPos": "2690.0", 
	                    "SNP_PPV-AllPos": "96.826220843116204", 
	                    "SNP_FP>=20x": "1635.0", 
	                    "InDel_Sensitivity>=1000x": 0, 
	                    "InDel_ConsensusAccuracy>=50x": "0.99998722646572658", 
	                    "InDel_TP>=100x": "369.0", 
	                    "Region_selected": "NIST", 
	                    "SNP_ConsensusAccuracy>=30x": "0.99996173753420159", 
	                    "InDel_Sensitivity-AllPos": "35.398081131122709", 
	                    "InDel_TP>=20x": "1896.0", 
	                    "InDel_AmbNotDetected-AllPos": "0.0", 
	                    "SNP_FP>=500x": "0.0", 
	                    "% Callable Bases": "98.971000000000004", 
	                    "SNP_FN>=20x": "4297.0", 
	                    "InDel_FP>=1000x": "0.0", 
	                    "SNP_Sensitivity>=30x": "95.089862563138723", 
	                    "InDel_FN>=1000x": "0.0", 
	                    "InDel_FP>=500x": "0.0", 
	                    "SNP_FP_400x-500x": "0.0", 
	                    "InDel_HP11-AllPos": "0.0", 
	                    "Combined Variant Positive Predictive Value for All Bases at all coverages": "94.536100000000005", 
	                    "SNP_FN>=1000x": "0.0", 
	                    "SNP_FN>=50x": "1998.0", 
	                    "InDel_TP>=500x": "0.0", 
	                    "InDel_PPV>=30x": "61.827560795873246", 
	                    "InDel_TP>=1000x": "0.0", 
	                    "Truth-minor_SNP_file": "None", 
	                    "SNP_FP_300x-400x": "1.0", 
	                    "SNP_Sensitivity>=50x": "95.905234250112713", 
	                    "Combined Variant Sensitivity for All Bases at >= 20x": "91.748149999999995", 
	                    "SNP_TP>=100x": "16507.0", 
	                    "Sample_selected": "NA12878", 
	                    "InDel_FP>=100x": "119.0", 
	                    "SNP_NoCalls-AllPos": "129194.0", 
	                    "Truth-major_InDel_file": "NA12878_NIST_NoChrY_indel.bed", 
	                    "InDel_Sensitivity>=500x": 0, 
	                    "SNP_TP>=20x": "73237.0", 
	                    "InDel_Sensitivity>=50x": "53.735498839907194", 
	                    "InDel_FN-AllAnnotations": "3838.0", 
	                    "InDel_TP>=50x": "1158.0", 
	                    "SNP_TP>=1000x": "0.0", 
	                    "InDel_FN>=30x": "1837.0", 
	                    "Variant-caller_name": "variantCaller", 
	                    "SNP_AmbNotDetected-AllPos": "0.0", 
	                    "SNP_TP>=50x": "46796.0", 
	                    "SNP_FP-ncRNA": "24.0", 
	                    "SNP_FN-AllPos": "9914.0", 
	                    "InDel_Sensitivity>=100x": "61.602671118530886", 
	                    "InDel_FP_100x-200x": "113.0", 
	                    "SNP_FP-Exons": "1069.0", 
	                    "Combined Variant Sensitivity for All Bases at all coverages": "85.956150000000008"
	                }, 
	                "timingPerformance": {
	                    "runtime": {
	                        "analysis": "314.42"
	                    }, 
	                    "threadinfo": {
	                        "bkgmodel Gpu": 1, 
	                        "fileaccess": 4, 
	                        "beadfind": 6, 
	                        "basecalling": 24, 
	                        "bkgmodel Cpu": 6
	                    }, 
	                    "chipinfo": {
	                        "oia": 1, 
	                        "flows": 520, 
	                        "chiptype": "900"
	                    }
	                }, 
	                "coverageAnalysis": {
	                    "Non-duplicate": "No", 
	                    "barcoded": "true", 
	                    "Uniquely mapped": "No", 
	                    "Amplicons reading end-to-end": "4.59%", 
	                    "Targetted regions": "/results/uploads/BED/46/hg19/merged/detail/AmpliSeqExome.20131001.designed.bed", 
	                    "Target padding": "0", 
	                    "barcodes": {
	                        "IonXpress_002": {
	                            "Bases in target regions": "57742646", 
	                            "Amplicons with at least 1 read": "99.30%", 
	                            "Target base coverage at 100x": "15.12%", 
	                            "Amplicons with at least 500 reads": "0.03%", 
	                            "Total assigned amplicon reads": "23367467", 
	                            "Reference (File)": "hg19", 
	                            "Total base reads on target": "3356512633", 
	                            "Target base coverage at 20x": "83.15%", 
	                            "Number of amplicons": "293903", 
	                            "Target bases with no strand bias": "62.30%", 
	                            "Percent reads on target": "92.46%", 
	                            "Amplicons with at least 100 reads": "30.14%", 
	                            "Average base coverage depth": "58.13", 
	                            "Average reads per amplicon": "79.51", 
	                            "Using": "All Mapped Reads", 
	                            "Amplicons reading end-to-end": "5.00%", 
	                            "Sample Name": "None", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Uniformity of base coverage": "91.28%", 
	                            "Alignments": "IonXpress_002_R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	                            "Amplicons with at least 20 reads": "89.93%", 
	                            "Number of mapped reads": "25272862", 
	                            "Percent assigned amplicon reads": "92.46%", 
	                            "Amplicons with no strand bias": "88.42%", 
	                            "Total aligned base reads": "3583042065", 
	                            "Target base coverage at 1x": "98.50%", 
	                            "Target base coverage at 500x": "0.01%", 
	                            "Percent base reads on target": "93.68%", 
	                            "Uniformity of amplicon coverage": "92.54%"
	                        }, 
	                        "IonXpress_001": {
	                            "Bases in target regions": "57742646", 
	                            "Amplicons with at least 1 read": "99.47%", 
	                            "Target base coverage at 100x": "22.98%", 
	                            "Amplicons with at least 500 reads": "0.06%", 
	                            "Total assigned amplicon reads": "28570518", 
	                            "Reference (File)": "hg19", 
	                            "Total base reads on target": "4029869840", 
	                            "Target base coverage at 20x": "86.67%", 
	                            "Number of amplicons": "293903", 
	                            "Target bases with no strand bias": "61.81%", 
	                            "Percent reads on target": "89.94%", 
	                            "Amplicons with at least 100 reads": "41.89%", 
	                            "Average base coverage depth": "69.79", 
	                            "Average reads per amplicon": "97.21", 
	                            "Using": "All Mapped Reads", 
	                            "Amplicons reading end-to-end": "4.18%", 
	                            "Sample Name": "139248", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Uniformity of base coverage": "91.27%", 
	                            "Alignments": "IonXpress_001_R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558", 
	                            "Amplicons with at least 20 reads": "92.08%", 
	                            "Number of mapped reads": "31765405", 
	                            "Percent assigned amplicon reads": "89.94%", 
	                            "Amplicons with no strand bias": "89.88%", 
	                            "Total aligned base reads": "4381736166", 
	                            "Target base coverage at 1x": "98.68%", 
	                            "Target base coverage at 500x": "0.02%", 
	                            "Percent base reads on target": "91.97%", 
	                            "Uniformity of amplicon coverage": "92.35%"
	                        }
	                    }
	                }, 
	                "VariantQC": {
	                    "IonXpress_002": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6049, 
	                                "REJECTION": 536, 
	                                "Cov": 174639, 
	                                "REF": 556213, 
	                                "HEALED": 228, 
	                                "SHIFT": 484477, 
	                                "SSE": 91743, 
	                                "STRINGENCY": 3530, 
	                                ".": 670236, 
	                                "Quality": 321249, 
	                                "STDBIAS": 58990
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1219, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 49188, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 541, 
	                                "10": 1069, 
	                                "13": 169, 
	                                "12": 250, 
	                                "15": 107, 
	                                "14": 149, 
	                                "1": 82309, 
	                                "0": 59946, 
	                                "3": 145485, 
	                                "2": 149295, 
	                                "5": 62545, 
	                                "4": 91674, 
	                                "7": 10079, 
	                                "6": 25508, 
	                                "9": 1849, 
	                                "8": 3669
	                            }, 
	                            "run": {
	                                "11": 11, 
	                                "10": 10, 
	                                "13": 13, 
	                                "12": 12, 
	                                "15": 15, 
	                                "14": 14, 
	                                "1": 1, 
	                                "0": 0, 
	                                "3": 3, 
	                                "2": 2, 
	                                "5": 5, 
	                                "4": 4, 
	                                "7": 7, 
	                                "6": 6, 
	                                "9": 9, 
	                                "8": 8
	                            }, 
	                            "unfiltered": {
	                                "11": 21, 
	                                "10": 25, 
	                                "13": 8, 
	                                "12": 18, 
	                                "15": 9, 
	                                "14": 8, 
	                                "1": 27726, 
	                                "0": 359, 
	                                "3": 4597, 
	                                "2": 11082, 
	                                "5": 1059, 
	                                "4": 2156, 
	                                "7": 227, 
	                                "6": 457, 
	                                "9": 46, 
	                                "8": 112
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 44415, 
	                                "del": 376893, 
	                                "snp": 45357, 
	                                "ins": 203571
	                            }, 
	                            "unfiltered": {
	                                "other": 1805, 
	                                "del": 972, 
	                                "snp": 45393, 
	                                "ins": 1018
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 670236, 
	                            "unfiltered": 49188
	                        }
	                    }, 
	                    "IonXpress_001": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6189, 
	                                "REJECTION": 521, 
	                                "Cov": 156886, 
	                                "REF": 544624, 
	                                "HEALED": 273, 
	                                "SHIFT": 482100, 
	                                "SSE": 92404, 
	                                "STRINGENCY": 3585, 
	                                ".": 654348, 
	                                "Quality": 270071, 
	                                "STDBIAS": 56415
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1184, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 50219, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 541, 
	                                "10": 1086, 
	                                "13": 167, 
	                                "12": 239, 
	                                "15": 119, 
	                                "14": 158, 
	                                "1": 79559, 
	                                "0": 56238, 
	                                "3": 140568, 
	                                "2": 146009, 
	                                "5": 62701, 
	                                "4": 90449, 
	                                "7": 10215, 
	                                "6": 25855, 
	                                "9": 1874, 
	                                "8": 3665
	                            }, 
	                            "run": {
	                                "11": 11, 
	                                "10": 10, 
	                                "13": 13, 
	                                "12": 12, 
	                                "15": 15, 
	                                "14": 14, 
	                                "1": 1, 
	                                "0": 0, 
	                                "3": 3, 
	                                "2": 2, 
	                                "5": 5, 
	                                "4": 4, 
	                                "7": 7, 
	                                "6": 6, 
	                                "9": 9, 
	                                "8": 8
	                            }, 
	                            "unfiltered": {
	                                "11": 13, 
	                                "10": 26, 
	                                "13": 3, 
	                                "12": 19, 
	                                "15": 7, 
	                                "14": 11, 
	                                "1": 28216, 
	                                "0": 398, 
	                                "3": 4676, 
	                                "2": 11382, 
	                                "5": 1070, 
	                                "4": 2176, 
	                                "7": 226, 
	                                "6": 492, 
	                                "9": 52, 
	                                "8": 109
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 43525, 
	                                "del": 373264, 
	                                "snp": 44296, 
	                                "ins": 193263
	                            }, 
	                            "unfiltered": {
	                                "other": 1892, 
	                                "del": 1047, 
	                                "snp": 46203, 
	                                "ins": 1077
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 654348, 
	                            "unfiltered": 50219
	                        }
	                    }, 
	                    "summary": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6049, 
	                                "REJECTION": 536, 
	                                "Cov": 174639, 
	                                "REF": 556213, 
	                                "HEALED": 228, 
	                                "SHIFT": 484477, 
	                                "SSE": 91743, 
	                                "STRINGENCY": 3530, 
	                                ".": 670236, 
	                                "Quality": 321249, 
	                                "STDBIAS": 58990
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1219, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 49188, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 541, 
	                                "10": 1069, 
	                                "13": 169, 
	                                "12": 250, 
	                                "15": 107, 
	                                "14": 149, 
	                                "1": 82309, 
	                                "0": 59946, 
	                                "3": 145485, 
	                                "2": 149295, 
	                                "5": 62545, 
	                                "4": 91674, 
	                                "7": 10079, 
	                                "6": 25508, 
	                                "9": 1849, 
	                                "8": 3669
	                            }, 
	                            "run": {
	                                "11": 11, 
	                                "10": 10, 
	                                "13": 13, 
	                                "12": 12, 
	                                "15": 15, 
	                                "14": 14, 
	                                "1": 1, 
	                                "0": 0, 
	                                "3": 3, 
	                                "2": 2, 
	                                "5": 5, 
	                                "4": 4, 
	                                "7": 7, 
	                                "6": 6, 
	                                "9": 9, 
	                                "8": 8
	                            }, 
	                            "unfiltered": {
	                                "11": 21, 
	                                "10": 25, 
	                                "13": 8, 
	                                "12": 18, 
	                                "15": 9, 
	                                "14": 8, 
	                                "1": 27726, 
	                                "0": 359, 
	                                "3": 4597, 
	                                "2": 11082, 
	                                "5": 1059, 
	                                "4": 2156, 
	                                "7": 227, 
	                                "6": 457, 
	                                "9": 46, 
	                                "8": 112
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 44415, 
	                                "del": 376893, 
	                                "snp": 45357, 
	                                "ins": 203571
	                            }, 
	                            "unfiltered": {
	                                "other": 1805, 
	                                "del": 972, 
	                                "snp": 45393, 
	                                "ins": 1018
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 670236, 
	                            "unfiltered": 49188
	                        }
	                    }
	                }
	            }, 
	            "resultsType": "", 
	            "tfFastq": "_", 
	            "tfmetrics": [], 
	            "parentIDs": "", 
	            "analysismetrics": [
	                "/rundb/api/v1/analysismetrics/30862/"
	            ], 
	            "timeToComplete": "0", 
	            "reportLink": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/", 
	            "fastqLink": "/output/Home/Auto_user_G35-494--R55155-500M_IC_loading_19558_52046/basecaller_results/R_2014_01_29_16_39_00_user_G35-494--R55155-500M_IC_loading_Auto_user_G35-494--R55155-500M_IC_loading_19558.fastq", 
	            "pluginresults": [
	                "/rundb/api/v1/pluginresult/661376/", 
	                "/rundb/api/v1/pluginresult/661375/", 
	                "/rundb/api/v1/pluginresult/661374/", 
	                "/rundb/api/v1/pluginresult/661373/", 
	                "/rundb/api/v1/pluginresult/661372/", 
	                "/rundb/api/v1/pluginresult/661371/", 
	                "/rundb/api/v1/pluginresult/661370/", 
	                "/rundb/api/v1/pluginresult/661369/", 
	                "/rundb/api/v1/pluginresult/661368/", 
	                "/rundb/api/v1/pluginresult/661367/", 
	                "/rundb/api/v1/pluginresult/661366/"
	            ], 
	            "framesProcessed": 0, 
	            "autoExempt": false, 
	            "resource_uri": "/rundb/api/v1/results/52046/"
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

