import os
import numpy as np  
import pandas as pd 
filePath = '/Users/computer/Documents/fraudDetection/PS_20174392719_1491204439457_log.csv'

def getData():
	data = pd.read_csv(filePath)
	data.info()
	targets1 = data['isFraud']
	targets2 = data['isFlaggedFraud']
	data.drop(columns = ['isFraud','isFlaggedFraud'],inplace = True)
	return data,np.array(targets1),np.array(targets2)

