#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, abort
import os, sys, json
app = Flask(__name__) #type: Flask

@app.route('/')
def index():
    # return 'hello world'
    path = 'C:\\Users\\john\\Desktop\\shiyanlou\\tiaozhan6\\files\\'
    title_list = []
    for roots, dirs, names in os.walk(path):
        for name in names:
            filename = os.path.join(roots, name)
            # return filename
            title = read_file(filename)['title']
            title_list.append(title)
    return render_template('index.html', title_list=title_list)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/files/<filename>')
def file(filename):
    filename = 'C:\\Users\\john\\Desktop\\shiyanlou\\tiaozhan6\\files\\' + filename + '.json'
    if os.path.exists(filename):
        data = read_file(filename)
        return render_template('file.html',data=data)
    else:
        abort(404)

def read_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data











if __name__ == '__main__':
    app.run(debug=True)