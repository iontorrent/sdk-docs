Django
======

Django is a web application framework that implements a RESTful API using the Tastypie framework.
Modern web-like services are typically implemented using the Model-View-Controller architectural pattern, which is similarly implemented by Django using the Python programming language.
The following figure shows a simplified Django architecture, resident on the server with a backend database and other resources.

	.. image:: ../images/apiug_sdkdjango.png

* The view component handles UI presentation tasks. In addition to supporting the REST API, Django also implements the Torrent Browser UI. In Django, the concept of view is implemented using templates.
 
* Django also includes a *request/response handler* to handle the HTTP request and transmit protocol, mapping JSON- or XML-formatted data to Python objects. HTTP requests and responses are another mechanism into the model view.
 
* The *model* component provides for database item representation, and access to persistent data. Persistent Torrent Server data are maintained in a PostgreSQL database.
 
* The *controller* component interacts with the view and model components to implement the Ion Torrent business logic of application processing, including view functions that populate the view.

With the addition of the Tastypie framework to Django, the Torrent Server supports a REST API in addition to the user interface.