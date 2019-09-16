# Inteligencia Artificial I 2019-2
# BIENVENIDOS!

<img src="/imgs/img_IA.jpg" style="width:400px;">

_Regístrate [aquí](https://forms.gle/DE1TkzdpReve7h8Q8)
                                            
La máquina virtual puede descargarse [aquí](https://drive.google.com/file/d/1X3h7U1JTSnKPTVPzVHeflKuOMv0kG3VN/view?usp=sharing)


## Máquina Virtual

Usaremos esta máquina virtual que tiene instalado un entorno Python Anaconda con Jupyter Notebooks disponibles en  [localhost:8008/tree](http://localhost:8008/tree) una vez que la máquina arranca.

**Observa la configuración de la máquina**

- Si tu máquina física tiene al menos 4GB de memoria configura la máquina virtual **con 2GB de memoria**
- Aunque casi no necesitarás un terminal, el interfaz de Jupyter Notebooks tiene un terminal para acceder a través del navegador. En cualquier caso, la máquina virtual tiene un servidor SSH en el puerto 2222 con user/user como usuario y pwd. Si tu máquina física es mac o linux usa `ssh -p 2222 user@localhost` para conectarte. Si es windows, usa [putty](https://www.putty.org/)
- Si compartes una carpeta entre la física y virtual asegúrate que **el nombre con el que se comparte** sea `share` (aunque el nombre de la carpeta en la máquina física puede ser distinto)

**Para montar la carpeta compartida** ejecuta lo siguiente en un terminal y la carpeta aparecerá en /home/user/share:

    sudo mount share

## Colaboratory (Google)

También puedes utilizar la plataforma de google para editar, compartir y correr notebooks: [**Colaboratory**](https://colab.research.google.com/notebooks/welcome.ipynb) 

## Calificación
40% Talleres (Problemsets)<br/>
30% Parciales (Quizes) <br/>
30 % + [10% ,20 %, 30 %] Proyecto funcional IA <br/>
+10% Online courses (MOOC)

## Talleres (Problemsets)

Los talleres pretender ser una herramienta practica para afianzar los conocimientos desarrollados durante las clases. En general se presentan como un conjunto de ejercicios que serán desarrollados **individualmente** por los estudiantes. Cada taller esta escrito como un notebook para la validación automática. Se pueden hacer tantos intentos como se quieran y unicamente la última respuesta será tomada en cuenta. Cada uno de los talleres ser desarrollará en casa, dentro de las fechas establecidas en el cronograma. 


## Parciales (Quizes)

Son evaluaciones **individuales** basadas en notebooks sobre los temas tratados en las clases. Los estudiantes deben solucionarlo en el salón de clase, en un tiempo determinado. Los apuntes y notebooks del curso se pueden utilizar. 


## Proyecto funcional IA

- **Funcionamiento del proyecto**. El proyecto se debe realizar como un notebook.  

- **Prototipo [+10% - +20%]**:  En este item se considera como esta estructurado el proyecto. Los porcentajes extras tienen en cuenta importancia o relevancia de 
del proyecto y también la solución a problemas  reales.

- **Presentación (banner, video y diapositivas) [+ 10%]**:  Se debe enviar un video corto (max 5 minutos) y un documento de máximo 5 páginas en donde se exponga: 

1- La motivación para el desarrollo del proyecto
2- El tema principal de inteligencia artificial abordado
3- funcionamiento y simulación del proyecto


- **Preguntas**: Se realizarán preguntas cortas a los estudiantes unicamente relacionadas con el proyecto. 
 
Todos los items tienen el mismo porcentaje de evaluación. 

- **PRE-SUS PROJ**: En la presustentación del proyecto se deben presentar avances y se dará un estimado de la nota definitiva. En las siguientes semanas se tendrá chance de mejorar la nota según previas observaciones. 


## Online Courses (MOOC) [Extra]

El avance vertiginoso de la tecnología nos obliga a adquirir destresas en el aprendizaje autónomo. Sobre todo en lo relacionado con tecnologias de la información, existen numerosos recursos virtuales que nos permiten estar actualizados con nuevos temas, estrategias y desarrollos. Teniendo en cuenta esta motivación, como parte complementaria del curo se tendrá en cuenta un porcentaje extra para los estudiantes que deseen realizar un MOOC online. El MOOC habrá de tratar un topico relacionado con la tecnología y ha de cubrir aproximadamente 15 horas de esfuerzo, que se evaluarán según la definición y dinámica de cada caso. Puedes hacerlo en cualquier plataforma existente, como por ejemplo: [Coursera](www.coursera.org), [EDX](www.edx.org), [Udacity](www.udacity.org),  [MiriadaX](https://miriadax.net/), etc.

Tendras que hacer un informe de tu seguimiento del MOOC. La entrega ha de constar de:

- Un archivo PDF llamado MOOC_descripcion.pdf donde se describa el MOOC (primera entrega)
- Un archivo PDF llamado MOOC_completado.pdf donde se incluya la evidencia de la realizacin del MOOC
- Un directorio llamado MOOC_materiales donde se incluyan los materiales pertinentes (scripts, datos, etc.) que apoyen la evidencia mostrada en el archivo PDF.

**TODA ENTREGA QUE NO CUMPLA CON ESTAS CONVENCIONES SERÁ CONSIDERADA COMO NO REALIZADA**

La calificación del curso vendrá dada por los siguientes criterios con el mismo peso cada uno:

- COMPLEJIDAD DEL MOOC
- CALIDAD DEL REPORTE 
- CLARIDAD DEL REPORTE

**UNICAMENTE SE TENDRAN EN CUENTA LOS MOOC QUE SE HAYAN POSTULADO AL FINALIZAR EL PRIMER CORTE**


## Calendario y plazos

                        SESSION 1            SESSION 2           STUDENT DEADLINES

     W01 Sep16-Sep20    0.Intro            1.PYTHON
     W02 Sep23-Sep27    2.PANDAS           3.STATS
     W03 Sep30-Oct04    3.STATS-PSETS      4.BAYES
     W04 Oct07-Oct11    4.BAYES-PSETS      QUIZPREP           PSETS FIRST DEADLINE
     W05 Oct14-Oct18    QUIZ               5.MLCLASS          Festivo 14 Octubre
     W06 Oct21-Oct25    6.MLREG            7.MLMETH           Oct26 Registro primera calificación
     W07 Oct28-Nov01    8.NAIVE            8.IMGCLASS
     W08 Nov04-Nov08    8.DeepL            9.DeepL-PSETS      Festivo 04 Noviembre
     W09 Nov11-Nov15    10.PRE-SUS PROJ    QUIZPREP           Festivo 11 Noviembre
     W10 Nov18-Nov22    QUIZ               13.KMEANS          PSETS SECOND DEADLINE
     W11 Nov25-Nov29    13.KMEANS          14.PLAN
     W12 Dic02-Dic06    0.PLAN-SETS        15.GA
     W13 Dic09-Dic13    0.GA-PSETS         14.SA
     W14 Dic16-Dic20    QUIZPREP           QUIZ               Vacaciones - (Diciembre 23 - Enero 15)
     W15 Ene13-Ene17    PROJECT            PROJECT


    Oct26 -        -> Registro primera calificación
    Oct27 -        -> Último día cancelación materias
    Dic23-Ene15    -> Vacaciones docentes
    Ene29 -        -> Finalización clase
    Ene30-Feb08    -> Evaluaciones finales
    Feb08 -        -> Registro calificaciones finales
    
[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2019/acuerdoAcad064_2019.pdf)

**CUALQUIER ENTREGA FUERA DE PLAZO SERÁ PENALIZADA CON UN 50%**
**LOS PROBLEMSETS ESTAN SUJETOS A CAMBIOS QUE SERÁN DEBIDAMENTE INFORMADOS%**
