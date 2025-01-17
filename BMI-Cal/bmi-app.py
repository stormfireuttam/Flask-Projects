from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    error = None
    
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))

            if weight > 0 and height > 0:
                bmi = round(weight / (height ** 2), 2)
                if bmi < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal weight"
                elif 25 <= bmi < 29.9:
                    category = "Overweight"
                else:
                    category = "Obesity"
            else:
                error = "Weight and height must be positive numbers."
        except ValueError:
            error = "Invalid input. Please enter numeric values."

    return render_template('bmi_calculator.html', bmi=bmi, category=category, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
