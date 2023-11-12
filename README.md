# Modelo predictivo para respuestas de Marketing 🤖

Se genero el código necesario para entrenar, optimizar y evaluar un modelo capaz de predecir cuáles clientes tienen mayor probabilidad de tener una respuesta positiva a la promoción del servicio. Este modelo puede ser de utilidad para manejar los recursos de marketing efectivamente. 

# Herramientas 🛠️

* Xgboost
* Optuna
* Pandas
* Numpy
* Sklearn
* Joblib

# Ingeniería de características ⚙️

En primera instancia se extrae la data del repositorio de Kaggle mediante el script _**data_extraction.ipynb**_. Posteriormente llenamos los datos vacíos y transformamos la data hacia una representación numérica conveniente para el modelo a utilizar. Luego se segmenta la data en dos grupos, uno de entrenamiento y otro de testeo. Este proceso esta plasmado en _**data_wraling.ipynb**_.

# Prueba y optimización del modelo 🦾

Utilizamos un bosque aleatorio con potenciación del gradiente (XGB) como modelo predictivo y optimizamos sus hiperparametros de aprendizaje con el objetivo de maximiar la métrica AUC, la cual nos da un indicativo de la efectividad del modelo. Este proceso puede verse en _**model_opt_xgb.ipynb**_.

# Finalización del modelo 💎

Ya con los hiperparametros óptimos para el aprendizaje del modelo, volvemos a segmentar la data en los conjuntos de entrenamiento y validación. Pero esta vez con una proporción mucho mayor para el entrenamiento y solo una pequeña muestra para el testeo (10%). Con esta nueva segmentación de data, procedemos a entrenar el modelo final que irá a producción.Esto lo hacemos en _**model_prod_xgb.ipynb**_. 

Luego exportamos el modelo final y construimos una tubería de procesamiento de datos y predicción que posteriormente puede ser utilizada como parte de un servicio predictivo ( API ). Esta tubería se encuentra en _**predict.ipynb**_.



