.. _api_reference_getchefscriptinfo:

Get Chef Script Info  Resource
==============================

| Resource URL ``http://mytorrentserver/rundb/api/v1/getchefscriptinfo/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/getchefscriptinfo/schema/``
| 

.. include:: ../references_manual_extras/getchefscriptinfo.rst

Resource Fields
---------------

==================== ========================================================================================== ======= ======== ======== ===== ====== ==== 
field                help text                                                                                  default nullable readonly blank unique type 
==================== ========================================================================================== ======= ======== ======== ===== ====== ==== 
**availableversion** A dictionary of data. Ex: {'Compatible_Chef_release': ['IC.5.4.0'], 'IS_scripts': '00515'} n/a     true     true     true  false  dict 
==================== ========================================================================================== ======= ======== ======== ===== ====== ==== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "object": {
	        "availableversion": {
	            "IS_scripts": "000609", 
	            "Compatible_Chef_release": [
	                "IC.5.6.0"
	            ]
	        }
	    }
	}

Allowed HTTP methods
--------------------


