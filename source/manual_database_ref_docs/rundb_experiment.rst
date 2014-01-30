Experiment description data model.

Lifecycle
---------

Each sequencing run has a corresponding ``rundb_experiment`` table record. These database items are set by the Crawler process, which monitors directories containing PGM or Proton experiment data and creates a record for each new experiment it finds.

Referenced by
-------------

* `rundb_backup <./rundb_backup.html>`_
* `rundb_results <./rundb_results.html>`_

Related tables
----------------

The following tables hold data related to experiments:

* `sample <./rundb_sample.html>`_
* `plannedexperiment <./rundb_plannedexperiment.html>`_
* `plannedexperimentqc <./rundb_plannedexperimentqc.html>`_
* `experimentanalysissettings <./rundb_experimentanalysissettings.html>`_

.. * `experiment <./rundb_experiment.html>`_
.. * `project <./rundb_project.html>`_
