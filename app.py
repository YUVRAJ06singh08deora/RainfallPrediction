from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    precipitation = request.form.get('precipitation')
    temp_max = request.form.get('temp_max')
    temp_min = request.form.get('temp_min')
    wind = request.form.get('wind')
    input_query = np.array([[precipitation,temp_max,temp_min,wind]])
    result = model.predict(input_query)[0]
    return jsonify({'weather':str(result)})
if __name__ == '__main__':
    app.run(debug=True)