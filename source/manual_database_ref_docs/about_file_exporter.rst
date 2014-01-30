Using the File Exporter Plugin
==============================

This page is designed to familiarize you with the File Exporter plugin, which can be used to download a report's bam, bai, sff, fastq, and vcf files with filenames defined by various report attributes.

Topics on this page:

* :ref:`Plugin_configuration`
* :ref:`Filename_configuration`
* :ref:`Add_rem_submit`

.. _Plugin_configuration:

Plugin Output Configuration
---------------------------

The plugin has a number of configuration options, both for automatic and one-time runs. The configuration screens are identical in both cases. Changing settings for automatic runs works the same as with other plugins, just access the configuration page from your Torrent Server's 'plugin' table.

Files with the .bam and .bai extension are automatically included in the plugin's output. There are three other filetypes that can be included:

* ``SFF``
* ``FASTQ``
* ``VCF`` (Variants)

The SFF and FASTQ files will be generated within the File Exporter plugin, and may increase the time the plugin takes to run on larger reports. Checking the 'Include Variants' box will put a link in the output page to a list of available variantCaller plugin runs, and the relevant vcf files for each one. This way, the output will be updated as variantCaller plugins are completed.

The final checkbox is an option to zip the results. Leaving this option unchecked will simply produce a list of available files with links to each individual one. Checking the box will generate a zip file of the appropriate files, excluding variants, and make it available for download. This option may increase the plugin's run time on large reports. The reason variants are not included is that they are often unavailable at runtime, and more may be added at a later date.

.. _Filename_configuration:

Filename Configuration
----------------------

Once you have decided what type of files you want to download, you must decide on the filename format. Simply choose a delimiter, which is a single character that will appear between your chosen options, and any number of report attributes. The options and how they will appear are as follows:

* ``Run Name`` - The name of the run associated with the current report.
* ``Report Name`` - The name of the current report.
* ``Report Date`` - The date of the current report.
* ``Chip Type`` - The type of chip used for the run associated with the current report. Ex: 314
* ``Sequencer Name`` - The name of the sequencer used for the current report's run.
* ``SampleID`` - The sampleID of the file's associated barcode, if applicable. Specified in the run plan.
* ``Barcode info.`` - The file's associated barcode, if applicable. Ex: IonXpress001

Note that if 'Barcode info.' is excluded in a report with barcodes, it will be prepended to the beginning of the filename with the chosen delimiter. Also, while the configuration page starts with only one naming option, you may add any number as described below.

.. _Add_rem_submit:

Add/Remove fields, and Submit
-----------------------------

At the bottom of the configuration page are three buttons. They are labeled:

* ``Add another field...``
* ``Submit``
* ``Remove last field...``

The ``Add another field`` button adds another filename selection field to the page, while the ``Remove last field`` button removes the field on the end of the current list. Note that leaving any field with 'Select option' selected will simply make that field have no effect on the filename.

The ``Submit`` button starts the plugin if it is being run manually, or saves the autorun configuration if it is being set up from the Torrent Server's plugins table. Further, autorun configurations are automatically used as default values when the page is brought up for manual runs.
