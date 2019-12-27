from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)+Fraction(value2)
    return '%s \n' % result

@app.route('/subtraction')
def subtraction():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)-Fraction(value2)
    return '%s \n' % result

if __name__ == "__main__":
    app.run()
