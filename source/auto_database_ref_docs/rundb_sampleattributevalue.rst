Database Table rundb_sampleattributevalue
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_sampleattributevalue``


.. include:: ../manual_database_ref_docs/rundb_sampleattributevalue.rst

Schema
-------

+--------------------+--------------------------------+-----------------------------------------+
| Field              | Type                           | Description                             |
+====================+================================+=========================================+
| creationDate       | Date (with time)               | creationDate                            |
+--------------------+--------------------------------+-----------------------------------------+
| creator            | User (ForeignKey)              | the related auth.User row               |
+--------------------+--------------------------------+-----------------------------------------+
| id                 | Integer                        | ID                                      |
+--------------------+--------------------------------+-----------------------------------------+
| lastModifiedDate   | Date (with time)               | lastModifiedDate                        |
+--------------------+--------------------------------+-----------------------------------------+
| lastModifiedUser   | User (ForeignKey)              | the related auth.User row               |
+--------------------+--------------------------------+-----------------------------------------+
| sample             | Sample (ForeignKey)            | the related rundb.Sample row            |
+--------------------+--------------------------------+-----------------------------------------+
| sampleAttribute    | SampleAttribute (ForeignKey)   | the related rundb.SampleAttribute row   |
+--------------------+--------------------------------+-----------------------------------------+
| value              | String (up to 1024)            | value                                   |
+--------------------+--------------------------------+-----------------------------------------+

