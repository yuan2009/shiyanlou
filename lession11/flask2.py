#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
	# return 'hello {}'.format(username)

	return render_template('user_index.html', username=username)
def index(username):
	return username



# @app.route('/post/<int: post_id>')
# def show_post(post_id):
# 	return 'Post {}'.format(post_id)


@app.route('/')
def index():
    return redirect(url_for('user_index', username='default'))



if __name__ == '__main__':
	app.run()