from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

# age	gender	rest_cp	rest_bp	cholesterol	fast_bloodsugar	rest_ecg	stress_HR	Exercise_cp	STdepression_Exerc	STpeak_exerc	coloured_vessels	thalassmia	
# http:// - protocol
# 127.0.0.1:- IP address
# 5000 - port number
# / - route, when someone visits this route what to do
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["post"])
def predict():

# load the model
    model=joblib.load("modelsaved.pkl")
    
    age=request.form.get("age")
    gender=request.form.get("gender")
    rest_cp=request.form.get("rest_cp")
    rest_bp=request.form.get("rest_bp")
    cholesterol=request.form.get("cholesterol")
    fast_bloodsugar=request.form.get("fast_bloodsugar")
    rest_ecg=request.form.get("rest_ecg")
    stress_HR=request.form.get("stress_HR")
    Exercise_cp=request.form.get("Exercise_cp")
    STdepression_Exerc=request.form.get("STdepression_Exerc")
    STpeak_exerc=request.form.get("STpeak_exerc")
    coloured_vessels=request.form.get("coloured_vessels")
    thalassmia=request.form.get("thalassmia")
   
    print(age,gender,rest_cp,rest_bp,cholesterol,fast_bloodsugar,rest_ecg,stress_HR,	Exercise_cp,STdepression_Exerc,	STpeak_exerc,coloured_vessels,thalassmia)

    output=model.predict([[age,gender,rest_cp,rest_bp,cholesterol,fast_bloodsugar,rest_ecg,stress_HR,	Exercise_cp,STdepression_Exerc,	STpeak_exerc,coloured_vessels,thalassmia]])

    if output[0]==0:
        message="person has no disease"
    else:
        message="person has no disease"
    return render_template("predict.html",message=message)

if __name__=="__main__":
    app.run(debug=True)