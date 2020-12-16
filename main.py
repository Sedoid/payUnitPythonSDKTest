import payUnit
from flask import Flask,render_template,request
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 

app = Flask(__name__) 

payment = payUnit.payUnit({
    "user_api": "payunit_FNn3tfr1B",
    "password_api": "bce66460-9c08-49be-af72-004bcc15e8df",
    "api_key": "4ab167344898c11faf309957c1d27770e47f372d",
    "return_url": "http://127.0.0.1:5000/thanks"
})


@app.route('/', methods=['GET','POST']) 
def hello_world(): 
    if(request.method == "POST"):
        amount = request.form['amount']
        result = payment.makePayment(request.form['amount'])
        print(result)
    return render_template('index.html')

@app.route('/thanks', methods=['GET'])
def welcome():
    return render_template('thanks.html')


# main driver function 
if __name__ == '__main__': 
    app.run() 
