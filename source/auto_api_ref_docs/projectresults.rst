Projectresults Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/projectresults/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/projectresults/schema/``


.. include:: ../manual_api_ref_docs/projectresults.rst

Fields table
------------

=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
field               help text                                                                                          default nullable readonly blank unique type     
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 
**reference**       Unicode string data. Ex: "Hello World"                                                             n/a     true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportStatus**    Unicode string data. Ex: "Hello World"                                                             Nothing true     false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**runid**           Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**id**              Integer data. Ex: 2673                                                                                     false    false    true  true   integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**metaData**        Unicode string data. Ex: "Hello World"                                                             {}      false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**log**             Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeStamp**       A date & time as a string. Ex: "2010-11-10T03:07:43"                                               true    false    false    true  false  datetime 
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsName**     Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**status**          Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedflows**  Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**processedCycles** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**sffLink**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**representative**  Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfSffLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**diskusage**       Integer data. Ex: 2673                                                                             n/a     true     false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**projects**        Many related resources. Can be either a list of URIs or list of individually nested resource data. n/a     false    false    false false  related  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resultsType**     Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**tfFastq**         Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**parentIDs**       Unicode string data. Ex: "Hello World"                                                                     false    false    true  false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**timeToComplete**  Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**reportLink**      Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**fastqLink**       Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**resource_uri**    Unicode string data. Ex: "Hello World"                                                             n/a     false    true     false false  string   
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**framesProcessed** Integer data. Ex: 2673                                                                             n/a     false    false    false false  integer  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**autoExempt**      Boolean data. Ex: True                                                                             false   false    false    true  false  boolean  
------------------- -------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ -------- 
**analysisVersion** Unicode string data. Ex: "Hello World"                                                             n/a     false    false    false false  string   
=================== ================================================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/projectresults/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/projectresults/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	projectresultss = ts_api_response["objects"]
	
	for projectresults in projectresultss:
	    print projectresults
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 43354, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/projectresults/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "reference": "hg19", 
	            "reportStatus": "Nothing", 
	            "runid": "DGMU8", 
	            "id": 293943, 
	            "metaData": {}, 
	            "log": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/log.html", 
	            "timeStamp": "2014-01-23T07:39:52.000803+00:00", 
	            "resultsName": "Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446", 
	            "status": "Completed", 
	            "processedflows": 0, 
	            "processedCycles": 0, 
	            "sffLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446.sff", 
	            "representative": false, 
	            "tfSffLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446.tf.sff", 
	            "diskusage": 151, 
	            "projects": [
	                {
	                    "name": "chef_827_909_20min_ext", 
	                    "creator": "/rundb/api/v1/user/1/", 
	                    "created": "2014-01-22T18:50:10.000920+00:00", 
	                    "results": [
	                        "/rundb/api/v1/results/294145/", 
	                        "/rundb/api/v1/results/293993/", 
	                        "/rundb/api/v1/results/293992/", 
	                        "/rundb/api/v1/results/293991/", 
	                        "/rundb/api/v1/results/293990/", 
	                        "/rundb/api/v1/results/293946/", 
	                        "/rundb/api/v1/results/293945/", 
	                        "/rundb/api/v1/results/293944/", 
	                        "/rundb/api/v1/results/293943/", 
	                        "/rundb/api/v1/results/293934/", 
	                        "/rundb/api/v1/results/293933/", 
	                        "/rundb/api/v1/results/293930/", 
	                        "/rundb/api/v1/results/293929/", 
	                        "/rundb/api/v1/results/293928/", 
	                        "/rundb/api/v1/results/293927/", 
	                        "/rundb/api/v1/results/293917/", 
	                        "/rundb/api/v1/results/293916/", 
	                        "/rundb/api/v1/results/293915/", 
	                        "/rundb/api/v1/results/293914/", 
	                        "/rundb/api/v1/results/293913/", 
	                        "/rundb/api/v1/results/293912/", 
	                        "/rundb/api/v1/results/293908/", 
	                        "/rundb/api/v1/results/293907/", 
	                        "/rundb/api/v1/results/293906/", 
	                        "/rundb/api/v1/results/293905/", 
	                        "/rundb/api/v1/results/293904/", 
	                        "/rundb/api/v1/results/293903/", 
	                        "/rundb/api/v1/results/293902/", 
	                        "/rundb/api/v1/results/293901/"
	                    ], 
	                    "modified": "2014-01-22T18:50:10.000920+00:00", 
	                    "id": 1080, 
	                    "resultsCount": 29, 
	                    "public": true, 
	                    "resource_uri": "/rundb/api/v1/project/1080/"
	                }
	            ], 
	            "resultsType": "", 
	            "tfFastq": "_", 
	            "parentIDs": "", 
	            "timeToComplete": "0", 
	            "reportLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/", 
	            "fastqLink": "/output/Home/Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446_293943/basecaller_results/R_2014_01_22_16_30_23_user_D1--632--R54651-p8s2_827b2_20m_man-cf_Auto_user_D1--632--R54651-p8s2_827b2_20m_man-cf_17446.fastq", 
	            "resource_uri": "/rundb/api/v1/projectresults/293943/", 
	            "framesProcessed": 0, 
	            "autoExempt": false, 
	            "analysisVersion": "db:4.1.21+2-1,an:4.1.24+0-1,"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get
- post
- put
- delete
- patch

