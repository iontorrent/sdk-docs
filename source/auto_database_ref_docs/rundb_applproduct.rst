Database Table rundb_applproduct
============================================================================

Postgres database: ``iondb``


Postgres table: ``rundb_applproduct``


.. include:: ../manual_database_ref_docs/rundb_applproduct.rst

Schema
-------

+------------------------------------+----------------------------------+------------------------------------+
| Field                              | Type                             | Description                        |
+====================================+==================================+====================================+
| applType                           | RunType (ForeignKey)             | the related rundb.RunType row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultAvalancheSequencingKit      | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultAvalancheTemplateKit        | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultBarcodeKitName              | String (up to 128)               | defaultBarcodeKitName              |
+------------------------------------+----------------------------------+------------------------------------+
| defaultChipType                    | String (up to 128)               | defaultChipType                    |
+------------------------------------+----------------------------------+------------------------------------+
| defaultControlSeqKit               | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultFlowCount                   | Positive integer                 | defaultFlowCount                   |
+------------------------------------+----------------------------------+------------------------------------+
| defaultGenomeRefName               | String (up to 1024)              | defaultGenomeRefName               |
+------------------------------------+----------------------------------+------------------------------------+
| defaultHotSpotRegionBedFileName    | String (up to 1024)              | defaultHotSpotRegionBedFileName    |
+------------------------------------+----------------------------------+------------------------------------+
| defaultIonChefPrepKit              | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultLibraryKit                  | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultPairedEndAdapterKit         | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultPairedEndLibraryKit         | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultPairedEndSequencingKit      | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultSamplePrepKit               | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultSequencingKit               | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultTargetRegionBedFileName     | String (up to 1024)              | defaultTargetRegionBedFileName     |
+------------------------------------+----------------------------------+------------------------------------+
| defaultTemplateKit                 | KitInfo (ForeignKey)             | the related rundb.KitInfo row      |
+------------------------------------+----------------------------------+------------------------------------+
| defaultVariantFrequency            | String (up to 512)               | defaultVariantFrequency            |
+------------------------------------+----------------------------------+------------------------------------+
| description                        | String (up to 1024)              | description                        |
+------------------------------------+----------------------------------+------------------------------------+
| id                                 | Integer                          | ID                                 |
+------------------------------------+----------------------------------+------------------------------------+
| instrumentType                     | String (up to 64)                | instrumentType                     |
+------------------------------------+----------------------------------+------------------------------------+
| isActive                           | Boolean (Either True or False)   | isActive                           |
+------------------------------------+----------------------------------+------------------------------------+
| isDefault                          | Boolean (Either True or False)   | isDefault                          |
+------------------------------------+----------------------------------+------------------------------------+
| isDefaultBarcoded                  | Boolean (Either True or False)   | isDefaultBarcoded                  |
+------------------------------------+----------------------------------+------------------------------------+
| isDefaultPairedEnd                 | Boolean (Either True or False)   | isDefaultPairedEnd                 |
+------------------------------------+----------------------------------+------------------------------------+
| isHotspotRegionBEDFileSuppported   | Boolean (Either True or False)   | isHotspotRegionBEDFileSuppported   |
+------------------------------------+----------------------------------+------------------------------------+
| isPairedEndSupported               | Boolean (Either True or False)   | isPairedEndSupported               |
+------------------------------------+----------------------------------+------------------------------------+
| isVisible                          | Boolean (Either True or False)   | isVisible                          |
+------------------------------------+----------------------------------+------------------------------------+
| productCode                        | String (up to 64)                | productCode                        |
+------------------------------------+----------------------------------+------------------------------------+
| productName                        | String (up to 128)               | productName                        |
+------------------------------------+----------------------------------+------------------------------------+

