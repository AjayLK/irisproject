

from flask import Flask, jsonify, render_template, request
from iris_model.utils import IrisDataset
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")

@app.route('/species_prediction',methods = ['GET','POST'])
def get_species_predicted():
    if request.method == 'GET':
        print('we are using GET method')
    
        data = request.form
        print("Data-->",data)

        SepalLengthCm = eval(request.args.get('SepalLengthCm'))
        SepalWidthCm = eval(request.args.get('SepalWidthCm'))
        PetalLengthCm = eval(request.args.get('PetalLengthCm'))
        PetalWidthCm = eval(request.args.get('PetalWidthCm'))
        
        id = IrisDataset(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
        species = id.get_predicted_species()
        return render_template("index.html",prediction = f"The predicted species is {species}")

        # return jsonify({'Result':f"The predicted species is {species} "})

    else: 
        print('we are using POST method')
    
        data = request.form
        print("Data-->",data)

        SepalLengthCm = eval(request.form.get('SepalLengthCm'))
        SepalWidthCm = eval(request.form.get('SepalWidthCm'))
        PetalLengthCm = eval(request.form.get('PetalLengthCm'))
        PetalWidthCm = eval(request.form.get('PetalWidthCm'))
        
        id = IrisDataset(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
        species = id.get_predicted_species()
        return render_template("index.html",prediction = f"The predicted species is {species}")

    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = True)