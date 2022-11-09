
import os
import json

from flask import Flask, request, render_template

import util

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/unpack/", methods=['POST'])
def unpack():
    if not request.json:
        return
    source = request.json['source']
    with open('input.php', 'w') as f:
        f.write(source)
    res = util.unpack('input.php')
    os.remove('input.php')
    return res

@app.route("/pack/", methods=['POST'])
def pack():
    if not request.json:
        return
    source = request.json['source']
    translated_texts = json.loads(request.json['translated_texts'])
    with open('input.php', 'w') as f:
        f.write(source)
    res = {"res": util.pack('input.php', translated_texts)}
    os.remove('input.php')
    return res
