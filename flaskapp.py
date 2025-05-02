from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        prediction = model.predict([[hours]])[0]
        return render_template('results.html', hours=hours, prediction=round(prediction, 2))
    except:
        return "Please enter a valid number."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

