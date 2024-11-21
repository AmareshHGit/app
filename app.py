
from flask import Flask
from flask import request



# A very simple Flask Hello World application for you to get started with

app = Flask(__name__)
#app = Flask(flask_skeleton)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
        req = request.get_json(silent = True, force = True)
        fulfillmentText = ''

        query_result = req.get('queryResult')
        parameters = queryResults.get('parameters', '')
#        if query_result.get('action') == 'get.address':           
        fulfillmentText = "Hello "+str(parameters.get('name', ''))+", glad to meet you!!"
        return {
          "fulfillmentText": fulfillmentText,
          "source": "webhookdata"
          }
        

if __name__ == '__main__':
 
   app.run()

def webhook():
    if request.method == 'POST':
        req = request.get_json(silent = True, force = True)

        queryResults = req.get('queryResult')
        parameters = queryResults.get('parameters', '')
        speech = "Hello "+str(parameters.get('name', ''))+", glad to meet you!!"
        response = {
            'fulfillmentText': speech
        }
        res = json.dumps(response, indent = 4)
        r = make_response(res)
        r.headers["Content-Type"] = "application/json"
        return r