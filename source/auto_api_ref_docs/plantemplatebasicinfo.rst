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
**isSystemDefault**               Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**hotSpotRegionBedFile**          Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planShortID**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planStatus**                    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chefLastUpdate**                A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatingKitBarcode**          Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sampleTubeLabel**               Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**planExecutedDate**              A date & time as a string. Ex: "2010-11-10T03:07:43"                           n/a     true     false    false false  datetime 
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**chefStatus**                    Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
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
**chefLogPath**                   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
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
**chefProgress**                  Floating point numeric data. Ex: 26.73                                         0.0     false    false    true  false  float    
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**autoName**                      Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**isReusable**                    Boolean data. Ex: True                                                         false   false    false    true  false  boolean  
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**controlSequencekitname**        Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**irAccountName**                 Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**sequencingInstrumentType**      Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**targetRegionBedFile**           Unicode string data. Ex: "Hello World"                                                 true     true     true  false  string   
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
**chefMessage**                   Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**templatePrepInstrumentType**    Unicode string data. Ex: "Hello World"                                         n/a     true     true     true  false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**pairedEndLibraryAdapterName**   Unicode string data. Ex: "Hello World"                                         n/a     true     false    false false  string   
--------------------------------- ------------------------------------------------------------------------------ ------- -------- -------- ----- ------ -------- 
**runMode**                       Unicode string data. Ex: "Hello World"                                                 false    false    true  false  string   
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
	        "total_count": 66, 
	        "offset": 0, 
	        "limit": 1, 
	        "next": "/rundb/api/v1/plantemplatebasicinfo/?offset=1&limit=1&format=json"
	    }, 
	    "objects": [
	        {
	            "isReverseRun": false, 
	            "planDisplayedName": "chef_nonGUI_Exome Panel_AmpliSeqExome.20131001", 
	            "storage_options": "A", 
	            "preAnalysis": true, 
	            "reference": "hg19", 
	            "isSystemDefault": false, 
	            "hotSpotRegionBedFile": "", 
	            "planShortID": "2OXYZ", 
	            "planStatus": "planned", 
	            "chefLastUpdate": null, 
	            "templatingKitBarcode": null, 
	            "sampleTubeLabel": "", 
	            "planExecutedDate": null, 
	            "chefStatus": "", 
	            "samplePrepKitName": "Ion AmpliSeq Exome Kit", 
	            "reverse_primer": null, 
	            "applicationGroup": "/rundb/api/v1/applicationgroup/1/", 
	            "applicationGroupDisplayedName": "DNA", 
	            "id": 100224, 
	            "metaData": {}, 
	            "sampleSet_uid": null, 
	            "isFavorite": true, 
	            "sampleSet_planIndex": 0, 
	            "seqKitBarcode": null, 
	            "chefLogPath": null, 
	            "isPlanGroup": false, 
	            "sampleGroupName": "", 
	            "templatingKitName": "Ion PI Template OT2 200 Kit v3", 
	            "barcodeKitName": "IonXpress", 
	            "runType": "AMPS_EXOME", 
	            "planPGM": null, 
	            "chefProgress": 0.0, 
	            "autoName": null, 
	            "isReusable": true, 
	            "controlSequencekitname": "", 
	            "irAccountName": "None", 
	            "sequencingInstrumentType": "PROTON", 
	            "targetRegionBedFile": "/results/uploads/BED/46/hg19/unmerged/detail/AmpliSeqExome.20131001.designed.bed", 
	            "date": "2014-05-20T13:55:02.000398+00:00", 
	            "isSystem": false, 
	            "libkit": null, 
	            "categories": "", 
	            "planName": "chef_nonGUI_Exome_Panel_AmpliSeqExome.20131001", 
	            "chefMessage": "", 
	            "templatePrepInstrumentType": "OneTouch", 
	            "pairedEndLibraryAdapterName": "", 
	            "runMode": "single", 
	            "adapter": null, 
	            "irworkflow": "", 
	            "chipBarcode": null, 
	            "planExecuted": false, 
	            "username": "ionuser", 
	            "usePostBeadfind": false, 
	            "storageHost": null, 
	            "expName": "", 
	            "runname": null, 
	            "usePreBeadfind": true, 
	            "planGUID": "a81c02b6-e8f7-411f-aeeb-302fa16baa51", 
	            "cycles": null, 
	            "notes": "Uploaded from amplseq.com and available at-jira.itw_wiki_x_HAHcAg\r\nReplace _ with slashes for link to Document collection on JIRA\r\nAdded AmpliseqExome.germline_lowstringency_p1.4_0.20130920.parameters.json parameter file.", 
	            "sampleSet_planTotal": 0, 
	            "resource_uri": "/rundb/api/v1/plantemplatebasicinfo/100224/"
	        }
	    ]
	}

Allowed HTTP methods
--------------------

- get

