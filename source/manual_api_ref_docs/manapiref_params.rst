Parameters 
==========

These required and optional parameters specify the format of the data sent and received and throttle the transferred data set.

For the GET method, options are appended as parameters to the URI with a question mark (?) and multiple parameters are separated by an ampersand (&), as shown in the following example::

	http://myhost/rundb/api/v1/experiment?format=json&order_by=date

For the PUT, POST and DELETE methods, options are specified in the request header, as shown in the following cURL example::

	--header "Content-Type: application/json"

The following tables indicate to which REST method(s) the option applies:

* C = Create (POST)
* R = Read (GET)
* U = Update (PUT)
* D = Delete (DELETE)
	 
Topics on this page:
	 
* :ref:`apimanref_required`
 
* :ref:`apimanref_optional`
 

.. _apimanref_required:

Required parameter
------------------

+-----------+---+---+-----+---+--------------+--------------------------------------------------------------+
| Parameter | C | R | U   | D | Usage        | Description                                                  |
+===========+===+===+=====+===+==============+==============================================================+
| format    | X | X | X   | X | format=json  |The ``format`` parameter specifies the format of              | 
|           |   |   |     |   |              |sent data and the expected format of received data:           | 
|           |   |   |     |   |              |                                                              | 
|           |   |   |     |   |              |* ``json`` = JSON-formatted data                              | 
|           |   |   |     |   |              |* ``xml`` = XML-formatted data (not supported currently)      |
+-----------+---+---+-----+---+--------------+--------------------------------------------------------------+

Example syntax::

	http://myhost.itw//rundb/api/v1/experiment?format=json

	
.. _apimanref_optional:

Optional parameters
-------------------

+-----------+---+---+---+---+---------------+--------------------------------------------------------------+
| Parameter | C | R | U | D | Example       | Description                                                  |
+===========+===+===+===+===+===============+==============================================================+
| limit     |   | X |   |   | limit=100     | The ``limit`` parameter specifies the maximum number of      | 
|           |   |   |   |   |               | elements to be returned in the response. Use with the        | 
|           |   |   |   |   |               | ``offset`` parameter to indicate a range.                    |
+-----------+---+---+---+---+---------------+--------------------------------------------------------------+
| offset    |   | X |   |   | offset=25     | The zero-based ``offset`` parameter specifies the first      |
|           |   |   |   |   |               | data element to return in the response, for ``limit`` or     |
|           |   |   |   |   |               | the default number of elements.                              |
+-----------+---+---+---+---+---------------+--------------------------------------------------------------+ 
| order-by  |   | X |   |   | order_by=date | The ``order_by`` parameter alphanumerically orders the       | 
|           |   |   |   |   |               | received data set by the specified field name. The           |
|           |   |   |   |   |               | default is to sort in ascending order. A minus (-) symbol    |
|           |   |   |   |   |               | in front of the sort field reverses the sort order.          |
+-----------+---+---+---+---+---------------+--------------------------------------------------------------+
| <field>   |   | X | X | X | name=testPGM  | Any field, except ``resource_uri`` can be included in the    |
|           |   |   |   |   |               | parameter list. The request matches on any and all           |
|           |   |   |   |   |               | resources whose field value equals the parameter value       |
|           |   |   |   |   |               | (or qualified value). Field parameters can be qualified      |
|           |   |   |   |   |               | with partially matching values using Filter Qualifiers       |
|           |   |   |   |   |               | (see :ref:`apiug-workdjangofilter`).                         |
+-----------+---+---+---+---+---------------+--------------------------------------------------------------+

Example syntax::

	http://myhost.itw//rundb/api/v1/experiment?format=json&limit=100

	http://myhost.itw//rundb/api/v1/experiment?format=json&offset=50

	http://myhost.itw//rundb/api/v1/experiment?format=json&offset=10&limit=25

	http://myhost.itw//rundb/api/v1/experiment?format=json&library__startswith=e_coli

	http://myhost.itw//rundb/api/v1/experiment?format=json&library__startswith=e_coli&order_by=date