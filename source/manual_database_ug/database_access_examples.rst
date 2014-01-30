Database Access Examples
========================

These examples give a brief demonstration of how to work with the Ion Torrent database. As a prerequisite, you should be familiar with SQL, the ``psql`` command, and a PostgreSQL API, and be able to easily see how these examples can be expanded to create more useful applications.

Connect to the database using the following command, for example::

	ionadmin@myserver:~$ psql -U ion -d iondb
	psql (8.4.7)
	Type "help" for help.
	
	iondb=>
	
End your psql session by entering the quit command::

	iondb=> \q

Examples:

* :ref:`listdbtblels`
* :ref:`getdbtblel`
* :ref:`getdballtblels`
* :ref:`getresults`
* :ref:`querywithfile`

.. _listdbtblels:

List database table elements
----------------------------

To get a list and brief description of table contents, use the ``\d <tableName>`` command::

	iondb-> \d rundb_template
	
			Table "public.rundb_template"
	Column     |         Type          |        Modifiers
	------------+-----------------------+-------------------------
	id         | integer               | not null default nextval
	name       | character varying(64) | not null
	sequence   | text                  | not null
	key        | character varying(64) | not null
	comments   | text                  | not null
	isofficial | boolean               | not null
	
	Indexes:
		"rundb_template_pkey" PRIMARY KEY, btree (id)

	(END)

This example lists information about the ``rundb_results`` table elements, including name, datatype, attributes and relationship to other tables.

.. _getdbtblel:

Get the value of a table element
--------------------------------

Use the SQL ``select`` command to get the data associated with one or more table elements::

	iondb=> select "experiment_id" from rundb_results;
	experiment_id
	---------------
				4
				3
	(2 rows)

The example lists the IDs of all experiments stored in the rundb_results table. Here, results data are stored for two experiments. You can further qualify which experiments are listed using the SQL ``where`` operator, as shown in the :ref:`getresults` example.

.. _getdballtblels:

Get the value of all elements in a table
----------------------------------------

Use the wildcard (*) character to match all elements in a table::

	iondb=> select * from rundb_template;
	id | name |       sequence     | key  | comments | isofficial
	----+------+--------------------+------+----------+-----------
	 1 | TF_A | TGTTTCCGTGAGACTAGG | ATCG |          | t
	 2 | TF_B | TGAAGCCGTGAGACTGG  | ATCG |          | t
	 3 | TF_C | TACGAACGTGAGACTGG  | ATCG |          | t
	 4 | TF_D | TTGCGGAAGAGACTAGG  | ATCG |          | t
	(4 rows)

The example displays the four templates stored in the database, and their attributes.

.. _getresults:

Get run and results data
------------------------

There are two interesting tables representing experiments (PGM™ or Proton™ sequencer runs) and results (runs analyses):

* A run has a single record on the `rundb_experiment <../auto_database_ref_docs/rundb_experiment.html>`_ table.
* Each time the analysis pipeline is executed, a record is created in the  `rundb_results <../auto_database_ref_docs/rundb_results.html>`_ table.

In the `rundb_results <../auto_database_ref_docs/rundb_results.html>`_ table, the experiment_id field provides an association between analysis results and a PGM experiment record in the `rundb_experiment <../auto_database_ref_docs/rundb_experiment.html>`_ table. There may be zero, one or multiple results for each experiment. If an experiment has never been analyzed, it will have zero `rundb_results <../auto_database_ref_docs/rundb_results.html>`_ records associated with it.

In the `rundb_results <../auto_database_ref_docs/rundb_results.html>`_ table, the analysis pipeline updates the status field, indicating a Started, Terminated, ERROR, or Complete condition. Completed means that the analysis pipeline has completed normally and analysis results are available.

A ``psql`` program SQL query to return only completed analysis results records and associated experiment records has the following form::

	iondb=> select "experiment_id", "resultsName", "reportLink"
	iondb=> from rundb_results where "status" = 'Completed';

The ``psql`` program handles case sensitivity by wrapping text in quotes. If your queries fail unexpectedly, try using quotation marks around field names and tables.
At the core of a relational database is the ability to maintain data dependencies. For tables that have links to related data, you can use the ID link to reference the associated data.

Building on the previous simple example, we know there are two experiments in the `rundb_results <../auto_database_ref_docs/rundb_results.html>`_ table::

	iondb=> select "experiment_id" from rundb_results;
	experiment_id
	---------------
             4
             3
	(2 rows)

Suppose we want to know the experiment name and sample name associated with the results for experiment_id 3. Again, we use the SQL ``select`` command, specifying the table elements of interest, but qualifying the query with the experiment ID so only those data associated with that experiment are returned::

	iondb=> select "expName", "sample"
	iondb=> from rundb_experiment where "id"= '3';
			expName            |      sample
	------------------------------+-------------------
	R_2013_06_32_00_user_B6--237 | ms505_xm_indirect
	(1 row)

The query returns the expName and sample fields for only the record that matched the specified experiment ID.
SQL commands can be entered on one or more lines and are terminated with a semicolon.

.. _querywithfile:

Query the database using a file
-------------------------------

Database queries can be specified in a file and executed by passing the filename to the ``psql`` program::

	psql -d iondb -U ion -f test.sql

When accessing the database remotely, you must also specify the host::

	psql -h myhost -d iondb -U ion -f test.sql

A ``test.sql`` file that contains the following SQL commands::

	select * from rundb_rig;
	select * from rundb_location where id = '1';

produces the following results::

	ionadmin@myhost:~/example$ psql -d iondb -U ion -f test.sql
	name     | location_id | comments
	---------+-------------+----------
	PGM_test |           1 |
	B6       |           1 |
	(2 rows)
	
	id  | name | comments
	----+------+----------
	1   | Home |
	(1 row)
	
The command sequence lists the rigs (PGM™ and Proton™ sequencers) stored in the database and uses the ``location_id`` element to display information about one of the rigs.
