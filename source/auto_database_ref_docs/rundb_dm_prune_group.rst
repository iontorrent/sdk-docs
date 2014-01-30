Database Table rundb_dm_prune_group
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_dm_prune_group``


.. include:: ../manual_database_ref_docs/rundb_dm_prune_group.rst

Schema
-------

+------------+----------------------------------+---------------+
| Field      | Type                             | Description   |
+============+==================================+===============+
| editable   | Boolean (Either True or False)   | editable      |
+------------+----------------------------------+---------------+
| id         | Integer                          | ID            |
+------------+----------------------------------+---------------+
| name       | String (up to 128)               | name          |
+------------+----------------------------------+---------------+
| ruleNums   | Comma-separated integers         | ruleNums      |
+------------+----------------------------------+---------------+

