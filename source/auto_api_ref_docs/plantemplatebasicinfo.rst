Plantemplatebasicinfo Resource
==========================================================================

Resource URL: ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/``


Schema URL: ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/schema/``


.. include:: ../manual_api_ref_docs/plantemplatebasicinfo.rst

Fields table
------------

================================= ============================================================================== ======= ======== ======== ===== ====== ======== 
field                             help text                                                                      default nullable readonly blank unique type     
================================= ============================================================================== ======= ======== ======== ===== ====== ======== 
**templatingSize**                Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isReverseRun**                  Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planDisplayedName**             Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**storage_options**               Unicode string data. Ex: "Hello World"                                         A       false    false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**preAnalysis**                   Boolean data. Ex: True                                                                 false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reference**                     Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planShortID**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**          Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planStatus**                    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runMode**                       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**               Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planExecutedDate**              A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**samplePrepKitName**             Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**reverse_primer**                Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applicationGroup**              A single related resource. Can be either a URI or set of nested resource data. n/a     true     false    true  false  related  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**applicationGroupDisplayedName** Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**id**                            Integer data. Ex: 2673                                                                 false    false    true  true   integer  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**metaData**                      Unicode string data. Ex: "Hello World"                                         {}      false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet_uid**                 Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isFavorite**                    Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet_planIndex**           Integer data. Ex: 2673                                                         0       false    false    false false  integer  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**seqKitBarcode**                 Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isPlanGroup**                   Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleGroupName**               Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingKitName**             Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**barcodeKitName**                Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runType**                       Unicode string data. Ex: "Hello World"                                         GENS    false    false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planPGM**                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystemDefault**               Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**autoName**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isReusable**                    Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sequencingInstrumentType**      Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**date**                          A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isSystem**                      Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libkit**                        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**categories**                    Unicode string data. Ex: "Hello World"                                                 true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planName**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**irAccountName**                 Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatePrepInstrumentType**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**           Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**adapter**                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**irworkflow**                    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chipBarcode**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planExecuted**                  Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**username**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**usePostBeadfind**               Boolean data. Ex: True                                                                 false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**storageHost**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**expName**                       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**libraryReadLength**             Integer data. Ex: 2673                                                         0       false    false    false false  integer  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runname**                       Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**usePreBeadfind**                Boolean data. Ex: True                                                                 false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planGUID**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**cycles**                        Integer data. Ex: 2673                                                         n/a     true     false    false false  integer  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**notes**                         Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleSet_planTotal**           Integer data. Ex: 2673                                                         0       false    false    false false  integer  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**resource_uri**                  Unicode string data. Ex: "Hello World"                                         n/a     false    true     false false  string   
================================= ============================================================================== ======= ======== ======== ===== ====== ======== 

Example request
---------------

Request URL: ``http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/?format=json&limit=1``


Python example
^^^^^^^^^^^^^^

.. code-block:: python

	
	import requests
	
	ts_api_request = requests.get("http://mytorrentserver/rundb/api/v1/plantemplatebasicinfo/", params={"format": "json", "limit": 1})
	ts_api_response = ts_api_request.json()
	
	plantemplatebasicinfos = ts_api_response["objects"]
	
	for plantemplatebasicinfo in plantemplatebasicinfos:
	    print plantemplatebasicinfo
	
Torrent Server response
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "meta": {
	        "previous": null, 
	        "total_count": 129, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plantemplatebasicinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "templatingSize": "200", 
	            "isReverseRun": false, 
	            "planDisplayedName": "IC_P1v2_VAL_ccp", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "reference": "hg19", 
	            "planShortID": "IL9TF", 
	            "hotSpotRegionBedFile": "/results/uploads/BED/47/hg19/unmerged/detail/CCP.20131001.hotspots.bed", 
	            "planStatus": "pending", 
	            "runMode": "single", 
	            "templatingKitBarcode": null, 
	            "sampleTubeLabel": "", 
	            "planExecutedDate": null, 
	            "samplePrepKitName": "", 
	            "reverse_primer": null, 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "applicationGroupDisplayedName": "DNA", 
	            "id": 111154, 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "seqKitBarcode": null, 
	            "isPlanGroup": false, 
	            "sampleGroupName": "", 
	            "templatingKitName": "Ion PROTON IC v2 Universal", 
	            "barcodeKitName": "IonXpress", 
	            "runType": "AMPS", 
	            "planPGM": null, 
	            "isSystemDefault": false, 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": "", 
	            "sequencingInstrumentType": "PROTON", 
	            "date": "2015-01-28T19:57:42.000445+00:00", 
	            "isSystem": false, 
	            "libkit": null, 
	            "categories": "", 
	            "planName": "IC_P1v2_VAL_ccp", 
	            "irAccountName": "None", 
	            "templatePrepInstrumentType": "IonChef", 
	            "pairedEndLibraryAdapterName": "", 
	            "targetRegionBedFile": "/results/uploads/BED/44/hg19/unmerged/detail/CCP.20131001.designed.bed", 
	            "adapter": null, 
	            "irworkflow": "", 
	            "chipBarcode": null, 
	            "planExecuted": false, 
	            "username": "ionuser", 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "", 
	            "libraryReadLength": 200, 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "b55face2-df5f-434c-89df-210f384170cb", 
	            "cycles": null, 
	            "notes": "", 
	            "sampleSet_planTotal": 0, 
	            "resource_uri": "/rundb/api/v1/plantemplatebasicinfo/111154/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get

