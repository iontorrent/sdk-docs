Torrent Server Suite 3.6: About PlannedExperiment REST API
==========================================================

|  :ref:`Plan_attributes`
|  :ref:`Examples_for_creating_a_plan`
|  :ref:`About_using_POST_to_update_a_plan`
|  :ref:`Sample_information`
|  :ref:`Example_for_creating_a_sample`

Even though the plannedExperiment db schema has changed dramatically in TSS 3.6 as part of the “plan data decentralization” (aka PDD) effort, a facade is provided so if you are already familiar with using the plan REST API, there is not much apparent change. However, note that “selectedPlugins” and “barcodedSamples” are JSON fields.

Overall, for the time being, validation for plan creation happens upstream from the REST API (for GUI-based plan creation) and thus validation during direct REST API posting is minimum. At times when an attribute fails validation, the attribute’s value will be ignored and the plan will be posted.  Until stringent validation is in place during non-GUI REST API posting, please do your due diligence to ensure the data and data format posted are valid.

Moreover, some attributes require "internal" value instead of "customer-facing" value to be persisted (e.g., sequencekitname, chipType). Please refer to the Comment/Expected Value column more details.

.. _Plan_attributes:

Plan Attributes
---------------

**REST API:**

.. code-block:: none

	http://<hostname>/rundb/api/v1/plannedexperiment/?format=json

**SCHEMA:**

