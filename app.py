# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:02:08 2020

@author: ss727
"""

# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
import bookreco

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method=='POST':
        try:
            book=request.form['book']
            res=bookreco.recommend3(book)
            
            return render_template('results.html',result=res)
        except Exception as e:
            print('The Exception message is:',e)
            return 'something is wrong'
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8000, debug=True)
	app.run(debug=True) # running the app