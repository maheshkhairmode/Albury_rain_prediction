from distutils.command.config import config
from models.utils import RainPrediction
from flask import Flask,jsonify,render_template,request
import config

app=Flask(__name__)
@app.route("/")
def Flask():
    return render_template("index.html")

@app.route("/rain_predict",methods=["POST","GET"])
def rain_prediction():
     if request.method=="POST":

        MinTemp=float(request.form.get("MinTemp"))
        MaxTemp=float(request.form.get("MaxTemp"))
        Rainfall=float(request.form.get("Rainfall"))
        WindGustSpeed=float(request.form.get("WindGustSpeed"))
        WindSpeed9am=float(request.form.get("WindSpeed9am"))
        WindSpeed3pm=float(request.form.get("WindSpeed3pm"))
        Humidity9am=float(request.form.get("Humidity9am"))
        Humidity3pm=float(request.form.get("Humidity3pm"))
        Pressure9am=float(request.form.get("Pressure9am"))
        Pressure3pm=float(request.form.get("Pressure3pm"))
        Cloud9am=float(request.form.get("Cloud9am"))
        Cloud3pm=float(request.form.get("Cloud3pm"))
        Temp9am=float(request.form.get("Temp9am"))
        Temp3pm=float(request.form.get("Temp3pm"))
        Location=request.form.get("Location")
        WindGustDir=request.form.get("WindGustDir")
        WindDir9am=request.form.get("WindDir9am")

        Rain_pred=RainPrediction(MinTemp,MaxTemp,Rainfall,Rainfall,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,
        Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Temp9am,Temp3pm,Location,WindGustDir,WindDir9am)
        Rain_status=Rain_pred.Prediction()
        print("rain status",Rain_status)

        return render_template("index.html",prediction=Rain_status)

if __name__=="__main__":

    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)


