from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('home', __name__)

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('home.home'))