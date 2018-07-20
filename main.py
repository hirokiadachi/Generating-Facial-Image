import sys
sys.path.append('/Library/Python/2.7/site-packages')
sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')

from PIL import Image
from network import Generator
from flask import Flask, render_template, redirect, request

import numpy as np
import chainer
import utils
import os


app = Flask(__name__)

def make_attr(vals):
    if 'm' in vals:
        m = 1
    else:
        m = 0
    if 'bh' in vals:
        bh = 1
    else:
        bh = 0
    if 'e' in vals:
        e = 1
    else:
        e = 0
    if 'nb' in vals:
        nb = 1
    else:
        nb = 0
    if 's' in vals:
        s = 1
    else:
        s = 0
    attr = np.asarray([m, bh, e, nb, s], dtype=np.float32)
    ind = np.where(attr > 0)
    return attr, ind[0]

def attr_name(index):
    attr = {0: 'Male', 1: 'Blond Hair', 2: 'Eyeglasses',
            3: 'No Beard', 4: 'Smiling'}
    return [attr[i] for i in index]

def save_image(img, filename):
    img = np.transpose(img, (1,2,0))
    img = img * 256
    img = (img.data).astype(np.int32)
    img[img<0] = 0
    img[img>=256] = 255
    img = np.uint8(img)
    img = Image.fromarray(img)
    img.save(filename)

def generate_image(attr):
    attr = np.reshape(attr, (1, 5, 1, 1))
    gen = Generator(6)
    chainer.serializers.load_npz('./results/gen', gen)
    
    z = gen.z(1)
    z = chainer.Variable(z)
    img = gen(z, attr, alpha=1.0)

    path = 'static/image'
    if not os.path.exists(path):
        os.makedirs(path)
    
    rand = np.random.randint(0, 100000)
    for im in img:
        filename = os.path.join(path, 'fake{}.jpg'.format(rand))
        save_image(im, filename)
    return filename

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/generate', methods=['GET'])
def generate():
    res = request.args.get('g')
    vals = request.args.getlist('attr')
    attr, ind = make_attr(vals=vals)
    attribute_name = attr_name(ind)
    filename = generate_image(attr=attr)
    html = render_template('index.html', img_url=filename,
                           attr_name=attribute_name)
        
    return html

if __name__ == "__main__":
    app.run()
