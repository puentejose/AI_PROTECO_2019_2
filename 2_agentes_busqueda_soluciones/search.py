#-*- coding: utf-8 -*-
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#Traducido al español por Juan Antonio Fonseca Méndez;
#segunda edición por Nicky García Fierros para el curso de
#Inteligencia Artificial PROTECO 2017-2 UNAM


"""
En search.py, implementamos los algoritmos de busqueda genericos, que son
llamados por los agentes Pacman (en searchAgents.py)
"""

import util

class SearchProblem:
    """
    Esta clase establece la estructura de un problema de busqueda,
    pero no implementa ninguno de los metodos.

    No es necesario que modifiques absolutamente nada de esta clase, jamas.
    """

    def getStartState(self):
        """
        Regresa el estado inicial del problema de busqueda
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Estado de busqueda

        Regresa True si, y solo si, el estado es una meta valida.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: estado de busqueda

        Para un estado dado, esto deberia regresar una lista de tripletas
        (successor, action, stepCost), donde es el sucesor del estado actual,
        'action' es la accion requerida para llegar ahi y 'stepCost' es el costo
        de expandir ese nodo
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: Una lista de acciones por hacer

        Este metodo regresa el costo total de una secuencia particular de acciones
        Debe estar compuesta por movimientos legales.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Regresa una secuencia de movimientos que soluciona tinyMaze. Para cualquier
    otro laberinto, la secuencia de movimientos es incorrecta.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """ Cómo probarlo:
        python pacman.py -l tinyMaze -p SearchAgent

        python pacman.py -l mediumMaze -p SearchAgent

        python pacman.py -l bigMaze -z .5 -p SearchAgent
    """

    """
    Search the deepest nodes in the search tree first.

    Tu algorimto debe regresar una lista de acciones que alcancen la meta
    Asegurate de implementar el algoritmo de busqueda por grafo

    Para iniciar, puede que te interese probar estos comandos simples para
    entender el problema que esta siendo pasado

    print "Inicio:", problem.getStartState()
    print "El inicio es una meta?", problem.isGoalState(problem.getStartState())
    print "Sucesores del inicio:", problem.getSuccessors(problem.getStartState())

    Las impresiones anteriores (comentadas) imprimen:
        Inicio: (5, 5)
        El inicio es una meta? False
        Sucesores del nodo inicial: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    """
    "*** Tu codigo aqui ***"

    # Estrategia DFS: Usar contenedor LIFO (Pila)
    pila = util.Stack()

    # Lista que almacena los nodos visitados
    visitados = []

    # Lista que almacenará los pasos tomados para llegar al estado
    plan = []

    # Un nodo consiste en: ((x, y), 'ACCION')
    # donde (x, y) es la tupla que contiene las coordenadas
    # y la ACCION es el movimiento realizado para llegar al estado
    # (North, South, East, West)
    pila.push( ( problem.getStartState(), plan ) )

    # Mientras todavia tenga nodos en la pila...
    while( not pila.isEmpty() ):

        # Obtengo las coordenadas de la posición de Pacman y el movimiento
        # realizado para llegar al estado del nodo contenido en la pila.
        edo_act, plan = pila.pop()

        # Si el estado actual no es un estado meta...
        if not problem.isGoalState(edo_act):

            # Si el estado actual no se encuentra visitado...
            if edo_act not in visitados:

                # Marcamos el estado actual como visitado
                visitados.append(edo_act)


                # El método getSuccessors(state) regresa una lista con los nodos
                # sucesores del estado 'state' con el siguiente formato:
                # [((x_1, y_1), 'DIRECCION', COSTO), ((x_2, y_2), 'DIRECCION', COSTO), ....]
                # Donde DIRECCION puede tomar los valores (North, South, East, West) y
                # el costo es un entero.

                # Por cada hijo dentro de la lista de sucesores...
                for hijo in problem.getSuccessors(edo_act):
                    # Los insertamos en la pila con el siguiente formato:
                    # ( (x, y), [LISTA DE ACCIONES TOMADAS PARA LLEGAR AL ESTADO] )
                    pila.push( ( hijo[0], plan+[hijo[1]]) )
        else:
            # Si el estado es un estado meta, terminamos la ejecución del algoritmo
            break

    # Regresamos la lista de acciones tomadas para llegar al estado meta.
    return plan

def breadthFirstSearch(problem):
    """
    Busca el nodo menos profundo

    Para probarlo puedes utilizar los siguientes comandos:

        python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

        python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
    """

    "*** Tu codigo aqui ***"
    # Estrategia BFS: Usar contenedor FIFO (Cola)
    cola = util.Queue()

    # Lista que almacena los nodos visitados
    visitados = []

    # Lista que almacenará los pasos tomados para llegar al estado
    plan = []

    # Un nodo consiste en: ((x, y), 'ACCION')
    # donde (x, y) es la tupla que contiene las coordenadas
    # y la ACCION es el movimiento realizado para llegar al estado
    # (North, South, East, West)
    cola.push( ( problem.getStartState(), plan ) )

    # Mientras todavia tenga nodos en la cola...
    while( not cola.isEmpty() ):

        # Obtengo las coordenadas de la posición de Pacman y el movimiento
        # realizado para llegar al estado del nodo contenido en la cola.
        edo_act, plan = cola.pop()

        # Si el estado actual no es un estado meta...
        if not problem.isGoalState(edo_act):

            # Si el estado actual no se encuentra visitado...
            if edo_act not in visitados:

                # Marcamos el estado actual como visitado
                visitados.append(edo_act)


                # El método getSuccessors(state) regresa una lista con los nodos
                # sucesores del estado 'state' con el siguiente formato:
                # [((x_1, y_1), 'DIRECCION', COSTO), ((x_2, y_2), 'DIRECCION', COSTO), ....]
                # Donde DIRECCION puede tomar los valores (North, South, East, West) y
                # el costo es un entero.

                # Por cada hijo dentro de la lista de sucesores...
                for hijo in problem.getSuccessors(edo_act):
                    # Los insertamos en la cola con el siguiente formato:
                    # ( (x, y), [LISTA DE ACCIONES TOMADAS PARA LLEGAR AL ESTADO] )
                    cola.push( ( hijo[0], plan+[hijo[1]]) )
        else:
            # Si el estado es un estado meta, terminamos la ejecución del algoritmo
            break

    # Regresamos la lista de acciones tomadas para llegar al estado meta.
    return plan

def uniformCostSearch(problem):
    """
    Busca el nodo con el costo total menor.
    Para probarlo puedes utilizar los siguientes comandos:

    

    """
    "*** Tu codigo aqui ***"
    # Variable que almacena el costo de la ruta
    costoDeRuta = heuristic(problem.getStartState(), problem)

    # Lista que almacena el camino tomado para llegar al nodo
    rutaAlNodo = []

    # Variable que almacena el nodo actual. Un nodo consta de
    # una tupla con una tupla con coordenadas (x,y), la ruta al nodo y el coste total para
    # llegar al nodo.
    nodo_actual = (problem.getStartState(), rutaAlNodo, costoDeRuta)

    # Estrategia UCS: Usar una cola de prioridad como contenedor
    frontera = util.PriorityQueue()

    # Insertamos a la frontera el nodo inicial.
    frontera.push(nodo_actual, 0)

    # Lista que almacena los estados visitados
    visitados = []

    # Mientras la frontera no se encuentre vacía...
    while not frontera.isEmpty():

        # El nodo actual va a ser aquel que saquemos del contenedor
        nodo_actual = frontera.pop()

        # Si el estado actual es un estado meta...
        if problem.isGoalState(nodo_actual[0]):
            # Regresamos la lista de pasos tomados para llegar al estado actual.
            return nodo_actual[1]

        # Si el nodo actual no se encuentra en la lista de visitados...
        if  nodo_actual[0] not in visitados:

            # Insertamos el nodo actual a la lista de visitados.
            visitados.append(nodo_actual[0])

            # Por cada nodo hijo de los sucesores del estado actual...
            for hijo in problem.getSuccessors(nodo_actual[0]):

                # Creamos un nodo con la siguiente estructura:
                # (estado, ruta al nodo, costo al nodo)
                # donde el estado es una tupla de coordenadas (x, y)
                # la ruta al nodo es la lista de acciones tomadas para llegar al estado
                # el costo al nodo es el costo total de llegar al nodo.
                hijo = (hijo[0], nodo_actual[1]+[hijo[1]], heuristic(hijo[0], problem))

                # Si el estado hijo (x, y) no se encuentra en mi lista de visitados...
                if hijo[0] not in visitados:
                    # Si el hijo ya se encuentra en la cola de prioridad con prioridad más alta, actualiza su prioridad y reconstruye la cola
                    # Si el hijo ya se encuentra en la cola de prioridad con prioridad igual o menor, no hace nada.
                    # Si el hijo no se encuentra dentro de la cola de prioridad, hace lo mismo que frontera.push(hijo)

                    frontera.update(hijo, hijo[2])

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    Heuristica trivial
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Busca el nodo que tiene el menor costo combinado y la heuristica primero
    Para probarlo puedes utilizar los siguientes comandos:

        python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

    """
    "*** Tu codigo aqui ***"

    # Variable que almacena el costo de la ruta
    costoDeRuta = heuristic(problem.getStartState(), problem)

    # Lista que almacena el camino tomado para llegar al nodo
    rutaAlNodo = []

    # Variable que almacena el nodo actual. Un nodo consta de
    # una tupla con una tupla con coordenadas (x,y), la ruta al nodo y el coste total para
    # llegar al nodo.
    nodo_actual = (problem.getStartState(), rutaAlNodo, costoDeRuta)

    # Estrategia UCS: Usar una cola de prioridad como contenedor
    frontera = util.PriorityQueue()

    # Insertamos a la frontera el nodo inicial.
    frontera.push(nodo_actual, 0)

    # Lista que almacena los estados visitados
    visitados = []

    # Mientras la frontera no se encuentre vacía...
    while not frontera.isEmpty():

        # El nodo actual va a ser aquel que saquemos del contenedor
        nodo_actual = frontera.pop()

        # Si el estado actual es un estado meta...
        if problem.isGoalState(nodo_actual[0]):
            # Regresamos la lista de pasos tomados para llegar al estado actual.
            return nodo_actual[1]

        # Si el nodo actual no se encuentra en la lista de visitados...
        if  nodo_actual[0] not in visitados:

            # Insertamos el nodo actual a la lista de visitados.
            visitados.append(nodo_actual[0])

            # Por cada nodo hijo de los sucesores del estado actual...
            for hijo in problem.getSuccessors(nodo_actual[0]):

                # Creamos un nodo con la siguiente estructura:
                # (estado, ruta al nodo, costo al nodo)
                # donde el estado es una tupla de coordenadas (x, y)
                # la ruta al nodo es la lista de acciones tomadas para llegar al estado
                # el costo al nodo es el costo total de llegar al nodo.
                hijo = (hijo[0], nodo_actual[1]+[hijo[1]], heuristic(hijo[0], problem))

                # Si el estado hijo (x, y) no se encuentra en mi lista de visitados...
                if hijo[0] not in visitados:
                    # Si el hijo ya se encuentra en la cola de prioridad con prioridad más alta, actualiza su prioridad y reconstruye la cola
                    # Si el hijo ya se encuentra en la cola de prioridad con prioridad igual o menor, no hace nada.
                    # Si el hijo no se encuentra dentro de la cola de prioridad, hace lo mismo que frontera.push(hijo)

                    frontera.update(hijo, hijo[2])

    #util.raiseNotDefined()

# Abreviaciones
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
