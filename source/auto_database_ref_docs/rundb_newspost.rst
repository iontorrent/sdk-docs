Database Table rundb_newspost
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_newspost``


.. include:: ../manual_database_ref_docs/rundb_newspost.rst

Schema
-------

+-----------+-----------------------+---------------+
| Field     | Type                  | Description   |
+===========+=======================+===============+
| guid      | String (up to 64)     | guid          |
+-----------+-----------------------+---------------+
| id        | Integer               | ID            |
+-----------+-----------------------+---------------+
| link      | String (up to 2000)   | link          |
+-----------+-----------------------+---------------+
| summary   | String (up to 300)    | summary       |
+-----------+-----------------------+---------------+
| title     | String (up to 140)    | title         |
+-----------+-----------------------+---------------+
| updated   | Date (with time)      | updated       |
+-----------+-----------------------+---------------+

