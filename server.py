from flask import Flask, render_template

import flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def render():
    txt=""

    # with open("myfile.html") as file:
    #     txt = file.read()
    return render_template("myfile.html")

@app.route('/latest_event.png')
def latest_event():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'test.png',
                           mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)