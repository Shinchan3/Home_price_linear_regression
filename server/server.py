from flask import Flask, request,jsonify
import util
from flask_cors import CORS 
app= Flask(__name__)
CORS(app)
@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'location': util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return  response
@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():   
    toal_sqft=float(request.form['total_sqft'])
    bhk=int(request.form['bhk'])
    balcony=int(3)
    bath=int(request.form['bath'])
    location=request.form['location']
    response=jsonify({
        'estimated_price':util.estimated_price(location,toal_sqft,bhk,bath,balcony)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("staring the server")
    util.get_location()
    app.run()