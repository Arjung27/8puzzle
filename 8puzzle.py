import os
import numpy as np
import sys
from queue import Queue

class Node:

    def __init__(self, key):
        self.key = key
        self.child = []
        self.position = key.find('0')

def convertToRow(initialState):

    size = np.sqrt(len(initialState))
    rowform = ''
    for i in range(int(size)):
        j = i;
        while j < len(initialState):
            rowform += initialState[j]
            j += 3
    return rowform

def isSolvable(state):

    invCount = 0
    size = len(state)
    for i in range(0, size-1):
        for j in range(i+1, size):
            if (state[j] and state[i] and  state[i] > state[j]):
                invCount += 1
    return (invCount%2 == 0)

def convertToCol(state):

    size = np.sqrt(len(initialState))
    colForm = ''
    for i in range(int(size)):
        j = i;
        while j < len(initialState):
            rowform += initialState[j]
            j += 3
    return colForm    

def isOpen(node, closedNode):

    for n in closedNode:
        if (n.position == node.position):
            if (n.key == nod.key):
                return 0
    return 1

def getChild(node, nodeList):

    # Calculating the row number of the element for puzzle size 3**2
    puzzleSize = 3
    row = int(node.position/puzzleSize)
    col = int(node.position%puzzleSize)

    if (row - 1 >= 0):
        

def findSolution(initialState, goalState):
    
    if (initialState == goalState):
        return 1

    initialState = convertToRow(initialState)
    goalState = convertToRow(goalState)
    closedNode = []
    nodeList = Queue()
    root = Node(initialState)

    if isSolvable(initialState):
        nodeList.put(root)
        while(nodeList.qsize() != 0):
            currNode = nodeList.get()
            if currNode.key == goalState:
                return 1
            elif isOpen(currNode, closedNode):
                if isSolvable(currNode.key):
                    getChild(currNode, nodeList)
                else: 
                    continue
            else:
                continue
    else:
        return 0

    return 1

if __name__ == '__main__':
    initialState = sys.argv[1]
    goalState = '147258360'

    if findSolution(initialState, goalState):
        print('Path found')
    else:
        print('No solution exists')
