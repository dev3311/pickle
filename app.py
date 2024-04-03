from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier
import pickle



app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        in_value1 = float(request.form['input_value1'])
        in_value2 = float(request.form['input_value2'])
        in_value3 = float(request.form['input_value3'])
        in_value4 = float(request.form['input_value4'])
        selected_value = float(request.form['Dream'])
        selected_value1 = float(request.form['Torgersen'])
        selected_value2 = float(request.form['gender'])

        input_feature = [[in_value1, in_value2, in_value3, in_value4, selected_value, selected_value1, selected_value2]]

        prediction = model.predict(input_feature)
        
        output = prediction[0]

        return render_template('index.html', prediction_text = 'The Penguin is {}'.format(output))
    
    except Exception as e:
        return render_template('error.html', error=str(e))
    
if __name__ == '__main__':
    app.run()    