REST
====

Representational State Transfer (REST) is an architectural model for implementing loosly-coupled, distributed applications, making REST similar to the RPC communication models. While not a standard, REST embraces the communication methods defined by the HTTP standard, adding the notion of resources as communication endpoints.

The resources REST operates on are addressable using a Uniform Resource Identifier (URI). Resources are located on the server. A core notion of the REST model is that resources are stateless. Communication by the client application with the server are in the form of requests of resource and any needed state information is carried in the request and not maintained on the server.

On Torrent Server, a resource is most often a database item located in the backend PostgreSQL database. (Files and plugins are also defined as resources in the API.) The following figure shows the components involved in making a REST request.

	.. image:: ../images/apiug_restmodel.png
	
The client application sends an HTTP GET request to retrieve an item from the database; in this example, the URI identifies a location resource whose ID is 2, also specifying that the data format is JSON::

	http://myhost/rundb/api/v1/location/2?format=json

The server decodes the request, finding the location resource and returning the data for location 2 to the client application in a response message. The response has a header and payload. The header includes the request status code, indicating if the request was successful or not, and the payload contains the requested resource data.

HTTP provides the underlying communication mechanism in the REST model.

HTTP methods
------------

The following HTTP communication methods are considered sufficient for a RESTful application to perform all necessary operations on resources. These are commonly abbreviated using the CRUD acronym: C - create, R - read, U - update and D - Delete.

GET
^^^

Use the GET method to retrieve resource information, or information about resources.

PUT
^^^

Use the PUT method to update resource data.

POST
^^^^
Use the POST method to create a resource.	

DELETE
^^^^^^
Use the DELETE resource to delete a resource.

Universal Resource Indicator (URI)
----------------------------------

The Uniform Resource Identifier (URI) is a address string used to locate a named resource or group of resources over a network. The REST communication model uses a URI to identify resources with each resource having a unique URI.

Th URI structure is hierarchical so a group of resources can be identified by specifying the location at a higher level in the address hierarchy, without specifying a particular resource.

Syntax
^^^^^^
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

Example::

	http://ionuser:ionuser@ionwest.itw/rundb/api/v1/experiment
		?format=json&expName__startswith=R_2013_06&order_by=date



