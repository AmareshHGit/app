
from flask import Flask
from flask import request



# A very simple Flask Hello World application for you to get started with

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
        req = request.get_json(silent = True, force = True)
        fulfillmentText = ''

        query_result = req.get('queryResult')
        if query_result.get('action') == 'get.address':
            
        fulfillmentText = "Hi"
        return 'Hello'
        

if __name__ == '__main__':
 
   app.run()
