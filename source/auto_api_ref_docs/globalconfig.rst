Globalconfig Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/globalconfig/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/globalconfig/schema/``


.. include:: ../manual_api_ref_docs/globalconfig.rst

Fields table
------------

============================= ====================================== ======= ======== ======== ===== ====== ======= 
field                         help text                              default nullable readonly blank unique type    
============================= ====================================== ======= ======== ======== ===== ====== ======= 
**enable_version_lock**       Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**site_name**                 Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**plugin_output_folder**      Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**auto_archive_ack**          Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**default_plugin_script**     Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                         false    false    true  true   integer 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**default_storage_options**   Unicode string data. Ex: "Hello World" D       false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**selected**                  Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**check_news_posts**          Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**realign**                   Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**ts_update_status**          Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**mark_duplicates**           Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**plugin_folder**             Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**auto_archive_enable**       Boolean data. Ex: True                 false   false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**reference_path**            Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**fasta_path**                Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**barcode_args**              Unicode string data. Ex: "Hello World" {}      false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**default_flow_order**        Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World" n/a     false    false    false false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**records_to_display**        Integer data. Ex: 2673                 20      false    false    true  false  integer 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**base_recalibrate**          Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**default_library_key**       Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**web_root**                  Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**default_test_fragment_key** Unicode string data. Ex: "Hello World"         false    false    true  false  string  
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**enable_auto_pkg_dl**        Boolean data. Ex: True                 true    false    false    true  false  boolean 
----------------------------- -------------------------------------- ------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World" n/a     false    true     false false  string  
============================= ====================================== ======= ======== ======== ===== ====== ======= 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/globalconfig/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/globalconfig/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	globalconfigs = ts_api_response["objects"]
	
	for globalconfig in globalconfigs:
	    print globalconfig
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 1, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": null
	    }, 
	    "objects": [
	        {
	            "enable_version_lock": false, 
	            "site_name": "IonEast", 
	            "plugin_output_folder": "plugin_out", 
	            "auto_archive_ack": true, 
	            "default_plugin_script": "launch.sh", 
	            "id": 1, 
	            "default_storage_options": "D", 
	            "selected": true, 
	            "check_news_posts": true, 
	            "realign": false, 
	            "ts_update_status": "No updates", 
	            "mark_duplicates": false, 
	            "plugin_folder": "plugins", 
	            "auto_archive_enable": false, 
	            "reference_path": "", 
	            "fasta_path": "", 
	            "barcode_args": {
	                "filter": "0.01"
	            }, 
	            "default_flow_order": "TACG", 
	            "name": "Config", 
	            "records_to_display": 20, 
	            "base_recalibrate": true, 
	            "default_library_key": "TCAG", 
	            "web_root": "http://ioneast.ite", 
	            "default_test_fragment_key": "ATCG", 
	            "enable_auto_pkg_dl": true, 
	            "resource_uri": "/rundb/api/v1/globalconfig/1/"
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

