# Inteligencia Artificial I 2021-1

## Bienvenidos!

<img src="/imgs/img_IA.jpg" style="width:400px;">


## Colaboratory (Google)

Vamos a utilizar la plataforma de google para editar, compartir y correr notebooks: [**Colaboratory**](https://colab.research.google.com/notebooks/welcome.ipynb) 

- Necesitas una cuenta de gmail y luego entras a drive
- Colaboratory es un entorno de notebook de Jupyter gratuito que no requiere configuración y se ejecuta completamente en la nube.
    - Usaremos parte de la infraestructura de computo de google... gratis! (máximo procesos de 8 horas)
- Con Colaboratory, puedes escribir y ejecutar código, guardar y compartir análisis, y acceder a recursos informáticos potentes, todo gratis en tu navegador.
- También puedes usar los recursos de computador Local. 

## Máquina Virtual

Alternativamente, usaremos una máquina virtual que tiene instalado un entorno Anaconda con Jupyter Notebooks disponibles en  [localhost:8008/tree](http://localhost:8008/tree) una vez que la máquina arranca.

La máquina virtual puede descargarse [aquí](https://drive.google.com/open?id=1lymG9E3m6tjblZinOQGDemxc_ZtFFCOW)
- Esta opción es util para contestar talleres y para trabajar desde casa. 


**Observa la configuración de la máquina**

- Si tu máquina física tiene al menos 4GB de memoria configura la máquina virtual **con 2GB de memoria**
- Aunque casi no necesitarás un terminal, el interfaz de Jupyter Notebooks tiene un terminal para acceder a través del navegador. En cualquier caso, la máquina virtual tiene un servidor SSH en el puerto 2222 con user/user como usuario y pwd. Si tu máquina física es mac o linux usa `ssh -p 2222 user@localhost` para conectarte. Si es windows, usa [putty](https://www.putty.org/)
- Si compartes una carpeta entre la física y virtual asegúrate que **el nombre con el que se comparte** sea `share` (aunque el nombre de la carpeta en la máquina física puede ser distinto)

**Para montar la carpeta compartida** ejecuta lo siguiente en un terminal y la carpeta aparecerá en /home/user/share:

    sudo mount share


## Calificación
- 40% Talleres (Problemsets)
- 30% Parciales (Quizes) 
- 30% Proyecto funcional IA 

## Talleres (Problemsets)

Los talleres pretenden ser una herramienta practica para afianzar los conocimientos desarrollados durante las clases. En general se presentan como un conjunto de ejercicios que serán desarrollados **individualmente** por los estudiantes. Cada taller esta escrito como un notebook para la validación automática. Se pueden hacer tantos intentos como se quieran y unicamente la última respuesta será tomada en cuenta. Cada uno de los talleres ser desarrollará en casa, dentro de las fechas establecidas en el cronograma. 


## Parciales (Quizes)

Son evaluaciones **individuales** basadas en notebooks sobre los temas tratados en las clases. Los estudiantes deben solucionarlo en el salón de clase, en un tiempo determinado. Los apuntes y notebooks del curso se pueden utilizar. 


## Proyecto funcional IA

- **Funcionamiento del proyecto**: El proyecto se debe realizar como un notebook y debe ser 100% funcional.

- **Prototipo (PRE-SUS PROJ)**: En este item se considera como esta estructurado el proyecto y se espera una nivel razonable de funcionalidad.

- **Presentación**:
Imagen relacionada con la siguiente información: título del proyecto e información de los estudiantes<br>
Video corto (ENTREGAR EL ARCHIVO DE VIDEO y también alojarlo en youtube)<br>

- **Sustentación**: Se realizarán preguntas cortas a los estudiantes unicamente relacionadas con el proyecto. 
 
Todos los items tienen el mismo porcentaje de evaluación. 

**UNICAMENTE SE TENDRAN EN CUENTA LOS PROYECTOS QUE SE HAYAN POSTULADO AL FINALIZAR EL PRIMER CORTE**


## Calendario y plazos

                        SESSION 1            SESSION 2              SESSION SATURDAY

     W01 Abr05-Abr09    Intro                Python-overall            
     W02 Abr12-Abr16    Python-Numpy         Python-Vis   
     W03 Abr19-Abr23    Pandas               Pandas 
     W04 Abr26-Abr30    Estadística          Estadística
     W05 May03-May07    Aclaraciones         Aclaraciones           
     W06 May10-May14    Intro A.M.S.         Clasificación A.M.S.   Parcial 1 (Nov28)
     W07 May17-May21    Regresión A.M.S.     Métodos A.M.S. (a)
     W08 May24-May28    -----                Métodos A.M.S. (b)   
     W09 Jun01-Jun04    Aplicación A.M.S.    Deep Learning (A)     
     W10 Jun07-Jun11    N8.Retaken ML        N9. Aplicación A.M.S.           
     W11 Jun14-Jun18    N10. Deep Learning   N11. Deep Learning (a)
     W12 Jun21-Jun25    Intro A.M.N.S.       K-means A.M.N.S.       parcial 2

    -----------------  VACACIONES -----------------

     W13 Jul12-Jul16    DBScan A.M.N.S.      PRE-SUS PROJ
     W14 Jul19-Jul23    Planning and S.      Genetic Alg.
     W15 Jul26-Jul30    Simulated anne.      Aclaraciones
     W16 Aug02-Aug06    Aclaraciones         Aclaraciones           Parcial 3
     W17 Aug09-Aug13    SUS PROJ             SUS PROJ


    May 28 -           -> Registro primera nota
    May 30 -           -> Último día cancelación materias
    Jun 28 - Jul 12    -> Vacaciones
    Ago 06             -> Finalización clase
    Ago 09 - Ago 13    -> Evaluaciones finales
    Ago 17 -           -> Registro calificaciones finales
    

[Calendario academico 2021-1](http://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2020/acuerdoAcad434_2020.pdf)

**CUALQUIER ENTREGA FUERA DE PLAZO SERÁ PENALIZADA CON UN 50%**

**LOS PROBLEMSETS ESTAN SUJETOS A CAMBIOS QUE SERÁN DEBIDAMENTE INFORMADOS**

**DEADLINE DE LOS PROBLEMSETS SERÁ EL DIA DE CADA PARCIAL**

