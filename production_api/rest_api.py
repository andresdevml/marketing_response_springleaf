

# implementacion de la API que dara servicio

from flask import Flask
from flask import jsonify
from flask import request
import pickle
import numpy as np 
import pandas as pd
import joblib
import xgboost as xgb



app=Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
	# input_data sera un json, para comodidad del usuario servido 
	
	try:
	
		input_data=np.array(request.get_json(force=True)['data'])
		
		df_data=pd.DataFrame(input_data)
		
		# nos traemos los categoriocs

		df_data_cat=df_data.select_dtypes(include=['object'])

		# llamamos la data numerica

		df_data_num=df_data.select_dtypes(include=['int','float'])

		# aplicamos las transformaciones

		for index, transf in enumerate(pre_proc_list):
			
			df_data_cat[df_data_cat.columns[index]]=transf.transform(
                   list(df_data_cat[df_data_cat.columns[index]].values))


		# juntamos la data categorica con numerica y normalizamos


		features_data=scaler.transform( pd.concat(
								[df_data_num,df_data_cat],axis=1,
													ignore_index=True))

     
		# definimos la entrada

		input_data=xgb.DMatrix(data=features_data)

		# realizamos la prediccion
     
		prediction = model_xgb.predict(input_data).tolist()
	
		return jsonify(y_pred=prediction)
		
	except:
		print('\n\nHubo un error en el servicio')
	
if __name__=='__main__':

	
	# importamos la lista de funciones de preprocesado

	pre_proc_list=joblib.load(dir_data+'/pre_pipeline.sav')

	scaler=joblib.load(dir_data+'/scaler.sav')
	
	# extraemos el modelo
	
	model_xgb= xgb.Booster()

	model_xgb.load_model('/xgb_clf.json')
	
	# corremos el servicio
	
	app.run(port=2205,debug=True)