+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| Attribute Name      | Required/     | Data Type    | Default| Valid   | Example              | Comment/Expected Value      |
|                     | Optional/     |              | value  | values  |                      |                             |
|                     | Nullable      |              |        |         |                      |                             |
+=====================+===============+==============+========+=========+======================+=============================+
| adapter             | Opt/Nullable  | varchar(256) |        |         |                      | Not really being used       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| autoAnalyze         |               | Boolean      | True   |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| autoName            | Opt/Nullable  | varchar(512) |        |         |                      | Not really being used       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| barcodeId           | Opt/Nullable  | varchar(128) |        |         | IonSet1              | rundb_dnabarcode.name       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| barcodedSamples     | Opt/Nullable  | json         |        |         | {"s1":{"barcodes":   |                             |
|                     |               |              |        |         | ["IonSet1_01"]},     |                             |
|                     |               |              |        |         | "s2":{"barcodes":    |                             |
|                     |               |              |        |         | ["IonSet1_02"]},     |                             |
|                     |               |              |        |         | "s3":{"barcodes":    |                             |
|                     |               |              |        |         | ["IonSet1_03"]}}     |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| bedfile             | Opt/Nullable  | varchar(1024)|        |         | /hg19/unmerged/detail| Target region BED file      |
|                     |               |              |        |         | /4477686_IDP_bedfile |                             |
|                     |               |              |        |         | _20120613.bed        | rundb_content.path          |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| chipBarcode         | Opt/Nullable  | varchar(64)  |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| chipType            | Opt           | varchar(32)  |        |         |                      | rundb_chip.name             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| controlSequence     | Opt/Nullable  | varchar(512) |        |         |                      | rundb_kitinfo.name          |
| kitname             |               |              |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| cycles              | Opt/Nullable  | int          |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| date                | Opt/Nullable  | DateTimeField|        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| expName             | Opt           | varchar(128) |        |         |                      | Do not set the value        |
|                     |               |              |        |         |                      | manually. Crawler will set  |
|                     |               |              |        |         |                      | it during explog processing.|
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| flows               | Req           | int          | 0      |         | 520                  |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| flowsInOrder        | Opt/Nullable  | varchar(512) |        |         |                      | Do not set the value        |
|                     |               |              |        |         |                      | manually.                   |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| forward3primeadapter| Req           | varchar(512) |        |         | ATCACCGACTGCCCATAGAGA|                             |
|                     |               |              |        |         | GGCTGAGAC            |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| id                  | Opt           | int          |        |         |                      | Do not set this value unless|
|                     |               |              |        |         |                      | you are updating a plan.    |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| irworkflow          | Opt           | varchar(1024)|        |         |                      | TS 2.4/IonReporter-related; |
|                     |               |              |        |         |                      | no longer being used.       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isFavorite          | Opt           | Boolean      | False  |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isPlanGroup         | Opt           | Boolean      | False  |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isReusable          | Opt           | Boolean      | False  |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isReverseRun        | Req           | Boolean      | False  | T, F    |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isSystem            | Opt           | Boolean      | False  |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| isSystemDefault     | Opt           | Boolean      | False  |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| libkit              | Opt/Nullable  | varchar(512) |        |         | Ion Xpress Plus      | rundb_kitinfo.name          |
|                     |               |              |        |         | Fragment Library Kit |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| library             | Opt/Nullable  | varchar(512) |        |         | e_coli_db10b         | rundb_referencegenome.      |
|                     |               |              |        |         |                      | short_name                  |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| libraryKey          | Req           | varchar(64)  |        |         | TCAG                 |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| librarykitname      | Opt/Nullable  | varchar(512) |        |         | Ion Xpress Plus      | rundb_kitinfo.name          |
|                     |               |              |        |         | Fragment Library Kit |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| metaData            | Opt           | json         |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| notes               | Opt/Nullable  | varchar(1024)|        |         |                      | See RULE-2                  |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| pairedEndLibrary    | Opt/Nullable  | varchar(512) |        |         |                      | Since paired-end sequencing |
| AdapterName         |               |              |        |         |                      | has been discontinued, do   |
|                     |               |              |        |         |                      | not use.                    |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| parentPlan          | Opt/Nullable  | FK           |        |         |                      | Currently used for paired-  |
|                     |               |              |        |         |                      | end plans only. Since PE    |
|                     |               |              |        |         |                      | plans have been             |
|                     |               |              |        |         |                      | discontinued, do not use.   |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planDisplayedName   |               | varchar(512) |        |         | demo plan            | see RULE-2                  |
|                     |               |              |        |         |                      | REST API posting does not   |
|                     |               |              |        |         |                      | support this attribute yet. |
|                     |               |              |        |         |                      | Use planName instead.       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planExecuted        | Opt           | Boolean      | False  | T, F    |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planExecutedDate    | Opt/Nullable  | DateTimeField|        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planGUID            | Opt/Nullable  | varchar(512) |        |         |                      | Do not set a value manually |
|                     |               |              |        |         |                      | during plan creation.       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planName            |               | varchar(512) |        |         |                      | See RULE-1                  |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planPGM             | Opt/Nullable  | varchar(128) |        |         |                      | Not being used.             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planShortID         | Opt/Nullable  |              |        |         |                      | Do not set a value manually |
|                     |               |              |        |         |                      | during plan creation.       |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| planStatus          |               | varchar(512) | ""     | "",run, | planned              | "void" and "reserved" were  |
|                     |               |              |        | voided, |                      | intended for Paired-End     |
|                     |               |              |        | planned,|                      | plans. We'll reuse these 2  |
|                     |               |              |        | reserved|                      | status in a different       |
|                     |               |              |        |         |                      | context in future releases. | 
|                     |               |              |        |         |                      | Once a plan has been        |
|                     |               |              |        |         |                      | selected for a sequencing   |
|                     |               |              |        |         |                      | run on the instrument, its  |
|                     |               |              |        |         |                      | status will be changed from |
|                     |               |              |        |         |                      | "" or "planned" to "run".   |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| preAnalysis         | Opt           | Boolean      |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| projects            | Opt           | varchar(64)  |        |         | ["project1",         | see RULE-1                  |
|                     |               | for each     |        |         | "project2]           | a list of comma-separated   |
|                     |               | project name |        |         |                      | project names               |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| regionfile          | Opt/Nullable  | varchar(1024)|        |         | /hg19/unmerged/detail| hotspot region BED file.    |
|                     |               |              |        |         | /HSMv12.1_hotspots   |                             |
|                     |               |              |        |         | _NO_JAK2.bed         |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| reverse_primer      | Opt/Nullable  | varchar(128) |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| runMode             | Opt           | varchar(64)  |        | "",     | single               |                             |
|                     |               |              |        | "single"|                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| runType             | Req           | varchar(512) | GENS   | "GENS", |                      | rundb_runtype.runType       |
|                     |               |              |        | "AMPS", |                      |                             |
|                     |               |              |        | "TAR",  |                      |                             |
|                     |               |              |        | "WGNM", |                      |                             |
|                     |               |              |        | "RNA",  |                      |                             |
|                     |               |              |        | "AMPS   |                      |                             |
|                     |               |              |        | _EXOME",|                      |                             |
|                     |               |              |        | AMPS_RNA|                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| runName             | Opt/Nullable  | varchar(255) |        |         |                      | Not being used.             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| sample              | Required for  | varchar(127) |        |         | my_sample            | see RULE-1, RULE-2          |
|                     | plan.         |              |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| sampleDisplayedName | Opt/Nullable  | varchar(127) |        |         | my sample            | see RULE-2, RULE-3          |
|                     |               |              |        |         |                      | REST API posting does not   |
|                     |               |              |        |         |                      | support this attribute yet. |
|                     |               |              |        |         |                      | Use sample instead.         |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| samplePrepKitName   | Opt/Nullable  | varchar(512) |        |         | Ion TargetSeq(tm)    | rundb_kitInfo.name          |
|                     |               |              |        |         | Custom Enrichment Kit|                             |
|                     |               |              |        |         | (1000kb-5000kb)      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| selectedPlugins     | Opt/Nullable  | json         |        |         | {"ERCC_ANALYSIS":{   | Since plugin configuration  |
|                     |               |              |        |         | "userInput":"",      | parameters are stored within|
|                     |               |              |        |         | "version":"3.4.51727"| the selected plugins, it can|
|                     |               |              |        |         | ,"features":[],      | get complicated fast. It is |
|                     |               |              |        |         | "id":52,"name":      | not advised to manually post|
|                     |               |              |        |         | "ERCC_ANALYSIS"}}    | the selectedPlugins json    |
|                     |               |              |        |         |                      | blob.                       |
|                     |               |              |        |         | See NOTE-1 for more. |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| seqKitBarcode       | Opt/Nullable  | varchar(64)  |        |         |                      | Not really being used.      |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| seqeuencekitname    | Recommended to| varchar(512) |        |         | IonPGM200Kit         | rundb_kitinfo.name          |
|                     | set.          |              |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| storageHost         | Opt/Nullable  | varchar(128) |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| storage_options     | Opt           | varchar(200) | A      | A,KI,D  |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| templatingKitName   | Opt/Nullable  | varchar(512) |        |         | Ion OneTouch 200     | for either OneTouch or      |
|                     |               |              |        |         | Template Kit v2 DL   | IonChef                     |
|                     |               |              |        |         |                      | rundb_kitInfo.name          |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| usePostBeadfind     | Opt           | Boolean      |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| usePreBeadfind      | Opt           | Boolean      |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| username            | Opt/Nullable  | varchar(128) |        |         | ionuser              | the user currently logged in|
|                     |               |              |        |         |                      | to Torrent Browser for this |
|                     |               |              |        |         |                      | GUI-based plan creation.    |
|                     |               |              |        |         |                      |                             |
|                     |               |              |        |         |                      | For REST API posting, this  |
|                     |               |              |        |         |                      | is just treated as freeform |
|                     |               |              |        |         |                      | text.                       |
|                     |               |              |        |         |                      |                             |
|                     |               |              |        |         |                      | auth_user.username          |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| variantfrequency    |               |              |        |         |                      | Now variantFrequency config |
|                     |               |              |        |         |                      | param is part of            |
|                     |               |              |        |         |                      | VariantCaller, Value set    |
|                     |               |              |        |         |                      | outside of selectedPlugins  |
|                     |               |              |        |         |                      | will be ignored. Do not use.|
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+

*RULE-1:*

Valid characters: letters, numbers, dashes, underscores, dots.

*RULE-2:*

Valid characters: letters, numbers, spaces, dashes, underscores, dots.

*RULE-3:*

Invalid leading characters: dashes, underscores, dots.

*NOTE-1:*

A more complicated example of the 'selectedPlugins' json blob. Note that they get still more complicated as more plugins are added.

.. code-block:: javascript

	{
		"IonReporterUploader":
		{
			"userInput":
			[
				{
					"Workflow":"Whole Genome",
					"Gender":"Male",
					"barcodeId":"IonXpress_001",
					"sample":"s1",
					"Relation":"Tumor_Normal",
					"RelationRole":"Tumor",
					"setid":"1__41484abf-0d0c-4ab9-8141-143297c28c2a"
				},
				{
					"Workflow":"Whole Genome",
					"Gender":"Male",
					"barcodeId":"IonXpress_002",
					"sample":"s2",
					"Relation":"Tumor_Normal",
					"RelationRole":"Normal",
					"setid":"1__41484abf-0d0c-4ab9-8141-143297c28c2a"
				}
			],
			"version":"3.6.0-r53557",
			"features":["export"],
			"id":"53",
			"name":"IonReporterUploader"
		},
		
		"ERCC_Analysis":
		{
			"userInput":"",
			"version":"3.4.51727",
			"features":[],
			"id":"52",
			"name":"ERCC_Analysis"
		}
	}

.. _Examples_for_creating_a_plan:

Examples for Creating a Plan:
-----------------------------

**Example 1:**

Post a non-barcoded Target Sequencing plan and associate results with 2 projects:

.. code-block:: javascript

	{
		"autoAnalyze":"true",
		"usePreBeadfind":"true",
		"usePostBeadfind":"true",
		"reverselibrarykey":"",
		"reverse3primeadapter":"",
		"libraryKey":"TCAG",
		"forward3primeadapter":"ATCACCGACTGCCCATAGAGAGGCTGAGAC",
		"flows":520,
		"library":"hg19",
		"bedfile": "/hg19/unmerged/detail/HSMv12.1_reqions_NO_JAK2_NODUP.bed",
		"regionfile": "/hg19/unmerged/detail/HSMv12.1_hotspots_NO_JAK2.bed",
		"planName":"DEMO-REST-API_TARS_plan1",
		"sample":"my_sample",
		"notes":"1T pool47 Lib2444 322_25xP73 lr2 ",
		"username":"demouser",
		"preAnalysis":"on",
		"isReverseRun":false,
		"isPlanGroup":false,
		"runMode":"single",
		"runType": "TARS",
		"chipType": "318",
		"sequencekitname": "IonPGM200Kit",
		"librarykitname": "Ion Xpress Plus Fragment Library Kit",
		"templatingKitName": "Ion OneTouch 200 Template Kit v2 DL",
		"samplePrepKitName": "Ion TargetSeq(tm) Custom Enrichment Kit (100kb-500kb)",
		"projects": ["myProject1","myProject2"]
	}

**Example 2:**

Post a barcoded AmpliSeq DNA Sequencing plan for Proton with PI chip, with one of the samples associated with two different barcodes, and to associate results with 1 project.

.. code-block:: javascript

	{
		"autoAnalyze":"true",
		"usePreBeadfind":"true",
		"usePostBeadfind":"true",
		"reverselibrarykey":"",
		"reverse3primeadapter":"",
		"libraryKey":"TCAG",
		"forward3primeadapter":"ATCACCGACTGCCCATAGAGAGGCTGAGAC",
		"flows":520,
		"library":"hg19",
		"bedfile": "",
		"regionfile": "",
		"planName":"DEMO-REST-API_AMPS_plan2",
		"sample":"my_sample",
		"notes":"1T pool47 Lib2444 322_25xP73 lr2 ",
		"username":"ionuser",
		"preAnalysis":true,
		"isReverseRun":false,
		"isPlanGroup":false,
		"runMode":"single",
		"runType": "AMPS",
		"chipType": "900",
		"sequencekitname": "IonPGM200Kit",
		"librarykitname": "Ion Xpress Plus Fragment Library Kit",
		"templatingKitName": "Ion OneTouch 200 Template Kit v2 DL",
		"samplePrepKitName": "",
		"controlSequencekitname": "Ion AmpliSeq Sample ID Panel",
		"projects": ["myProject1"],
		"barcodeId":"IonSet1",
		"barcodedSamples":"{'s1':{'barcodes':['IonSet1_01']}, 's2':{'barcodes':['IonSet1_02', 'IonSet1_03']}, 's3':{'barcodes':['IonSet1_04']}}"
	}

.. _About_using_POST_to_update_a_plan:

About Using POST to Update a Plan:
----------------------------------

If you are planning on updating a plan via the REST API, perform a GET operation first so that you'll have all of the internally created values necessary to perform an update with POST.

To update with POST, include "id":<plan PK> in your data packet. (e.g., "id":1234)

**------------------------------------------REMOVE CONTENT BEYOND THIS POINT--------------------------------------------------------**

**------------------------------------------REMOVE CONTENT BEYOND THIS POINT--------------------------------------------------------**

**------------------------------------------REMOVE CONTENT BEYOND THIS POINT--------------------------------------------------------**

.. _Sample_information:

Sample Information:
-------------------

In TSS 3.6, the database has been enhanced to lay down the groundwork for future releases such that samples are no longer a mere annotation to a sequencing run or to a barcode.  When a plan is created, a sample entry will be added to the database if one does not exist yet. Sample can be associated with many plans and sequencing runs and its uniqueness is based on its external id and name.  However, plans in TS 3.6 are still dealing with sample name only.  Difference between a name and its displayed name is that the displayed name allows spaces. 

Overall, for the time being, validation for sample creation happens upstream from the REST API (for GUI-based plan creation) and thus validation during direct REST API posting is not implemented for TSS 3.6.  Until validation is in place during direct REST API posting, REST API users need to do due diligence to ensure sample uniqueness and that the data posted are valid.

WARNING: If you want to start posting richer contents of your samples to TSS, you can do that via REST API posting. However, since plans in TS 3.6 are not using external id yet, it is not advised to post samples with external id yet.  For example, you have posted a richer contents of your sample with sample id "123", sample name "S1", sample displayed name "S1" and some description), then you post a plan that references sample with name "S1" (with no external id), the S1 sample referenced in the plan will be treated as a different sample since it does not have the same external id.

