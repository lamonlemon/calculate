from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_expression(expression):
    try:
        expression = expression.replace('π', str(math.pi)).replace('e', str(math.e))
        if '!' in expression:
            num = int(expression[:-1])
            result = math.factorial(num)
        elif '√' in expression:
            num = float(expression[1:])
            result = math.sqrt(num)
        elif '^' in expression:
            base, exp = map(float, expression.split('^'))
            result = base ** exp
        else:
            result = eval(expression)
        return str(int(result)) if result == int(result) else str(result)
    except Exception as e:
        return "Error"

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = calculate_expression(expression)
    return render_template('calculator.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
