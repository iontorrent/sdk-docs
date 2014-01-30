Run a Plugin
================

You can use the API to run plugins programmatically, including passing parameters to plugins.

Topics on this page:

* :ref:`Get_a_list_of_plugins`
* :ref:`Start_a_plugin_without_parameters`
* :ref:`Start_a_plugin_with_parameters`

	For more information about the plugin execution environment and plugins development, see the following documents on the Ion Community:
	
	* `Plugin SDK Documentation <http://ioncommunity.lifetechnologies.com/docs/DOC-7215>`_ 
	* `Introduction to Python Plugins <http://ioncommunity.lifetechnologies.com/docs/DOC-7214>`_ 

.. _Get_a_list_of_plugins:

Get a list of plugins
---------------------

Enter the plugin resource name in the URI to get a list of all plugins. Use the parameter ``active=True`` to restrict the list to the currently installed plugins.

.. code-block:: none

	http://myhost/rundb/api/v1/plugin/?format=json&active=True

The response includes plugin metadata and the data for each plugin in the system. Notice that, by default, the response only included 20 elements but the total_count meta field indicates there are 28 plugins. (Append ``limit=0`` to show all the results in a single response, or use ``offset=20`` to get the next 20 entries.)

.. code-block:: javascript

	{
		"meta": {
			"limit": 20,
			"next": "/rundb/api/v1/plugin/?offset=20&limit=20&format=json",
			"offset": 0,
			"previous": null,
			"total_count": 28
		},
		"objects": [
			{
				"autorun": true,
				"chipType": "",
				"date": "2011-05-06T19:09:45.438365",
				"id": "23",
				"libraryName": "",
				"name": "top100Ionogram",
				"path": "/results/plugins/top100Ionogram",
				"project": "",
				"resource_uri": "/rundb/api/v1/plugin/23/",
				"sample": "",
				"selected": false,
				"version": "0"
			},
			{
				"autorun": true,
				"chipType": "",
				"date": "2011-05-06T19:09:45.477418",
				"id": "24",
				"libraryName": "",
				"name": "AmpliconRep",
				"path": "/results/plugins/AmpliconRep",
				"project": "",
				"resource_uri": "/rundb/api/v1/plugin/24/",
				"sample": "",
				"selected": false,
				"version": "0"
			},
				.
				.
				.
			{
				"autorun": true,
				"chipType": "",
				"date": "2011-05-06T19:09:45.760567",
				"id": "42",
				"libraryName": "",
				"name": "igv",
				"path": "/results/plugins/igv",
				"project": "",
				"resource_uri": "/rundb/api/v1/plugin/42/",
				"sample": "",
				"selected": false,
				"version": "0"
			}
		]
	}

Specify the filtering criteria or the plugin id to retrieve the data for a single plugin.

.. _Start_a_plugin_without_parameters:

Start a plugin without parameters
---------------------------------

The following code snippet shows how to start a plugin that requires no parameters. (The requests and simplejson Python libraries are used, as in previous examples.)

Use a dictionary that has the plugin keyword and the plugin name as the value:

.. code-block:: python

	myPlugin = json.dumps( {"plugin": ["AmpliconRep"]} )

Send a POST request to run the plugin with the plugin name in the request body:

.. code-block:: python

	status = requests.post('http://myhost/rundb/api/v1/plugin/84/',
                       data=myPlugin,
                       headers={'content-type':'application/json'},
                       auth=('myusername', 'mypassword'))

.. _Start_a_plugin_with_parameters:

Start a plugin with parameters
------------------------------

To run a plugin requiring runtime parameters, simply add the parameters to the dictionary, as in the following code snippet, and include the plugin name and parameters in the request body:

.. code-block:: python

	myPlugin = json.dumps(
	{
		"plugin": ["AmpliconRep"],
		"pluginconfig" : { "user_variables" : "foo" }
	})

Again, send a POST request to run the plugin.

Here is a complete example using httplib2. (The shebang ``#!`` just allows for easy execution.)

.. code-block:: python

	#!/usr/bin/python
	import httplib2
	import json
	#the primary key for the report
	reportPrimaryKey = "1234"
	#the name of the plugin to run
	pluginName = "YOUR_PLUGIN"
	h = httplib2.Http()
	h.add_credentials('ionadmin', 'ionadmin')
	headers = {"Content-type": "application/json","Accept": "application/json"}
	url = 'http://ionwest' + '/rundb/api/v1/results/' + reportPrimaryKey + "/plugin/"
	pluginUpdate  = {"plugin": [pluginName]}
	resp, content = h.request(url, "POST", body=json.dumps(pluginUpdate),headers=headers )
	print resp
	print content
