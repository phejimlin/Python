# -*- coding: utf-8 -*-
import requests
import json
import txt_to_json as converter


#get Organizations' id 
def get_Org_ID():
	URL='https://api.signalfx.com/v1/organization?query=sf_organization:YOUR ORG NAME'
	headers={'X-SF-Token':'YOUR account TOKEN'}



	request = requests.get(URL,headers=headers)    
	print(request.status_code)    
	print(request.headers)
	print request.text

#post data 
def post_Data(data):
	URL='https://ingest.signalfx.com/v2/datapoint?orgid="YOUR ORGID"'
	headers={'X-SF-Token':'YOUR account TOKEN'}


	payload={"gauge":[{"metric": "testmetric", "dimensions": {"host": "myserver"}, "value": '77'}]}
	
	# request = requests.post(URL,data=json.dumps(payload),headers=headers)    
	request = requests.post(URL,data=json.dumps(data),headers=headers)    

	print request.status_code
	print request.headers
	print request.text

get_Org_ID()


test = converter.txt_To_Json('test')
print(json.dumps(test.transform()))
