import requests

myURL='https://localhost:5000/v1/api/trsrv/all-conids?exchange=NYSE'

r = requests.get(myURL , verify=False )
print ( r.text )
