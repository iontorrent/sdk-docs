URI Structure
=============

The Uniform Resource Identifier (URI) is a address string used to locate a named resource or group of resources over a network. The REST communication model uses a URI to identify resources with each resource having a unique URI.

The URI structure is hierarchical so a group of resources can be identified by specifying the location at a higher level in the address hierarchy, without specifying a particular resource.

Simplified syntax
-----------------

The URI has a similar appearance to the Uniform Resource Locator (URL) you use in your browser. In fact, URL is a subset of the URI specification. REST URI components include:

* The protocol (HTTP)
* domain
* path
* resource ID

Examples
^^^^^^^^

+--------------------------------------------+-----------------------------------------------+
| REST URI                                   | Description                                   |
+============================================+===============================================+
| ``http://myhost/rundb/api/v1/rig/testPGM`` | Reference the specific rig resource named     | 
|                                            | ``testPGM`` located at domain ``myhost`` and  | 
|                                            | path ``rundb/api/v1/rig/``.                   |
+--------------------------------------------+-----------------------------------------------+
| ``http://myhost/rundb/api/v1/rig/``        | Reference all resources located at domain     |
|                                            | ``myhost`` and path ``rundb/api/v1/rig/``.    |
+--------------------------------------------+-----------------------------------------------+
| ``rundb/api/v1/rig/testPGM``               | Reference the specific rig resource named     |
|                                            | ``testPGM`` on ``localhost``.                 |
+--------------------------------------------+-----------------------------------------------+

The URI may include your login username and password, and port number, as part of the host name.

Parameters
----------

Parameters can be appended to the URI to qualify requests.

The following symbols are used to specify URI parameters:

+---------+----------------------------------------+
| Symbol  | Description                            |
+=========+========================================+
|    ?    | Introduces the parameter list.         | 
+---------+----------------------------------------+
|    &    | Parameter separator character.         |
+---------+----------------------------------------+

Parameters are usually specified as name-value pairs.

Example
^^^^^^^
 
	``http://myhost/rundb/api/v1/rig/?format=json&limit=0&order_by=name``

Syntax specification
^^^^^^^^^^^^^^^^^^^^
 ::
 
	 http://<username>:<password>@]<host>/rundb/api/<version>
		 [/<resource>[/<key>]?format=json
		 [[&<filter>{=<value> | __<qualifier>=<value>}]...]
		 [&order_by=[-]<filter>\]

		username ::= User login name.

		password ::= User login password.

		host ::= Host server name.

		version ::= API version ID; e.g., 'V1'.

		resource ::= "analysismetrics" | "experiment" |
			   "fileserver" | "globalconfig" | "libmetrics" |
			   "location" | "plugin" |"qualitymetrics" |
			   "referencegenome" | "results" |"rig" | "tfmetrics"

		key ::= Specific resource instance name or identifier;
			Example: '12' for experiment 'id' = 12.

		filter ::= (resource-dependent)

		value ::= (filter-dependent)

		qualifier ::= contains | icontains | iexact | month | day | 
			   in | range | endswith | iregex | regex | exact |
			   isnull | search | gt | istartswith | startswith |
			   gte | lt | week_day | iendswith | lte | year





