# This program implements search algorithms for the 8-puzzle problem
import sys
import time
import copy



class Node:
    def __init__(self, currentBoard, parent = None, depth = 0):
        self.currentBoard = currentBoard
        self.parent = parent
        self.children = []
        self.depth = depth
        self.heuristic = ""
        self.cost = 0
        self.emptySpace = []


    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.currentBoard[i][j], end = " ")
            print("")

    def setHeuristic(self, heuristic):
        self.heuristic = heuristic

    def setCost(self, cost):
        self.cost = cost

    def findEmptySpace(self):
        for i in range(3):
            for j in range(3):
                if self.currentBoard[i][j] == 0:
                    return [i, j]

    def moveUp(self):
        if self.emptySpace[0] < 2:                                                  # nao ta na primeira linha do tabuleiro

            # atualiza tabuleiro
            updatedBoard = copy.deepcopy(self.currentBoard)                           # cria copia do tabuleiro
            moved = self.currentBoard[self.emptySpace[0] + 1][self.emptySpace[1]]        # guarda o valor da posicao que vai ser movido
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved             # desce a peca movida
            updatedBoard[self.emptySpace[0] + 1][self.emptySpace[1]] = 0            # coloca o espaco vazio na posicao da peca movida

            updatedDepth = self.depth + 1                                           # aumenta o nivel do novo nó

            newNode = Node(updatedBoard, self, updatedDepth)                       # cria novo nó, com essa ação
            newNode.emptySpace = [self.emptySpace[0] + 1, self.emptySpace[1]]      # atualiza a posicao do espaco vazio
            return newNode

        else:
            return None


    def moveDown(self):
        if self.emptySpace[0] > 0:                                               # nao ta na primeira linha do tabuleiro
            updatedBoard = copy.deepcopy(self.currentBoard)                      # cria copia do tabuleiro
            moved = self.currentBoard[self.emptySpace[0] - 1][self.emptySpace[1]]    # guarda a posicao que vai ser movido
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved              # desce a peca movida
            updatedBoard[self.emptySpace[0] - 1][self.emptySpace[1]] = 0          # coloca o espaco vazio na posicao da peca movida

            updatedDepth = self.depth + 1                                     # aumenta o nivel do novo nó
            newNode = Node(updatedBoard, self, updatedDepth)                       # cria novo nó, com essa ação
            newNode.emptySpace = [self.emptySpace[0] - 1, self.emptySpace[1]]      # atualiza a posicao do espaco vazio
            return newNode
        else:
            return None

    def moveRight(self):
        if self.emptySpace[1] > 0:                                               # nao ta na primeira linha do tabuleiro
            updatedBoard = copy.deepcopy(self.currentBoard)                      # cria copia do tabuleiro
            moved = self.currentBoard[self.emptySpace[0]][self.emptySpace[1] - 1]    # guarda a posicao que vai ser movido
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved              # desce a peca movida
            updatedBoard[self.emptySpace[0]][self.emptySpace[1] - 1] = 0          # coloca o espaco vazio na posicao da peca movida

            updatedDepth = self.depth + 1                                     # aumenta o nivel do novo nó
            newNode = Node(updatedBoard, self, updatedDepth)                       # cria novo nó, com essa ação
            newNode.emptySpace = [self.emptySpace[0], self.emptySpace[1] - 1]      # atualiza a posicao do espaco vazio
            return newNode
        else:
            return None

    def moveLeft(self):
        if self.emptySpace[1] < 2:                                               # nao ta na primeira linha do tabuleiro
            updatedBoard = copy.deepcopy(self.currentBoard)                      # cria copia do tabuleiro
            moved = self.currentBoard[self.emptySpace[0]][self.emptySpace[1] + 1]    # guarda a posicao que vai ser movido
            updatedBoard[self.emptySpace[0]][self.emptySpace[1]] = moved              # desce a peca movida
            updatedBoard[self.emptySpace[0]][self.emptySpace[1] + 1] = 0          # coloca o espaco vazio na posicao da peca movida

            updatedDepth = self.depth + 1                                     # aumenta o nivel do novo nó
            newNode = Node(updatedBoard, self, updatedDepth)                       # cria novo nó, com essa ação
            newNode.emptySpace = [self.emptySpace[0], self.emptySpace[1] + 1]      # atualiza a posicao do espaco vazio
            return newNode
        else:
            return None










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

    # descobrindo a posicao do espaco vazio
    root = Node(initialBoard)
    root.emptySpace = root.findEmptySpace()
    print("empty space = ", root.emptySpace)


    # testando o movimentos -----------------------------------------------------------------------------
    print("before move")
    root.printBoard()
    newNode = root.moveUp()
    print("after move up")
    newNode.printBoard()
    newNode2 = newNode.moveDown()
    print("after move down")
    newNode2.printBoard()
    newNode3 = newNode2.moveRight()
    print("after move right ")
    newNode3.printBoard()
    newNode4 = newNode3.moveLeft()
    print("after move left")
    newNode4.printBoard()
    # testando o movimentos -----------------------------------------------------------------------------


    if algorithm == "A":
        print("A*")

    elif algorithm == "B":
        print("BFS")

    elif algorithm == "G":
        print("Greedy")

    elif algorithm == "H":
        print("Hill Climbing")

    elif algorithm == "I":
        print("Iterative Deepening")

    elif algorithm == "U":
        print("Uniform Cost")

    else:
        print("Invalid algorithm")
        exit(1)


algorithm, initialState = computeInput()
runAlgorithm(algorithm, initialState)
