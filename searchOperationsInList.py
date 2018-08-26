'''
Searching in a List
This program implements the linear search and binary search algorithm in Python
This program also shows the time taken by linear search and two versions of binary search
Written by: Asif Nashiry
'''


import random
import time

# linear search
def linearSearch(dataList, target):
    if len(dataList) == 0:
        print("The list is empty.")
        return -1
    elif len(dataList) == 1 and dataList[0] != target:
        return -1
    else:
        index = -1
        for i in range(len(dataList)):
            if target == dataList[i]:
                index = i
                return index
        return index


# binary search with iteration
def binarySearchIteration(dataList, target):
    if len(dataList) == 0:
        print("The list is empty")
        return -1
    elif len(dataList) == 1 and dataList[0] != target:
        return -1
    else:
        low = 0
        high = len(dataList) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == dataList[mid]:
                return mid
            elif target < dataList[mid]:
                high = mid - 1
            elif target > dataList[mid]:
                low = mid + 1
        return -1


# binary search with recursion
def binarySearchRecursion(dataList, target, low, high):
    if len(dataList) == 0:
        return -1;
    if len(dataList) == 1 and target != dataList[0]:
        return -1;
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == dataList[mid]:
            return mid
        elif target < dataList[mid]:
            return binarySearchRecursion(dataList, target, low, mid-1)
        else:
            return binarySearchRecursion(dataList, target, mid+1, high)



# number of data in the list
N = int(input("How many elements: "))

# list of data
listOfElements = []

# list of random N data
for i in range(N):
    data = random.randint(1, 100)
    listOfElements.append(data)

print("The list of elements: ")
print(listOfElements)

# sorting the list
listOfElements.sort()

print("The list after sorting: ")
print(listOfElements)

# element to be searched
target = int(input("Enter the element to be searched: "))

print("Linear search: ")
startTime = time.time()
index = linearSearch(listOfElements, target)
endTime = time.time()
print("Execution Time in milli second: ", (endTime - startTime)*1000)
if index == -1:
    print("The target element", target, "is not in the list")
else:
    print("The target element", target, "appears at position ", index+1, "in the list")



print("Binary search with iteration: ")
startTime = time.time()
indexBinaryIte = binarySearchIteration(listOfElements, target)
endTime = time.time()
print("Execution Time in milli second: ", (endTime - startTime)*1000)
if indexBinaryIte == -1:
    print("The target element", target, "is not in the list")
else:
    print("The target element", target, " appears at position", indexBinaryIte+1, "in the list")



print("Binary search with recursion: ")
startTime = time.time()
low = 0
high = len(listOfElements) - 1
indexBinaryRec = binarySearchRecursion(listOfElements, target, low, high)
endTime = time.time()
print("Execution Time in milli second: ", (endTime - startTime)*1000)
if indexBinaryRec == -1:
    print("The target element", target, "is not in the list")
else:
    print("The target element", target, " appears at position", (indexBinaryRec+1), "in the list")
