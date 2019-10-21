#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from releaxapi import github
import requests
import config
import requests
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template(
        'index.html',
        data = config.release_data
    )

@app.route('/wiki')
def wiki():
    return render_template(
        'wiki.html',
        data = config.release_data
    )

@app.route('/team')
def team():
    return render_template(
        'team.html',
        data = config.release_data
    )

'''
@app.route('/news')
def news():
    g = github.github('releax')
    reposdata = {}
    for repo in g.get_repos():
        reposdata[repo['name']] = g.get_commits(repo['name'])

    return render_template(
        'news.html',
        title = 'news',
        heading = 'releax news',
        subheading = 'things going on here',
        repos = reposdata,
    )
'''
# Route for handling login page logic
@app.route('/login', methods = ['GET','POST'])
def login():
    err = None
    if request.method == 'POST':
        if request.form['userid'] != 'admin' or request.form['passcode'] != 'admin':
            err = 'Invalid Credentials'
        else:
            return redirect(url_for('dashboard'))
    return render_template(
        'login.html',
         err = err,
         title = 'login',
         heading = 'releax Home',
         subheading = 'Login to your account')

if __name__ == '__main__':
    app.run(debug=True)