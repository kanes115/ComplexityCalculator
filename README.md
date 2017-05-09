# Complexity Calculator
This is a module that takes care of calculating time complexity of algorithm given by a function passed to constructor of ComplexityCalc class and its input data. Input data must implement ArgData interface (inherit from it in fact). If confused, take a look at example of implementation of input data provided in ArgData.py file (for list input).

## Example of working
It works like this (NlogN example):
    
    t(N) = c * N*log(N), c is a constance, we divide both sides by Nlog(N)
    
    t(N) / NlogN = c
    
We get c for each measure. If the complexity is NlogN, all the c should be almost the same, so using count_errors() we calculate variance of these consts for each complexity (among all measures) and check for which complexity we get the smalles variance. This our complexity!

## Usage
1) Implement input data class which will contain input data to your tested function. It must provide for example increasing the data size (adding some random data) or setting size of a problem for a certain amount.
2) Create ComplexityCalc object, pass tested function and input data to its constructor.
3) Use ComplexityCalc.calculate_complexity() method to get complexity as a string.
4) Additionally you can get functions allowing you to forecast the time it will take tested function to procces input data of size N and max size input data can have so that tested function will end up calculating before a specified time. Use ComplexityCalc.get_timeforecaster() and ComplexityCalc.get_sizeforecaster() respectively.

## Installation
Type in a command line
`pip3 install performance_control`

visit our pypi page:
[link](https://pypi.python.org/pypi?:action=display&name=performance_control&version=0.2)
    
