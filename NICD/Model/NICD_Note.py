from sklearn.metrics import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score,accuracy_score,auc,confusion_matrix
import joblib





df_train=pd.read_csv('NACD_training.csv')
df_test=pd.read_csv('NACD_testing.csv')





df_com = pd.concat([df_train, df_test])
df_combined=df_com.drop(['ackdat', 'ct_ftp_cmd', 'djit', 'is_ftp_login', 'is_sm_ips_ports', 'response_body_len', 'sjit', 'synack', 'tcprtt','smean','id','dload','trans_depth','ct_flw_http_mthd', 'dinpkt','label'], axis=1)
df_train=df_com.drop(['ackdat', 'ct_ftp_cmd', 'djit', 'is_ftp_login', 'is_sm_ips_ports', 'response_body_len', 'sjit', 'synack', 'tcprtt','smean','id','dload','trans_depth','ct_flw_http_mthd', 'dinpkt','label'], axis=1)
df_test=df_com.drop(['ackdat', 'ct_ftp_cmd', 'djit', 'is_ftp_login', 'is_sm_ips_ports', 'response_body_len', 'sjit', 'synack', 'tcprtt','smean','id','dload','trans_depth','ct_flw_http_mthd', 'dinpkt','label'], axis=1)





catagory = df_combined['attack_cat']
le_target = LabelEncoder()
le = LabelEncoder()
catagory = df_combined['attack_cat']
df_combined['attack_cat'] = le_target.fit_transform(catagory)
df_combined['proto'] = le.fit_transform(df_combined['proto'])
df_combined['service'] = le.fit_transform(df_combined['service'])
df_combined['state'] = le.fit_transform(df_combined['state'])




le_ta_train = LabelEncoder()
le_train = LabelEncoder()
catagory_train = df_train['attack_cat']
df_train['attack_cat'] = le_ta_train.fit_transform(catagory_train)
df_train['proto'] = le_train.fit_transform(df_train['proto'])
df_train['service'] = le_train.fit_transform(df_train['service'])
df_train['state'] = le_train.fit_transform(df_train['state'])



le_ta_test = LabelEncoder()
le_test = LabelEncoder()
catagory_test = df_test['attack_cat']
df_test['attack_cat'] = le_ta_test.fit_transform(catagory_test)
df_test['proto'] = le_test.fit_transform(df_test['proto'])
df_test['service'] = le_test.fit_transform(df_test['service'])
df_test['state'] = le_test.fit_transform(df_test['state'])



data_x = df_combined.drop(['attack_cat'], axis=1) 
data_y = df_combined.loc[:,['attack_cat']]

# del combined_data # free mem
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=.20, random_state=42) 

sc_x=StandardScaler()
x_train=sc_x.fit_transform(X_train)
x_test=sc_x.fit_transform(X_test)


#  Accuracy on the train dataset

y=y_train['attack_cat']

clf = RandomForestClassifier(n_estimators=150, random_state=42)

clf.fit(X_train, y)

#randomModel=clf.fit(X_train,y)

#train_pred=randomModel.predict(X_train)

pickle.dump(clf, open("ml_model_final.sav", "wb"))