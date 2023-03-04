from flask import Flask,render_template,request
import numpy as np
from DelhiHouseModel import give_pred

app = Flask(__name__)

@app.route("/")
@app.route("/Hello")
def home():
    return render_template("website1.html")

@app.route("/result",methods=['POST','GET'])
def result():
    outpt= request.form.to_dict()
    area=outpt["Area"]
    bhk=outpt['BHK']
    bathroom=outpt['Bathrooms']
    parking=outpt['Parking']
    typ=outpt['type']
    status=outpt['status']
    transcation=outpt['Transcation']
    Frnishing=outpt['Furnishing']
    Locality=outpt['Locality']

    test=np.array([[area,bhk,bathroom,Frnishing,Locality,parking,status,transcation,typ]])
    inwords=give_pred(test)
    return render_template("website1.html",name=inwords)

if __name__=='__main__':
    app.run(debug=True,port=5000)
 