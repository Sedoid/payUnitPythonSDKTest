import json
import uuid
import base64
import requests
import webbrowser
from requests.auth import HTTPDigestAuth

class payUnit:
    """
    Initiates and processes payments
    """
    def __init__(self,data):      
        self.config_data = data

    def makePayment(self,amount): 
        if(int(amount) <= 0):
            return {"message":"Invalid transaction amount","status":False}
            
        user_api = self.config_data["user_api"]
        password_api = str(self.config_data["password_api"])
        api_key = str(self.config_data["api_key"])  
        auth = user_api+":"+password_api
        base64AuthData = base64.b64encode((auth).encode()).decode()
        # auth = base64.encode(auth,'')``
        return_url = str(self.config_data["return_url"])
        test_url = "http://192.168.100.70:5000/api/gateway/initialize"

        headers = {
            "x-api-key": str(api_key),
            "content-type": "application/json",
            "Authorization": "Basic "+ str(base64AuthData)
        }

        test_body = {
            "description":"A sample description for a reason for a transaction",
            "transaction_id":  str(uuid.uuid1()),
            "total_amount": str(amount),
            "return_url": str(self.config_data['return_url'])
        }
        # response = requests.post(test_url,auth = HTTPDigestAuth(user_api,password_api),data = json.dumps(test_body),headers = headers)
        # response = requests.post(test_url,data = json.dumps(test_body),headers = headers)
        # print(response.content)
        try:   
            response = requests.post(test_url,data = json.dumps(test_body),headers = headers)
            response = response.json()
            if(response['body']['status'] == 200):
                webbrowser.open(response['body']['transaction_url'])
                return {"message":"Successfylly initated Transaction","status":True}
        except:
            
            return {"message":"Oops, an error occured, Payment gateway could not be found","status":False}
 