Fields
======

Fields, as used in this documentation, are the resource schema columns.

A field is a name-value pair, where each field has a name identifier and may or may not have an associated value assigned. For example::

	"chipBarcode": "AA0000000",
	"chipType": "\"314R\"",
	"date": "2013-05-07T17:48:53",
	
Field names are useful in the API for selecting resource elements and sorting results.

Select resources using field names
----------------------------------

You can identify one or more resources by specifying the field name and the value to match on::

	http://myhost/rundb/api/v1/location?format=json&name=myLab

In this example, all location resource elements whose name field is ``myLab`` are returned by the server.

See the `Basic Filtering <../manual_database_ref_docs/ts_basicfiltering.html>`_ and `Qualifying Filters <../manual_database_ref_docs/ts_qualifyingfilters.html>`_ sections of the :ref:`api-cook` for a more detailed description of selecting resources using field names.

Sort resources by field names
-----------------------------

You sort resources returned by the server using the order_by key word and assigning it a field name. All resource elements returned are sorted by the value of the specified field. The following example sorts experiment elements by date::

	http://myhost/rundb/api/v1/experiment?format=json&order_by=date

See the `Sort Response Output <../manual_database_ref_docs/ts_sorting.html>`_ section of the :ref:`api-cook` for more detailed information about using field names to sort results.