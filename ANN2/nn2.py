import numpy as np
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

seed = 7
np.random.seed(seed)

dataframe = pandas.read_csv("dataset.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:300].astype(float)
Y = dataset[:,300]

print "Encoding Done!"
def baseline_model():
	
	model = Sequential()
	model.add(Dense(150, input_dim = 300, activation='relu'))
	#model.add(Dense(75,activation = 'relu'))
	model.add(Dense(3, activation = 'softmax'))
	
	model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])
	return model
	
estimator = KerasClassifier(build_fn=baseline_model, epochs=1000, batch_size=5000, verbose=0)
print "Estimating Done!"
np.random.shuffle(dataset)
x_train = dataset[:int(7*dataset.shape[0]/10),0:300].copy()
y_train = dataset[:int(7*dataset.shape[0]/10),300].copy()
x_test = dataset[int(7*dataset.shape[0]/10):,0:300].copy()
y_test = dataset[int(7*dataset.shape[0]/10):,300].copy()
encoder = LabelEncoder()
encoder.fit(y_train)
encoded_Y = encoder.transform(y_train)
dummy_y = np_utils.to_categorical(encoded_Y)
encoder2 = LabelEncoder()
encoder2.fit(y_test)
encoded_Y2 = encoder2.transform(y_test)
dummy_y2 = np_utils.to_categorical(encoded_Y2)
looku = {1:"Misc",2:"Person",0:"Location"}
estimator.fit(x_train,dummy_y)
pred_val = estimator.predict(x_test, batch_size=200, verbose=1)
print np.reshape(pred_val,(-1,1)).shape,x_test.shape,dummy_y2.shape
li=list()
for i in range(len(pred_val)):
	li.append(looku[pred_val[i]])
li_arr = np.array(li)
X_con = np.concatenate((np.reshape(y_test,(-1,1)),np.reshape(li_arr,(-1,1))),axis=1)
np.savetxt("text", X_con, fmt='%.1e', delimiter=',', newline='\n')
#print("Baseline: %.2f%% (%.2f%%)" %(results.mean()*100, results.std()*100))
