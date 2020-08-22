<!-- # Inteligencia Artificial I 2019-2 -->

# Inteligencia Artificial I 2020-1

## Bienvenidos!

<img src="/imgs/img_IA.jpg" style="width:400px;">

<!-- _Regístrate [aquí](https://forms.gle/DE1TkzdpReve7h8Q8) -->
                                            
La máquina virtual puede descargarse [aquí](https://drive.google.com/open?id=1lymG9E3m6tjblZinOQGDemxc_ZtFFCOW)

## Colaboratory (Google)

Vamos a utilizar la plataforma de google para editar, compartir y correr notebooks: [**Colaboratory**](https://colab.research.google.com/notebooks/welcome.ipynb) 

- Necesitas una cuenta de gmail y luego entras a drive
- Colaboratory es un entorno de notebook de Jupyter gratuito que no requiere configuración y se ejecuta completamente en la nube.
    - Usaremos parte de la infraestructura de computo de google... gratis! (máximo procesos de 8 horas)
- Con Colaboratory, puedes escribir y ejecutar código, guardar y compartir análisis, y acceder a recursos informáticos potentes, todo gratis en tu navegador.
- También puedes usar los recursos de computador Local. 

## Máquina Virtual

Alternativamente, usaremos una máquina virtual que tiene instalado un entorno Anaconda con Jupyter Notebooks disponibles en  [localhost:8008/tree](http://localhost:8008/tree) una vez que la máquina arranca.

- Esta opción es util para contestar talleres y para trabajar desde casa. 
- También para contestar parciales desde la U.

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

- **Poster**: 
en donde se muestra: título del proyecto, abstract (resumen), introducción, y:<br>
1. La motivación para el desarrollo del proyecto
2. El tema principal de inteligencia artificial abordado
3. Funcionamiento y simulación del proyecto<br>
El poster debe elaborarse utilizando la siguiente plantilla: [Descargar plantilla](https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-uis-student/-/raw/master/projects/TemplateSystemsFest_IA2020-1.pptx)<br>
Se entrega en formato PPTX (PowerPoint) y en formato PDF.

- **Sustentación**: Se realizarán preguntas cortas a los estudiantes unicamente relacionadas con el proyecto. 
 
Todos los items tienen el mismo porcentaje de evaluación. 

<!-- - **PRE-SUS PROJ**: En la presustentación del proyecto se deben presentar avances y se dará un estimado de la nota definitiva. En las siguientes semanas se tendrá chance de mejorar la nota según previas observaciones. -->


<!--## Online Courses (MOOC) [Extra]

El avance vertiginoso de la tecnología nos obliga a adquirir destrezas en el aprendizaje autónomo. Sobre todo en lo relacionado con tecnologias de la información, existen numerosos recursos virtuales que nos permiten estar actualizados con nuevos temas, estrategias y desarrollos. Teniendo en cuenta esta motivación, como parte complementaria del curso se tendrá en cuenta un porcentaje extra para los estudiantes que deseen realizar un MOOC online. Puedes hacerlo en cualquier plataforma existente, como por ejemplo: [Coursera](www.coursera.org), [EDX](www.edx.org), [Udacity](www.udacity.org),  [MiriadaX](https://miriadax.net/), etc.

Tendras que hacer un informe de tu seguimiento del MOOC. La entrega ha de constar de:

- Un archivo PDF llamado MOOC_descripcion.pdf donde se describa el MOOC (primera entrega)
- Un archivo PDF llamado MOOC_completado.pdf donde se incluya la evidencia de la realización del MOOC
- Un directorio llamado MOOC_materiales donde se incluyan los materiales pertinentes (scripts, datos, etc.) que apoyen la evidencia mostrada en el archivo PDF.

**TODA ENTREGA QUE NO CUMPLA CON ESTAS CONVENCIONES SERÁ CONSIDERADA COMO NO REALIZADA**

La calificación del curso vendrá dada por los siguientes criterios con el mismo peso cada uno:

- COMPLEJIDAD DEL MOOC
- CALIDAD DEL REPORTE 
- CLARIDAD DEL REPORTE

**UNICAMENTE SE TENDRAN EN CUENTA LOS MOOC QUE SE HAYAN POSTULADO AL FINALIZAR EL PRIMER CORTE**-->


## Calendario y plazos

                        SESSION 1            SESSION 2              SESSION SATURDAY

     W01 May19-May20    Intro                Python (a)            
     W02 May26-May27    Python (b)           Pandas (a)
     W03 Jun02-Jun03    Pandas (b)           Estadística
     W04 Jun09-Jun10    Estadística          Talleres
     W05 Jun16-Jun17    Aclaraciones         Aclaraciones           Parcial 1
     W06 Jun23-Jun24    Intro A.M.S.         Clasificación A.M.S.
     W07 Jun30-Jul01    Regresión A.M.S.     Métodos A.M.S. (a)
     W08 Jul07-Jul08    Métodos A.M.S. (b)   Aplicación A.M.S.
     W09 Jul14-Jul15    Deep Learning (a)    Deep Learning (b)
     W10 Jul21-Jul22    Aclaraciones         Aclaraciones           parcial 2
     W11 Jul28-Jul29    Intro A.M.N.S.       K-means A.M.N.S.
     W12 Ago04-Ago05    DBScan A.M.N.S.      PRE-SUS PROJ
     W13 Ago11-Ago12    Planning and S.      Genetic Alg.
     W14 Ago18-Ago19    Simulated anne.      Aclaraciones
     W15 Sep01-Sep02    Aclaraciones         Aclaraciones           Parcial 3
     W16 Sep08-Sep09    Systems Fest         Systems Fest
     W17 Sep15-Sep16    TBA                  TBA


    Jul 05 -           -> Retroalimentación estudiantes
    Jul 17 -           -> Último día cancelación materias
    Sep 9 - Sep 11     -> Systems Fest (proyectos finales)
    Sep 11             -> Finalización clase
    Sep 12 - Sep 18    -> Evaluaciones finales
    Sep 19 -           -> Registro calificaciones finales
    
<!--[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2019/acuerdoAcad064_2019.pdf)-->
<!--[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2019/acuerdoAcad314-2019.pdf)-->
<!--[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2020/acuerdoAcad001_2020.pdf)-->
[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2020/acuerdoAcad104_2020.pdf)

**CUALQUIER ENTREGA FUERA DE PLAZO SERÁ PENALIZADA CON UN 50%**

**LOS PROBLEMSETS ESTAN SUJETOS A CAMBIOS QUE SERÁN DEBIDAMENTE INFORMADOS**

**DEADLINE DE LOS PROBLEMSETS SERÁ EL DIA DE CADA QUIZ**

