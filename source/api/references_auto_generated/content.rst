.. _api_reference_content:

Content  Resource
=================

| Resource URL ``http://mytorrentserver/rundb/api/v1/content/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/content/schema/``
| 

.. include:: ../references_manual_extras/content.rst

Resource Fields
---------------

==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
field                help text                                                                      default nullable readonly blank unique type     
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 
**publisher**        A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**description**      Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**extra**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**contentupload**    A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**notes**            Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**enabled**          Boolean data. Ex: True                                                         true    false    false    true  false  boolean  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload_date**      A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     false    true     false false  datetime 
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**application_tags** Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**meta**             Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**upload_id**        Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**file**             Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**path**             Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**     Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**type**             Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**               Integer data. Ex: 2673                                                                 false    false    true  true   integer  
-------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**name**             Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
==================== ============================================================================== ======= ======== ======== ===== ====== ======== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 31, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/content/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "publisher": "/rundb/api/v1/publisher/BED/", 
	            "description": "Noonan Panel", 
	            "extra": "hg19", 
	            "contentupload": "/rundb/api/v1/contentupload/1/", 
	            "notes": "", 
	            "enabled": true, 
	            "upload_date": "2018-01-16T18:30:05+00:00", 
	            "application_tags": "", 
	            "meta": {
	                "upload_date": "2018-01-16T18:30:05", 
	                "description": "Noonan Panel", 
	                "reference": "hg19", 
	                "is_ampliseq": true, 
	                "hotspot": false, 
	                "choice": "pgm", 
	                "num_targets": 268, 
	                "num_genes": 14, 
	                "design": {
	                    "number_of_amplicon_pools": 2, 
	                    "design_name": "Noonan Panel", 
	                    "configuration_choices": [], 
	                    "solution_name": null, 
	                    "id": 60011570, 
	                    "number_of_amplicons": 268, 
	                    "genome_reference": null, 
	                    "target_size": 26992, 
	                    "genome": "hg19", 
	                    "type": "COMMUNITY_PANEL", 
	                    "status": "ORDERABLE", 
	                    "min_number_amplicons_per_pool": 132, 
	                    "description": "<table class=\"design-template-info-wrapper-table\">\r\n    <tr>\r\n        <td colspan=\"3\">\r\n        <br>\r\n            <p>Noonan syndrome is a relatively common autosomal dominant congenital disorder with a high phenotypic variability. It is a clinically and genetically heterogeneous disorder that belongs to the group of Rasopathy diseases, caused by mutations in genes dysregulating the RAS/MAPK pathway.\r\nThe Noonan  Research Gene Panel has been developed in collaboration with an European consortia composed by  Marco Tartaglia(1), Jose Luis Costa (2), Kornelia Neveling and Marcel Nelen (3) . 1) Istituto Superiore di Sanit\u00e0, Rome, Italy, 2) Ipatimup, Porto 3) Human Genetics, Radboud UMC Nijmegen .\r\nThe panel assesses 14 genes known to be related with this disorder. <i>A2ML1</i>, <i>BRAF</i>, <i>CBL</i>, <i>HRAS</i>, <i>KRAS</i>, <i>MAP2K1</i>, <i>MAP2K2</i>, <i>NRAS</i>, <i>PTPN11</i>, <i>RAF1</i>, <i>RIT1</i>, <i>SHOC2</i>, <i>SOS1</i>, <i>SPRED1</i>. In a first study of 60 archived samples we showed that very high sensitivity and specificity are achievable. For further details see ASHG 2014 poster \u201cDevelopment and verification of a Noonan genes Ion AmpliSeq\u2122 panel\u201d M. Nelen et al.\r\n</p>\r\n        </td>\r\n    </tr>\r\n    <tr class=\"design-template-statistics\">\r\n        <td><strong>Design Date</strong></td>\r\n        <td colspan=\"2\" style=\"text-align: left\">\r\n            <b>Publication:</b> ASHG 2014 Poster \"Development and verification of a Noonan genes Ion AmpliSeq\u2122 panel\"<br/>\r\n            <b>Author:</b> Marcel Nelen (<a href='Marcel.Nelen@radboudumc.nl'>Marcel.Nelen@radboudumc.nl</a>)<br/>\r\n            <b>Affiliation:</b> Dept. of Human Genetics, Radboud university medical center, Nijmegen, The Netherlands<br/>\r\n        </td>\r\n    </tr>\r\n    <tr class=\"design-template-statistics\">\r\n        <td>\r\n            <strong>Recommended Application</strong>\r\n            Germ line mutation detection\r\n        </td>\r\n        <td>\r\n            <strong>Recommended Configuration</strong>\r\n            Sample per Chip: 8 per 318 chip<br/>\r\n            Minimum coverage: 684 \r\n        </td>\r\n        <td>\r\n            <strong>Sample Type</strong>\r\n            High molecular weight DNA\r\n        </td>\r\n    </tr>\r\n    <tr class=\"design-template-statistics\">\r\n        <td>\r\n            <strong>Number of sample in Publication</strong>\r\n            60 samples \r\n        </td>\r\n        <td>\r\n            <strong>Observed Performance</strong>\r\n            Panel uniformity: 93.05%<br/>\r\n            Reads on-targets: 98.42% \r\n        </td>\r\n        <td>\r\n            <strong>Input DNA required </strong>\r\n            2 pool<br/>\r\n            20 ng total\r\n        </td>\r\n    </tr>\r\n    <tr>\r\n        <td colspan=\"3\">\r\n            <b>Disease Research Area</b>: Developmental Disorders\r\n        </td>\r\n    </tr>\r\n</table>", 
	                    "results_uri": "/ws/tmpldesign/60011570/download/results", 
	                    "plan": {
	                        "missed_bed": "WG_noonan.20150501.missed.bed", 
	                        "hotspot_bed": null, 
	                        "coverage_summary": "WG_noonan.20150501.results_coverage_summary.csv", 
	                        "designed_bed": "WG_noonan.20150501.designed.bed", 
	                        "target_mutations": null, 
	                        "primer_bed": null, 
	                        "runType": "AMPS", 
	                        "selectedPlugins": {}, 
	                        "inputDna": "20 ng", 
	                        "coverage_detail": "WG_noonan.20150501.results_coverage_details.csv", 
	                        "primer_sequences": null, 
	                        "displayedPanelSize": "26.99 kb", 
	                        "submitted_bed": "WG_noonan.20150501.submitted.bed", 
	                        "well_plate_data": "WG_noonan.20150501.384WellPlateDataSheet.csv"
	                    }, 
	                    "design_id": "Noonan", 
	                    "pipeline": "DNA", 
	                    "request_id_and_solution_ordering_id": "Noonan", 
	                    "pipeline_version": null, 
	                    "created_date": "2015-05-22T20:52:38.703+0000", 
	                    "order_number": 0, 
	                    "amplicons_coverage_summary": 100
	                }, 
	                "pre_process_files": [
	                    "WG_noonan.20150501.designed.bed", 
	                    "WG_noonan.20150501.missed.bed", 
	                    "WG_noonan.20150501.submitted.bed", 
	                    "WG_noonan.20150501.results_coverage_details.csv", 
	                    "WG_noonan.20150501.ampliconDataSheet.csv", 
	                    "WG_noonan.20150501.384WellPlateDataSheet.csv", 
	                    "WG_noonan.20150501.concentration.tab", 
	                    "WG_noonan.20150501.results_coverage_summary.csv", 
	                    "plan.json"
	                ], 
	                "num_bases": 47724
	            }, 
	            "upload_id": "1", 
	            "file": "/results/uploads/BED/1/hg19/unmerged/plain/WG_noonan.20150501.designed.bed", 
	            "path": "/hg19/unmerged/plain/WG_noonan.20150501.designed.bed", 
	            "resource_uri": "/rundb/api/v1/content/1/", 
	            "type": "target", 
	            "id": 1, 
	            "name": "WG_noonan.20150501.designed.bed"
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

