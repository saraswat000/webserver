#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from releaxapi import github, team, data
import requests
import config
import requests
import json

app = Flask(__name__)
@app.route('/')
def indexApi():
    f = data.load_json("static/data/features.json")
    all_features = f.get_json()
    return render_template(
        'index.html',
        Features = all_features,
        data = config.release_data
    )

@app.route('/wiki')
def wikiApi():
    return render_template(
        'wiki.html',
        data = config.release_data
    )


@app.route('/todo')
def newsApi():
    f = data.load_json("static/data/todo.json")
    todo = f.get_json()
    return render_template(
        'todo.html',
        ToDo = todo,
    )

@app.route('/join')
def join():
    return render_template(
        'join.html'
    )

@app.route('/requestfeature')
def requestFeature():
    return render_template(
        'requestFeature.html'
    )
# Route for handling login page logic
@app.route('/login', methods = ['GET','POST'])
def login():
    err = None
    if request.method == 'POST':
        if request.form['userid'] != 'admin' or request.form['passcode'] != 'admin':
            err = 'Invalid Credentials'
        else:
            return redirect(url_for('/'))
    return render_template(
        'login.html',
         err = err,)

if __name__ == '__main__':
    app.run(debug=True)