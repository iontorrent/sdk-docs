API Acronyms and Abbreviations
==============================

 
+-------------+-----------------+--------------------------------------------------------------------------------------+
| Acronym     | Expanded        | Description                                                                          |
+=============+=================+======================================================================================+
| API         | Application     | A well-defined programmatic interface to a software                                  |
|             | Programming     | component. The programmatic interface to the Torrent                                 |
|             | Interface       | Server database and software functionality is through                                |
|             |                 | the API described in this document.                                                  |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| AJAX        | Asynchronous    | JavaScript examples in this documentation use AJAX to make requests to the           |
|             | JavaScript and  | server using the REST API.                                                           |
|             | XML             | (`wikipedia AJAX <http://en.wikipedia.org/wiki/Ajax_(programming)>`_)                |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| CRUD        | Create, Read,   | This common acronym lists the REST API methods.                                      |
|             | Update. Delete  | (`wikipedia CRUD <http://en.wikipedia.org/wiki/Create,_read,_update_and_delete>`_)   |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| CSS         | Cascading Style | Style sheets are used in some examples in this documentation.                        |
|             | Sheets          | (`http://www.w3.org/Style/CSS <http://www.w3.org/Style/CSS/>`_)                      |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| HTTP        | Hypertext       | A request-response communication model for client-server computing architectures,    |
|             | Transfer        | commonly known as the underlying communication mechanism of the Web. The protocol    |
|             | Protocol        | defines message for create, read, update and delete (CRUD), among others, used by    |
|             |                 | the REST communication model.                                                        |
|             |                 | ( `http://tools.ietf.org/html/rfc2616 <http://tools.ietf.org/html/rfc2616>`_ )       |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| JSON        |                 | JSON is a language-independent data interchange format using JavaScript conventions. |
|             |                 | JSON is currently the only data transport format supported by the Torrent Suite™     |
|             |                 | Software API. See XML.                                                               |
|             |                 | ( `http://www.json.org/ <http://www.json.org/>`_)                                    |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| JSONP       | JSON with       | JSONP is an extension of the JSON data format to support cross-domain data transfer. |
|             | Padding         | JavaScript restricts such cross-domain operations using simple JSON, for security    |
|             |                 | reasons. Implementing applications using the REST API with JavaScript necessitates   |
|             |                 | using JSONP.                                                                         |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| MVC         | Model View      | MVC describes a common architectural pattern used to implement web-based application |
|             | Controller      | servers, where core functionality is decomposed into three components: model, view,  |
|             |                 | and controller. The model part is the back-end database component, the view part is  |
|             |                 | the UI or presentation component, and the controller part implements the application |
|             |                 | logic. While Django may not strictly implemented the MVC pattern, it is conceptually |
|             |                 | similar enough to discuss the Torrent Suite architectural framework in MVC terms.    |
|             |                 | ( `wikipedia <http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_) |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| REST        | Representation  | A client-server communication model for transferring representations of              |
|             | State Transfer  | resources, which can be database or functional components. REST uses HTTP as         |
|             |                 | the communication mechanism without assuming that resource state is maintained       |
|             |                 | between request messages. The Torrent Suite™ Software API uses REST as the           |
|             |                 | underlying communication model between client application programs and server        |
|             |                 | resources. Using a noun-verb abstraction, the REST methods are the verbs that        |
|             |                 | operate on resources as nouns. Resources are addressable by their URI.               |
|             |                 | ( `wikipedia REST <http://en.wikipedia.org/wiki/Representational_State_Transfer>`_)  |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| RPC         | Remote Procedure| A Remote Procedure Call is similar to a programming language subroutine call,        |
|             | Call            | except that the "call" is to a remote system and the parameters and data             |
|             |                 | associated with the call are contained in a message. A synchronous RPC is also       |
|             |                 | like a subroutine call in that the calling function pends on the response, or        |
|             |                 | completion. REST is a form of RPC.                                                   |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| SGE         | Sun Grid Engine | An opensource distributed computing solution from Sun Microsystems that              |
|             |                 | enables multiple computers or servers to be linked. The SGE provides a               |
|             |                 | mechanism for creating and managing a job queue to distribute computing tasks        |
|             |                 | over a cluster of machines, reducing CPU utilization on any single machine.          |
|             |                 | The SGE is used to schedule plugins among compute resources, including running       |
|             |                 | in parallel on a single server as resources permit.                                  |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| SQL         | Structured Query| Torrent Server uses a PostgreSQL database for persistent backend data storage.       |
|             | Language        | PostgreSQL supports access to the data using standardized SQL. Django                |
|             |                 | integrates PostgreSQL as the model of an MVC framework and exports an SQL-like       |
|             |                 | interface, using Tastypie, through the REST API.                                     |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| URI         | Uniform Resource| REST resources are addressable by their HTTP URI global identifier.                  |
|             | Identifier      | (`http://tools.ietf.org/html/rfc3986 <http://tools.ietf.org/html/rfc3986>`_)         |
+-------------+-----------------+--------------------------------------------------------------------------------------+
| XML         | Extensible      | A set of rules for encoding documents. XML is one the REST API data transfer         |
|             | Markup Language | formats but is not currently supported by the Torrent Suite™ Software API.           |
|             |                 | (`http://www.w3.org/Style/CSS <http://www.w3.org/Style/CSS/>`_,                      |
|             |                 | `http://www.w3.org/TR/REC-xml <http://www.w3.org/TR/REC-xml>`_)                      |
+-------------+-----------------+--------------------------------------------------------------------------------------+