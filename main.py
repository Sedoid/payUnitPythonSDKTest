# from payUnit import payUnit
import payUnit_

from flask import Flask,render_template,request
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 

app = Flask(__name__) 

payment = payUnit_.payUnit({
    "user_api": "payunit_TLYswhcCJ",
    "password_api": "0dc757b3-0abe-4b59-8523-e10d6f085897",
    "api_key": "d97fe9e7de10b042bc01d26241a4fcd7f972cc85",
    "return_url": "http://127.0.0.1:5000/thanks"
})

# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/',methods=['GET','POST']) 
def hello_world(): 
    if(request.method == "POST"):
        amount = request.form['amount']
        result = payment.makePayment(request.form['amount'])
        print(result)
    return render_template('index.html')

@app.route('/thanks',methods=['GET'])
def welcome():
    return render_template('thanks.html')



# main driver function 
if __name__ == '__main__': 
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run() 
