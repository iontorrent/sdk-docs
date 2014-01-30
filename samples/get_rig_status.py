import requests

ts_api_request = requests.get("http://localhost:10500/rundb/api/v1/rig/", params={"format": "json"})
ts_api_response = ts_api_request.json()

rigs = ts_api_response["objects"]

print "Found %i sequencer(s):" % len(rigs)

for rig in rigs:
	print
	print "Name: %s" % rig["name"]
	print "Status: %s" % rig["state"]

