
# aqui haremos las peticiones y verificaremos todo anda bien 

import requests
import pandas as pd 
import numpy as np

if __name__=='__main__':
	url = 'http://127.0.0.1:2205/predict'

	# extraemos data para hacer una verificacion de servidor 

	Y=pd.read_csv(filepath_or_buffer=dir_data+'/train.csv').sample(n=100,random_state=42)['target']

	X=pd.read_csv(
            filepath_or_buffer=dir_data+'/train.csv'
              ).drop(['ID', 'target'],axis=1).fillna(value=-1).sample(
												n=100,random_state=42)
												
	# Pasamos a formato numpy

	X=data.to_numpy()
	Y=Y.to_numpy()

	input_data=X.tolist()

	response= requests.post(url,json={'data':input_data})

	print(np.array(response.json()['y_pred'])==Y)
	print(Y)
