"""Loading dataset"""

import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2
import pickle
from tqdm import tqdm
import random
import numpy as np
DATA_DIR = "D:\kagglecatsanddogs_3367a\PetImages"
CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATA_DIR, category)  # create path to dogs and cats
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_array = cv2.imread(os.path.join(path, img),
                               cv2.IMREAD_GRAYSCALE)  # convert to array
        # plt.imshow(img_array, cmap='gray')  # graph it
        # plt.show()  # display!
        break
    break


IMG_SIZE = 100
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
# plt.imshow(new_array, cmap='gray')  # graph it
# plt.show()  # display!


training_data = []


def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATA_DIR, category)
        # get the classification  (0 or a 1). 0=dog 1=cat
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(
                    path, img), cv2.IMREAD_GRAYSCALE)  # convert to array
                # resize to normalize data size
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                # add this to our training_data
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()

# print(len(training_data))

random.shuffle(training_data)

# Build the model
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

#print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# Save the data
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
