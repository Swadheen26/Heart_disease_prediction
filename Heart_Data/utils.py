import json
import pickle
import config
import numpy as np

class HeartPatient():
  def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    
    self.age = age
    self.sex = sex
    self.cp = cp
    self.trestbps = trestbps
    self.chol = chol
    self.fbs = fbs
    self.restecg = restecg
    self.thalach = thalach
    self.exang = exang
    self.oldpeak = oldpeak
    self.slope = slope
    self.ca = ca
    self.thal = thal


  def load_model(self):
    with open(config.MODEL_FILE_PATH,'rb') as f:
      self.model = pickle.load(f)

    with open(config.JSON_FILE_PATH,'r')as f:
      self.json_data = json.load(f)

  def get_predicted_patient(self):
    self.load_model()
    print("*"*30,self.json_data)

    test_array = np.zeros(len(self.json_data['columns']))
    test_array[0] = self.age
    test_array[1] = self.sex
    test_array[2] = self.cp
    test_array[3] = self.trestbps
    test_array[4] = self.chol
    test_array[5] = self.fbs
    test_array[6] = self.restecg
    test_array[7] = self.thalach
    test_array[8] = self.exang
    test_array[9] = self.oldpeak
    test_array[10] = self.slope
    test_array[11] = self.ca
    test_array[12] = self.thal

    predicted = self.model.predict([[test_array]][0])
    return predicted

if __name__ == "__main__":
  age=41
  sex=0
  cp=1
  trestbps=130
  chol=204
  fbs=0
  restecg=0
  thalach=172
  exang=0
  oldpeak=1.4
  slope=2
  ca=0
  thal=2

  heart_pred = HeartPatient(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
  heart_pred.get_predicted_patient()