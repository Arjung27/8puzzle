import numpy as np
import sys
from queue import Queue
from queue import LifoQueue

class Node:

    def __init__(self, key, parent, index):
        self.key = key
        self.position = key.find('0')
        self.parent = parent
        self.index = index

def convertToRow(initialState):
    """
    Function to convert the column form to row form
    """
    size = np.sqrt(len(initialState))
    rowform = ''
    for i in range(int(size)):
        j = i;
        while j < len(initialState):
            rowform += initialState[j]
            j += 3
    return rowform

def isSolvable(state):
    """
    Function to check if the solution exists from the current node
    configuration
    """

    invCount = 0
    size = len(state)
    for i in range(0, size-1):
        for j in range(i+1, size):
            if (int(state[j]) and int(state[i]) and  state[i] > state[j]):
                invCount += 1
    # return (invCount%2 == 0)
    return 1 

def isOpen(node, closedNode):
    """
    To check if the node is already visited or not
    """
    if node.key in closedNode:
        return 0
    return 1

def getChild(node, nodeList, closedNode, count):
    """
    Function to find all the children associated with the node
    """

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
        newNode = Node(tempKey, node, count)
        if isOpen(newNode, closedNode):
           nodeList.put(newNode)
           count += 1

    if (row + 1 < puzzleSize):
        tempKey = list(node.key)[:]
        temp = tempKey[int((row + 1)*puzzleSize + col)]
        tempKey[int((row + 1)*puzzleSize + col)] = '0'
        tempKey[node.position] = temp
        tempKey = "".join(tempKey)
        newNode = Node(tempKey, node, count)
        if isOpen(newNode, closedNode):
           nodeList.put(newNode)
           count += 1

    if (col - 1 >= 0):
        tempKey = list(node.key)[:]
        temp = tempKey[int(row*puzzleSize + col - 1)]
        tempKey[int((row)*puzzleSize + col - 1)] = '0'
        tempKey[node.position] = temp
        tempKey = "".join(tempKey)
        newNode = Node(tempKey, node, count)
        if isOpen(newNode, closedNode):
           nodeList.put(newNode)
           count += 1

    if (col + 1 < puzzleSize):
        tempKey = list(node.key)[:]
        temp = tempKey[int(row*puzzleSize + col + 1)]
        tempKey[int((row)*puzzleSize + col + 1)] = '0'
        tempKey[node.position] = temp
        tempKey = "".join(tempKey)
        newNode = Node(tempKey, node, count)
        if isOpen(newNode, closedNode):
           nodeList.put(newNode)
           count += 1

    return count

def findSolution(initialState, goalState):
    """
    Function implementing the bfs algorithm
    """
    initialState = convertToRow(initialState)
    goalState = convertToRow(goalState)
    closedNode = set()
    nodeList = Queue()
    allNode = Queue()
    count = 0
    root = Node(initialState, None, count)
    count += 1
    if isSolvable(initialState):
        nodeList.put(root)
        while(nodeList.qsize() != 0):
            currNode = nodeList.get()
            if currNode.key == goalState:
                allNode.put(currNode)
                return 1, currNode, closedNode, allNode
            elif isOpen(currNode, closedNode):
                allNode.put(currNode)
                closedNode.add(currNode.key)
                if isSolvable(currNode.key):
                    count = getChild(currNode, nodeList, closedNode, count)
                else: 
                    continue
            else:
                continue
    else:
        return 0, None, closedNode, allNode
    return 0, None, closedNode, allNode

def writeFile(file, stack):
    """
    Function to write the final result in the file
    """

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
    flag, node, list_, allNode = findSolution(initialState, goalState)
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

    file = open('Nodes.txt', 'w+')
    for ele in list_:
        for s in ele:
            file.write(s + " ")
        file.write('\n')

    file = open('NodesInfo.txt', 'w+')
    count = 1
    while(allNode.qsize() != 1):
        ele = allNode.get()
        if count != 1:
            file.write(str(ele.index) + " " + str(ele.parent.index) + " " + str(0))
            file.write('\n')
        count += 1
    