# -*- coding: utf-8 -*-
"""
This graph solving system was created by Nicky García Fierros
for PROTECO's Inteligencia Artificial 2017-2 course.

Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to Nicky García Fierros, including a link to
https://github.com/kotoromo.

"""

import util
import solutions


class Problem:

    graph_2 = {
        'A': [('B', 2)],
        'B': [('C', 1), ('D', 5)],
        'D': [('E', 1), ('F', 3)],
        'E': [('D', 5)],
        'F': [('D', 5)]
    }

    """
    Grafo con costos
    """
    graph_1 = {
        'A': [('B', 1)],
        'B': [('C', 1), ('D', 1), ('A', 1)],
        'C': [('B', 1)],
        'D': [('E', 1), ('F', 1), ('B', 1)],
        'E': [('D', 1)],
        'F': [('D', 1)]
    }

    graph_3 = {
        'A': [('B', 3), ('C', 1)],
        'B': [('C', 1), ('D', 2), ('A', 3)],
        'C': [('B', 1), ('A', 1), ('F', 7)],
        'D': [('E', 2), ('F', 1), ('B', 2)],
        'E': [('D', 2)],
        'F': [('D', 1), ('C', 7)]
    }

    metro = {
        'Mixcoac': [
            ('Tacubaya', 2), ('Zapata', 2)
        ],
        'Tacubaya': [
            ('Mixcoac', 2), ('Tacuba', 4), ('Balderas', 5), ("Centro Médico", 2)
        ],
        'Tacuba': [
            ('Hidalgo', 6), ('Tacubaya', 4), ('El Rosario', 3)
        ],
        'Hidalgo': [
            ('Tacuba', 6), ('Balderas', 1), ('Bellas Artes', 0), ('Guerrero', 0)
        ],
        'Balderas': [
            ('Hidalgo', 1), ('Tacubaya', 5), ('Centro Médico', 2), ('Salto del Agua', 0)
        ],
        'Centro Médico': [
            ('Balderas', 2), ('Tacubaya', 2), ('Zapata', 3), ('Chabacano', 1)
        ],
        'Zapata': [
            ('Mixcoac', 2), ('Ermita', 2), ('Centro Médico', 3)
        ],
        'Guerrero': [
            ('Hidalgo', 0), ('Garibaldi', 0), ('La Raza', 1)
        ],
        'La Raza': [
            ('Guerrero', 1), ('Instituto', 1), ('Deportivo', 1), ('Consulado', 2)
        ],
        'Instituto': [
            ('El Rosario', 5), ('Deportivo', 1), ('La Raza', 1)
        ],
        'Deportivo': [
            ('Instituto', 1), ('La Raza', 1), ('Martín Carrera', 1)
        ],
        'Martín Carrera': [
            ('Deportivo', 1), ('Consulado', 2)
        ],
        'Consulado': [
            ('Martín Carrera', 2), ('La Raza', 2), ('Morelos', 1), ("Oceanía", 2)
        ],
        'Morelos': [
            ('Consulado', 1), ('Garibaldi', 2), ('Candelaria', 0), ('San Lázaro', 0)
        ],
        'Garibaldi': [
            ('Guerrero', 0), ('Bellas Artes', 0), ('Morelos', 2)
        ],
        'Bellas Artes': [
            ('Garibaldi', 0), ('Hidalgo', 0), ('Salto del Agua', 1), ('Pino Suárez', 2)
        ],
        'Salto del Agua': [
            ('Bellas Artes', 1), ('Balderas',0), ('Chabacano', 2), ('Pino Suárez', 1)
        ],
        'Pino Suárez': [
            ('Bellas Artes', 2), ('Candelaria', 1), ('Chabacano', 1), ('Salto del Agua', 1)
        ],
        'Chabacano':[
            ('Santa Anita', 1), ('Jamaica', 0), ('Salto del Agua', 2), ('Pino Suárez', 1),('Ermita',5),('Centro Médico',1)
        ],
        'Ermita':[
            ('Chabacano',5),('Atlalilco',1),('Zapata',2)
        ],
        'Atlalilco':[
            ('Ermita',1),('Santa Anita',5)
        ],
        'Santa Anita':[
            ('Atlalilco',5),('Chabacano',1),('Jamaica',0)
        ],
        'Jamaica':[
            ('Candelaria',1),('Pantitlán',4),('Santa Anita',0),('Chabacano',0)
        ],
        'Candelaria':[
            ('Morelos',0),('San Lázaro',0),('Jamaica',1),('Pino Suárez',1)
        ],
        'San Lázaro':[
            ('Morelos',0),('Oceanía',2),('Pantitlán',5),('Candelaria',0)
        ],
        'Oceanía':[
            ('Consulado',2),('San Lázaro',2),('Pantitlán',2)
        ],
        'Pantitlán':[
            ('Oceanía',2),('San Lázaro',5),('Jamaica',4)
        ],
        'El Rosario':[
            ('Tacuba',3),('Instituto',5)
        ]
    }

    """
    Problem abstraction.
    Arguments:
        'space' = state space [OPTIONAL]
        'goal' = goal state
        'start' = start state
        'goal_fn' = custom goal function, if not specified
         uses one that checks for equality between the state given
         and the goal state defined within the problem. [OPTIONAL]
        'heur' = heuristic function to use. [OPTIONAL]
        'suc_fn' = succesor function to use. [OPTIONAL]

    """

    def __init__(self, *args, **kwargs):
        # Dictionary which states the available default graphs.
        spaces = {'g1': self.graph_1, 'g2': self.graph_2, 'g3': self.graph_3, 'metro':self.metro}

        if kwargs is not None:
            if kwargs.get('space') is not None:
                if kwargs.get('space') in spaces.keys():
                    self.state_space = spaces.get(kwargs.get('space'))
                else:
                    self.state_space = kwargs.get('space')
            else:
                self.state_space = spaces['g1']

            self.goal_state = kwargs.get('goal')
            self.start_state = kwargs.get('start')

            if(kwargs.get('goal_fn') is None):
                self.goal_function = self.defaultIsGoal
            else:
                self.goal_function = kwargs.get('goal_fn')

            if kwargs.get('heur') is None:
                self.heuristic = self.nullHeuristic
            else:
                self.heuristic = kwargs.get('heur')

            if kwargs.get('suc_fn') is None:
                self.suc_fn = self.defautlSuccessorFunction
            else:
                self.suc_fn = kwargs.get('suc_fn')

        self.nodes_expanded = 0

    def getSuccessors(self, state):
        return self.suc_fn(state)

    """
    Successor function.
    Given a node, returns the list of successors associated with it.
    """

    def defautlSuccessorFunction(self, state):
        self.nodes_expanded += 1
        return self.state_space[state]

    """
    Trivial heuristic function
    """

    def nullHeuristic(self, *args, **kwargs):
        pass

    """
    Sets the heuristic function
    """

    def setHeuristic(self, h):
        self.heuristic = h

    """
    Default goal check function.
    Given a node, returns whether the node given is the same as the goal state.
    """

    def defaultIsGoal(self, state):
        return self.goal_state == state

    """
    Custom goal check function.
    Returns true if the given state is a goal.
    """

    def isGoal(self, state):
        return self.goal_function(state)

    """
    Start state getter.
    Returns the start state as defined by the problem.
    """

    def getStartState(self):
        return self.start_state

    """
    System is probably badly designed. This is the soulution I came up with.
    Method which finds the appropiate key for the given state.
    """

    def findKey(self, node_letter):
        keys = self.state_space.keys()
        for tuple in keys:
            if node_letter == tuple[0]:
                return tuple

    def restartCounter(self):
        self.nodes_expanded = 0

    def getNodesExpanded(self):
        a = self.nodes_expanded
        self.restartCounter()
        return a

    def getSolutionCost(self, solution):
        cost = 0
        if solution is None:
            return 0

        for i in range(0, len(solution)-1):
            # ('A', 0):[('B', 3), ('C', 1)]
            # state_space = {(NODE, COST): [LIST OF TUPLES]}
            current = solution[i]
            successors = self.getSuccessors(current)

            # finding tuple with value
            for tuple in successors:
                if solution[i+1] == tuple[0]:
                    cost += tuple[1]

        return cost


