import numpy as numpy
import keras.models
from keras.models import model_from_json
from imageio import imread as imread
from scipy.misc import imshow as imshow
from skimage.transform import resize as imresize
import tensorflow as tf
from keras.optimizers import RMSprop

#USED TO PREPARE THE DEFAULT GRAPH .

def init():
    json_file = open('model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    print("Loaded from disk")
    optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    loaded_model.compile(loss = 'categorical_crossentropy', optimizer = optimizer, metrics = ['accuracy'])
    graph = tf.get_default_graph()

    return loaded_model, graph