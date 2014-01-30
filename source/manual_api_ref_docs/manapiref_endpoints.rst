Endpoint Metadata 
=================

Each endpoint response includes metadata similar to the following example::

	"meta":
	{
		"limit": 20,
		"next": null,
		"offset": 0,
		"previous": null,
		"total_count": 1
	}

+----------------+------------------------------------------------------------------------------------+
| Metadata field | Description                                                                        |
+================+====================================================================================+
| limit          | The maximum number of elements to return in the response. A response may include   | 
|                | fewer elements if the resource has less than ``limit`` elements. Default = 20.     | 
+----------------+------------------------------------------------------------------------------------+
| offset         | The number of the first element to return in the response. The total number        | 
|                | returned is determined by the ``limit`` field. Default = 0.                        |
+----------------+------------------------------------------------------------------------------------+
| total_count    | The total number of resource elements. This is not the number of elements actually | 
|                | returned in the response unless the response included all resource elements.       |
+----------------+------------------------------------------------------------------------------------+
| next           | The URI of the next element, following the last element returned in the response.  | 
|                | If all resource elements are included in the response, this value is null.         |
+----------------+------------------------------------------------------------------------------------+
| previous       | The URI of the previous resource element, if the first element returned in the     | 
|                | response is not the first resource element. If all resource elements are included  |
|                | in the response, this value is null.                                               | 
+----------------+------------------------------------------------------------------------------------+


**Tip:** Recall that an endpoint request does not specify a particular resource element. Example::
	
	http://myhost/rundb/api/v1/results

	
	



