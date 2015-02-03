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
**sffLink**         Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
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
**tfSffLink**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
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
	        "total_count": 56103, 
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
	            "analysisVersion": "db:4.1.21+2-1,an:4.1.24+0-1,", 
	            "runid": "DGMU8", 
	            "id": 293943, 
	            "filesystempath": "/results/analysis/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943", 
	            "metaData": {}, 
	            "log": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/log.html", 
	            "timeStamp": "2014-01-23T07:39:52.000803+00:00", 
	            "libmetrics": [
	                "/rundb/api/v1/libmetrics/32368/"
	            ], 
	            "experiment": "/rundb/api/v1/experiment/17446/", 
	            "resultsName": "Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	            "status": "Completed", 
	            "planShortID": "ONPK8", 
	            "processedCycles": 0, 
	            "bamLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446.bam", 
	            "sffLink": null, 
	            "representative": false, 
	            "pluginState": {
	                "coverageAnalysisLite": "Completed", 
	                "SystematicErrorAnalysis": "Completed", 
	                "1_Torrent_Accuracy": "Error", 
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
	                "/rundb/api/v1/qualitymetrics/31678/"
	            ], 
	            "diskusage": 151, 
	            "eas": "/rundb/api/v1/experimentanalysissettings/18714/", 
	            "tfSffLink": null, 
	            "projects": [
	                "/rundb/api/v1/project/1080/"
	            ], 
	            "pluginStore": {
	                "coverageAnalysisLite": {
	                    "Non-duplicate": "", 
	                    "barcoded": "true", 
	                    "Uniquely mapped": "No", 
	                    "Targetted regions": "/results/uploads/BED/46/hg19/merged/plain/AmpliSeqExome.20131001.designed.bed", 
	                    "Target padding": "0", 
	                    "barcodes": {
	                        "IonXpress_033": {
	                            "Bases in target regions": "57742646", 
	                            "Number of mapped reads": "41517304", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Percent reads on target": "94.39%", 
	                            "Average base coverage depth": "112.4", 
	                            "Reference (File)": "hg19", 
	                            "Coverage Analysis Lite Report": "N/A", 
	                            "Target base coverage at 100x": "51.05%", 
	                            "Target base coverage at 20x": "94.26%", 
	                            "Uniformity of base coverage": "93.56%", 
	                            "Target base coverage at 1x": "98.53%", 
	                            "Using": "All Mapped Reads", 
	                            "Target base coverage at 500x": "0.10%", 
	                            "Alignments": "IonXpress_033_R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	                            "Total base reads on target": "6490060189"
	                        }, 
	                        "IonXpress_034": {
	                            "Bases in target regions": "57742646", 
	                            "Number of mapped reads": "48026110", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Percent reads on target": "94.01%", 
	                            "Average base coverage depth": "130.8", 
	                            "Reference (File)": "hg19", 
	                            "Coverage Analysis Lite Report": "N/A", 
	                            "Target base coverage at 100x": "61.01%", 
	                            "Target base coverage at 20x": "94.93%", 
	                            "Uniformity of base coverage": "93.55%", 
	                            "Target base coverage at 1x": "98.55%", 
	                            "Using": "All Mapped Reads", 
	                            "Target base coverage at 500x": "0.22%", 
	                            "Alignments": "IonXpress_034_R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	                            "Total base reads on target": "7552568443"
	                        }
	                    }
	                }, 
	                "SystematicErrorAnalysis": {
	                    "qts_peak": "NaN", 
	                    "indel-5-per-mb": "10626.700000000001", 
	                    "positions-with-sse": "0.0080719999999999993", 
	                    "qts_base": "NaN", 
	                    "barcoded": "true", 
	                    "positions-with-sse-d15": "0.0080719999999999993", 
	                    "Target-regions_file": "/results/uploads/BED/46/hg19/merged/plain/AmpliSeqExome.20131001.designed.bed", 
	                    "stb-95-per-mb": "67945.399999999994", 
	                    "positions-with-sse-i5": "0.0073000000000000001", 
	                    "positions-with-sse-d5": "0.023935000000000001", 
	                    "positions-with-sse-i15": "0.0018799999999999999", 
	                    "indel-15-per-mb": "3118.8000000000002", 
	                    "barcodes": {
	                        "IonXpress_033": {
	                            "indel-5-per-mb": "10600.3", 
	                            "positions-with-sse": "0.007770", 
	                            "positions-with-sse-d15": "0.007770", 
	                            "stb-95-per-mb": "68851.0", 
	                            "positions-with-sse-i5": "0.007519", 
	                            "positions-with-sse-d5": "0.022925", 
	                            "positions-with-sse-i15": "0.001964", 
	                            "indel-15-per-mb": "3126.1"
	                        }, 
	                        "IonXpress_034": {
	                            "indel-5-per-mb": "10653.1", 
	                            "positions-with-sse": "0.008373", 
	                            "positions-with-sse-d15": "0.008373", 
	                            "stb-95-per-mb": "67039.8", 
	                            "positions-with-sse-i5": "0.007080", 
	                            "positions-with-sse-d5": "0.024945", 
	                            "positions-with-sse-i15": "0.001796", 
	                            "indel-15-per-mb": "3111.5"
	                        }
	                    }
	                }, 
	                "1_Torrent_Accuracy": {}, 
	                "duplicateReads_useZC": {
	                    "adapter_found_rate_chr1": "0.89400000000000002", 
	                    "duplicate_reads_chr1": 673650, 
	                    "duprate_at_725k_chr1": "0.89300000000000002", 
	                    "duplicate_rate_chr1": "0.89200000000000002", 
	                    "total_reads_chr1": 754826
	                }, 
	                "autoCal": {
	                    "dc_range": 0
	                }, 
	                "variantCaller": {
	                    "barcodes": {
	                        "IonXpress_033": {
	                            "hotspots": {}, 
	                            "variants": {
	                                "no_call": 0, 
	                                "homo_snps": 18047, 
	                                "het_snps": 31409, 
	                                "other": 1321, 
	                                "variants": 54343, 
	                                "het_indels": 2444, 
	                                "homo_indels": 1122
	                            }
	                        }, 
	                        "IonXpress_034": {
	                            "hotspots": {}, 
	                            "variants": {
	                                "no_call": 0, 
	                                "homo_snps": 18134, 
	                                "het_snps": 31524, 
	                                "other": 1308, 
	                                "variants": 54522, 
	                                "het_indels": 2422, 
	                                "homo_indels": 1134
	                            }
	                        }
	                    }, 
	                    "barcoded": "true", 
	                    "targets_bed": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	                    "Target Regions": "AmpliSeqExome.20131001.designed", 
	                    "Trim Reads": true, 
	                    "Target Loci": "Not using", 
	                    "Configuration": "Germ Line - Proton - Low Stringency", 
	                    "Aligned Reads": "R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf", 
	                    "Library Type": "AmpliSeq"
	                }, 
	                "ConversionRate": {}, 
	                "validateVariantCaller": {
	                    "SNP_FP-ConfidentPos": 5410, 
	                    "InDel_AmbPos-AllPos": 0, 
	                    "SNP_PPV>=30x": "96.7228784857032", 
	                    "InDel_FN>=100x": 930, 
	                    "SNP_FN>=100x": 896, 
	                    "InDel_TP-AllPos": 2591, 
	                    "InDel_FP>=30x": 1689, 
	                    "SNP_FN>=30x": 2004, 
	                    "SNP_FP>=1000x": 0, 
	                    "SNP_ConsensusAccuracy-AllPos": "0.999914181450164", 
	                    "InDel_NoCalls-AllPos": 894775, 
	                    "InDel_FP-AllPos": 2681, 
	                    "InDel_FP_50x-100x": 695, 
	                    "InDel_Sensitivity>=20x": "47.7212806026365", 
	                    "SNP_TP>=500x": 132, 
	                    "SNP_Sensitivity>=100x": "98.2144280589877", 
	                    "SNP_Sensitivity>=500x": "99.2481203007519", 
	                    "InDel_ConsensusAccuracy-AllPos": "0.999949885886992", 
	                    "SNP_ConsensusAccuracy>=50x": "0.999971537775062", 
	                    "InDel_FN>=20x": 2776, 
	                    "SNP_FP>=50x": 1762, 
	                    "InDel_PPV-AllPos": "49.1464339908953", 
	                    "InDel_ConsensusAccuracy>=30x": "0.999964918459836", 
	                    "InDel_FP-ncRNA": 18, 
	                    "InDel_ReferenceCalls-AllPos": 0, 
	                    "Target-regions_file": "/results/analysis/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/plugin_out/validateVariantCaller_out.570190/../variantCaller_out.564691/AmpliSeqExome.20131001.designed.bed", 
	                    "SNP_TP-AllPos": 87058, 
	                    "InDel_Sensitivity>=30x": "49.0349819059107", 
	                    "InDel_FN>=500x": 3, 
	                    "InDel_FP_20x-50x": 827, 
	                    "InDel_FP-ConfidentPos": 2681, 
	                    "InDel_FN-AllPos": 3353, 
	                    "SNP_HP11-AllPos": 0, 
	                    "InDel_FN>=50x": 2041, 
	                    "SNP_Sensitivity-AllPos": "94.6478076994162", 
	                    "Truth-major_SNP_file": "NA12878_NIST_NoChrY_SNP.bed", 
	                    "InDel_Sensitivity-AllAnnotations": "87.1800314804519", 
	                    "SNP_FP_200x-300x": 84, 
	                    "InDel_FP>=20x": 2020, 
	                    "SNP_FN>=500x": 1, 
	                    "Combined Variant Positive Predictive Value for All Bases at >=20x": "94.0001", 
	                    "SNP_Sensitivity>=1000x": 100, 
	                    "InDel_FP_700x-1000x": 0, 
	                    "SNP_FP>=30x": 2777, 
	                    "SNP_FP_700x-1000x": 0, 
	                    "SNP_ConsensusAccuracy>=20x": "0.999952352557784", 
	                    "InDel_TP>=30x": 2439, 
	                    "SNP_AmbPos-AllPos": 0, 
	                    "Truth-minor_InDel_file": "None", 
	                    "SNP_FP_500x-700x": 1, 
	                    "SNP_FP_50x-100x": 1095, 
	                    "InDel_ConsensusAccuracy>=20x": "0.999960167834606", 
	                    "InDel_FP-Exons": 1062, 
	                    "SNP_TP>=30x": 81962, 
	                    "SNP_ReferenceCalls-AllPos": 0, 
	                    "InDel_FP_500x-700x": 1, 
	                    "InDel_FP_200x-300x": 65, 
	                    "barcoded": "true", 
	                    "SNP_FP_20x-50x": 1773, 
	                    "SNP_FP>=100x": 667, 
	                    "SNP_Sensitivity>=20x": "97.4601197273262", 
	                    "InDel_FP_300x-400x": 9, 
	                    "SNP_FP_100x-200x": 565, 
	                    "barcodes": {
	                        "IonXpress_033": {
	                            "SNP_FP-ConfidentPos": "2733", 
	                            "InDel_AmbPos-AllPos": "0", 
	                            "SNP_PPV>=30x": "96.7970258096804", 
	                            "InDel_FN>=100x": "411", 
	                            "SNP_FN>=100x": "406", 
	                            "InDel_TP-AllPos": "1281", 
	                            "InDel_FP>=30x": "838", 
	                            "SNP_FN>=30x": "1006", 
	                            "SNP_FP>=1000x": "0", 
	                            "SNP_ConsensusAccuracy-AllPos": "0.999912578529413", 
	                            "InDel_NoCalls-AllPos": "450359", 
	                            "InDel_FP-AllPos": "1375", 
	                            "InDel_FP_50x-100x": "369", 
	                            "InDel_Sensitivity>=20x": "47.4402730375427", 
	                            "SNP_TP>=500x": "44", 
	                            "SNP_Sensitivity>=100x": "98.2229614391386", 
	                            "SNP_Sensitivity>=500x": "100", 
	                            "InDel_ConsensusAccuracy-AllPos": "0.999949088579261", 
	                            "SNP_ConsensusAccuracy>=50x": "0.999972775263102", 
	                            "InDel_FN>=20x": "1386", 
	                            "SNP_FP>=50x": "829", 
	                            "InDel_PPV-AllPos": "48.230421686747", 
	                            "InDel_ConsensusAccuracy>=30x": "0.99996518422908", 
	                            "InDel_FP-ncRNA": "9", 
	                            "InDel_ReferenceCalls-AllPos": "0", 
	                            "SNP_TP-AllPos": "43461", 
	                            "InDel_Sensitivity>=30x": "48.7158581328985", 
	                            "InDel_FN>=500x": "1", 
	                            "InDel_FP_20x-50x": "437", 
	                            "InDel_FP-ConfidentPos": "1375", 
	                            "InDel_FN-AllPos": "1690", 
	                            "SNP_HP11-AllPos": "0", 
	                            "InDel_FN>=50x": "977", 
	                            "SNP_Sensitivity-AllPos": "94.4989237024635", 
	                            "InDel_Sensitivity-AllAnnotations": "43.1167956916863", 
	                            "SNP_FP_200x-300x": "34", 
	                            "InDel_FP>=20x": "1013", 
	                            "SNP_FN>=500x": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at >=20x": "94.022600", 
	                            "SNP_Sensitivity>=1000x": "0", 
	                            "InDel_FP_700x-1000x": "0", 
	                            "SNP_FP>=30x": "1344", 
	                            "SNP_FP_700x-1000x": "0", 
	                            "SNP_ConsensusAccuracy>=20x": "0.999952742906361", 
	                            "InDel_TP>=30x": "1195", 
	                            "SNP_AmbPos-AllPos": "0", 
	                            "SNP_FP_500x-700x": "0", 
	                            "SNP_FP_50x-100x": "536", 
	                            "InDel_ConsensusAccuracy>=20x": "0.999960151224028", 
	                            "InDel_FP-Exons": "537", 
	                            "SNP_TP>=30x": "40617", 
	                            "SNP_ReferenceCalls-AllPos": "0", 
	                            "InDel_FP_500x-700x": "0", 
	                            "InDel_FP_200x-300x": "29", 
	                            "SNP_FP_20x-50x": "911", 
	                            "SNP_FP>=100x": "293", 
	                            "SNP_Sensitivity>=20x": "97.439640391121", 
	                            "InDel_FP_300x-400x": "0", 
	                            "SNP_FP_100x-200x": "255", 
	                            "SNP_Sensitivity-AllAnnotations": "94.4989237024635", 
	                            "InDel_FP_400x-500x": "2", 
	                            "InDel_FP>=50x": "576", 
	                            "SNP_FN-AllAnnotations": "2530", 
	                            "SNP_FP-AllPos": "2733", 
	                            "SNP_PPV-AllPos": "94.0836472269126", 
	                            "SNP_FP>=20x": "1740", 
	                            "InDel_Sensitivity>=1000x": "0", 
	                            "InDel_ConsensusAccuracy>=50x": "0.999974203772787", 
	                            "InDel_TP>=100x": "616", 
	                            "SNP_TP>=50x": "36440", 
	                            "SNP_ConsensusAccuracy>=30x": "0.999960965142337", 
	                            "InDel_Sensitivity-AllPos": "43.1167956916863", 
	                            "InDel_TP>=20x": "1251", 
	                            "InDel_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP>=500x": "0", 
	                            "% Callable Bases": "99.161500", 
	                            "SNP_FN>=20x": "1105", 
	                            "InDel_FP>=1000x": "0", 
	                            "SNP_Sensitivity>=30x": "97.5830670542729", 
	                            "InDel_FN>=1000x": "0", 
	                            "InDel_FP>=500x": "0", 
	                            "SNP_FP_400x-500x": "2", 
	                            "InDel_HP11-AllPos": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at all coverages": "91.590500", 
	                            "SNP_FN>=1000x": "0", 
	                            "SNP_FN>=50x": "810", 
	                            "InDel_TP>=500x": "2", 
	                            "InDel_PPV>=30x": "58.780127889818", 
	                            "InDel_TP>=1000x": "0", 
	                            "SNP_FP_300x-400x": "2", 
	                            "SNP_Sensitivity>=50x": "97.8255033557047", 
	                            "Combined Variant Sensitivity for All Bases at >= 20x": "94.560500", 
	                            "SNP_TP>=100x": "22441", 
	                            "InDel_FP>=100x": "207", 
	                            "SNP_NoCalls-AllPos": "56910", 
	                            "InDel_Sensitivity>=500x": "66.6666666666667", 
	                            "SNP_TP>=20x": "42053", 
	                            "InDel_Sensitivity>=50x": "52.3182040019522", 
	                            "InDel_FN-AllAnnotations": "1690", 
	                            "InDel_TP>=50x": "1072", 
	                            "SNP_TP>=1000x": "0", 
	                            "InDel_FN>=30x": "1258", 
	                            "SNP_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP-ncRNA": "28", 
	                            "SNP_FN-AllPos": "2530", 
	                            "InDel_Sensitivity>=100x": "59.9805258033106", 
	                            "InDel_FP_100x-200x": "176", 
	                            "SNP_FP-Exons": "993", 
	                            "Combined Variant Sensitivity for All Bases at all coverages": "91.381000"
	                        }, 
	                        "IonXpress_034": {
	                            "SNP_FP-ConfidentPos": "2677", 
	                            "InDel_AmbPos-AllPos": "0", 
	                            "SNP_PPV>=30x": "96.6501472719622", 
	                            "InDel_FN>=100x": "519", 
	                            "SNP_FN>=100x": "490", 
	                            "InDel_TP-AllPos": "1310", 
	                            "InDel_FP>=30x": "851", 
	                            "SNP_FN>=30x": "998", 
	                            "SNP_FP>=1000x": "0", 
	                            "SNP_ConsensusAccuracy-AllPos": "0.999915784370915", 
	                            "InDel_NoCalls-AllPos": "444416", 
	                            "InDel_FP-AllPos": "1306", 
	                            "InDel_FP_50x-100x": "326", 
	                            "InDel_Sensitivity>=20x": "47.9985035540591", 
	                            "SNP_TP>=500x": "88", 
	                            "SNP_Sensitivity>=100x": "98.2072952109172", 
	                            "SNP_Sensitivity>=500x": "98.876404494382", 
	                            "InDel_ConsensusAccuracy-AllPos": "0.999950683194723", 
	                            "SNP_ConsensusAccuracy>=50x": "0.999970300287021", 
	                            "InDel_FN>=20x": "1390", 
	                            "SNP_FP>=50x": "933", 
	                            "InDel_PPV-AllPos": "50.0764525993884", 
	                            "InDel_ConsensusAccuracy>=30x": "0.999964652690593", 
	                            "InDel_FP-ncRNA": "9", 
	                            "InDel_ReferenceCalls-AllPos": "0", 
	                            "SNP_TP-AllPos": "43597", 
	                            "InDel_Sensitivity>=30x": "49.3454978183261", 
	                            "InDel_FN>=500x": "2", 
	                            "InDel_FP_20x-50x": "390", 
	                            "InDel_FP-ConfidentPos": "1306", 
	                            "InDel_FN-AllPos": "1663", 
	                            "SNP_HP11-AllPos": "0", 
	                            "InDel_FN>=50x": "1064", 
	                            "SNP_Sensitivity-AllPos": "94.7966949336812", 
	                            "InDel_Sensitivity-AllAnnotations": "44.0632357887656", 
	                            "SNP_FP_200x-300x": "50", 
	                            "InDel_FP>=20x": "1007", 
	                            "SNP_FN>=500x": "1", 
	                            "Combined Variant Positive Predictive Value for All Bases at >=20x": "93.977600", 
	                            "SNP_Sensitivity>=1000x": "100", 
	                            "InDel_FP_700x-1000x": "0", 
	                            "SNP_FP>=30x": "1433", 
	                            "SNP_FP_700x-1000x": "0", 
	                            "SNP_ConsensusAccuracy>=20x": "0.999951962209208", 
	                            "InDel_TP>=30x": "1244", 
	                            "SNP_AmbPos-AllPos": "0", 
	                            "SNP_FP_500x-700x": "1", 
	                            "SNP_FP_50x-100x": "559", 
	                            "InDel_ConsensusAccuracy>=20x": "0.999960184445184", 
	                            "InDel_FP-Exons": "525", 
	                            "SNP_TP>=30x": "41345", 
	                            "SNP_ReferenceCalls-AllPos": "0", 
	                            "InDel_FP_500x-700x": "1", 
	                            "InDel_FP_200x-300x": "36", 
	                            "SNP_FP_20x-50x": "862", 
	                            "SNP_FP>=100x": "374", 
	                            "SNP_Sensitivity>=20x": "97.4804198534647", 
	                            "InDel_FP_300x-400x": "9", 
	                            "SNP_FP_100x-200x": "310", 
	                            "SNP_Sensitivity-AllAnnotations": "94.7966949336812", 
	                            "InDel_FP_400x-500x": "0", 
	                            "InDel_FP>=50x": "617", 
	                            "SNP_FN-AllAnnotations": "2393", 
	                            "SNP_FP-AllPos": "2677", 
	                            "SNP_PPV-AllPos": "94.2148938928988", 
	                            "SNP_FP>=20x": "1795", 
	                            "InDel_Sensitivity>=1000x": "0", 
	                            "InDel_ConsensusAccuracy>=50x": "0.999972077618838", 
	                            "InDel_TP>=100x": "771", 
	                            "SNP_TP>=50x": "38295", 
	                            "SNP_ConsensusAccuracy>=30x": "0.999959619685541", 
	                            "InDel_Sensitivity-AllPos": "44.0632357887656", 
	                            "InDel_TP>=20x": "1283", 
	                            "InDel_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP>=500x": "1", 
	                            "% Callable Bases": "99.176600", 
	                            "SNP_FN>=20x": "1097", 
	                            "InDel_FP>=1000x": "0", 
	                            "SNP_Sensitivity>=30x": "97.6430578844201", 
	                            "InDel_FN>=1000x": "0", 
	                            "InDel_FP>=500x": "1", 
	                            "SNP_FP_400x-500x": "2", 
	                            "InDel_HP11-AllPos": "0", 
	                            "Combined Variant Positive Predictive Value for All Bases at all coverages": "91.853100", 
	                            "SNP_FN>=1000x": "0", 
	                            "SNP_FN>=50x": "855", 
	                            "InDel_TP>=500x": "2", 
	                            "InDel_PPV>=30x": "59.3794749403341", 
	                            "InDel_TP>=1000x": "0", 
	                            "SNP_FP_300x-400x": "11", 
	                            "SNP_Sensitivity>=50x": "97.816091954023", 
	                            "Combined Variant Sensitivity for All Bases at >= 20x": "94.618200", 
	                            "SNP_TP>=100x": "26843", 
	                            "InDel_FP>=100x": "291", 
	                            "SNP_NoCalls-AllPos": "53768", 
	                            "InDel_Sensitivity>=500x": "50", 
	                            "SNP_TP>=20x": "42442", 
	                            "InDel_Sensitivity>=50x": "51.5041020966272", 
	                            "InDel_FN-AllAnnotations": "1663", 
	                            "InDel_TP>=50x": "1130", 
	                            "SNP_TP>=1000x": "3", 
	                            "InDel_FN>=30x": "1277", 
	                            "SNP_AmbNotDetected-AllPos": "0", 
	                            "SNP_FP-ncRNA": "32", 
	                            "SNP_FN-AllPos": "2393", 
	                            "InDel_Sensitivity>=100x": "59.7674418604651", 
	                            "InDel_FP_100x-200x": "245", 
	                            "SNP_FP-Exons": "958", 
	                            "Combined Variant Sensitivity for All Bases at all coverages": "91.716100"
	                        }
	                    }, 
	                    "SNP_Sensitivity-AllAnnotations": "189.295618636145", 
	                    "InDel_FP_400x-500x": 2, 
	                    "InDel_FP>=50x": 1193, 
	                    "SNP_FN-AllAnnotations": 4923, 
	                    "SNP_FP-AllPos": 5410, 
	                    "SNP_PPV-AllPos": "94.1493273348618", 
	                    "SNP_FP>=20x": 3535, 
	                    "InDel_Sensitivity>=1000x": 0, 
	                    "InDel_ConsensusAccuracy>=50x": "0.999973140695813", 
	                    "InDel_TP>=100x": 1387, 
	                    "Region_selected": "NIST", 
	                    "SNP_ConsensusAccuracy>=30x": "0.999960292413939", 
	                    "InDel_Sensitivity-AllPos": "43.5901749663526", 
	                    "InDel_TP>=20x": 2534, 
	                    "InDel_AmbNotDetected-AllPos": 0, 
	                    "SNP_FP>=500x": 1, 
	                    "% Callable Bases": "99.16905", 
	                    "SNP_FN>=20x": 2202, 
	                    "InDel_FP>=1000x": 0, 
	                    "SNP_Sensitivity>=30x": "97.6133196770121", 
	                    "InDel_FN>=1000x": 0, 
	                    "InDel_FP>=500x": 1, 
	                    "SNP_FP_400x-500x": 4, 
	                    "InDel_HP11-AllPos": 0, 
	                    "Combined Variant Positive Predictive Value for All Bases at all coverages": "91.7218", 
	                    "SNP_FN>=1000x": 0, 
	                    "SNP_FN>=50x": 1665, 
	                    "InDel_TP>=500x": 4, 
	                    "InDel_PPV>=30x": "59.0843023255814", 
	                    "InDel_TP>=1000x": 0, 
	                    "Truth-minor_SNP_file": "None", 
	                    "SNP_FP_300x-400x": 13, 
	                    "SNP_Sensitivity>=50x": "97.8206806282722", 
	                    "Combined Variant Sensitivity for All Bases at >= 20x": "94.58935", 
	                    "SNP_TP>=100x": 49284, 
	                    "Sample_selected": "NA12878", 
	                    "InDel_FP>=100x": 498, 
	                    "SNP_NoCalls-AllPos": 110678, 
	                    "Truth-major_InDel_file": "NA12878_NIST_NoChrY_indel.bed", 
	                    "InDel_Sensitivity>=500x": "57.1428571428571", 
	                    "SNP_TP>=20x": 84495, 
	                    "InDel_Sensitivity>=50x": "51.897242517087", 
	                    "InDel_FN-AllAnnotations": 3353, 
	                    "InDel_TP>=50x": 2202, 
	                    "SNP_TP>=1000x": 3, 
	                    "InDel_FN>=30x": 2535, 
	                    "Variant-caller_name": "variantCaller", 
	                    "SNP_AmbNotDetected-AllPos": 0, 
	                    "SNP_TP>=50x": 74735, 
	                    "SNP_FP-ncRNA": 60, 
	                    "SNP_FN-AllPos": 4923, 
	                    "InDel_Sensitivity>=100x": "59.8618903754855", 
	                    "InDel_FP_100x-200x": 421, 
	                    "SNP_FP-Exons": 1951, 
	                    "Combined Variant Sensitivity for All Bases at all coverages": "91.54855"
	                }, 
	                "timingPerformance": {
	                    "runtime": {
	                        "analysis": "334.17000000000002"
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
	                        "flows": 500, 
	                        "chiptype": "900"
	                    }
	                }, 
	                "coverageAnalysis": {
	                    "Non-duplicate": "No", 
	                    "barcoded": "true", 
	                    "Uniquely mapped": "No", 
	                    "Amplicons reading end-to-end": "26.72%", 
	                    "Targetted regions": "/results/uploads/BED/46/hg19/merged/detail/AmpliSeqExome.20131001.designed.bed", 
	                    "Target padding": "0", 
	                    "barcodes": {
	                        "IonXpress_033": {
	                            "Bases in target regions": "57742646", 
	                            "Amplicons with at least 1 read": "99.21%", 
	                            "Target base coverage at 100x": "51.05%", 
	                            "Amplicons with at least 500 reads": "0.13%", 
	                            "Total assigned amplicon reads": "39187438", 
	                            "Reference (File)": "hg19", 
	                            "Total base reads on target": "6490060189", 
	                            "Target base coverage at 20x": "94.26%", 
	                            "Number of amplicons": "293903", 
	                            "Target bases with no strand bias": "76.79%", 
	                            "Percent reads on target": "94.39%", 
	                            "Amplicons with at least 100 reads": "64.34%", 
	                            "Average base coverage depth": "112.4", 
	                            "Average reads per amplicon": "133.3", 
	                            "Using": "All Mapped Reads", 
	                            "Amplicons reading end-to-end": "25.70%", 
	                            "Sample Name": "None", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Uniformity of base coverage": "93.56%", 
	                            "Alignments": "IonXpress_033_R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	                            "Amplicons with at least 20 reads": "95.84%", 
	                            "Number of mapped reads": "41517304", 
	                            "Percent assigned amplicon reads": "94.39%", 
	                            "Amplicons with no strand bias": "92.84%", 
	                            "Total aligned base reads": "6846723653", 
	                            "Target base coverage at 1x": "98.53%", 
	                            "Target base coverage at 500x": "0.10%", 
	                            "Percent base reads on target": "94.79%", 
	                            "Uniformity of amplicon coverage": "94.62%"
	                        }, 
	                        "IonXpress_034": {
	                            "Bases in target regions": "57742646", 
	                            "Amplicons with at least 1 read": "99.24%", 
	                            "Target base coverage at 100x": "61.01%", 
	                            "Amplicons with at least 500 reads": "0.24%", 
	                            "Total assigned amplicon reads": "45147738", 
	                            "Reference (File)": "hg19", 
	                            "Total base reads on target": "7552568443", 
	                            "Target base coverage at 20x": "94.93%", 
	                            "Number of amplicons": "293903", 
	                            "Target bases with no strand bias": "77.82%", 
	                            "Percent reads on target": "94.01%", 
	                            "Amplicons with at least 100 reads": "72.27%", 
	                            "Average base coverage depth": "130.8", 
	                            "Average reads per amplicon": "153.6", 
	                            "Using": "All Mapped Reads", 
	                            "Amplicons reading end-to-end": "27.74%", 
	                            "Sample Name": "None", 
	                            "Targeted Regions": "AmpliSeqExome.20131001.designed", 
	                            "Uniformity of base coverage": "93.55%", 
	                            "Alignments": "IonXpress_034_R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	                            "Amplicons with at least 20 reads": "96.17%", 
	                            "Number of mapped reads": "48026110", 
	                            "Percent assigned amplicon reads": "94.01%", 
	                            "Amplicons with no strand bias": "92.98%", 
	                            "Total aligned base reads": "8002544816", 
	                            "Target base coverage at 1x": "98.55%", 
	                            "Target base coverage at 500x": "0.22%", 
	                            "Percent base reads on target": "94.38%", 
	                            "Uniformity of amplicon coverage": "94.48%"
	                        }
	                    }
	                }, 
	                "VariantQC": {
	                    "IonXpress_033": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6386, 
	                                "REJECTION": 610, 
	                                "Cov": 72787, 
	                                "REF": 472111, 
	                                "HEALED": 348, 
	                                "SHIFT": 458087, 
	                                "SSE": 78820, 
	                                "STRINGENCY": 1500, 
	                                ".": 538589, 
	                                "Quality": 103314, 
	                                "STDBIAS": 12975
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1036, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 54299, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 432, 
	                                "10": 972, 
	                                "13": 178, 
	                                "12": 193, 
	                                "15": 160, 
	                                "14": 143, 
	                                "1": 74456, 
	                                "0": 57194, 
	                                "3": 92797, 
	                                "2": 124391, 
	                                "5": 52748, 
	                                "4": 62684, 
	                                "7": 11651, 
	                                "6": 25769, 
	                                "9": 2199, 
	                                "8": 4196
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
	                                "11": 43, 
	                                "10": 45, 
	                                "13": 20, 
	                                "12": 38, 
	                                "15": 27, 
	                                "14": 27, 
	                                "1": 29948, 
	                                "0": 561, 
	                                "3": 5112, 
	                                "2": 12151, 
	                                "5": 1238, 
	                                "4": 2386, 
	                                "7": 248, 
	                                "6": 567, 
	                                "9": 73, 
	                                "8": 145
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 37034, 
	                                "del": 278917, 
	                                "snp": 37539, 
	                                "ins": 185099
	                            }, 
	                            "unfiltered": {
	                                "other": 2479, 
	                                "del": 1093, 
	                                "snp": 49277, 
	                                "ins": 1450
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 538589, 
	                            "unfiltered": 54299
	                        }
	                    }, 
	                    "IonXpress_034": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6511, 
	                                "REJECTION": 545, 
	                                "Cov": 65871, 
	                                "REF": 462781, 
	                                "HEALED": 355, 
	                                "SHIFT": 454012, 
	                                "SSE": 83658, 
	                                "STRINGENCY": 1396, 
	                                ".": 529663, 
	                                "Quality": 83379, 
	                                "STDBIAS": 12531
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1082, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 54469, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 407, 
	                                "10": 968, 
	                                "13": 156, 
	                                "12": 186, 
	                                "15": 145, 
	                                "14": 154, 
	                                "1": 67025, 
	                                "0": 51375, 
	                                "3": 92736, 
	                                "2": 124890, 
	                                "5": 54756, 
	                                "4": 63630, 
	                                "7": 12138, 
	                                "6": 26845, 
	                                "9": 2248, 
	                                "8": 4436
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
	                                "11": 39, 
	                                "10": 49, 
	                                "13": 35, 
	                                "12": 32, 
	                                "15": 18, 
	                                "14": 33, 
	                                "1": 30034, 
	                                "0": 522, 
	                                "3": 5116, 
	                                "2": 12152, 
	                                "5": 1261, 
	                                "4": 2435, 
	                                "7": 267, 
	                                "6": 573, 
	                                "9": 65, 
	                                "8": 139
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 35770, 
	                                "del": 302522, 
	                                "snp": 35483, 
	                                "ins": 155888
	                            }, 
	                            "unfiltered": {
	                                "other": 2501, 
	                                "del": 1095, 
	                                "snp": 49486, 
	                                "ins": 1387
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 529663, 
	                            "unfiltered": 54469
	                        }
	                    }, 
	                    "summary": {
	                        "reason": {
	                            "filtered": {
	                                "HPLEN": 6386, 
	                                "REJECTION": 610, 
	                                "Cov": 72787, 
	                                "REF": 472111, 
	                                "HEALED": 348, 
	                                "SHIFT": 458087, 
	                                "SSE": 78820, 
	                                "STRINGENCY": 1500, 
	                                ".": 538589, 
	                                "Quality": 103314, 
	                                "STDBIAS": 12975
	                            }, 
	                            "unfiltered": {
	                                "HPLEN": 0, 
	                                "REJECTION": 0, 
	                                "Cov": 0, 
	                                "REF": 0, 
	                                "HEALED": 1036, 
	                                "SHIFT": 0, 
	                                "SSE": 0, 
	                                "STRINGENCY": 0, 
	                                ".": 54299, 
	                                "Quality": 0, 
	                                "STDBIAS": 0
	                            }
	                        }, 
	                        "hrun": {
	                            "filtered": {
	                                "11": 432, 
	                                "10": 972, 
	                                "13": 178, 
	                                "12": 193, 
	                                "15": 160, 
	                                "14": 143, 
	                                "1": 74456, 
	                                "0": 57194, 
	                                "3": 92797, 
	                                "2": 124391, 
	                                "5": 52748, 
	                                "4": 62684, 
	                                "7": 11651, 
	                                "6": 25769, 
	                                "9": 2199, 
	                                "8": 4196
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
	                                "11": 43, 
	                                "10": 45, 
	                                "13": 20, 
	                                "12": 38, 
	                                "15": 27, 
	                                "14": 27, 
	                                "1": 29948, 
	                                "0": 561, 
	                                "3": 5112, 
	                                "2": 12151, 
	                                "5": 1238, 
	                                "4": 2386, 
	                                "7": 248, 
	                                "6": 567, 
	                                "9": 73, 
	                                "8": 145
	                            }
	                        }, 
	                        "type": {
	                            "filtered": {
	                                "other": 37034, 
	                                "del": 278917, 
	                                "snp": 37539, 
	                                "ins": 185099
	                            }, 
	                            "unfiltered": {
	                                "other": 2479, 
	                                "del": 1093, 
	                                "snp": 49277, 
	                                "ins": 1450
	                            }
	                        }, 
	                        "basic": {
	                            "filtered": 538589, 
	                            "unfiltered": 54299
	                        }
	                    }
	                }
	            }, 
	            "resultsType": "", 
	            "tfFastq": "_", 
	            "tfmetrics": [
	                "/rundb/api/v1/tfmetrics/3119/", 
	                "/rundb/api/v1/tfmetrics/3118/", 
	                "/rundb/api/v1/tfmetrics/3117/"
	            ], 
	            "parentIDs": "", 
	            "analysismetrics": [
	                "/rundb/api/v1/analysismetrics/31763/"
	            ], 
	            "timeToComplete": "0", 
	            "reportLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/", 
	            "fastqLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/basecaller_results/R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446.fastq", 
	            "pluginresults": [
	                "/rundb/api/v1/pluginresult/570190/", 
	                "/rundb/api/v1/pluginresult/564696/", 
	                "/rundb/api/v1/pluginresult/564695/", 
	                "/rundb/api/v1/pluginresult/564694/", 
	                "/rundb/api/v1/pluginresult/564692/", 
	                "/rundb/api/v1/pluginresult/564691/", 
	                "/rundb/api/v1/pluginresult/564690/", 
	                "/rundb/api/v1/pluginresult/564689/", 
	                "/rundb/api/v1/pluginresult/564688/", 
	                "/rundb/api/v1/pluginresult/564687/", 
	                "/rundb/api/v1/pluginresult/564686/"
	            ], 
	            "framesProcessed": 0, 
	            "autoExempt": false, 
	            "resource_uri": "/rundb/api/v1/results/293943/"
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

