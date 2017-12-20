import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.optimizers import SGD
y_train = np.load("./y_train.npy")
x_train = np.load("./x_train.npy")
x_test = np.load("./x_test.npy")
y_test = np.load("./y_test.npy")
model = Sequential()
model.add(Dense(60,input_dim=24*5,activation="relu"))
model.add(Dense(19,activation="sigmoid"))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=1000,batch_size=47000)
score = model.evaluate(x_test,y_test,batch_size=850)
model.save("ANN_2")
print(score)
