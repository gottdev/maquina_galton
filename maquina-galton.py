import random        #libreria que ayuda con numeros aleatorios
import matplotlib.pyplot as plt #nos ayuda a pintar grafica en pantalla
import numpy as np



# funcion que genera el arreglo con las posiciones de las pelotas
def maquina_galton ( level , bals ): 
    resultados = np.zeros(level+1) #devuelve un arreglo de el tamano indicado

    for j in range(bals): #inciamos un ciclo for para el recorrido de cada pelota
        pos = 0

        for i in range(level): # vamos recorriendo cada nivel
           direccion = random.randint(0,1) #utilizo random para generar un numero aleatorio entre el 0 y 1
           pos += direccion #suma la posicion dependiendo si es derecha o izquierda

        resultados[pos] += 1 #agrega al arreglo el resultado final

    return resultados #retornamos el arreglo ya con los datos almacenados


#funcion  que pinta la grafica
def grafica_maquina_galton(level , bals):
    resultados = maquina_galton(level , bals)#llamamos a la funcion que ejecuta la maquina de galton 
    print(resultados)
    # genera la grafica pasandole 2 arreglos
    # la funcion arange genera
    # el segundo parametro es el arreglo con los resultados de la grafica 
    plt.bar(np.arange(len(resultados-1)),resultados)
    plt.title('MAQUINA DE GALTON')#cambia el titulo de la grafica
    plt.show()#permite visualizar la grafica


if __name__ == '__main__':
    grafica_maquina_galton(12 , 3000)