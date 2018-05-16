#!/usr/bin/env python3
from flask import Flask, request, make_response, render_template
app = Flask(__name__)
@app.route('/user/<username>')

def user_index(username):
    resp = make_response(render_template('user_index.html'), username)
    resp.set_cookie('username', username)
    return resp

@app.route('/resp')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

if __name__ == '__main__':
    app.run(debug=True)