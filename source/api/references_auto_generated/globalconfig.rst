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
**enable_version_lock**       Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**site_name**                 Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_support_upload**     Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**plugin_output_folder**      Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**auto_archive_ack**          Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_compendia_OCP**      Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**id**                        Integer data. Ex: 2673                                false    false    true  true   integer 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**base_recalibration_mode**   Unicode string data. Ex: "Hello World" standard_recal false    false    false false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_storage_options**   Unicode string data. Ex: "Hello World" D              false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**selected**                  Boolean data. Ex: True                                false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**check_news_posts**          Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**realign**                   Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**ts_update_status**          Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**mark_duplicates**           Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**auto_archive_enable**       Boolean data. Ex: True                 false          false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_auto_security**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_nightly_email**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**sec_update_status**         Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_flow_order**        Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**name**                      Unicode string data. Ex: "Hello World" n/a            false    false    false false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**records_to_display**        Integer data. Ex: 2673                 20             false    false    true  false  integer 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_library_key**       Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**cluster_auto_disable**      Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**web_root**                  Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**default_test_fragment_key** Unicode string data. Ex: "Hello World"                false    false    true  false  string  
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**enable_auto_pkg_dl**        Boolean data. Ex: True                 true           false    false    true  false  boolean 
----------------------------- -------------------------------------- -------------- -------- -------- ----- ------ ------- 
**resource_uri**              Unicode string data. Ex: "Hello World" n/a            false    true     false false  string  
============================= ====================================== ============== ======== ======== ===== ====== ======= 

Example Response
^^^^^^^^^^^^^^^^

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
	            "site_name": "Torrent Server", 
	            "enable_support_upload": false, 
	            "plugin_output_folder": "plugin_out", 
	            "auto_archive_ack": true, 
	            "enable_compendia_OCP": true, 
	            "id": 1, 
	            "base_recalibration_mode": "standard_recal", 
	            "default_storage_options": "A", 
	            "selected": false, 
	            "check_news_posts": true, 
	            "realign": false, 
	            "ts_update_status": "Ready to install", 
	            "mark_duplicates": false, 
	            "auto_archive_enable": true, 
	            "enable_auto_security": true, 
	            "enable_nightly_email": true, 
	            "sec_update_status": "", 
	            "default_flow_order": "TACG", 
	            "name": "Config", 
	            "records_to_display": 20, 
	            "default_library_key": "TCAG", 
	            "cluster_auto_disable": true, 
	            "web_root": "", 
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

