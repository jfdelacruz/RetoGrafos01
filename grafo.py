def numero_aristas_grafo(key_vertice,grafo : dict )-> int:
    # Uso de un try y except para el caso de que un vertice no exista en el grafo
    # en caso de no estar se retornara el valor de -1
    try:
        lista_aristas=list(grafo[key_vertice])
        numero_aristas=len(lista_aristas)
    except KeyError:
        numero_aristas=-1 # -1 para indicar que el vertice no esta en el grafo
    return numero_aristas

G={"a":["c"],
   "b":["c","e"],
   "c":["a","b","d","e"],
   "d":["c"],
   "e":["c","b"],
   "f":[]
   }
print(numero_aristas_grafo("c",G))
