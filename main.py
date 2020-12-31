import payUnit_
from flask import Flask,render_template,request
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 

app = Flask(__name__) 

payment = payUnit_.payUnit({
    
    "user_api":'payunit_sand_Jsyd8u75t',
    "password_api":'1789ca10-f3cb-4254-bee5-02533973a123',
    "api_key":'c7576818c469e5d2c85bc8d4b1390004e1ebd1e6',
    "return_url": "http://127.0.0.1:5000/thanks",
    "notify_url":"http://192.168.100.10/seven-payunit-sandbox/sandbox/notify",
    "mode": "live",
})


@app.route('/', methods=['GET','POST']) 
def hello_world(): 
    if(request.method == "POST"):
        amount = request.form['amount']
        result = payment.makePayment(request.form['amount'])
        print(result)
    return render_template('index.html')

@app.route('/thanks', methods = ['GET'])
def welcome():
    return render_template('thanks.html')

@app.route('/notify', methods = ['POST'])
def notify():
    if(request.method == "POST"):
        print('******** heraders **********')
        print(request.headers)
        print('******** body **********')
        print(request.data)
        print('A post request format arrived')
        print(request.data)
    return render_template('thanks.html')


# main driver function 
if __name__ == '__main__': 
    app.run() 
