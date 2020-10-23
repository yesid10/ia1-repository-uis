
# Funcion encargada de realizar la limpieza del texto, es decir
# eliminar la puntiacion, lematizar las palabras y colocar las 
# en minusculas.
# Recibe una columna como parametro.
# Devuelve los un array que contiene las listas de palabras para 
# cada oracion o parrafo de la columna
def clean_text(col):
  import numpy as np
  import pandas as pd
  from nltk.stem import WordNetLemmatizer
  from nltk.tokenize import word_tokenize
  import string
  import nltk
  nltk.download('punkt')
  nltk.download('wordnet')
  nltk.download('stopwords')
  from nltk.corpus import stopwords

  lematizador = WordNetLemmatizer()
  modificado = []
  for texto in (col):
    mods = word_tokenize(texto)
    mods = [mod.lower() for mod in mods if mod.isalpha()]
    mods = [mod for mod in mods if mod not in string.punctuation and mod not in set(stopwords.words('english'))]
    mods = [lematizador.lemmatize(mod) for mod in mods]
    modificado.append(mods)
  
  print('Limpieza completada')
  return modificado

###############################################################################
# Funcion encargada de vectorizar cada palabra
# Recibe como parametros de entrenamiento y testeo en forma de lista
# y devuelve los datasets de testeo y entrenamiento vectorizados
def vectorizar(data_train, data_test, data_prueba):
  import numpy as np
  import pandas as pd
  from sklearn.feature_extraction.text import TfidfVectorizer

  training = []
  testing = []
  prueba = []
  tfidf_train = TfidfVectorizer(min_df=0.1, preprocessor=' '.join)
  res_train = tfidf_train.fit_transform(data_train)
  names_train = tfidf_train.get_feature_names()
  training = res_train.todense()
  training = pd.DataFrame(training, columns=names_train)

  tfidf_test = TfidfVectorizer(preprocessor=' '.join, vocabulary=names_train)
  res_test = tfidf_test.fit_transform(data_test)
  names_test = tfidf_test.get_feature_names()
  testing = res_test.todense()
  testing = pd.DataFrame(testing, columns=names_test)

  tfidf_prue = TfidfVectorizer(preprocessor=' '.join, vocabulary=names_train)
  res_prue = tfidf_prue.fit_transform(data_prueba)
  names_prue = tfidf_prue.get_feature_names()
  prueba = res_prue.todense()
  prueba = pd.DataFrame(prueba, columns=names_prue)
  print('Vectorizacion completada')
  return training, testing, prueba

# funcion encargada de realizar el proceso de embedding para el dataset
# que recibe como parametro
def embedding(dataframe):
  import numpy as np
  import pandas as pd
  import scipy.stats as stats
  from sklearn.model_selection import KFold
  from sklearn.model_selection import train_test_split
  
  
  title = clean_text(dataframe['title'])
  X_t = title
  y = dataframe['label']
  n = int(len(X_t)*0.75)
  nt = n + int(len(X_t)*0.20)
  X_train_t = X_t[:n]
  X_test_t = X_t[n:nt]
  X_prue_t = X_t[nt:]
  y_train = y[:n]
  y_test = y[n:nt]
  y_prue = y[nt:]
  X_train_t, X_test_t, X_prue_t = vectorizar(X_train_t, X_test_t, X_prue_t)
  print('title vectorizado')

  text = clean_text(dataframe['text'])
  X_c = text
  y = dataframe['label']
  n = int(len(X_c)*0.75)
  nt = n + int(len(X_c)*0.20)
  X_train_c = X_c[:n]
  X_test_c= X_c[n:nt]
  X_prue_c = X_c[nt:]
  y_train = y[:n]
  y_test = y[n:nt]
  y_prue = y[nt:]
  X_train_c, X_test_c, X_prue_c = vectorizar(X_train_c, X_test_c, X_prue_c)
  print('text vectorizado')

  titles = pd.DataFrame(X_t)
  titles.to_csv('DatasetsTrainAndTest/titles.csv')

  X_train_t.to_csv('DatasetsTrainAndTest/titles_entrenamiento.csv')

  X_test_t.to_csv('DatasetsTrainAndTest/titles_testeo.csv')
  
  X_prue_t.to_csv('DatasetsTrainAndTest/titles_prueba.csv')

  y.to_csv('DatasetsTrainAndTest/labels.csv')

  y_test.to_csv('DatasetsTrainAndTest/labels_testeo.csv')

  y_train.to_csv('DatasetsTrainAndTest/labels_entrenamiento.csv')
  
  y_prue.to_csv('DatasetsTrainAndTest/labels_prueba.csv')

  text = pd.DataFrame(X_c)
  text.to_csv('DatasetsTrainAndTest/cuerpo.csv')

  X_train_c.to_csv('DatasetsTrainAndTest/cuerpo_entrenamiento.csv')

  X_test_c.to_csv('DatasetsTrainAndTest/cuerpo_testeo.csv')
  
  X_prue_c.to_csv('DatasetsTrainAndTest/cuerpo_prueba.csv')
  