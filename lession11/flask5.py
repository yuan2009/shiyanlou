#!/usr/bin/env python3
from flask import Flask, make_response, render_template, request
app = Flask(__name__)
@app.route('/user/<username>')
def user_index(username):
	resp = make_response(render_template('user_index.html', username=username))
	resp.set_cookie('username', username)
	return resp

@app.route('/')
def index():
	username = request.cookies.get('username')
	return 'Hello {}'.format(username)

if __name__ == '__main__':
	app.run()