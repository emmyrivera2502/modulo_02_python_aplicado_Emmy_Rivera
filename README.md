PREGUNTAS DE RAZONAMIENTO TRABAJO FINAL MES 2

-----Etapa 1

1. ¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a  limpiar directamente desde la 
primera columna que veas?
.. Bueno, simplemente porque lo mas preferible es que antes de comenzar a editar, evalues las columnas con mas valores nulos para poder corregirlas.
Ademas, siempre es bueno observar primero y despues actuar.

-----Etapa 2

2. ¿Qué pasaría si rellenaras Budget con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna Ganancia que vas a crear en la
próxima etapa?
.. Eso afectaria directamente a la nueva columna que creamos llamada "Ganancia". Esta columna se hizo restando el Budget con el WorldGross,
significando que si hubieramos puesto 0 en todos los valores vacios, ese cero me afectaria en dicha ecuacion. 

-----Etapa 3

3. Ganancia se calcula restando (WorldGross - Budget). ¿Qué representaría, en cambio, una columna que dividiera WorldGross entre
Budget? ¿En qué caso preferirías esa versión en vez de la resta?
.. La columna WorldGross entre el Budget representaría cuántas veces la película recuperó su presupuesto mediante sus ingresos mundiales.
Preferiría la división cuando quiero comparar películas de diferentes presupuestos y medir qué tan eficiente fue una película respecto 
al dinero que costó hacerla. La resta muestra cuánto dinero hay de diferencia, mientras que la división muestra el rendimiento en 
proporción al presupuesto.


-----Etapa 4

4. ¿Qué habría pasado si hubieras intentado ordenar por Ganancia antes de limpiar los nulos de WorldGross y Budget en la Etapa 2? ¿Por qué
el orden en que se hacen las etapas importa aquí?
.. Basicamente, lo que hubiera pasado es que las peliculas que tuvieran valores vacios tambien hubieran tenido la Ganancia vacia. El orden importa
mucho porque como vemos con este ejemplo, si no sigues el orden de revisar tus datos y valores nulos antes de realizar cualquier otra cosa, las
cosas pueden saslir mal.

-----Etapa 5

5.  De los géneros con más películas en el dataset (Comedia, Acción, Drama), ¿cuál tiene el promedio de calificación de crítica más alto? ¿Te
sorprende, o era lo que esperabas?
.. De los tres géneros con más películas, Drama tiene el promedio de calificación más alto en Rotten Tomatoes, superando a Acción y Comedia.
El resultado realmente no me sorprenden, ya que las peliculas en el Genre de Drama suelen tener mas profundidad en la trama que peliculas de 
Accion y Comedia, lo que las hace mas propensas a obtener mayores calificaciones.

-----Etapa 6

6. ¿Por qué guardar el resultado en un archivo nuevo (hollywood_limpio.csv), en vez de sobrescribir el archivo original hollywood.csv que
descargaste?
.. Guardar el resultado en un archivo nuevo como hollywood_limpio.csv permite conservar el dataset original sin modificaciones. Esto es 
importante porque el archivo original funciona como una fuente de respaldo a la que podemos regresar si cometemos algún error durante la 
limpieza o necesitamos aplicar un procedimiento diferente. 

Respuestas a preguntas de la seccion "Escenarios: ¿qué harías si...?"

ESCENARIO 1
Si el dataset tuviera una columna de fechas completas (día, mes y año) en vez de solo el año, ¿qué tendrías que verificar antes de 
poder ordenar el dataset cronológicamente por esa columna?
.. Bueno, yo verificaria si el formato de las fechas esta correcto y si hay algun valor nulo en las fechas.

ESCENARIO 2
Si quisieras aplicar este mismo pipeline a un dataset completamente distinto (por ejemplo, canciones con su artista, género y número de
reproducciones), ¿qué partes de tu código cambiarían, y cuáles seguirían exactamente igual?
..  Yo cambiaria las partes especificas de mi codigo y los adaptaria a las necesidades de ese dataset. Por ejemplo, cambiaria la operacion de 
budjet con World gross. Ahora, las partes que seguirian igual son las etapas, osea el orden en el que se hace el proceso.

ESCENARIO 3
Si una columna nueva tuviera 95% de sus valores nulos (mucho peor que Genre, que tenía cerca del 29%), ¿seguirías rellenándola de la misma
forma? ¿Qué harías distinto, y por qué?
.. Definitivamente no la rellenaria de la misma manera. Yo considero que si tiene el 95% de datos nulos, realmente hay demasiado que rellenar
y pocos datos para trabajar. Entonces, en lo personal yo la eliminaria. 
