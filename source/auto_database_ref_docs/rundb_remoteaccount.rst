Database Table rundb_remoteaccount
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_remoteaccount``


.. include:: ../manual_database_ref_docs/rundb_remoteaccount.rst

Schema
-------

+--------------------+-----------------------+-------------------+
| Field              | Type                  | Description       |
+====================+=======================+===================+
| access\_token      | String (up to 2048)   | access token      |
+--------------------+-----------------------+-------------------+
| account\_label     | String (up to 64)     | account label     |
+--------------------+-----------------------+-------------------+
| id                 | Integer               | ID                |
+--------------------+-----------------------+-------------------+
| refresh\_token     | String (up to 2048)   | refresh token     |
+--------------------+-----------------------+-------------------+
| remote\_resource   | String (up to 2048)   | remote resource   |
+--------------------+-----------------------+-------------------+
| token\_expires     | Date (with time)      | token expires     |
+--------------------+-----------------------+-------------------+
| user\_name         | String (up to 255)    | user name         |
+--------------------+-----------------------+-------------------+

