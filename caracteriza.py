# Módulo que permite realizar preguntas, almacenar en diccionario.
# Ütil para hacer una caracterización de un objeto
# git-hub url: https://github.com/grumot/CLI

import os
from prettytable import PrettyTable

# Esta función puede ser innecesaria
def crea_lista_preguntas():
    '''Crea una lista con las palabras clave que seran preguntas.
       Son características de un objeto cualquiera a describir.
       Ej. Color, sabor, longitud, peso, etc.'''
        
    preguntas = []
    pregunta = ""

    num_preguntas = int(input("Numero de preguntas -> "))
    for n in list(range(num_preguntas)):
        pregunta = input("Palabra clave %i: " % (n))
        preguntas.append(pregunta)
        
    return preguntas

    
    
    
def crea_diccio_vacio(lista_palabras_clave):
    '''Retorna un diccionario cuyas palabras clave, son la lista suministrada.
       Ej. {'Color': "", 'Sabor': ""}'''
    
    dic = {}
    for palabra in lista_palabras_clave:
        dic[palabra] = ""
    
    return dic




def hace_preguntas(lista_preguntas):
    '''1- Imprime en pantalla un conjunto de preguntas (lista_preguntas)
       2- Crea un diccionario cuya palabra clave es (lista_preguntas)
       3- Almacena las respuestas en el diccionario
       4- Devuelve el diccionario completo'''
    
#    print(encabezado + "\n") # Introduccion al usuario del tipo de preguntas a 
                             # responder
    
    palabras_clave = lista_preguntas
    diccio_completo = crea_diccio_vacio(palabras_clave) 
     
    for palabra_clave in palabras_clave:                                   
        diccio_completo[palabra_clave] = input(palabra_clave + ": ")
        
    return diccio_completo
    
    


def muestra_respuestas(dic_respuestas):
    '''Imprime las respuestas almacenadas en el diccionario suministrado'''
    
    os.system(clear)
    for e in dic_respuestas:
        print(e + ": " + str(dic_respuestas[e]))
        
        
        
def tabla_rta(titulo_tabla, diccionario):
    '''Muestra las respuestas como la funcion muestra_respuestas(), pero
       en una tabla.
       '''
    tabla = PrettyTable()  #Usa la librería prettytable para crear una tabla
    
    titulos = []
    valores = []
    
    # Saca las llaves del diccionario y las añade a la lista: titulos
    # al mismo tiempo añade los valores a la otra lista: valores
    
    for titulo in diccionario:
           titulos.append(titulo) 
           valores.append(diccionario[titulo]) 
           
    tabla.field_names = titulos # Añade los títulos a la tabla creada
    tabla.add_row(valores) # añade los valores a la tabla
       
    print(tabla.get_string(title=titulo_tabla))
        
        
        
def caracteriza(cadena_intro, lista_rasgos):
    '''Devuelve un dicionario que contiene las caracteristicas de un objeto
       cualquiera, previamente preguntadas al usuario
       
       cadena_intro, es el texto introductorio que pone en contexto al usuario
       lista_rasgos, son cada característica del objeto 
    
        Esta funcion podría ser utilizada para inicializar objetos?
    '''
    os.system('clear')
    print(cadena_intro + "\n")
    diccio_rasgos = hace_preguntas(lista_rasgos)
    
    return diccio_rasgos
        
        
        
#La siguiente función necesita ser reevaluada
def menu_principal(mensaje_intro, lista_opciones):
    '''Retorna un CLI con opciones a escoger
        lista_opciones: Es una lista con palabras que corresponden
            a cada elemento del menu
            
        mensaje_intro: Es el encabezado que pone en contexto el menu'''
    
    print(mensaje_intro + "\n\n")
    
    for index, opcion in enumerate(lista_opciones):
        print("[%i] %s" % (index, opcion))
        

        
        
#resp = menu_ingreso_datos(preguntas) # Crea el diccionario con las respuestas
#muestra_respuestas(resp)
                                                            

