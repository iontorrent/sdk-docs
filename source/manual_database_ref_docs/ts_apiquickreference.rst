.. _quickref:

Ion Torrent™ Server API Quick Reference
=======================================


.. _REST_request_format:

REST request format
-------------------

Syntax
^^^^^^

.. code-block:: none

	http://[<username>:<password>@]
		<host>/rundb/api/<version>/<resource>?format=json
		[[&<filter>{=<value> | __<qualifier>=<value>}]...][&order_by=[-]<filter>]

Examples
^^^^^^^^

.. code-block:: none

	http://ionuser:ionuser@ionwest.itw/rundb/api/v1/experiment
		?format=json&expName__startswith=R_2010_11&order_by=date

.. code-block:: none

	curl --user ionuser:ionuser --header "Content-Type: application/json"
		--location 'http://ionwest.itw/rundb/api/v1/results'

.. _REST_methods:

REST methods
------------

+-------+---------+------------------+-----------------+
| Method| Function| Element URI      | List URI        |
+=======+=========+==================+=================+
| POST  | Create  | Create new entry | Create new entry|
|       |         | in element       | in list         |
+-------+---------+------------------+-----------------+
| GET   | Read    | Get URI content  | List URI members|
+-------+---------+------------------+-----------------+
| PUT   | Update  | Replace URI      | Replace URI     |
|       |         | content          | members         |
+-------+---------+------------------+-----------------+
| DELETE| Delete  | Delete URI       | Delete list     |
|       |         | element          | members         |
+-------+---------+------------------+-----------------+

.. _HTTP_stat_codes:

HTTP status codes
-----------------

+---------+-----+------------------------+
| Method  | Code| Meaning                |
+=========+=====+========================+
| GET     | 200 | Resource exists        |
|         +-----+------------------------+
|         | 301 | Permanently moved      |
|         +-----+------------------------+
|         | 401 | Authorization err or   |
|         +-----+------------------------+
|         | 404 | Not found              |
|         +-----+------------------------+
|         | 410 | No longer exists       |
+---------+-----+------------------------+
| PUT/POST| 200 | Resource replaced      |
|         +-----+------------------------+
|         | 201 | Resource created       |
|         +-----+------------------------+
|         | 204 | No response            |
|         +-----+------------------------+
|         | 301 | Redirect               |
|         +-----+------------------------+
|         | 400 | Invalid data           |
|         +-----+------------------------+
|         | 401 | Authorization error    |
|         +-----+------------------------+
|         | 409 | Resource state conflict|
|         +-----+------------------------+
|         | 500 | Internal error         |
|         +-----+------------------------+
|         | 501 | Method not implemented |
+---------+-----+------------------------+
| DELETE  | 200 | Resource deleted       |
|         +-----+------------------------+
|         | 400 | Resource not deleted   |
|         +-----+------------------------+
|         | 401 | Authorization error    |
+---------+-----+------------------------+

.. _Toplevel_requests:

Top-level requests
------------------

+------------------+--------------------+
| URI              | Scope              |
+==================+====================+
| /rundb/api/v1/   | Resource list      |
+------------------+--------------------+
| /rundb/api/v1/   | Resource element   |
| <resource>/      | list (default      |
|                  | limit: 20)         |
+------------------+--------------------+
| /rundb/api/v1/   | Resource element   |
| <resource>?limit | list; all elements |
| =0               |                    |
+------------------+--------------------+
| /rundb/api/v1/   | Resrouce element   |
| <resource>/<key>/|                    |
+------------------+--------------------+
| /rundb/api/v1/   | Multiple resource  |
| <resource>/set/  | elements           |
| <key>;<key>;.../ |                    |
+------------------+--------------------+
| /rundb/api/v1/   | Resource schema    |
| <resource>/schema|                    |
+------------------+--------------------+

.. _Resources:

Resources
---------

* *++ indicates PUT/POST/DELETE permitted*
* *Bold type indicates KEY field*

analysismetrics
^^^^^^^^^^^^^^^

amb, bead, dud, empty, excluded, **id**, ignored, keypass_all_beads, lib, libFinal, libKp, libLive, libMix, lib_pass_basecaller, lib_pass_cafie, live, pinned, report, sysCF, sysDR, sysIE, tf, tfFinal, tfKp, tfLive, tfMix, washout, washout_ambiguous, washout_dud, washout_library, washout_live, washout_test_fragment

dnabarcode ++
^^^^^^^^^^^^^

adapter, annotation, floworder, **id**, index, length, name, sequence, type

experiment ++
^^^^^^^^^^^^^

autoAnalyze, backup, barcodeId, baselineRun, chipBarcode, chipType, cycles, date, expCompInfo, expDir, expName, flows, flowsInOrder, ftpStatus, **id**, library, libraryKey, log, metaData, notes, pgmName, project, reagentBarcode, results, sample, seqKitBarcode, star, storageHost, storage_options, unique, usePreBeadfind

fileserver
^^^^^^^^^^

comments, filesPrefix, **id**, location, name

globalconfig
^^^^^^^^^^^^

default_command_line, default_flow_order, default_library_key, default_plugin_script, default_storage_options, default_test_fragment_key, fasta_path, **id**, name, plugin_folder, plugin_output_folder, records_to_display, reference_path, selected, sfftrim, sfftrim_args, site_name, web_root

