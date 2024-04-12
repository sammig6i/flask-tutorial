import os
from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def index():
  return redirect(url_for('login'))

@app.route('/login')
def login():
  abort(404)




with app.test_request_context():
  print(url_for('index'))
  print(url_for('login'))




 


