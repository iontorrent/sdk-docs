.. _api_reference_qualitymetrics:

Quality Metrics  Resource
=========================

| Resource URL ``http://mytorrentserver/rundb/api/v1/qualitymetrics/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/qualitymetrics/schema/``
| 

.. include:: ../references_manual_extras/qualitymetrics.rst

Resource Fields
---------------

========================== ============================================================================== ======= ======== ======== ===== ====== ======= 
field                      help text                                                                      default nullable readonly blank unique type    
========================== ============================================================================== ======= ======== ======== ===== ====== ======= 
**id**                     Integer data. Ex: 2673                                                                 false    false    true  true   integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_100bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_150bp_reads**         Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_50bp_reads**          Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_bases**               Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_max_read_length**     Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mean_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_median_read_length**  Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mode_read_length**    Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_reads**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_max_read_length**    Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mean_read_length**   Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_max_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mean_read_length**   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**                 A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**           Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
========================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": "/rundb/api/v1/qualitymetrics/?offset=1&limit=1&format=json",
	        "offset": 0,
	        "previous": null,
	        "total_count": 6
	    },
	    "objects": [
	        {
	            "id": 6,
	            "q0_100bp_reads": 1353,
	            "q0_150bp_reads": 31,
	            "q0_50bp_reads": 1485,
	            "q0_bases": "194418",
	            "q0_max_read_length": 159,
	            "q0_mean_read_length": 127.403669724771,
	            "q0_median_read_length": 135,
	            "q0_mode_read_length": 141,
	            "q0_reads": 1526,
	            "q17_100bp_reads": 1353,
	            "q17_150bp_reads": 31,
	            "q17_50bp_reads": 1485,
	            "q17_bases": "178131",
	            "q17_max_read_length": 159,
	            "q17_mean_read_length": 127.403669724771,
	            "q17_median_read_length": 135,
	            "q17_mode_read_length": 141,
	            "q17_reads": 1526,
	            "q20_100bp_reads": 1353,
	            "q20_150bp_reads": 31,
	            "q20_50bp_reads": 1485,
	            "q20_bases": "172077",
	            "q20_max_read_length": 159,
	            "q20_mean_read_length": 127,
	            "q20_median_read_length": 135,
	            "q20_mode_read_length": 141,
	            "q20_reads": 1526,
	            "report": "/rundb/api/v1/results/6/",
	            "resource_uri": "/rundb/api/v1/qualitymetrics/6/"
	        }
	    ]
	}

Allowed list HTTP methods
-------------------------

- GET
- POST
- PUT
- DELETE
- PATCH


Allowed detail HTTP methods
---------------------------

- GET
- POST
- PUT
- DELETE
- PATCH

