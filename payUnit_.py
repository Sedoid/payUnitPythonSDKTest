import json
import uuid
import base64
import requests
import webbrowser

class payUnit():
    """
    Initiates and processes payments
    """
    def __init__(self,data):      
        self.config_data = data

    def makePayment(self,amount): 
        user_api = str(self.config_data["user_api"])
        password_api = str(self.config_data["password_api"])
        api_key = str(self.config_data["api_key"])
        return_url = str(self.config_data["return_url"])
        auth = user_api+':'+ password_api
        base64AuthData = base64.b64encode((auth).encode()).decode()

        # url = "http://192.168.100.70:7500/payments/gateway/initialize"
        test_url = "http://192.168.100.70:5000/api/gateway/initialize"

        headers = {
            "Authorization": 'Basic '+str(base64AuthData),
            "x-api-key": str(api_key),
            "content-type": "application/json"
        }
        # body = {
        #     "transactionId" : str(uuid.uuid1()),
        #     "description" : f'A Sample Description',
        #     "amount": "4000",
        #     "returnUrl": str(return_url),
        # } 
        test_body = {
            "bills": [
                {
                    "amount": amount,
                    "bill_ref": 360582888
                }
            ],
            "transaction_id": str(uuid.uuid1()),
            "total_amount": amount,
            "return_url": "https://sturep.herokuapp.com"
        }
        try:
            response = requests.post(test_url, data =json.dumps(test_body),headers = headers)
            response = response.json()
            if(response['status'] == 200):
                webbrowser.open(response['transaction_url'])
        except:
            return("Oops, an error occured, Payment gateway could not be found")
