Torrent Suite™ Software SDK Code Samples
========================================

.. contents::
	
Get experiment by name (Python)
-------------------------------

.. code-block:: python

    import requests

    experiment_name = "b006f48b-27fc-4e93-8a26-cef5bf71b8b0"

    ts_api_request = requests.get("http://localhost:10500/rundb/api/v1/experiment/", params={"format": "json", "expName": experiment_name})
    ts_api_response = ts_api_request.json()

    print ts_api_response

Write an experiment note (Python)
---------------------------------

.. code-block:: python

	import json
	import requests
	
	metaData = json.dumps({ "notes":"updated note" })
	
	putResp = requests.put('http://myhost/rundb/api/v1/experiment/<pk>/'%base_url, \
	data=metaData, headers={'content-type':'application/json'}, \
	auth=('myusername', 'mypassword'))
	
	print resp.status_code

Get analysis result metadata and metrics (Python)
-------------------------------------------------

.. code-block:: python

	import requests
	import simplejson as json
	import sys
	
	if len(sys.argv) == 2:
		[runName] = sys.argv[1:2]
	else:
		print '\n\tUsage:   getruninfo.py <runName>'
		print '\n\tExample: getruninfo.py Auto_user_f4--134-br_21'
		sys.exit(1)
	
	resp = requests.get('http://myhost/rundb/api/v1/results?format=json&resultsName=%s'%runName, \
		auth=('myusername', 'mypassword'))
	resp_json = resp.json()
	
	try:
		runData = resp_json[u'objects'][0]
		experLoc = runData[u'experiment']
	except (KeyError, IndexError):
		print 'ERROR: Invalid name given.'
		sys.exit(1)
	
	expResult = requests.get('http://%s%s'%(myhost, experLoc))
	expData = expResult.json()
	
	try:
		print '\nProject:\t\t%s'%expData[u'log'][u'project']
		print 'Experiment Name:\t%s'%expData[u'expName']
		print 'PGM Name:\t\t%s'%expData[u'pgmName']
		print 'Library:\t\t%s'%expData[u'log'][u'library']
		print 'Notes:\t\t\t%s'%expData[u'notes']
	except KeyError:
		print 'ERROR: Invalid key in expData.'
	
	try:
		print 'Results:\t\t%s'%runData['resultsName']
		print 'Timestamp:\t\t%s'%runData['timeStamp']
	except KeyError:
		print 'ERROR: Invalid key in runData.'
	
	ametricsLoc = runData[u'analysismetrics'][0]
	aResult = requests.get('http://%s%s'%(myhost,ametricsLoc))
	aData = aResult.json()
	
	print '\n\nAnalysis Metrics:\n==================\n'
	for propType, propVal in aData.iteritems():
		if propType != 'resource_uri':
			print '%s\t\t= %s'%(propType, propVal)
	
	qmetricsLoc = runData[u'qualitymetrics'][0]
	qResult = requests.get('http://%s%s'%(myhost,qmetricsLoc))
	qData = qResult.json()
	
	print '\n\nQuality Metrics:\n===================\n'
	for propType, propVal in qData.iteritems():
		if propType != 'resource_uri':
			print '%s\t\t=%s'%(propType, propVal)

Add a PGM™ or Proton™ Sequencer (Python)
-------------------------------------------

.. code-block:: python

	import json
	import requests
	
	resp = requests.get('http://myhost/rundb/api/v1/rig/<existing_rig>?format=json', \
		auth=('myusername', 'mypassword'))
	resp_json = resp.json()
	
	resp_json.update(name='<new_rig_name>')
	resp_json.pop('resource_uri')
	resp_json['location'].pop('resource_uri')
	
	pdata = json.dumps(resp_json)
	
	status = requests.put('http://myhost/rundb/api/v1/rig/<new_rig_name>/', \
		data=pdata, headers={'content-type':'application/json'}, auth=('myusername', 'mypassword))

*The same code can be used to update a sequencer with the following changes; replace the 'name' field with whatever needs updating, and direct the put request to the original rig.*

Get the status for a PGM™ or Proton™ Sequencer (Python)
-------------------------------------------------------

.. code-block:: python

    import requests

    ts_api_request = requests.get("http://localhost:10500/rundb/api/v1/rig/", params={"format": "json"})
    ts_api_response = ts_api_request.json()

    rigs = ts_api_response["objects"]

    print "Found %i sequencer(s):" % len(rigs)

    for rig in rigs:
            print
            print "Name: %s" % rig["name"]
            print "Status: %s" % rig["state"]

Download a FASTQ file (Python)
------------------------------

.. code-block:: python

	import json
	import requests
	
	resp = requests.get('http://myhost/rundb/api/v1/results/<pk>?format=json', \
		auth=('myusername', 'mypassword'))
	resp_json = resp.json()
	
	resp = requests.get('http://myhost/%s'%resp_json['fastqlink'], \
		auth=('myusername', 'mypassword'))
	
	print resp_json['fastqlink']
	print resp.content #(The FASTQ file contents.)

List file servers (Python)
-----------------------------

.. code-block:: python

	import httplib2
	import json
	
	h = httplib2.Http(".cache")
	h.add_credentials('myusername', 'mypassword')
	
	resp, content = h.request("http://myhost/rundb/api/v1/fileserver?format=json", "GET")
	contentdict = json.loads(content)
	
	objects = contentdict['objects']
	for obj in objects:
		print obj['filesPrefix']

\

.. seealso:: See the API Cookbook for information on how to access the API programatically:  :ref:`api-cook`.



