#!/usr/bin/python3
import json

with open('students.json') as json_data :
	data_dict = json.load(json_data)
data_str = json.dumps(data_dict)
print(data_str)	
