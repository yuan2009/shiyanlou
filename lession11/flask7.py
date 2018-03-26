#!/usr/bin/env python3
from flask import Flask, render_template, abort
app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route('/user/<username>')
def user_index(username):
	if username == 'invalid':
		abort(404)
	return render_template('user_index.html', username=username)


if __name__ == '__main__':
	app.run()