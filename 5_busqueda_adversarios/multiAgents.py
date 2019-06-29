# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
      python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
      python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3

      python pacman.py -p MinimaxAgent -l mediumClassic -a depth=4
      python pacman.py -p MinimaxAgent -l mediumClassic -a depth=3

      python pacman.py -p MinimaxAgent -l openClassic -a depth=4
      python pacman.py -p MinimaxAgent -l openClassic -a depth=3


    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game

          gameState.isWin():
            Returns whether or not the game state is a winning state

          gameState.isLose():
            Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # obtenemos las acciones legales del agente con indice 0 (pacman)
        pLM = gameState.getLegalActions(0)

        # Como es pacman a quien le corresponde tomar una decision, y asumimos que pacman es un agente maximizador,
        # inicializamos el valor v en menos infinito.
        v = float("-inf")

        # Por defecto, como no hemos explorado ningun nodo, la mejor accion es la primera.
        indiceMejorAccion = 0

        # Variable que me ayudara a iterar sobre acciones
        i = -1

        # Para cada sucesor dentro de los sucesores generados al tomar la accion action de la lista pLM del agente
        # con indice 0, haz lo siguiente:
        for succ in [gameState.generateSuccessor(0, action) for action in pLM]:
          # incrimenta el contador de acciones
          i+=1
          #  calcula el puntaje. Como el siguiente agente es un agente minimizador, llama a minVal.
          score = self.minVal(succ, 1, 0)

          # Ya que termines de calcular el valor de los estados, ya puedes maximizar.
          if v < score:
            # Si la accion que tomaste fue la mejor que has evaluado hasta este momento, actualiza el indice
            # de la mejor accion.
            indiceMejorAccion = i
          
          # Finalmente, maximiza sobre el valor v calculado y el puntaje obtenido de evaluar los nodos max-min
          v = max(v, score)
        
        # Regresa aquella accion que te brinde el mejor puntaje.
        return pLM[indiceMejorAccion]
        #util.raiseNotDefined()

    def maxVal(self, gameState, currentDepth):
      # Si el estado actual es un estado terminal:
      if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
        # Regresa lo que me diga mi funcion de evaluacion.
        return scoreEvaluationFunction(gameState)
      # Si no es un estado terminal, inicializamos el valor para el nodo maximizador como -inf
      v = float("-inf")

      # Para cada sucesor dentro de los sucesores dado que el indice del agente es 0 y dada que la accion
      # se encuentra en la lista de las acciones legales del agente con indice 0:
      for succ in [gameState.generateSuccessor(0, action) for action in gameState.getLegalActions(0)]:
        # como somos un nodo maximizador, entonces el que sigue debe ser minimizador.
        # El indice del siguiente agente es 1; la profundidad sigue sin cambiar.
        v = max(v, self.minVal(succ, 1, currentDepth))
      return v

    def minVal(self, gameState, agentIndex, currentDepth):
      # Si el estado actual es un estado terminal:
      if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
        # Regresa lo que me diga mi funcion de evaluacion.
        return scoreEvaluationFunction(gameState)
      
      # Como estamos considerando un nodo minimizador, en el peor de los casos mi valor es un numero
      # positivo enorme.
      v = float("inf")

      # Para cada sucesor dentro de los sucesores dado que el indice del agente es agentIndex y dada que la accion
      # se encuentra en la lista de las acciones legales del agente con indice agentIndex:
      for succ in [gameState.generateSuccessor(agentIndex, action) for action in gameState.getLegalActions(agentIndex)]:
        # Si estamos lideando con el penultimo agente, sabemos que el agente que sigue es un agente
        # maximizador entonces, llamamos a min, pero con el siguiente agente. 
        if agentIndex == gameState.getNumAgents()-1:
          v = min(v, self.maxVal(succ, currentDepth+1))
        else:
          # Si no estamos en el penultimo agente, entonces llamamos a otro min.
          v = min(v, self.minVal(succ, agentIndex+1, currentDepth))
      
      # Regresamos el valor de v calculado.
      return v


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

