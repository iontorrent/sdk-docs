Database Table rundb_plannedexperimentqc
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_plannedexperimentqc``


.. include:: ../manual_database_ref_docs/rundb_plannedexperimentqc.rst

Schema
-------

+---------------------+----------------------------------+-------------------------------------------+
| Field               | Type                             | Description                               |
+=====================+==================================+===========================================+
| id                  | Integer                          | ID                                        |
+---------------------+----------------------------------+-------------------------------------------+
| plannedExperiment   | PlannedExperiment (ForeignKey)   | the related rundb.PlannedExperiment row   |
+---------------------+----------------------------------+-------------------------------------------+
| qcType              | QCType (ForeignKey)              | the related rundb.QCType row              |
+---------------------+----------------------------------+-------------------------------------------+
| threshold           | Positive integer                 | threshold                                 |
+---------------------+----------------------------------+-------------------------------------------+