class Solver:
    """
    dfs ha sido implementado en tu lugar.
    """

    def dfs(self, problem):
        problem.restartCounter() #NO BORRAR!
        #Escribe tu código aquí
        pila = util.Stack()
        explorados = []
        plan = [problem.getStartState()]

        # Meteremos tuplas de las coordenadas o posición y 
        # las acciones que hemos tomado
        pila.push((problem.getStartState(), plan))

        # Mientras haya elementos en la pila:
        while(not pila.isEmpty()):
            estadoAct, plan = pila.pop()
            # Evaluamos si estamos en el estado deseado
            if not problem.isGoal(estadoAct):
                # Si aún no llegamos al objetivo
                if estadoAct not in explorados:
                    # Introducimos nuestra posición a la lista de posiciones recorridas
                    explorados.append(estadoAct)
                    # Expandemos nuestra frontera y agregamos nuevos 
                    # elementos a nuestra pila.
                    for hijo in problem.getSuccessors(estadoAct):
                        pila.push((hijo[0], plan + [hijo[0]]))
            return solutions.Algorithms().dfs(problem)
            util.raiseNotDefined()

    """
    Función que implementa Búsqueda por Amplitud (Breadth First Search)
    """

    def bfs(self, problem):
        problem.restartCounter()  # NO BORRAR!
        # Escribe tu código aquí
        # Crear una cola para colocar que nodos vamos a explorar
        cola = util.Queue()
        # Definimos dos variables, una para almacenar los
        # nodos que ya exploramos y otra para los pasos que hemos tomado
        explorados = []
        plan = [problem.getStartState()]
        # Usamos push/append en cola para colocar el estado inicial y plan de pasos
        cola.push((problem.getStartState(), plan))
        # Iniciamos ciclo while evaluando si la cola esta vacía o no, 
        # mientras tenga elementos:
        while not cola.isEmpty():
            # Declaramos variables, plan quita el primer elemento en la fila y
            # lo agrega a nuestro plan de pasos para el estado en el que estamos.
            nodo, plan = cola.pop()
            # Ciclo if revisamos si estamos en el objetivo
            if not problem.isGoal(nodo):
                # Si no es meta, revisamos si ya lo exploramos
                if nodo not in explorados:
                # Agregamos nodo a los nodos explorados
                    explorados.append(nodo)
                # For por cada hijo, direccion en sucesores:
                    for hijo in problem.getSuccessors(nodo):
                    #Insertamos en cola su posicion, plan de pasos para llegar 
                        cola.push((hijo[0], plan + [hijo[0]]))
            return solutions.Algorithms().bfs(problem)
            util.raiseNotDefined()
        
    """
    Función que implementa Búsqueda de Coste Uniforme
    (conocido como Dijkstra o Uniform Cost Search)
    """

    def ucs(self, problem):
        problem.restartCounter()  # NO BORRAR!
        # Escribe tu código aquí

        # Iniciamos variable del costo de la ruta
        costoDeLaRuta = 0

        # Nuestro array que almacena los pasos que hemos tomado
        rutaAlNodo = [problem.getStartState()]

        # Esta variable almacena el nodo actual: sus coordenadas,
        # la ruta y el costo total para alcanzarlo
        nodoActual = (problem.getStartState(), rutaAlNodo, costoDeLaRuta)

        # Usamos una cola de prioridad para almacenar los nodos
        frontera = util.PriorityQueue()

        # Almecenaremos los lugares que ya hemos visitado
        estadosRecorridos = []

        # Pushamos el nodo inicial a la frontera
        frontera.push(nodoActual, 0)

        # Mientras la frontera no este vacía:
        while not frontera.isEmpty():

            # Sacamos el nodo actual de la frontera
            nodoActual = frontera.pop()

            # Evaluamos si el nodo actual es la meta
            if problem.isGoal(nodoActual[0]):
                # Si es meta, regresamos la ruta para llegar
                return nodoActual[1]
            # Si el nodo actual no se halla en nodos recorridos
            if nodoActual[0] not in estadosRecorridos:
                # Lo agregamos
                estadosRecorridos.append(nodoActual[0])
                # Por cada hijo en los sucesores del nodo actual:
                for hijo in problem.getSuccessors(nodoActual[0]):
                    # Creamos un nodo con sus coordenadas
                    # la ruta del inicio al nodo actual + del nodo actual a su hijo 
                    # El costo de llegar del nodo actual a él + el costo acumulado del inicio al nodo actual
                    # Esta linea me tomó como mil millones de años a pesar de usar el
                    # codigo del moodle que hicimos en clase 😓
                    hijo = (hijo[0], nodoActual[1] + [hijo[0]], hijo[1]+nodoActual[2])
                    # Si dicho hijo no se halla en nodos recorridos
                    if hijo[0] not in estadosRecorridos:
                        # Actualizamos su lugar y su costo en la fila
                        frontera.update(hijo, hijo[2])


        return solutions.Algorithms().ucs(problem)
        util.raiseNotDefined()
    """
    Función que implementa A* (A estrella).
    """

    def astar(self, problem):
        problem.restartCounter()
        # Escribe tu código aquí

        # Ya tengo sueño T^T
        # AIUDA 😭

        return solutions.Algorithms().ucs(problem)
        util.raiseNotDefined()


