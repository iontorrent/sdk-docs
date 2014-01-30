Select a Subset of Resources
============================

All resource elements
---------------------

If you specify only the resource in the URI, all of the resource elements are returned. For example:

.. code-block:: none

	http://myhost/rundb/api/v1/dnabarcode/?format=json

A single resource element
-------------------------

Similarly, you can select a specific resource element by providing the primary key value of the element, usually the id field:

.. code-block:: none

	http://myhost/rundb/api/v1/dnabarcode/34?format=json

Multiple resource elements
----------------------------

To request multiple elements, use the set keyword following the resource name in the URI, then separate each desired element using a semicolon:

.. code-block:: none

	http://myhost/rundb/api/v1/dnabarcode/set/34;35?format=json

This example returns only elements with id 34 and 35.
