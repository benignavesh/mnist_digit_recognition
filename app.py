from flask import Flask, render_template, request
#from scipy.misc import imshow as imshow
#from scipy.misc import imread
#from imageio import imread
#from imageio import imwrite as imsave
#from skimage.transform import resize as imresize
from PIL import Image
import PIL.ImageOps # to invert the image
import numpy as np
import keras
import re
import sys
import os
sys.path.append(os.path.abspath('./model'))
from load import *
import base64


# Initialize flask app

app = Flask(__name__)

global model, graph
model,graph = init() # from load package

def convertImage(imgData1):
    imgData1 = imgData1.decode('utf-8')
    imgstr = re.search(r'base64,(.*)',imgData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route('/') #if the user is in the main page, serve them the index.
def index():
    return render_template('index.html')
    
@app.route('/predict', methods =['GET', 'POST'])
def predict():
    imgData = request.get_data() # raw serialized data, needs reshaping so that it's fit for the model
    convertImage(imgData)
    im = Image.open('output.png').convert("L") # returns image object
    #out_img = imread('output.png')
    #im = PIL.ImageOps.invert(im) 
    #out_img = np.invert(out_img)
    im = im.resize((28,28))
    #out_img = imresize(out_img, (28,28))
    im = np.reshape(im, (1,28,28,1))
    #out_img = out_img.reshape(1,    28,28,1)

    with graph.as_default():
        out = model.predict(im)
        print(out)
        print(np.argmax(out, axis=1))
        response = np.array_str(np.argmax(out, axis = 1))
        return response
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '127.0.0.1', port = port)

