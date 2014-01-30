Database Table rundb_samplesetitem
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_samplesetitem``


.. include:: ../manual_database_ref_docs/rundb_samplesetitem.rst

Schema
-------

+---------------------+---------------------------+------------------------------------+
| Field               | Type                      | Description                        |
+=====================+===========================+====================================+
| creationDate        | Date (with time)          | creationDate                       |
+---------------------+---------------------------+------------------------------------+
| creator             | User (ForeignKey)         | the related auth.User row          |
+---------------------+---------------------------+------------------------------------+
| dnabarcode          | dnaBarcode (ForeignKey)   | the related rundb.dnaBarcode row   |
+---------------------+---------------------------+------------------------------------+
| gender              | String (up to 127)        | gender                             |
+---------------------+---------------------------+------------------------------------+
| id                  | Integer                   | ID                                 |
+---------------------+---------------------------+------------------------------------+
| lastModifiedDate    | Date (with time)          | lastModifiedDate                   |
+---------------------+---------------------------+------------------------------------+
| lastModifiedUser    | User (ForeignKey)         | the related auth.User row          |
+---------------------+---------------------------+------------------------------------+
| relationshipGroup   | Integer                   | relationshipGroup                  |
+---------------------+---------------------------+------------------------------------+
| relationshipRole    | String (up to 127)        | relationshipRole                   |
+---------------------+---------------------------+------------------------------------+
| sample              | Sample (ForeignKey)       | the related rundb.Sample row       |
+---------------------+---------------------------+------------------------------------+
| sampleSet           | SampleSet (ForeignKey)    | the related rundb.SampleSet row    |
+---------------------+---------------------------+------------------------------------+

