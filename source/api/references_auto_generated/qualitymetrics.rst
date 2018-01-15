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
**q0_reads**               Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_max_read_length**    Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**report**                 A single related resource. Can be either a URI or set of nested resource data. n/a     false    false    false false  related 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mean_read_length**   Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**resource_uri**           Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_max_read_length**     Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_100bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**id**                     Integer data. Ex: 2673                                                                 false    false    true  true   integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mean_read_length**   Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_bases**               Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_reads**              Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_50bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_median_read_length** Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_50bp_reads**          Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_150bp_reads**        Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_150bp_reads**         Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mean_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_mode_read_length**    Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_max_read_length**    Floating point numeric data. Ex: 26.73                                         n/a     false    false    false false  float   
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q20_bases**              Unicode string data. Ex: "Hello World"                                         n/a     false    false    false false  string  
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_median_read_length**  Integer data. Ex: 2673                                                         0       false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q0_100bp_reads**         Integer data. Ex: 2673                                                         n/a     false    false    false false  integer 
-------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ ------- 
**q17_mode_read_length**   Integer data. Ex: 2673                                                         0       false    false    false false  integer 
========================== ============================================================================== ======= ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 6, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/qualitymetrics/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "q0_reads": 93969124, 
	            "q17_max_read_length": 361, 
	            "q20_median_read_length": 149, 
	            "q20_reads": 93969124, 
	            "report": "/rundb/api/v1/results/3/", 
	            "q17_mean_read_length": 149.579903660696, 
	            "q17_100bp_reads": 82389255, 
	            "resource_uri": "/rundb/api/v1/qualitymetrics/1/", 
	            "q0_max_read_length": 361, 
	            "q20_100bp_reads": 82389255, 
	            "id": 1, 
	            "q20_mean_read_length": 149, 
	            "q20_150bp_reads": 46834701, 
	            "q0_bases": "14055892515", 
	            "q20_50bp_reads": 91801424, 
	            "q17_reads": 93969124, 
	            "q17_50bp_reads": 91801424, 
	            "q17_median_read_length": 149, 
	            "q0_50bp_reads": 91801424, 
	            "q17_150bp_reads": 46834701, 
	            "q0_150bp_reads": 46834701, 
	            "q0_mean_read_length": 149.579903660696, 
	            "q17_bases": "12627160533", 
	            "q0_mode_read_length": 141, 
	            "q20_mode_read_length": 141, 
	            "q20_max_read_length": 361, 
	            "q20_bases": "11916010889", 
	            "q0_median_read_length": 149, 
	            "q0_100bp_reads": 82389255, 
	            "q17_mode_read_length": 141
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

