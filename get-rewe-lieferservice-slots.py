#get-rewe-lieferservice-slots.py

import requests
from datetime import datetime, timedelta

url = 'https://shop.rewe.de/checkout/timeslot'

start_date = datetime.today().date().strftime('%Y-%m-%dT%H:%M:%S')
end_date = (datetime.today().date() + timedelta(days=14)).strftime('%Y-%m-%dT%H:%M:%S')

json_data = {
            	"customerUuid": "2ac0989d-0cac-4f52-b6c4-a88114c08e0f",
            	"slotId": '35c760a9-f02a-4f92-a063-18c255c6d3b9',
            	"serviceType": 'lieferservice',
	            "timeSlotStartTime": None,
            	"timeSlotEndTime": None,
            	"cutoffTime": None,
            	"storeId": None,
            	"zipCode": '51503',
	            "undiscountedServiceFee": None,
            	"undiscountedServiceFeeNan": None,
            	"modifiedOrderId": None
            }

# Make POST request to calendar, sending required JSON data
r = requests.post(url, json=json_data)

r.status_code # Inspect status code of response
#r.json() # Decoding JSON response content

# Initialise empty dictionary for data
slot_data = {}
