General Architecture
====================

The Torrent Suite™ Software API is implemented as conventional web service, where your client application sends and receive messages to access server functionality.

The following figure describes the client-server relationship and the layered implementation of the web service implemented by the server.

	.. image:: ../images/apiug_sdkarch.png

Programming model
-----------------

Client application
^^^^^^^^^^^^^^^^^^

Your application is the client application in the client-server architecture, which can be further described as a service-oriented architecture. The client makes requests for information, or data or some service and the server responds to the request. The server makes system facilities available to your application as a service. Your application behaves very much like the web browser with which you are familiar, except that as a specialized program your application can do more than simply view the data.

REST
^^^^

Representational State Transfer (REST) is another architectural concept applied to data interchange between clients and servers. Using the communication methods inherent in the underlying HTTP protocol, clients make requests for resources resident on the server. Resources are usually database items but can be any service or functionality implemented by the server. These communication methods are the following:

* GET to retrieve information from the server.
* PUT to update information on the server.
* POST to create a new information record on the server.
* DELETE to delete information on the server.

Web developers should already be familiar with these methods.

Other characteristics that make REST the architecture of choice for the Torrent Suite API include:

* Server resources are addressable using a Universal Resource Identifier (URI), which is similar to the URL in your browser address window.
* The JavaScript Object Notation (JSON) data format is supported, providing a simple data encoding, transfer and decoding, while meeting the needs of most applications.
* REST is stateless, as the name implies, meaning the server does not have or provide the additional complexity of maintaining the state of the application.
* REST is easy to implement and easy to use.

Server
^^^^^^

The server makes resources and functionality available to client applications upon request.

Web application servers typically implement the Model-View-Controller architecture pattern. Simply, the server software implementation abstracts the backend database, or *model*, and presents a view of the data in a way that the application can access and use. The *controller* part of the pattern implements the business logic around the data.

This decomposition of web application server software is in widespread use and Django is used to implement an MVC-like pattern in Torrent Server.

Django
^^^^^^

Django is a web application framework that implements a RESTful API using the Tastypie framework.

Modern web-like services are typically implemented using the Model-View-Controller architectural pattern, which is similarly implemented by Django using the Python programming language.

Resources
^^^^^^^^^

The API operates on resources, which are addressable using a URI. The conventional notion of a web application resource is a database item but the API extends the notion to include the file system and plugins.

Resources that are not database entities, such as plugins, are not included in the REST API schema listing.

PostgreSQL database
^^^^^^^^^^^^^^^^^^^

Torrent Server uses a PostgreSQL database for persistent backend data storage. PostgreSQL supports access to the data using standardized SQL.

Django integrates PostgreSQL as the model of an MVC framework and exports an SQL-like interface, using Tastypie, through the REST API.

File system
^^^^^^^^^^^

The API can be used to download files, typically, analysis data and results files.

A number of database resources, such as results, have fields that link to results files. An application can use these links to reference and download files.

Plugin framework
^^^^^^^^^^^^^^^^

Plugins provide a mechanism for you to write code that can be run, automatically or manually, using a shell script after analysis pipeline processing completes. The plugin feature extends Torrent Server capabilities in an open-ended, flexible way.

The API provides methods to submit plugins to the job scheduler.
