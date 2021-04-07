import re

def printMatrix(M):
    cantFilas = len(M)
    cantColumnas = len(M[0])
    for i in range(cantFilas):
        for j in range(cantColumnas):
            print(str(M[i][j]).ljust(10," "),end = " ")
        print("\n")
    print()

file = open("./in.txt")
string = file.read()
#print(f"Esta es la string:\n{string}")
q0 = re.search("\s*q0\s*=\s*.*\s",string)
q0 = q0.group()
#print("Este es q0 :\n%r"%q0)
q0 = re.sub('\s*q0\s*=\s*','',q0)
q0 = q0.strip()
#print("Este es q0 masterizado:\n%r"%q0)
tripletas_eps = re.findall(".*\s*-\s*>\s*eps\s*-\s*>.*",string)
string = re.sub(".*\s*-\s*>\s*eps\s*-\s*>.*","",string)
tripletas = re.findall(".*\s*-\s*>\s*.*\s*-\s*>.*",string)
#print(f"1er intento :{tripletas}")
Alfabeto = set()
Estados = set()
aux = []
for s in tripletas:
    s = re.sub(" ","",s)
    s = s.split("->")
    Estados.update([s[0],s[2]])
    Alfabeto.add(s[1])
    aux.append((s[0],s[1],s[2]))
    #print(f"Del estado {s[0]} con el caracter {s[1]} vamos al estado {s[2]}")
tripletas = aux
#print(f"Estas son las tripletas 1er intento: {tripletas}")
Estados = sorted(Estados)
Estados.append('Pozo')
Alfabeto = sorted(Alfabeto)
Tabla = []
#EpsClausura = []
for i in range(len(Estados)):
    Columna = []
    #ColumnaEpsClausura = []
    for j in range(len(Alfabeto)):
        Columna.append({'Pozo'})
        #ColumnaEpsClausura.append(set())
    Tabla.append(Columna)
    #EpsClausura.append(ColumnaEpsClausura)

#print("Esta es una Tabla llena de Pozos crudos: ")
#print(Tabla)
#print("Esta es una Tabla llena de Pozos")
#print(f" Estos son los estados : {Estados} ")
#print(f" Este es el alfabeto : {Alfabeto} ")
#printMatrix(Tabla)
#print(f"Estas son las tripletas: {tripletas}")
for t in tripletas:
    #print()
    #print(t)
    #print(f"Estados.index({t[0]}): {Estados.index(t[0])}")
    #print(f"Alfabeto.index({t[1]}):{Alfabeto.index(t[1])}")
    if(Tabla[Estados.index(t[0])][Alfabeto.index(t[1])] == {'Pozo'}):  
        Tabla[Estados.index(t[0])][Alfabeto.index(t[1])] = {t[2]}
    else:
        Tabla[Estados.index(t[0])][Alfabeto.index(t[1])].add(t[2])
#print(f"Esta es la tabla cruda: {Tabla}")
#print("Esta es la tabla")
#printMatrix(Tabla)

Tabla_eps = []

for i in range(len(Estados)):
    Tabla_eps.append(set())

for t in tripletas_eps:
    t = re.sub(" ","",t)
    t = t.split("->")
    Tabla_eps[Estados.index(t[0])].add(t[2])

for i in range(len(Estados)):
    # i = voy a ver a todos los elementos que puedo 
    # llegar desde Estados[i] y guardarlos como un
    # set en Tabla_eps[i]
    Alcanzados = {Estados[i]} 
    Pendientes = {Estados[i]} 
    #print(f"Voy a calcular Eps Clausura del estado {Estados[i]}")
    while(len(Pendientes) > 0):
        #print()
        #print(f"Pendientes: {Pendientes}")
        #print("Evaluar Pendientes != {} da :  ",end = "")
        #print(Pendientes != {})
        #print(f"Pendientes largo: {len(Pendientes)}")
        try:
            Elemento_A_Analizar = Pendientes.pop()
        except KeyError:
            print(f"Error: Intentaste hacer pop del conjunto {Pendientes}")
        if( Estados.index(Elemento_A_Analizar) < i ):
            Alcanzados = Alcanzados | Tabla_eps[ Estados.index(Elemento_A_Analizar) ]
            Pendientes = Pendientes -  Tabla_eps[ Estados.index(Elemento_A_Analizar) ]
        else:
            Alcanzados = Alcanzados | Tabla_eps[ Estados.index(Elemento_A_Analizar) ]
            #Pendientes unión los nuevos que puedo alcanzar con las transiciónes eps de Tabla_eps[...]
            # que no estaban ni en pendientes ni en Alcanzados
            Pendientes = Pendientes | ( Tabla_eps[ Estados.index(Elemento_A_Analizar) ] - Alcanzados)
        #endif
    #endwhile
    Tabla_eps[i] = Alcanzados

