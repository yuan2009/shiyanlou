from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route('/')
# def index():
#     return redirect(url_for('req'), username='default')
# @app.route('/user/<username>')
def req():
    agent = request.headers.get('User-agent')
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    return render_template('user_index.html', agent=agent, page=page, per_page=per_page)


if __name__ == '__main__':
    app.run()