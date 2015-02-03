Database Table rundb_kitpart
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_kitpart``


.. include:: ../manual_database_ref_docs/rundb_kitpart.rst

Schema
-------

+-----------+------------------------+---------------------------------+
| Field     | Type                   | Description                     |
+===========+========================+=================================+
| barcode   | String (up to 64)      | barcode                         |
+-----------+------------------------+---------------------------------+
| id        | Integer                | ID                              |
+-----------+------------------------+---------------------------------+
| kit       | KitInfo (ForeignKey)   | the related rundb.KitInfo row   |
+-----------+------------------------+---------------------------------+

