Database Table rundb_dm_reports
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_dm_reports``


.. include:: ../manual_database_ref_docs/rundb_dm_reports.rst

Schema
-------

+--------------+----------------------------------+---------------+
| Field        | Type                             | Description   |
+==============+==================================+===============+
| autoAge      | Integer                          | autoAge       |
+--------------+----------------------------------+---------------+
| autoPrune    | Boolean (Either True or False)   | autoPrune     |
+--------------+----------------------------------+---------------+
| autoType     | String (up to 32)                | autoType      |
+--------------+----------------------------------+---------------+
| id           | Integer                          | ID            |
+--------------+----------------------------------+---------------+
| location     | String (up to 512)               | location      |
+--------------+----------------------------------+---------------+
| pruneLevel   | String (up to 128)               | pruneLevel    |
+--------------+----------------------------------+---------------+