libmetrics
^^^^^^^^^^

See `Filters (continued) <ts_apiquickreference-2.html>`_

location
^^^^^^^^

comments, **id**, name

plugin
^^^^^^

autorun, chipType, date, **id**, libraryName, name, path, project, sample, selected, version

qualitymetrics
^^^^^^^^^^^^^^

**id**, q0_100bp_reads, q0_15bp_reads, q0_50bp_reads, q0_bases, q0_max_read_length, q0_mean_read_length, q0_reads, q17_100bp_reads, q17_150bp_reads, q17_50bp_reads, q17_bases, q17_max_read_length, q17_mean_read_length, q17_reads, q20_100bp_reads, q20_150bp_reads, q20_50bp_reads, q20_bases, q20_max_read_length, q20_mean_read_length, q20_reads, report

referencegenome
^^^^^^^^^^^^^^^

bled, **id**, index_version, name, notes, reference_path, short_name, source, species, status, verbose_error, version

results ++
^^^^^^^^^^

analysisVersion, analysismetrics, experiment, fastqLink, framesProcessed, **id**, libmetrics, log, metaData, pluginState, pluginStore, processedCycles, qualitymetrics, reportLink, reportstorage, resultsName, sffLink, status, tfFastq, tfSffLink, tfmetrics, timeStamp, timeToComplete

rig ++
^^^^^^

alarms, comments, ftppassword, ftprootdir, ftpserver, ftpusername, last_clean_date, last_experiment, last_init_date, location, **name**, <nameValue>/status, state, updateflag, updatehome, version

runtype ++
^^^^^^^^^^

barcode, description, **id**, runType

tfmetrics
^^^^^^^^^

See `Filters (continued) <ts_apiquickreference-2.html>`_

.. _Extended_resources:

Extended resources
------------------

Plugins
^^^^^^^

POST:
	*Request Header:*

		.. code-block:: none

			Content-Type: application/json

	*Request Body:*

		.. code-block:: javascript

			{"plugin":["<pluginName>"]}
		
			or
		
			{"plugin":["<pluginName>"], pluginconfig : { json params } }

.. code-block:: none

	http://myhost/rundb/api/v1/results/<key>/plugin?format=json

Files
^^^^^

Example:

1. From *results* resource response:

	.. code-block:: javascript

		{"log": "/output/Home/Auto_B15-45_4_013/log.html"}

2. Get file:

	.. code-block:: none

		http://myhost/output/Home/Auto_B15-45_4_013/log.html

.. _Filter_qualifiers:

Filter qualifiers
-----------------

Usage: ``<field>__<qualifier>=<value>``

Example: ``library__contains=coli``

+--------------+---------------+-----------------+----------------+
| **contains** | **icontains** | **istartswith** | **search**     |
+--------------+---------------+-----------------+----------------+
| **day**      | **iendswith** | **lt**          | **startswith** |
+--------------+---------------+-----------------+----------------+
| **endswith** | **iexact**    | **lte**         | **week_day**   |
+--------------+---------------+-----------------+----------------+
| **exact**    | **in**        | **month**       | **year**       |
+--------------+---------------+-----------------+----------------+
| **gt**       | **iregex**    | **range**       |                |
+--------------+---------------+-----------------+----------------+
| **gte**      | **isnull**    | **regex**       |                |
+--------------+---------------+-----------------+----------------+

.. _Sort_parameter:

Sort parameter
--------------

Usage: ``order_by=[-]<filter>``

Examples:

|		(ascending) ``order_by=date``
|		(descending) ``order_by=-date``

.. _Data_format_parameter:

Data format parameter
---------------------

+-------+-------------+---------------+
| Format| Parameter   | Note          |
+=======+=============+===============+
| JSON  | ?format=json|               |
+-------+-------------+---------------+
| XML   | ?format=xml | Not supported |
+-------+-------------+---------------+

.. _Supported_run_types:

Supported run types (>= 3.x)
----------------------------

+-------------------+--------------------------+
| Run Type          | Description              |
+===================+==========================+
| RunType.FULLCHIP  | Whole chip PGM run.      |
+-------------------+--------------------------+
| RunType.THUMB     | Thumbnail run.           |
+-------------------+--------------------------+
| RunType.COMPOSITE | Proton run.              |
+-------------------+--------------------------+

.. _Supported_run_levels:

Supported run levels (>= 3.x)
-----------------------------


+-------------------+--------------------------+
| Run Level         | Description              |
+===================+==========================+
| RunLevel.PRE      | Runs after all analysis  |
|                   | jobs have been submitted,|
|                   | but before any finish.   |
+-------------------+--------------------------+
| RunLevel.BLOCK    | Runs when an individual  |
|                   | block finishes analysis. |
|                   | Occurs once for each     |
|                   | block.                   |
+-------------------+--------------------------+
| RunLevel.POST     | Runs after all blocks are|
|                   | done processing.         |
+-------------------+--------------------------+
| RunLevel.LAST     | Runs after everything,   |
|                   | including other plugins. |
|                   | Multiple plugins w/ LAST |
|                   | will run at the same     |
|                   | time.                    |
+-------------------+--------------------------+
| RunLevel.DEFAULT  | Default run level,       |
|                   | generally PGM runs.      |
+-------------------+--------------------------+
