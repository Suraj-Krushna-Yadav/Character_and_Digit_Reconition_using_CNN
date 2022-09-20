# from re import A
# from unittest import result
from flask import Flask
from flask import render_template
import numpy as np
import keras
from tkinter import *
import cv2

app = Flask(__name__)

@app.route('/')
def entry_point():
    res=""
    return render_template('Index.html',result=res)


if __name__ == '__main__':
    app.run(debug=True) 