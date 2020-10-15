from flask import Flask, request
from flask_cors import CORS, cross_origin
import joblib
import os
app = Flask(__name__)
CORS(app)
 
@app.route('/')
def helloworld():
    return 'Helloworld'
 
@app.route('/area')
@cross_origin()
def area():
    w = float(request.values['w'])
    h = float(request.values['h'])
    return str(w * h)

@app.route('/bmi', methods=['GET'])
@cross_origin()
def bmi():
    weight = float(request.values['w'])
    height = float(request.values['h'])
    return str(weight/(height/100)**2)

@app.route('/iris', methods=['POST'])
@cross_origin()
def iris():
    '''
    sl = sepal length (cm)
    sw = sepal width (cm)
    pl = petal length (cm)
    pw = petal width (cm)
    result : ['setosa', 'versicolor', 'virginica']
    '''
    result = request.get_json(force=True)
    sl = float(result['sl'])
    sw = float(result['sw'])
    pl = float(result['pl'])
    pw = float(result['pw'])
    model = joblib.load('iris.model')
    l = [sl,sw,pl,pw]
    pred = model.predict([l])
    keys_list =  ['setosa', 'versicolor', 'virginica']
    return str(l) +' : '+ str(keys_list[int(pred[0])])

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)