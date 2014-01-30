Qualifying Filters
==================

Topics on this page:

* :ref:`Example_selecting_all_experiments_with_common_field`
* :ref:`More_restrictive_example`
* :ref:`Example_selecting_experiments_with_given_date`

.. _Example_selecting_all_experiments_with_common_field:

Select all experiments with a common ``expName`` field
------------------------------------------------------

Filter values can be qualified so the value does not need to be an exact match to select an element.

	(!) The full set of filter qualifiers is listed in the :ref:`apiug-workdjangofilter` section of the :ref:`api-ug`.

Use the following syntax to specify a filter qualifier, where two underscore characters (__) separate the filter name from the filter qualifier name:

.. code-block:: none

	<filterName>__<filterQualifierName>=<value>

For some qualifiers, the behavior is similar to using a wildcard. The names of most qualifiers is self-explanatory, describing how it matches on a value.

In the following example, the ``startswith`` qualifier is used so any element whose field value "starts with" the specified value is returned, for the specified field.

General form of a URI request with a filter qualifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&expName__startswith=R_2013

Python implementation of a filter qualifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&expName__startswith=R_2013'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

The example returns two elements whose experiment name, expName, starts with R_2013.

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 2
		},
		"objects": [
			{
				"autoAnalyze": true,
				"barcodeId": "",
				"baselineRun": false,
				"chipBarcode": "AA0000000",
				"chipType": "\"314R\"",
				"cycles": 27,
				"date": "2013-03-07T17:48:53",
				"expCompInfo": "",
				"expDir": "/results/PGM_test/sample",
				"expName": "R_2013_11_08_22_30_04_user_B15-45",
					.
					.
					.
				"unique": "/results/PGM_test/sample",
				"usePreBeadfind": true
			},
			{
				"autoAnalyze": true,
				"barcodeId": "",
				"baselineRun": false,
				"chipBarcode": "AA0011641",
				"chipType": "\"314R\"",
				"cycles": 55,
				"date": "2013-11-05T18:32:00",
				"expCompInfo": "",
				"expDir": "/results/B6/R_2013_11_05_18_32_00_user_B6--237",
				"expName": "R_2013_11_05_18_32_00_user_B6--237",
					.
					.
					.
				"unique": "/results/B6/R_2013_11_05_18_32_00_user_B6--237",
				"usePreBeadfind": true
			}
		]
	}

.. _More_restrictive_example:

A more restrictive example
--------------------------

This example is the same as the previous example, except that the stricter criteria are applied by specifying that the experiment name must start with R_2013_11_05. From the results of the previous example, you can see that only one element is expected to meet this qualification.

General form of a more restrictive filter qualifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&expName__startswith=R_2013_11_05

Python implementation of a stricter filter qualifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&expName__startswith=R_2013_11_05'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

The response shows that only one element matches the ``expName`` filter:

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 1
		},
		"objects": [
			{
				"autoAnalyze": true,
				"barcodeId": "",
				"baselineRun": false,
				"chipBarcode": "AA0011641",
				"chipType": "\"314R\"",
				"cycles": 55,
				"date": "2013-11-05T18:32:00",
				"expCompInfo": "",
				"expDir": "/results/B6/R_2013_11_05_18_32_00_user_B6--237",
				"expName": "R_2013_11_05_18_32_00_user_B6--237",
					.
					.
					.
				"unique": "/results/B6/R_2013_11_05_18_32_00_user_B6--237",
				"usePreBeadfind": true
			}
		]
	}

.. _Example_selecting_experiments_with_given_date:

Select experiments with a given date field
------------------------------------------

The filter qualifier shown in this example works, as most qualifiers do, similar to the previous examples. Here, instead of searching for an element that "starts with" a particular value, you are searching for elements that "contain" a particular value. This example looks for elements whose date field contains the string value 2013-03.

General form of a URI with a filter qualifier on the date field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&date__icontains=2013-03

Python implementation of applying a filter qualifier on the date field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&date__icontains=2013-03'%base_url, 
		auth=('myusername', 'mypassword'))

One experiment is returned whose date field contains the string ``2013-03``. Notice that the ``startswith`` filter qualifier could also have been used. Considerable flexibility is available to you in choosing a qualifier and the best choice depends on the application and the data set.

.. code-block:: javascript

		{
		"meta": {
			"limit": 20,
			"next": null,
			"offset": 0,
			"previous": null,
			"total_count": 1
		},
		"objects": [
			{
				"autoAnalyze": true,
				"barcodeId": "",
				"baselineRun": false,
				"chipBarcode": "AA0000000",
				"chipType": "\"314R\"",
				"cycles": 27,
				"date": "2011-03-07T17:48:53",
				"expCompInfo": "",
				"expDir": "/results/PGM_test/sample",
				"expName": "R_2010_11_08_22_30_04_user_B15-45",
					.
					.
					.
				"unique": "/results/PGM_test/sample",
				"usePreBeadfind": true
			}]
		}
			

`Sort Response Output <ts_sorting.html>`_ demonstrates how to sort the returned experiment data by date.
