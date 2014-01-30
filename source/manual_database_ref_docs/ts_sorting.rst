Sort Response Output
====================

Topics on this page:

* :ref:`Sorting_by_date_example`
* :ref:`Sorting_in_reverse_order`

.. _Sorting_by_date_example:

Sort by date
------------

To sort multiple elements, add a sort parameter to your request. Otherwise, elements are returned in the order they occur in the database.

Sorting is specified by using the keyword order_by, which works the same way as the SQL ordering statement. You must also specify the field you want to sort on. The sort parameter has the following syntax:

.. code-block:: none

	order_by=<field>

You can request sorting in ascending or descending alphanumeric order, as these example will demonstrate.

	(!) Elements with, for example, field values of 1, 2, 10 are returned in 1, 10, 2 order.

The first example requests elements to be sorted by the date field. This is the default form of the order_by parameter and returns elements in ascending order. (You should already be familiar with the startswith filter qualifier used in previous examples.)

General form of a sort request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&expName__startswith=R_2013&order_by=date

Python implementation of a sort request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&order_by=date'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

Two matching elements are returned, sorted in ascending order, by date:

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
			},
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
			}
		]
	}

.. _Sorting_in_reverse_order:

Sort in reverse order
---------------------

To reverse the order of the elements returned in the previous example, add a minus symbol before the name of the field you are sorting on. This returns elements in descending order, for the specified field.

General form of a descending-order request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	http://myhost/rundb/api/v1/experiment?format=json&expName__startswith=R_2013&order_by=-date

Python implementation of a descending-order request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	import json
	import requests
	
	base_url = 'http://myhost/rundb/api/v1'
	resp = requests.get('%s/experiment?format=json&order_by=-date'%base_url, auth=('myusername', 'mypassword'))
	resp_json = resp.json()

You can see that the elements are returned in inverse order of the previous example:

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
