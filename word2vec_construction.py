from keras.models import Model
from keras.layers import Dense, Input
from keras.optimizers import SGD
import numpy as np
import pandas as pd

df = pd.read_csv('NER_data_combined_4.txt', sep = '\s+',header=None,error_bad_lines=False)
words_arr = df.iloc[:,0].copy()
map_wor = dict()
c = 0
for i in df.iloc[:,0]:
	if not map_wor.has_key(i):
		map_wor[i]=c
		c+=1
k=len(map_wor)
c = 1
arr = None
for i in df.iloc[:,0]:
	if c==1:
		arr = np.zeros(k)
		arr[map_wor[i]]=1
		c=0
	else:
		temp = np.zeros(k)
		temp[map_wor[i]]=1
		arr = np.concatenate((arr,temp),axis=0)
print(arr)
###########################################
# This the model for data input code it in the above section, k is the vocabulary
############################################
inputs = Input(shape=(,k))
x = Dense(300,activation="linear")(inputs)
out = Dense(k,activation="softmax")(x)
model = Model(inputs = inputs, outputs=out)
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optomizer=sgd,loss="categorical_crossentropy",metrics=['accuracy'])
model.fit(x_train,y_train)
