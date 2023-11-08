# Modelo predictivo para respuestas de Marketing 🤖

El proyecto consiste en generar el código necesario para entrenar, optimizar y evaluar un modelo capaz de predecir cuáles clientes tienen mayor probabilidad de tener una respuesta positiva a la promoción del servicio. Este modelo puede ser de utilidad para utilizar los recursos de marketing efectivamente. 

# Herramientas 🛠️

* Xgboost
* Optuna
* Pandas
* Numpy
* Sklearn
* Joblib

# Ingeniería de características ⚙️

En primera instancia se extrae la data del repositorio de Kaggle mediante el script _**data_extraction.ipynb**_. Posterior a esto llenamos los datos vacíos y transformamos la data hacia una representación numérica conveniente para el modelo a utilizar. Posteriormente se segmenta la data en dos grupos, uno de entrenamiento y otro de testeo. Este proceso esta plasmado en _**data_wraling.ipynb**_.

# Prueba y optimización de modelo 🦾

Utilizamos un bosque aleatorio con potenciación del gradiente (XGB) como modelo predictivo y optimizamos sus hiperparametros de aprendizaje con el objetivo de maximiar la métrica AUC, la cual nos da un indicativo de la efectividad del modelo. Este proceso puede verse en _**model_opt.ipynb**_.

# Finalización del modelo 💎

Ya con los hiperparametros óptimos para el aprendizaje del modelo, volvemos a segmentar la data en entrenamiento y validación. Pero esta vez con una proporción mucho mayor para el entrenamiento y solo una pequeña muestra para el testo (10%). Este proceso corresponde al _**script data_prod.ipynb**_.

Con esta nueva segmentación de data procedemos a entrenar el modelo final que irá a producción, esto lo hacemos en _**model_prod.ipynb**_. Luego exportamos el modelo final y construimos una tubería de procesamiento de datos y predicción que posteriormente puede ser utilizada como parte de un servicio predictivo ( API ). Esta tubería se encuentra en _**predict.ipynb**_.