def main():
    """
    Objetivo:
    1. Crear un modelo del problema así como su planteamiento.

    Recuerda que un problema de búsqueda está definido por los siguientes
    elementos:
        a. Modelo del Mundo
        b. Estado Inicial/Estado Meta
        c. Función de sucesores
        d. Prueba de meta

    2. Implementar todos los algoritmos de búsqueda vistos en clase.
    Encontrar la solución del modelo del mundo utilizando cada una de las
    funciones implementadas (bfs, ucs y a*); DFS ha sido implementado para ti.

    Además, presentar los recorridos realizados por sus algoritmos paso a paso
    en hojas aparte para demostrar la correcta implementación de estos.

    Para ejecutar un problema y probar su solución es necesario hacer lo siguiente:

    # Crear una instancia de la clase 'Problem'. Verificar la definición
    del método constructor para los parámetros que puede tomar.

    # Definimos un problema con inicio en el nodo 'F' y meta en 'C' utilizando
    # El espacio de estados G3 (O el grafo 3)

    problem = Problem(goal='C', start = 'F', space = 'g3')

    # Después, debes crear una instancia de la clase 'Solver'.

    solver = Solver()

    # Debes imprimir la salida de los métodos 'bfs', 'ucs' y 'astar'
    # tal y como se muestra en el método principal main.

    print("Solución: " + str(solver.dfs(problem)))
    print("Nodos expandidos: " + str(problem.getNodesExpanded()))

    # Para pasar un grafo declarado en cualquier otra parte, puedes hacer uso del
    # parámetro 'space' del método constructor de la clase problem,
    # el cual es un diccionario como los demás grafos.

    # ej.
    problema = Problem(start = 'X', goal = 'Y', space = mi_grafo)
    solver = Solver()
    solucion = solver.dfs(problema)
    print "Resultado: %s"%(str(solucion))
    print "Nodos expandidos: %i"%(problem.getNodesExpanded())
    print "Costo: %i"%(problem.getSolutionCost(solucion))

    #Para implementar A*, necesitas desarrollar una heuristica admisible
    ( f(s) = g(s) + h(s) admisible <->  0 < h(s)<= g(s) )
    # Una vez hayas escrito tu heuristica, definela en el método constructor
    # del problema mediante el parámetro 'heur'
    # ej.
        def mi_heuristica(estado):
            ...

        problema = Problem(start = 'A', goal = 'F', space = 'g3', heur='mi_heuristica')
        solucionador = Solver(problema)
        solucionador.astar()
            ...


    Éxito y que te diviertas :)
    """

    """
    Programa en esta función tu heuristica
    """
    def heuristica(nodo):
        # Escribe tu código aquí

        # BORRA ESTA LINEA CUANDO HAYAS PROGRAMADO TU HEURISTICA
        return solutions.Algorithms().dist_heur(nodo)

    # DEFINICION DEL PROBLEMA
    # problem = Problem(start='A', goal='F', space='g3', heur=heuristica)
    problem = Problem(start='Zapata', goal='Santa Anita', space='metro', heur=heuristica)
    solv = Solver()

    """
    Soluciones muestra para tu apoyo en el uso del sistema.
    Si te estorban puedes comentarlas sin problema o, en su defecto, borrarlas.
    """

    print("--------------DFS----------------------")
    sol = solv.dfs(problem)
    print "Solucion: %s" % (str(sol))
    print "Nodos expandidos: %s" % (str(problem.getNodesExpanded()))
    print "Costo: %i" % (problem.getSolutionCost(sol))

    print("--------------BFS----------------------")
    sol = solv.bfs(problem)
    print "Solucion: %s" % (str(sol))
    print "Nodos expandidos: %s" % (str(problem.getNodesExpanded()))
    print "Costo: %i" % (problem.getSolutionCost(sol))

    print("--------------UCS----------------------")
    sol = solv.ucs(problem)
    print "Solucion: %s" % (str(sol))
    print "Nodos expandidos: %s" % (str(problem.getNodesExpanded()))
    print "Costo: %i" % (problem.getSolutionCost(sol))

    print("--------------A*----------------------")
    sol = solv.astar(problem)
    print "Ya no entendi bien como definir la heuristica :("
    '''
    print "Solucion: %s" % (str(sol))
    print "Nodos expandidos: %s" % (str(problem.getNodesExpanded()))
    print "Costo: %i" % (problem.getSolutionCost(sol))
    '''

if __name__ == '__main__':
    main()
