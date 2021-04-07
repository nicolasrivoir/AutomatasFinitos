Hola, Gracias por usar este programa. 

El propósito del mismo es crear un entorno amigable donde se pueda hacer uso de los autómatas finitos.
Cuenta con una primera etapa que se encarga de leer los datos de archivos de entrada donde se lee la 
definición del lenguaje y las tiras a leer. Luego una segunda parte que genera la salida tras correr 
las tiras en el autómata definido.


Cómo usarlo?

	Para hacer un correcto uso se debe crear un archivo con el nombre "in.txt" cuyo contenido será la información de la máquina autómata determinista.
	Cada renglón del texto será de la forma "tag_i -> x -> tag_j" donde los "tags" y "x" pueden ser cualquier secuencia de caracteres.
	Los tags son los nombres designados a los estados de la máquina de estados, en el ejemplo estamos declarando que la función de transición
	al estar en el estado "tag_i" y recibir en la entrada el caracter "x" pasará a estar en el estado "tag_j". El orden de la declaración no afecta
	el comportamiento de la misma. Las transiciones que no sean declaradas irán a un estado de no aceptación llamado "Pozo". 

	El programa se puede usar de 2 formas:
	
	1ra:
		Se crea un archivo con el nombre "tiras.txt". En el mismo se pone todas las tiras del lenguaje que se quieren reconocer. Los caracteres
		usados en el lenguaje deben aparecer al menos una vez en el archivo "in.txt". Si un renglón se encuentra vacío a menos de espacions y 
		tabuladoses se toma como la tira vacía.	

	2da:
		Si el programa no recibe un archivo "tiras.txt" procede a pedir un valor desde la terminal. Este valor le indicará que tiene que calcular si el
		autómata reconoce todas las tiras de sigma aster cuyo largo sea menor o igual al de ese valor.

	Luego ejecutamos el main.py con python 3 parados en la ruta donde se encuentra el archivo "main.py". La salida del programa se encontrará en un archivo llamado "salida.txt" cuyo contenido tenrá un renglón por cada uno de las tiras analizadas
	con un indicador "Yes" en caso de que la tira haya sido reconocida, y "No en caso contrario.

Definir q0

	Uno y solo uno de los renglones del archivo "in.txt" deberá tener la forma "q0 = tag_0", donde tag_0 sigue el mismo formato que el resto de los tags.

Definir Estados Finales

	Para definir estados finales el tag del mismo deberá comenzar con un "."

Definir AFND

	Solo se debe definir más de una transición de un estado con un mismo caracter. Con el mismo formato que las demás transiciones. 

Definir AFND-eps

	Si en la declaración de una transición escribimos "eps" como caracter de entrada,el programa entiende que usa transición epsilon.

Checkear si un AF = ER

	El programa cuanta con una funcionalidad que permite verificar si una expresión regular conicide con las salidas de el autómata definido.
	Para esto lee la expresión regular declarad en el archivo "check.txt". El uso de esta funcionalidad es opcional, la falta de este archivo
	no afecta la ejecución del resto del programa. El propósito será verificar si hay evidencia que indique que ambos podrian llagar a 
	reconocer el mismo lenguaje, de lo contrario no desplega un contraejemplo en pantalla. Tener en cuenta que solo verifica en el rango de tiras de "tiras.txt"
	o en el rango de tiras menores a un largo dado dependiendo el uso que se le de al programa.

Cualquier error, duda o sugerencia dejá un mensaje en nicolas.rivoir@fing.edu.uy. Espero que te sea de utilidad !!! :)
