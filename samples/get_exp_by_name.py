import requests

experiment_name = "b006f48b-27fc-4e93-8a26-cef5bf71b8b0"

ts_api_request = requests.get("http://localhost:10500/rundb/api/v1/experiment/", params={"format": "json", "expName": experiment_name})
ts_api_response = ts_api_request.json()

print ts_api_response
