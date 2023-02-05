import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import os 
from PIL import Image

IMG_PATH = os.path.join(os.getcwd(), 'Images', 'Items', '')
ITEMS_TRAINER_PATH = os.path.join(os.getcwd(), 'Trainer', '')

def train_items_model(confidence = 0.91):
    """
    Description
    -----------
    Train and save a neural network fully dense model that recognizes all the items in League of Legends.
    The items are represented as a 40x40 image as it is in a screenshot in 1920x1080. At the moment, the
    confidence of the model is at least 91%.

    Parameters
    ----------
    confidence : float
        Model confidence in recognizing the images. The training dataset is the same as the testing one.

    """

    x_data = []

    images_list_names = []

    for img_name in [i for i in os.listdir(IMG_PATH) if i.endswith('.png')]:

        img = np.array(Image.open(os.path.join(IMG_PATH, img_name)).convert('L'))/255.
        img = img.astype('float32')

        if img.shape[0] == 40 and img.shape[1] == 40:      
            x_data.append(img)
            images_list_names.append(img_name)
            
    x_data = np.array(x_data)

    n = x_data[0].shape[0]
    N = len(images_list_names)

    # Define labels and use the one-hot encoder. To be used with categorical_crossentropy loss function.
    # This loss function is used to classify data in mutually exclusive classes.
    y_data = np.array([i for i in range(N)])
    y_data = tf.keras.utils.to_categorical(y_data)

    # This is to re-order the data: at the moment I want to overfit the data, so I use the same dataset for both
    # training and testing. Good? No, but it worked and I don't have time to take thousands of screenshots.
    x_train = x_data
    y_train = y_data
    x_test = x_data
    y_test = y_data

    del x_data, y_data

    # Use dense neural network as model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(n, n)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(N, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model (to plot the behavior declare this in history), and save it once
    # the required accuracy is reached
    _, test_acc = model.evaluate(x_test, y_test, verbose=0)
    epo = 1

    while test_acc<confidence:
        model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))
        _, test_acc = model.evaluate(x_test, y_test, verbose=0)
        epo+=1

    model.save(os.path.join(ITEMS_TRAINER_PATH, f'item_recognition_{epo}epochs.h5'))
