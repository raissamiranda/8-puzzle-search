# This program implements search algorithms for the 8-puzzle problem
import sys
import timeit
import copy
import queue


# Class that represents a node in the search tree
class Node:
    def __init__(self, currentBoard, parent = None, depth = 0):
        self.currentBoard = currentBoard
        self.parent = parent
        self.children = []
        self.depth = depth
        self.heuristic = 0
        self.cost = 0
        self.emptySpace = []

    # Prints board in a readable way
    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.currentBoard[i][j], end = " ")
            print("")

    # All Node information
    def __str__(self):
        return f"Node: depth={self.depth}, board={self.currentBoard}, cost={self.cost}, emptySpace={self.emptySpace}"

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.currentBoard == other.currentBoard
        return False

    # Looks for the empty space in the board
    def findEmptySpace(self):
        for i in range(3):
            for j in range(3):
                if self.currentBoard[i][j] == 0:
                    return [i, j]

    # Checks if the current board is the solution
    def foundSolution(self):
        return self.currentBoard == [[1,2,3],[4,5,6],[7,8,0]]

    # Print path from root to solution
    def printPath(self):
        if(self.parent != None):
            self.parent.printPath()
        self.printBoard()
        print("")

    # Moves the empty space up, down, left or right
    def moveUp(self):
        if self.emptySpace[0] < 2:

            updatedBoard = copy.deepcopy(self.currentBoard)
            moved = self.currentBoard[self.emptySpace[0] + 1][self.emptySpace[1]]
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved
            updatedBoard[self.emptySpace[0] + 1][self.emptySpace[1]] = 0

            updatedDepth = self.depth + 1
            newNode = Node(updatedBoard, self, updatedDepth)
            newNode.emptySpace = [self.emptySpace[0] + 1, self.emptySpace[1]]
            return newNode

        else:
            return None

    def moveDown(self):
        if self.emptySpace[0] > 0:
            updatedBoard = copy.deepcopy(self.currentBoard)
            moved = self.currentBoard[self.emptySpace[0] - 1][self.emptySpace[1]]
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved
            updatedBoard[self.emptySpace[0] - 1][self.emptySpace[1]] = 0

            updatedDepth = self.depth + 1
            newNode = Node(updatedBoard, self, updatedDepth)
            newNode.emptySpace = [self.emptySpace[0] - 1, self.emptySpace[1]]
            return newNode
        else:
            return None

    def moveRight(self):
        if self.emptySpace[1] > 0:
            updatedBoard = copy.deepcopy(self.currentBoard)
            moved = self.currentBoard[self.emptySpace[0]][self.emptySpace[1] - 1]
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved
            updatedBoard[self.emptySpace[0]][self.emptySpace[1] - 1] = 0

            updatedDepth = self.depth + 1
            newNode = Node(updatedBoard, self, updatedDepth)
            newNode.emptySpace = [self.emptySpace[0], self.emptySpace[1] - 1]
            return newNode
        else:
            return None

    def moveLeft(self):
        if self.emptySpace[1] < 2:
            updatedBoard = copy.deepcopy(self.currentBoard)
            moved = self.currentBoard[self.emptySpace[0]][self.emptySpace[1] + 1]
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved
            updatedBoard[self.emptySpace[0]][self.emptySpace[1] + 1] = 0

            updatedDepth = self.depth + 1
            newNode = Node(updatedBoard, self, updatedDepth)
            newNode.emptySpace = [self.emptySpace[0], self.emptySpace[1] + 1]
            return newNode
        else:
            return None

    # Kept children in order [up, down, left, right]
    def expand(self):
        tentatives = [self.moveUp(), self.moveDown(), self.moveLeft(), self.moveRight()]
        self.children = [move for move in tentatives if move is not None]

    # Counts the number of pieces in the wrong position, used for heuristic function
    def countWrongPlacedPieces(self):
        wrongPositions = sum([1 for i in range(3) for j in range(3) if self.currentBoard[i][j] != 0 and self.currentBoard[i][j] != (i*3 + j + 1)])
        return wrongPositions

    # Finds the distance of each piece to its correct position, used for heuristic function
    def findDistanceToCorrectPosition(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.currentBoard[i][j] != 0:
                    correctPosition = self.currentBoard[i][j] - 1
                    distance += abs(i - correctPosition//3) + abs(j - correctPosition%3)
        return distance

    # Breath First Search
    def bfs(self):
        expandedStates = 0
        solution = None
        queue = [self] # fila para armazenar nós que serão explorados
        while solution == None: # enquanto a fila não estiver vazia
            for node in queue:
                if node.foundSolution(): # se o nó for solução, retorna ele
                    solution = node
                    break
            newQueue = []
            for node in queue:
                node.expand()
                expandedStates += 1
                for child in node.children:  # para cada filho do nó
                    newQueue.append(child)  # adiciona o filho na fila
            queue.clear()
            queue = newQueue.copy()
        return solution, expandedStates # se a fila ficar vazia e não encontrar solução, retorna None

    # Dijkstra algorithm
    def dijkstra(self):
        pq = queue.Queue()   # cria fila de prioridade
        pq.put(self)             # coloca o nó raiz na fila -> (numero de prioridade, nó)
        expandedNodes = 0
        visited = []
        solution = None

        while not pq.empty():
            node = pq.get()    # vai pegar o com menor valor de prioridade
            expandedNodes += 1
            visited.append(node)

            if node.foundSolution():
                solution = node
                break

            node.expand()
            for child in node.children:
                if child not in visited:
                    if child not in pq.queue:
                        pq.put(child)
                    else:
                        for nd in pq.queue:
                            if child == nd:
                                if child.depth < nd.depth:
                                    nd.depth = child.depth
                                    nd.parent = child.parent
                                    nd.emptySpace = child.emptySpace
                                    nd.currentBoard = child.currentBoard
                                    nd.children = child.children
        return solution, expandedNodes

    # Depth First Search
    def dfs(self, limit):
        stack = queue.LifoQueue() # pilha para armazenar nós que serão explorados
        stack.put(self)
        solution = None
        expandedStates = 0
        while not stack.empty():
            node = stack.get()
            if node.foundSolution():
                solution = node
                break
            if node.depth < limit:
                node.expand()
                expandedStates += 1
                for child in node.children:
                    stack.put(child)
        return solution, expandedStates

    # Iterative Deepening Search algorithm
    def ids(self):
        limit = 0
        while (1):
            solution, expandedStates = self.dfs(limit)
            if solution is not None:
                return solution, expandedStates
            limit += 1

    # A* algorithm
    def aStar(self):
        pq = [self]
        visited = []
        solution = None
        expandedStates = 0
        while pq:
            node = pq[0]
            if node.foundSolution():
                solution = node
                break
            else:
                visited.append(node)
                pq.pop(0)
                node.expand()
                expandedStates += 1
                for child in node.children:
                    if child not in visited:
                        child.cost = node.depth + child.countWrongPlacedPieces()
                        pq.append(child)
            pq.sort(key=lambda x: x.cost)
        return solution, expandedStates

    # Greedy algorithm
    def greedy(self):
        nodes = [self]  # Lista de nós a serem explorados
        visited = []  # Conjunto para manter os nós visitados
        solution = None
        expandedStates = 0
        while nodes:
            nodes.sort(key=lambda node: node.heuristic)  # Ordena os nós com base na heurística
            node = nodes[0]  # Pega o nó com a menor heurística
            if node.foundSolution():
                solution = node
                break
            nodes.pop(0)
            visited.append(node)
            node.expand()
            expandedStates += 1
            for child in node.children:
                if child not in visited:
                    child.heuristic = child.findDistanceToCorrectPosition()  # Calcula a heurística do filho
                    nodes.append(child)  # Adiciona o filho à lista de nós a serem explorados
        return solution, expandedStates

    # Hill Climbing algorithm
    def hillClimbing(self):
        node = self
        self.cost = self.findDistanceToCorrectPosition()
        lateralMovements = 100
        expandedStates = 0
        solution = None
        while (1):
            node.expand()
            expandedStates += 1
            neighbours = node.children
            for child in neighbours:
                child.cost = child.findDistanceToCorrectPosition()
            best = min(neighbours, key=lambda x: x.cost)
            if best.cost > node.cost:
                solution = node
                break
            elif best.cost < node.cost:
                lateralMovements = 100
            elif best.cost == node.cost:
                lateralMovements -= 1
            if lateralMovements == 0:
                solution = node
                break
            node = best
        return solution, expandedStates



# Reading init state and algorithm used from command line
def computeInput():
    algorithm = sys.argv[1]

    # Init board positions
    initialBoard = [[],[],[]]
    for i in range(3):
        for j in range(3):
            initialBoard[i].append(int(sys.argv[i*3+j+2]))
    return algorithm, initialBoard


# Running the algorithm
def runAlgorithm(algorithm, initialBoard):

    # Creating root node
    root = Node(initialBoard)
    root.emptySpace = root.findEmptySpace()
    solution = None

    if algorithm == "A":
        solution, expandedStates = root.aStar()
        print(expandedStates)


    elif algorithm == "B":
        solution, expandedStates = root.bfs()
        print(expandedStates)


    elif algorithm == "G":
        solution, expandedStates = root.greedy()
        print(expandedStates)


    elif algorithm == "H":
        solution, expandedStates = root.hillClimbing()
        print(expandedStates)


    elif algorithm == "I":
        solution, expandedStates = root.ids()
        print(expandedStates)


    elif algorithm == "U":
        solution, expandedStates = root.dijkstra()
        print(expandedStates)

    else:
        print("Invalid algorithm")
        exit(1)

    if (len(sys.argv) >= 12):
        if (sys.argv[11] == "PRINT"):
            solution.printPath()
        else:
            print("Invalid argument")
            exit(1)


algorithm, initialState = computeInput()
#start = timeit.default_timer()
runAlgorithm(algorithm, initialState)
#stop = timeit.default_timer()
#print('Time: ', stop - start)