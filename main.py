from flask import Flask, request
from fractions import Fraction
import pytest

app = Flask(__name__)


@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

@app.route('/')
def index():
    return 'Usage;\n /Operation?A=<Value1>&B=<Value2>; available operations: add,subtraction,multiplication,division \n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)+Fraction(value2)
    return '%s \n' % result
    #unit test case for add
def test_addition_function(client):
    response = client.get('/add?A=4/5&B=2/4')
    assert b'13/10' in response.data

@app.route('/subtraction')
def subtraction():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)-Fraction(value2)
    return '%s \n' % result
    #unit test case for subtract 
def test_subtract_function(client):
    response = client.get('/subtraction?A=4/5&B=2/4')
    assert b'3/10' in response.data

@app.route('/multiplication')
def multiplication():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)*Fraction(value2)
    return '%s \n' % result
    #unit test case for multiplication
def test_multiplication_function(client):
    response = client.get('/multiplication?A=4/5&B=2/4')
    assert b'2/5' in response.data
   
@app.route('/division')
def division():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)/Fraction(value2)
    return '%s \n' % result
    #unit test case for division
def test_division_function(client):
    response = client.get('/division?A=4/5&B=2/4')
    assert b'8/5' in response.data

if __name__ == "__main__":
    app.run()
