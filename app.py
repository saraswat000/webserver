#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from releaxapi import github, team, features
import requests
import config
import requests
import json

app = Flask(__name__)
@app.route('/')
def indexApi():
    f = features.load_features("static/data/features.json")
    all_features = f.get_features()
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

@app.route('/team')
def teamApi():
    t = team.loadTeam("static/data/team.json")
    releax_team = t.getTeam()
    return render_template(
        'team.html',
        ReleaxTeam = releax_team
    )


@app.route('/news')
def newsApi():
    g = github.github('itsmanjeet')
    repos = g.__user_commits__()
    return render_template(
        'news.html',
        repos = repos,
    )

@app.route('/join')
def join():
    return render_template(
        'join.html'
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