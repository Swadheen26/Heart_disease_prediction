import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from Heart_Data.utils import HeartPatient

app = Flask(__name__)

############################# BASE API ##############################

@ app.route('/')
def Hello_flask():
  print("Welcome in flask")
  return 'I will definitely be a Data Scientist'

@ app.route('/predict',methods = ['POST','GET'])
def get_predicted_patient():

    data = request.form
    age = eval(data['age'])
    sex = eval(data['sex'])
    cp = eval(data['cp'])
    trestbps = eval(data['trestbps'])
    chol = eval(data['chol'])
    fbs = eval(data['fbs'])
    restecg = eval(data['restecg'])
    thalach = eval(data['thalach'])
    exang = eval(data['exang'])
    oldpeak = eval(data['oldpeak'])
    slope = eval(data['slope'])
    ca = eval(data['ca'])
    thal = eval(data['thal'])



    print("age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal",age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

    heart = HeartPatient(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    prediction = heart.get_predicted_patient()

    return jsonify({"Result":f"Predicted Patient of Heart : {prediction}"})


if __name__ == "__main__":
  app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)
