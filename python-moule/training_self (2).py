
#Step 1: Import necessary libraries
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense , Dropout
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

#Step 2: Initialising CNN and adding a convolutional layer
model=Sequential()
model.add(Convolution2D(filters=32, kernel_size=3, padding="same", activation="relu", input_shape=(200, 200, 1)))

#Step 3: Pooling Operation (Maxpooling)
model.add(MaxPooling2D(pool_size=2))

model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

#Step 4: Flattening the layers
model.add(Flatten())

#Step 5: Adding Dense Layers
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=96, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=29, activation='softmax'))

#Step 6: Compiling the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

from google.colab import drive
drive.mount('/content/drive')

train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split = 0.95)

test_datagen = ImageDataGenerator(rescale=1./255,  validation_split = 0.95)

training_set = train_datagen.flow_from_directory('/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train',target_size=(200, 200), color_mode='grayscale', subset = 'training')

test_set = test_datagen.flow_from_directory('/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test', target_size=(200, 200),color_mode='grayscale', subset = 'training')

model.fit_generator(
        training_set,
        epochs=50,
        validation_data=test_set
        )# No of images in test set

#Saving the model
model_json = model.to_json()
with open("/content/drive/MyDrive/Weights(Project)/model-bw.json", "w") as json_file:
    json_file.write(model_json)
print('Model Saved')
model.save_weights('/content/drive/MyDrive/Weights(Project)/model-bw-second.h5')
print('Weights saved')

label_map = (training_set.class_indices)
print(label_map)

loss, acc = model.evaluate_generator(test_set)

print(loss)
print(acc)