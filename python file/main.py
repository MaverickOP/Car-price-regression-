import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


with open('LinearRRegressionModell.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        car_model = request.form["model"]  
        year = int(request.form['year'])
        transmission = request.form['transmission']
        total_driven = float(request.form['total_driven'])
        fuelType = request.form['fuelType']
        tax = float(request.form['tax(£)'])  
        mpg = float(request.form['mpg'])
        engineSize = float(request.form['engineSize'])

   
        input_data = pd.DataFrame({
            'model': [car_model],
            'year': [year],
            'transmission': [transmission],
            'total_driven': [total_driven],
            'fuelType': [fuelType],
            'tax(£)': [tax],  
            'mpg': [mpg],
            'engineSize': [engineSize]
        })

        
        print("Input Data:")
        print(input_data)

       
        prediction = model.predict(input_data)

       
        print("Prediction:")
        print(prediction)

        return render_template('index.html', prediction=f"Predicted Price: £{prediction[0]:.2f}")

    
    return render_template('index.html', prediction="")

if __name__ == "__main__":
    app.run(debug=True)
