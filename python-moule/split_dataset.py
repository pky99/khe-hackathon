
from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import shutil
import random

#Splitting the dataset
#Trying for B

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/B"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/B")

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/C"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/C") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/D"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/D") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/E"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/E") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/F"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/F") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/G"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/G") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/H"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/H") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/I"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/I")

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/J"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/J") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/K"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/K") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/L"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/L") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/M"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/M") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/N"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/N") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/O"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/O") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/P"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/P")

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/Q"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/Q") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/R"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/R") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/S"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/S") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/T"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/T") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/U"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/U") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/V"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/V") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/W"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/W")

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/X"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/X") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/Y"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/Y") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/Z"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/Z") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/space"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/space") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/del"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/del") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/nothing"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/nothing") 

source = "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_train/A"
allFileNames = os.listdir(source)
np.random.shuffle(allFileNames)

test_ratio = 0.30 

train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*(1 - test_ratio))])

test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

for name in test_FileNames:
  shutil.move(name, "/content/drive/MyDrive/Preprocessed_Dataset/ASL_alphabet_test/A")