+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| Attribute Name      | Required/     | Data Type    | Default| Valid   | Example              | Comment/Expected Value      |
|                     | Optional/     |              | value  | values  |                      |                             |
|                     | Nullable      |              |        |         |                      |                             |
+=====================+===============+==============+========+=========+======================+=============================+
| status              | Opt           | varchar(512) | ""     | "",run, |                      |                             |
|                     |               |              |        | planned,|                      |                             |
|                     |               |              |        | loaded  |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| name                | Req           | varchar(127) |        |         | my_sample            | see RULE-1, RULE-3          |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| displayedName       | Req           | varchar(127) |        |         | my sample            | see RULE-2, RULE-3          |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| externalId          | Opt/Nullable  | varchar(127) |        |         | xyz 123_5.72         |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| description         | Opt/Nullable  | varchar(1024)|        |         |                      | see RULE-2                  |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+
| date                | Opt/Nullable  | Date         |        |         |                      |                             |
+---------------------+---------------+--------------+--------+---------+----------------------+-----------------------------+

*RULE-1:*

Valid characters: letters, numbers, dashes, underscores, dots.

*RULE-2:*

Valid characters: letters, numbers, spaces, dashes, underscores, dots.

*RULE-3:*

Invalid leading characters: dashes, underscores, dots.

.. _Example_for_creating_a_sample:

Example for creating a sample:
------------------------------

.. code-block:: javascript

	{
		"status":"planned",
		"name":"demo_sample",
		"displayedName":"demo sample",
		"externalId":"xyz 123_5.72",
		"description":"demo sample for customer 5.72"
	}