def esDelLenguaje(tira):
    global Tabla
    global Tabla_eps
    global Estados
    global Alfabeto
    estados = {q0} | Tabla_eps[Estados.index(q0)]
    #print(f"Los estados al arrancar son:{estados} ")
    #print(f"La tira que debo analizar: {tira}")
    for c in tira:
        #print(f"Dame una {c}")
        #print(f"Los estados actuales son :{estados} ")
        nuevos_estados = set()

        #consumo un caracter
        #en estados guardo todos los estados a los que llego luego de
        #consumir el caracter c
        for e in estados:
            #print(f"Estados.index(e): {Estados.index(e)}")
            #print(f"Alfabeto.index({c}):{Alfabeto.index(c)}")
            nuevos_estados = nuevos_estados | Tabla[Estados.index(e)][Alfabeto.index(c)]
        estados = nuevos_estados.copy()

        #no consumo ningún caracter
        #en estados guardo todos los estados a los que llego con las
        #transiciones eps
        for e in estados:
            nuevos_estados = nuevos_estados | Tabla_eps[Estados.index(e)]
        #endfor

        estados = nuevos_estados

    for e in estados: 
        if(e.startswith('.')):
            return True
    return False

def generador(tira,largo):
    global tiras
    if(largo == 0):
        tiras.append(tira)
    else:
        for c in Alfabeto:
            generador(tira + c,largo - 1)

try:
    tiras_file = open("./tiras.txt")
    tiras = tiras_file.read()
    tiras_file.close()
    tiras = tiras.split("\n")
except FileNotFoundError:
    largo = input("Ingrese el largo tope a analizar:") 
    largo = int(largo) + 1
    tiras = [] 
    for x in range(largo):
        generador("",x)

for i in range(len(tiras)):
    tiras[i] = tiras[i].strip()
#print(f"Las tiras que tengo que analizar son:\n{tiras}")
salida = open("./salida.txt","w")
#print("La Tabla:")
#printMatrix(Tabla)
for t in tiras:
    #print(f"La tira que voy a procesar: {t}")
    salida.write(t)
    if(esDelLenguaje(t)): 
        salida.write(" Yes\n")
    else:
        salida.write(" No\n")
salida.close()
#check
try:
    check = open("./check.txt","r")
    check_string = check.read()
    check.close()
    check_string = check_string.strip()
    unaTira = re.compile(check_string,re.MULTILINE)
    tiraYes = re.compile("\s*Yes\s*")
    tiraNo = re.compile("\s*No\s*")
    tiraVacia = re.compile("\s*")
    salida = open("./salida.txt","r")
    string = salida.read()
    salida.close()
    lines = re.compile("^.*$",re.MULTILINE) 
    info = lines.findall(string)
    check_bool = True
    for i in range(len(info)):
        if(tiraYes.fullmatch(info[i])):
           aux = ["","Yes"] 
        elif(tiraNo.fullmatch(info[i])):
            aux = ["","No"]
        elif(tiraVacia.fullmatch(info[i])):
            pass
        else:
            aux = info[i].split()
        #print(f"aux vale {aux}")
        if(unaTira.fullmatch(aux[0]) and tiraNo.fullmatch(aux[1])):#reconoce la Regex pero no el AF
            print(f"La tira {aux[0]} SI cumple con la expresión regular: {check_string} pero NO es reconocida por el autómata") 
            check_bool = False 
            break
        elif(not(unaTira.fullmatch(aux[0])) and tiraYes.fullmatch(aux[1])):#reconoce AF pero no la Regex
            print(f"La tira {aux[0]} NO cumple con la expresión regular: {check_string} pero SI es reconocida por el autómata") 
            check_bool = False 
            break
    if(check_bool == True): 
        print("La evidencia indica que el autómata reconoce las mismas tiras que la expresión regular para las tiras procesada")
except FileNotFoundError:
    pass
finally:
    pass
print("Gracias por usar este programa")
