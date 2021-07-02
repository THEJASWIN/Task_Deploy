from flask import Flask
from flask import request
import numpy as np
import pickle

app = Flask(__name__)
filename = "model.pkl"
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/')
def main_page():
    return"Hello World"

@app.route('/prediction' ,methods= ['POST','GET'])
def score():
    Hours= float(request.args.get('Hours'))
    print(request)
    result= loaded_model.predict([[Hours]])
    return str(result)

if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)
   app.run(debug=True)