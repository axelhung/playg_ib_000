import requests
import time

# myURL='https://localhost:5000/v1/api/trsrv/all-conids?exchange=NYSE'
# myURL='https://localhost:5000/v1/api/iserver/marketdata/snapshot?conids=8314&fields=31,84,86'
# myURL='https://localhost:5000/v1/api/iserver/marketdata/snapshot?conids=1616390&fields=55,70,71'
myURL='https://localhost:5000/v1/api/iserver/marketdata/snapshot?conids=1616390&fields=55,31,84,86,70,71,106f'

headers = {
    "Origin": "*",
    "Access-Control-Request-Method": "GET",
    "Access-Control-Request-Headers": "Content-Type"
}

# response = requests.options( myURL, headers=headers, verify=False)

preflight_001 = requests.options(myURL, headers=headers, verify=False )
print ( preflight_001.headers  )

time.sleep(10)

r = requests.get(myURL , verify=False )
print ( r.text )
