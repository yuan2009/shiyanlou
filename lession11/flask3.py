#!/usr/bin/env python3
from flask import render_template, redirect, url_for, Flask, request

app = Flask(__name__)

@app.route('/<username>')
def index(username):
	return redirect(url_for('user_index', username=username))

@app.route('/user/<username>')
def user_index(username):
	req = request.headers.get('User-Agent')
	page = request.args.get('page')
	per_page = request.args.get('per_page')
	return render_template('user_index.html', username=username, req=req, page=page, per_page=per_page)
	

if __name__ == '__main__':
	app.run()