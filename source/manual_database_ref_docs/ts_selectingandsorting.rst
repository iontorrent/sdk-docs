Filter and Sort
===============

You can select a particular element or a group of resource elements by specifying filtering criteria. A filter may specify an exact match or a partial match using a filter qualifier.

Query results can be sorted in either ascending or descending order, using the order_by parameter and specifying the field on which to sort.

.. toctree::
    :maxdepth: 2

    ./ts_selectingresourcesubset.rst
    ./ts_basicfiltering.rst
    ./ts_qualifyingfilters.rst
    ./ts_sorting.rst

The selection semantics are the same as those of the SQL SELECT statement, where a selection filter equates to the SELECT column name parameter. The API provides that any resource field, with the exception of the resource_uri, can be used as a filter. This gives considerable flexibility in selecting only the desired resource elements. Filters are specified as URI parameters, a filter=value pair, and any resource elements matching the filter criteria are returned in the response. Filter values can be further qualified using certain keywords that act as wildcards or logical operators.

Any of the fields in the resource schema ordering list can be used to sort responses. Ordering is alphanumeric, so elements with, for example, name field values of 1, 2, 10 are returned in the order 1, 10, 2.

You can use filters to retrieve metadata and analysis metrics for runs, for instance, with a given project name or genome name, or within a specific date range.