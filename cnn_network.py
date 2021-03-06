#!/usr/bin python
import numpy as np 
from matplotlib import pyplot as plt
from keras.utils.np_utils import to_categorical 
from keras.models import Sequential 
from keras.layers.core import Dense, Dropout, Flatten 
from keras.layers import Conv2D, MaxPooling2D


## Import data
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

rows, cols = X_train[0].shape[0], X_train[0].shape[1] 
X_train = X_train.reshape(X_train.shape[0], rows, cols, 1) 
X_test = X_test.reshape(X_test.shape[0], rows, cols, 1) 

X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

num_of_classes = len(set(y_train)) 
y_train = to_categorical(y_train, num_of_classes) 
y_test = to_categorical(y_test, num_of_classes) 


# Model Creation 
model = Sequential() 

#model.add(Conv2D(32, kernel_size=(3, 3), activation='rectifier', input_shape=(rows, cols, 1)))
#model.add(Conv2D(64, kernel_size=(3, 3), activation='rectifier')) 
#model.add(Conv2D(128, kernel_size=(3, 3), activation='rectifier')) 

model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', input_shape=(rows, cols, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='linear')) 
model.add(Conv2D(128, kernel_size=(3, 3), activation='linear')) 

model.add(Dropout(0.5)) 

model.add(MaxPooling2D(pool_size = (2, 2)))


model.add(Flatten())

model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.5)) 
model.add(Dense(num_of_classes, activation='softmax'))

model.compile(loss= 'categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 


from keras.layers.advanced_activations import LeakyReLU

model.add(Conv2D(32, kernel_size=(3, 3), activation='linear',input_shape=(rows, cols, 1)))
model.add(LeakyReLU(alpha=0.1))



# Training
model.fit(X_train, y_train, batch_size=128, epochs=20, verbose=1, validation_split=0.2) 

score = model.evaluate(X_test, y_test, verbose=0) 

print('Accuracy:', score[1])


# Prediction
predictions = model.predict(X_test)


# Results
plt.figure(figsize=(15, 15)) 
for i in range(10):    
    ax = plt.subplot(2, 10, i + 1)    
    plt.imshow(X_test[i, :, :, 0], cmap='gray')    
    plt.title("Digit: {}\nPredicted:    {}".format(np.argmax(y_test[i]), np.argmax(predictions[i])))    
    plt.axis('off') 
plt.show()