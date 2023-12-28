# Modelo predictivo para respuestas de Marketing 🤖

Se genero el código necesario para entrenar, optimizar y evaluar un modelo capaz de predecir cuáles clientes tienen mayor probabilidad de tener una respuesta positiva a la promoción del servicio. Este modelo resultautil para manejar los recursos de marketing efectivamente. 

# Herramientas 🛠️

* Xgboost
* Optuna
* Pandas
* Numpy
* Sklearn
* Joblib
* Flask

# Ingeniería de características ⚙️

En primera instancia se extrae la data de la fuente de datos. Posteriormente llenamos los datos vacíos y transformamos la data hacia una representación numérica conveniente para el modelo a utilizar. Luego se segmenta la data en dos grupos, uno de entrenamiento y otro de testeo. Este proceso esta plasmado en _**data_wraling.ipynb**_.

# Prueba y optimización del modelo 🦾

Utilizamos un bosque aleatorio con potenciación del gradiente (XGB) como modelo predictivo y optimizamos sus hiperparametros de aprendizaje con el objetivo de maximiar la métrica AUC, la cual nos da un indicativo de la efectividad del modelo. Este proceso puede verse en _**model_opt_xgb.ipynb**_.

# Finalización del modelo 💎

Ya con los hiperparametros óptimos para el aprendizaje del modelo, volvemos a segmentar la data en los conjuntos de entrenamiento y validación. Pero esta vez con una proporción mucho mayor para el entrenamiento y solo una pequeña muestra para el testeo (10%). Con esta nueva segmentación de data, procedemos a entrenar el modelo final que irá a producción.Esto lo hacemos en _**model_prod_xgb.ipynb**_. 

Luego exportamos el modelo final y construimos una tubería de procesamiento de datos y predicción que posteriormente puede ser utilizada como parte de un servicio predictivo ( API ). Esta tubería se encuentra en _**predict.ipynb**_.

# Modelo en producción 🏭

Con el modelo finalizado, creamos una REST API para poder dar acceso al modelo como servicio, dentro de esta api se realiza todo el proceso necesario sobre los datos crudos para que el modelo pueda arrojar la predicción requerida. Este servicio se encuentra codificado en el script _**rest_api.py**_. Adicionalmente tenemos un script para generar un request a la api y así testear su correcto funcionamiento. Este, es el script  _**test_request.py**_.




