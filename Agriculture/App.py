import joblib
import pickle
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

model = pickle.load(open('classifier.pkl','rb'))
ferti = pickle.load(open('fertilizer.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop')
def recomendation():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index_1.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        joblib.load('G:\\Final_year\\Crop-Recommendation-system--main\\Crop-Recommendation-system--main\\Crop recommendation system\\crop_app\\crop_prediction','r')
        model = joblib.load(open('G:\\Final_year\\Crop-Recommendation-system--main\\Crop-Recommendation-system--main\\Crop recommendation system\\crop_app\\crop_prediction','rb'))
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"


@app.route('/fert')
def welcome():
    return render_template('fertilizer.html')

@app.route('/prediction',methods=['POST'])
def predict():
    temp = request.form.get('temp')
    humi = request.form.get('humid')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    input = [int(temp),int(humi),int(mois),int(soil),int(crop),int(nitro),int(pota),int(phosp)]

    res = ferti.classes_[model.predict([input])]

    return render_template('fprediction.html',x = ('Predicted Fertilizer is {}'.format(res)))


if __name__ == '__main__':
    app.run(debug=True)















