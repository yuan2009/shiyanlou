#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELAOD'] = True
app.config['DEBUG'] = True

@app.route('/')
def index():
    teacher = {
        'name': 'yuan',
        'age': 18
    }
    courser = {
        'name': 'python',
        'teachder': 'xiao',
        'score': 100
    }
    return render_template('index.html', courser=courser)

if __name__ == '__main__':
    app.run()