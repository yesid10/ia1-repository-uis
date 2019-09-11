---
# Proyectos 2018-2. Inteligencia Artificial. 

## Prof: Fabio Martínez, Ph.D

---

# Lista de Proyectos
1. [Clasificador de Música por Género](#proy1)
2. [Análisis de datos del Twiter como mecanismo de identificación de violencia simbólica. ](#proy2)
3. [Estudio de factores sociales que influyen en las pruebas icfes usando analítica de datos](#proy3)
4. [Anime genide: An anime  popularity predictor from regression strategies](#proy4)
5. [Predicción de patrones parkinsonianos en video como apoyo al diagnostico](#proy5)
6. [LIKING (your perfect couple): Sugerencia de perfiles visuales de parejas, según anotaciones de usuarios](#proy6)
7. [Offline handwritten signature verification](#proy7)
8. [Socker regression: Analítica de actitudes futbolisticas de jugadores de elite](#proy8)
9. [Siendo tus ojos: Traducción auditiva de caracteres representados visualmente](#proy9)
10. [Modelo de regresión para la Valorizacion-de-Diamantes](#proy10)
11. [Clasificador de estrellas pulsares](#proy11)
12. [Caracteristicas que afeactan el consumo de combustible en carros](#proy12)

---

## Clasificador de Música por Género <a name="proy1"></a>

**Autores: William Palomino, Henry Peña, Diego Medina**

<img src="https://i.imgur.com/ueLN6rk.jpg" style="width:700px;">

**Objetivo:** Predecir el genero de las canciones según su caracteristicas relevantes de los expectogramas 

- Dataset: 1000 canciones classificadas en 10 generos de música. 
- Librerias: Librosa (extracción de caracteristicas), tensorflow (clasificación), sklearn
- Modelo: deep neuronal network: 2 capas oculatas: 128, 64. Salida: capa de 10 unidades. 

[(code)](https://github.com/pecons/MusicClassifierAI2018-2); [(video)](https://www.youtube.com/watch?v=5gOOh8O8p3k&feature=youtu.be); [(+info)](https://github.com/pecons/MusicClassifierAI2018-2/blob/master/presentation/Music%20Classifier%20Presentation.pdf)

---

## Análisis de datos del Twiter como mecanismo de identificación de violencia simbólica <a name="proy2"></a>

**Autores: Alejandro Ramirez, David Villabona**

<img src="https://github.com/dabid-va/ViolenciaSimbolicaTwitter/blob/master/data/una.jpeg" style="width:700px;">


**Objetivo:** Anaĺitica de datos para predecir twits que contengan violencia simbólica. 

- [Dataset](https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/): 49000 twits etiquetados según la violencia simbólica.
- Librerias: nltk.steam, sklearn, wordclap, word2vec, gensim
- Modelo: SVM, Ranfom forest for classification

[(proyecto)](https://github.com/dabid-va/ViolenciaSimbolicaTwitter); [(+info)](https://github.com/dabid-va/ViolenciaSimbolicaTwitter/blob/master/presentacion/expo_IA.pdf); [(video)](https://github.com/dabid-va/ViolenciaSimbolicaTwitter/blob/master/presentacion/20190404_205640.mp4)

---

## Estudio de factores sociales que influyen en las pruebas icfes usando analítica de datos <a name="proy3"></a>

**Autores: Juan Mantilla, Luisa Jaimes, Hector Gonzalez**

<img src="https://github.com/juandmantilla/Estudio-de-Factores-Sociales-Icfes/blob/master/img/banner_.jpg" style="width:700px;">

**Objetivo:** Analizar los factores sociales que influyen en los puntajes del icfes utilizando analítica de datos y  modelos de regresión. 

- [Dataset](https://www.datos.gov.co/Educaci-n/Saber-11-2018-2/m2nt-jw2h): Más de 490000 registros de pruebas de estudiantes con caracteristicas como: estrato, situación económica, tv, dtpto, otros. 
- Librerias: pandas, sklearn
- Modelos: extra-tree-regressor, feature importances.  

[(proyecto)](https://github.com/juandmantilla/Proyecto-Icfes-2018); [(video)](https://vimeo.com/328628007); [(+info)](https://github.com/juandmantilla/Estudio-de-Factores-Sociales-Icfes/blob/master/EXPO-IA.4.pdf)

---

## Anime genide: An anime  popularity predictor from regression strategies <a name="proy4"></a>

**Autores: Douglas Ramirez, Marianne Rojas**

<img src="https://github.com/Doukuest/IA_Regresor_shows_animados/blob/master/data/other/ProjectBanner.png" style="width:700px;">

**Objetivo:**  Predecir la popularidad  de shows animados en terminos de, cantidad de personas, puntaje y favoritos a partir del tipo de show, fuente de material y genereros. 

- [Dataset](https://www.kaggle.com/azathoth42/myanimelist#anime_filtered.csv): Más de 6000 shows animados, con 17 generos, 6 tipos de shows y 14 diferentes fuentes. 
- Librerias: sklearn, pandas
- Modelos: Decision tree, gradient boost, baging regressor. 

[(proyecto)](https://github.com/Doukuest/IA_Regresor_shows_animados); [(video)](https://github.com/Doukuest/IA_Regresor_shows_animados/blob/master/project/Proyecto.wmv); [(+info)](https://github.com/Doukuest/IA_Regresor_shows_animados/blob/master/project/Slides%20-%20Anime%20Genie.pdf) 

---

## Predicción de patrones parkinsonianos en video como apoyo al diagnostico <a name="proy5"></a>

**Autores: Brayan Valenzuela, Alejandra Moreno, Lina Ruiz**

<img src="https://github.com/Brayan-Valenzuela/Caracterizacion-de-Marcha-Parkinsoniana-Empleando-Trayectorias-de-Movimiento./blob/master/Parkinson%20disease.png" style="width:400px;">

**Objetivo:** Reconocer patrones relacionados con la enfermedad del parkinson utilizando clasificadores automáticas y trayectorias de movimiento. 

- [Dataset](http://bivl2ab.uis.edu.co). El dataset por el momento es privado, para su consulta contactar al grupo Bivl2ab. Se adelantan tramites con el comité de etica para su disposición al público con fines académicos.
- Librerias: sklearn, opencv, subprocess
- Modelos: RandomForest, Knn SVM. 

[(proyecto)](https://github.com/Brayan-Valenzuela/Caracterizacion-de-Marcha-Parkinsoniana-Empleando-Trayectorias-de-Movimiento.); [(video)](https://drive.google.com/file/d/1VW3zzVLGkJg4H1Sfb8gf8y57lkGxjZ1-/view); [(+info)](https://github.com/Brayan-Valenzuela/Caracterizacion-de-Marcha-Parkinsoniana-Empleando-Trayectorias-de-Movimiento./blob/master/Unofficial_NEO_UEA_Template__1_(2).pdf)


---

## LIKING (your perfect couple): Sugerencia de perfiles visuales de parejas, según anotaciones de usuarios <a name="proy6"></a>

<img src="/imgs/banner-20182/banner.png" style="width:400px;">


**Objetivo:** Seleccionar perfiles de pareja según anotaciones visuales de los usuarios.

- [Dataset](https://github.com/adeleeee041096/Artificial-Intelligence-Project/blob/master/Archivo.zip): 56 personas, mas de 200 imagenes tomadas desde diferentes perspectivas. 
- Librerias: pandas, opencv, sklearn
- Modelos: Random forest

[proyecto](https://github.com/adeleeee041096/Artificial-Intelligence-Project); [video](https://github.com/adeleeee041096/Artificial-Intelligence-Project/blob/master/video%20proyecto.rtf); [+info](https://github.com/adeleeee041096/Artificial-Intelligence-Project/blob/master/liking1.pdf)


---

## Offline handwritten signature verification <a name="proy7"></a>
**Autores: Juan Sebastian Marcon, Andrés Chia**

<img src="/imgs/banner-20182/marchia.png" style="width:700px;">


**Objetivo:** Determinar si una firma es genuina o ha sido falsificada. 

- [Dataset]: se construyó un dataset que consiste en 120 firmas de una persona. 60 muestras genuinas y 60 muestras falsas. 
- Librerias: tensorflow, sklearn, opencv, tensorboard
- Modelo: una red convolucional de dos capas de convolución con  32 y 64 filtros. Luego una capa full connected de 1024.  

[(proyecto)](https://github.com/juanse1080/Proyecto-ai-20182); [(video)](https://github.com/juanse1080/Proyecto-ai-20182/blob/master/signature_copy.mp4); [(+info)](https://github.com/juanse1080/Proyecto-ai-20182/blob/master/presentaciones/Classification_of_offline_handwritten_signatures.pdf)


---

## Socker regression: Analítica de actitudes futbolisticas de jugadores de elite <a name="proy8"></a>

**Autores: Edgar Montenegro, Jorge Triana, Brayan Rivera**

<img src="https://github.com/EdgarAndresMontenegro/Soccer-Regression/blob/master/img/FIFA-19.jpg" style="width:300px;">


**Objetivo:** Construir un modelo cuntitativo del futbol de elite para ser usado como referencia en otras ligas. 

- [Dataset](https://www.kaggle.com/karangadiya/fifa19): Más de 16000 registros, con 54 caracteristicas sobre actitudes futbolisticas. Se usaron 2000 registros y 43 caracteristicas. 
- Librerias: sklearn, pandas
- Modelos: Kmeans, DBScan

[(proyecto)](https://github.com/EdgarAndresMontenegro/Soccer-Regression); [(video)](https://drive.google.com/file/d/1Mbm41DXqFyP6VZdRSrH_RluAFm5e-7Ga/view); [(+info)](https://github.com/EdgarAndresMontenegro/Soccer-Regression/blob/master/PresentacionIA1.pptx)


---

## Siendo tus ojos: Traducción auditiva de caracteres representados visualmente  <a name="proy9"></a>

**Autores: Karina Sequeda, Veronica Lucena, Angel Gómez, Brayan Alvarez**

<img src="https://github.com/sequedakarina/reconocimiento-de-caracteres-y-reproduccion-de-voz/blob/master/Banner.png" style="width:300px;">

**Objetivo:** desarrollar una aplicación para el apoyo a personas con discapacidad visual reconociendo automaticamente los caracteres y traduciendolos a señales auditivas. 

- [Dataset](https://www.westernsydney.edu.au/bens/home/reproducible_research/emnist): 80000 imagenes, con contiene 26 clases de caracteres
- [Datset propio]() mas de 800 imagenes y 26 clases de caracteres que incluyen letras en mayusculas y minusculas. 
- Librerias: sklearn, opencv, gtts (google text to speech), pandas
- Modelos: Random forest, Decision tree


[(proyecto)](https://github.com/sequedakarina/reconocimiento-de-caracteres-y-reproduccion-de-voz); [(video)](https://github.com/sequedakarina/reconocimiento-de-caracteres-y-reproduccion-de-voz/blob/master/Promocion_Proyecto.mp4);  [(+info)](https://github.com/sequedakarina/reconocimiento-de-caracteres-y-reproduccion-de-voz/blob/master/Reconocimiento%20de%20caracteres%20y%20reproducci%C3%B3n%20de%20voz.pdf)


---

## Modelo de regresión para la Valorizacion-de-Diamantes <a name="proy10"></a>


**Autores: Nicolás Gutierrez**


<img src="/imgs/banner-20182/bannerNicolas.jpeg" style="width:700px;">


**Objetivo:** predecir el costo de los diamantes en USD utilizando un randomRegressor y un DesicionTree

- [Dataset](https://www.kaggle.com/shivam2503/diamonds): 53940 muestras de diamantes caracterizados por 9 caracteristicas. Dataset disponible en kaggle
- Librerias: sklearn
- Modelo: Random forest regression

[(proyecto)](https://github.com/NG2C/Valorizacion-de-Diamantes); [(+info)](https://github.com/NG2C/Valorizacion-de-Diamantes/blob/master/Valorizaci%C3%B3n%20de%20Diamantes.pptx)

---

## Clasificador de estrellas pulsares <a name="proy11"></a>

**Autores: Alfredo Puertas, Cristian Fernandez, Johan Castro**

<img src="/imgs/banner-20182/pulsar.png" style="width:700px;">


**Objetivo:** Predecir estrellas pulsares según caracteristicas físicas de estos cuerpos celestes.

- [Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00372/): Más de 17000 registros con ocho caracteristicas estadisticas sobre medidas físicas de las estrellas.
- Librerias: sklearn 
- Modelo: DT, SVM, RandomForest, KNN, regresión logística. 

[(proyecto)](https://github.com/johanca965/proyecto-ai); [(video)](https://github.com/johanca965/proyecto-ai/blob/master/presentaci%C3%B3n%20video.mp4); [(+info)](https://github.com/johanca965/proyecto-ai/blob/master/Clasificaci%C3%B3n%20de%20estrellas.pptx)

---
## Caracteristicas que afeactan el consumo de combustible en carros <a name="proy12"></a>

**Autores: Juan Felipe Silva, Javier Rueda**

<img src="https://github.com/felipe0479/Caracteristicas-que-afectan-el-consumo-de-combustible-en-los-carros/blob/master/BANNER.jpg" style="width:500px;">


**Objetivo:** Predecir el factor que mas influye en el consumo de combustible de un carro. 

-[Dataset](https://github.com/RodolfoViana/exploratory-data-analysis-dataset-cars): 400 registros de carros con 10 caracteristicas como aceleración, millas por galón, modelo.
- Librerias: sklearn
- Modelo: Random forest, logistic regression, Decision tree. 

[(proyecto)](https://github.com/felipe0479/Caracteristicas-que-afectan-el-consumo-de-combustible-en-los-carros);
[(video)](https://github.com/johanca965/proyecto-ai/blob/master/presentaci%C3%B3n%20video.mp4 ), [(+info)](https://github.com/felipe0479/Caracteristicas-que-afectan-el-consumo-de-combustible-en-los-carros/blob/master/Caracter%C3%ADsticas%20que%20afectan%20el%20consumo%20de%20combustible%20en%20los%20carros.pdf)


---


