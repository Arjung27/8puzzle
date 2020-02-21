import os
import numpy as np
import sys
from queue import Queue
from queue import LifoQueue
import time

class Node:

    def __init__(self, key, parent):
        self.key = key
        self.child = []
        self.position = key.find('0')
        self.parent = parent

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
            if (int(state[j]) and int(state[i]) and  state[i] > state[j]):
                invCount += 1
    # return (invCount%2 == 0)
    return 1 

def isOpen(node, closedNode):

    if node.key in closedNode:
        return 0
    return 1

def getChild(node, nodeList):

    # Calculating the row number of the element for puzzle size 3**2
    puzzleSize = 3
    row = int(node.position/puzzleSize)
    col = int(node.position%puzzleSize)
    if (row - 1 >= 0):
    	tempKey = list(node.key)[:]
    	temp = tempKey[int((row - 1)*puzzleSize + col)]
    	tempKey[int((row - 1)*puzzleSize + col)] = '0'
    	tempKey[node.position] = temp
    	tempKey = "".join(tempKey)
    	nodeList.put(Node(tempKey, node))

    if (row + 1 < puzzleSize):
    	tempKey = list(node.key)[:]
    	temp = tempKey[int((row + 1)*puzzleSize + col)]
    	tempKey[int((row + 1)*puzzleSize + col)] = '0'
    	tempKey[node.position] = temp
    	tempKey = "".join(tempKey)
    	nodeList.put(Node(tempKey, node))

    if (col - 1 >= 0):
    	tempKey = list(node.key)[:]
    	temp = tempKey[int(row*puzzleSize + col - 1)]
    	tempKey[int((row)*puzzleSize + col - 1)] = '0'
    	tempKey[node.position] = temp
    	tempKey = "".join(tempKey)
    	nodeList.put(Node(tempKey, node))

    if (col + 1 < puzzleSize):
    	tempKey = list(node.key)[:]
    	temp = tempKey[int(row*puzzleSize + col + 1)]
    	tempKey[int((row)*puzzleSize + col + 1)] = '0'
    	tempKey[node.position] = temp
    	tempKey = "".join(tempKey)
    	nodeList.put(Node(tempKey, node))

def findSolution(initialState, goalState):
    
    if (initialState == goalState):
        return 1, Node(initialState, None)

    initialState = convertToRow(initialState)
    goalState = convertToRow(goalState)
    closedNode = set()
    nodeList = Queue()
    root = Node(initialState, None)
    count = 0
    if isSolvable(initialState):
        nodeList.put(root)
        while(nodeList.qsize() != 0):
            currNode = nodeList.get()
            if currNode.key == goalState:
                return 1, currNode
            elif isOpen(currNode, closedNode):
                closedNode.add(currNode.key)
                if isSolvable(currNode.key):
                    getChild(currNode, nodeList)
                else: 
                    continue
            else:
                continue
    else:
        return 0, None
    return 0, None

def writeFile(file, stack):
    while(stack.qsize() != 0):
        top = stack.get()
        for s in top:
            file.write(s + " ")
        file.write('\n')

if __name__ == '__main__':
    initialState = sys.argv[1]
    goalState = '147258360'
    if initialState == goalState:
        print("Initial State is same the goal state")
        exit(-1)
    flag, node = findSolution(initialState, goalState)
    file = open('nodePath.txt', 'w+')
    stack = LifoQueue()
    if flag:
        print('Path found')
        while(node != None):
            Key = convertToRow(node.key)
            stack.put(Key)
            node = node.parent
    else:
        print('No solution exists')

    writeFile(file, stack)
    