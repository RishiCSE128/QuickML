from crypt import methods
from webapp import create_app
import json
from flask import Flask, render_template, request


app = create_app()

if __name__ == '__main__':
    # Turn off when running in production
    app.run(debug=True, port = 5005)



