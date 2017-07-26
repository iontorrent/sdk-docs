Data Formats
============

The JavaScript Object Notation (JSON) is currently the only supported data format for exchanging data with Torrent Server.

JSON is a lightweight data interchange format organized as a list, or list of lists, of name-value pairs.

You must specify JSON as the desired data format for sending and receiving data as either a URI parameter or in the request header:

URI example
-----------
 :: 
 
	http://myhost/rundb/api/v1/results/122/?format=json

Request header example
----------------------
 ::
 
	Content-Type:application/json







