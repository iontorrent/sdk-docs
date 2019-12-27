.. _api_reference_globalconfig:

Global Config Resource
======================

| Resource URL ``http://mytorrentserver/rundb/api/v1/globalconfig/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/globalconfig/schema/``
| 

.. include:: ../references_manual_extras/globalconfig.rst

Resource Fields
---------------

============================= ====================================== ============== ======== ======== ===== ====== ======= 
field                         help text                              default        nullable readonly blank unique type    
============================= ====================================== ============== ======== ======== ===== ====== ======= 
**auto_archive_ack**          Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**auto_archive_enable**       Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**base_recalibration_mode**   Unicode string data. Ex: "Hello World" standard_recal false    false    false false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**check_news_posts**          Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**cluster_auto_disable**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_flow_order**        Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_library_key**       Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_storage_options**   Unicode string data. Ex: "Hello World" D              false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_test_fragment_key** Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_auto_pkg_dl**        Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_auto_security**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_compendia_OCP**      Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_nightly_email**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_support_upload**     Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_version_lock**       Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                                false    false    true  true   integer 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**mark_duplicates**           Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World" n/a            false    false    false false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**plugin_output_folder**      Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**realign**                   Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**records_to_display**        Integer data. Ex: 2673                 20             false    false    true  false  integer 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World" n/a            false    true     false false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**sec_update_status**         Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**selected**                  Boolean data. Ex: True                                false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**site_name**                 Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**telemetry_enabled**         Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**ts_update_status**          Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**web_root**                  Unicode string data. Ex: "Hello World"                false    false    true  false  string  
============================= ====================================== ============== ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "limit": 1,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 1
	    },
	    "objects": [
	        {
	            "auto_archive_ack": true,
	            "auto_archive_enable": true,
	            "base_recalibration_mode": "standard_recal",
	            "check_news_posts": true,
	            "cluster_auto_disable": true,
	            "default_flow_order": "TACG",
	            "default_library_key": "TCAG",
	            "default_storage_options": "A",
	            "default_test_fragment_key": "ATCG",
	            "enable_auto_pkg_dl": true,
	            "enable_auto_security": true,
	            "enable_compendia_OCP": true,
	            "enable_nightly_email": true,
	            "enable_support_upload": false,
	            "enable_version_lock": false,
	            "id": 1,
	            "mark_duplicates": false,
	            "name": "Config",
	            "plugin_output_folder": "plugin_out",
	            "realign": false,
	            "records_to_display": 20,
	            "resource_uri": "/rundb/api/v1/globalconfig/1/",
	            "sec_update_status": "",
	            "selected": false,
	            "site_name": "Torrent Server",
	            "telemetry_enabled": true,
	            "ts_update_status": "No updates",
	            "web_root": ""
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

