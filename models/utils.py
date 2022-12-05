import pandas as pd 
import numpy as np 
import pickle
import json

class RainPrediction():
    def __init__(self,MinTemp,MaxTemp,Rainfall,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,
        Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,Location,WindGustDir,WindDir9am):


        self.MinTemp=MinTemp
        self.MaxTemp=MaxTemp
        self.Rainfall=Rainfall
        self.WindGustSpeed=WindGustSpeed
        self.WindSpeed9am=WindSpeed9am
        self.WindSpeed3pm=WindSpeed3pm
        self.Humidity9am=Humidity9am
        self.Humidity3pm=Humidity3pm
        self.Pressure9am=Pressure9am
        self.Pressure3pm=Pressure3pm
        self.Cloud9am=Cloud9am
        self.Cloud3pm=Cloud3pm
        self.Temp9am=Temp9am
        self.Temp3pm=Temp3pm
        self.Location="Location_"+Location
        self.WindGustDir="WindGustDir_"+WindGustDir
        self.WindDir9am="WindDir9am_"+WindDir9am

    def Load_files(self):
        with open("models/Ada_boost_hyp_model.pkl","rb")as f:
            self.Adaboost_model=pickle.load(f)

        with open("models/project_data.json","r")as f:
            self.project_data=json.load(f)

    def Prediction(self):
        self.Load_files()
        array=np.zeros(len(self.project_data["columns"]))
        index_value1=self.project_data["columns"].index(self.Location)
        index_value2=self.project_data["columns"].index(self.WindGustDir)
        index_value3=self.project_data["columns"].index(self.WindDir9am)

        array[0]=self.MinTemp
        array[1]=self.MaxTemp
        array[2]=self.Rainfall
        array[3]=self.WindGustSpeed
        array[4]=self.WindSpeed9am
        array[5]=self.WindSpeed3pm
        array[6]=self.Humidity9am
        array[7]=self.Humidity3pm
        array[8]=self.Pressure9am
        array[9]=self.Pressure3pm
        array[10]=self.Cloud9am
        array[11]=self.Cloud3pm
        array[12]=self.Temp9am
        array[13]=self.Temp3pm
        array[index_value1]=1
        array[index_value2]=1
        array[index_value3]=1

        prediction=self.Adaboost_model.predict([array])[0]

        print("Rain predixtion is",prediction)

        if prediction=="Yes":
            return "There will be rain tommorow"

        else:
            return "There will not be rain tommorow"


if __name__ == "__main__":
    MinTemp=17.013501
    MaxTemp=5.087968
    Rainfall=5.332514
    WindGustSpeed=51.779144
    WindSpeed9am=8.779144
    WindSpeed3pm=10.214711
    Humidity9am=67.889572
    Humidity3pm=92.889572
    Pressure9am=1010.307970
    Pressure3pm=1008.308585
    Cloud9am=6.376685
    Cloud3pm=7.977914
    Temp9am=21.525773
    Temp3pm=19.836201
    Location="Albury"
    WindGustDir="ESE"
    WindDir9am="SW"

    Rain_pred=RainPrediction(MinTemp,MaxTemp,Rainfall,Rainfall,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,
    Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Temp9am,Temp3pm,Location,WindGustDir,WindDir9am)
    Rain_status=Rain_pred.Prediction()
    print("rain status",Rain_status)







        
