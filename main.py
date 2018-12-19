import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

from mlcode import apply_model_to_image

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files.get('file')
        if f is None:
        	return "No Image Uploaded!!!"
        f.save('./static/'+secure_filename(f.filename))
        fname = './static/'+secure_filename(f.filename)
        caption = apply_model_to_image(fname).capitalize()
        return render_template("main.html", after=True, caption=caption, imgname=secure_filename(f.filename))
    return render_template("main.html", after=False)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1,firefox=1'
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


