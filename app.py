from crypt import methods
from webapp import create_app
import json
from flask import Flask, render_template, request
import pandas as pd


app = create_app() 

if __name__ == '__main__':
    # Set fo False when running in production
    app.run(debug=True, port = 5006)

