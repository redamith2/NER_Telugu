import pandas as pd
import numpy as np
import pickle as pk
df1 = pd.read_csv("./data/processed2.txt",sep=" ",header=None,dtype=np.dtype("str"))
y_train = df1.iloc[:,0].copy().as_matrix()
x_train = df1.iloc[:,1:].copy().as_matrix()
y_train_ann = np.zeros((y_train.shape[0],19))
x_train_ann = np.zeros((x_train.shape[0],24*5))
NER_tag_dict = {"B-PERSON":1,"I-PERSON":2,"B-ORG":3,"I-ORG":4,"B-LOC":5,"I-LOC":6,"B-NUM":7,"I-NUM":8,"B-TIME":9,"I-TIME":10,"B-DAY":11,"B-MONEY":12,"I-MONEY":13,"B-DATE":14,"I-DATE":15,
                "B-PERIOD":16,"I-PERIOD":17,"B-YEAR":18,"O":19}
pos_tag_dict = {"NN":1,"NST":2,"NNP":3,"PRP":4,"DEM":5,"VM":6,"JJ":7,"RB":8,"PSP":9,"RP":10,"CC":11,"WQ":12,"QF":13,"QC":14,"QO":15,
                "CL":16,"INTF":17,"INJ":18,"UT":19,"SYM":20,"RDP":21,"0":22,"SYMP":23,"NNO":24}
for i,j in enumerate(y_train):
    y_train_ann[i,NER_tag_dict.get(str(j))-1]=1
for i,j in enumerate(x_train):
    for a,k in enumerate(j):
        if np.abs(a-2)==2:
            weight = 0.25
        elif np.abs(a-2)==1:
            weight= 0.125
        else:
            weight =1;
        x_train_ann[i,24*a+(pos_tag_dict.get(str(k))-1)]=weight
np.save("y_train",y_train_ann)
np.save("x_train",x_train_ann)
# np.savetxt("y_test",y_train_ann,delimiter=" ",fmt="%d")
# np.savetxt("x_test",x_train_ann,delimiter=" ",fmt="%d")
#np.save("y_test_n",y_train_ann)
