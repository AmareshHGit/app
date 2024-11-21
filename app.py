
from flask import Flask
from flask import request, jsonify



# A very simple Flask Hello World application for you to get started with

app = Flask(__name__)
#app = Flask(flask_skeleton)

@app.route('/')
def home():
    student_number = "200625943" 
    return jsonify({"student_number": student_number})

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
        req = request.get_json(silent = True, force = True)
        fulfillmentText = ''

        query_result = req.get('queryResult')
        parameters = queryResults.get('parameters', '')
        if query_result.get('action') == 'get.name':           
        fulfillmentText = "Hello "+str(parameters.get('name', ''))+", glad to meet you!!"
        return {
          "fulfillmentText": fulfillmentText,
          "source": "webhookdata"
          }
        

if __name__ == '__main__':
 
   app.run(debug=True)

