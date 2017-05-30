import csv
import random
import time



#Сортировка слиянием
def MergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        global OM, CM
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
                OM += 1
            else:
                alist[k] = righthalf[j]
                j = j+1
                OM += 1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
            OM += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
            OM += 1
    CM += 1
    return alist


#Быстрая сортировка
def QuickSort(A):
    global OQ, CQ
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                OQ += 1
                L.append(elem)
            elif elem > q:
                OQ += 1
                R.append(elem)
            else:
                M.append(elem)
                OQ += 1
        CQ += 1
        return QuickSort(L) + M + QuickSort(R)


#Сортировка пузырьком
def BSort(Arr):
    M = 0
    for i in range(len(Arr)-1):
        for j in range(len(Arr)-1):
            M += 1
            if Arr[j] > Arr[j]:
                Arr[j+1], Arr[j] = Arr[j], Arr[j+1]
    print('M =', M)
    return Arr


#Сортировка деревом и поиск по дереву
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        # print('.')

    def set_value(self, val):
        self.key = val

class Tree:
    def __init__(self):
        self.root = None
#Добавление узла
    def add_key(self, val):
        global OT
        global MT
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                OT += 1
                if current.left == None:
                    MT += 1
                    current.left = Node(val, None, None)
                    break
                current = current.left
            elif val > current.key:
                OT += 1
                if current.right == None:
                    MT += 1
                    current.right = Node(val, None, None)
                    break
                current = current.right
            else:
                break

    def insert(self, val):
        self.add_key(val)
#Вывод дерева
    def inorder_(self):
        if self.root == None:
            return None
        stack = []
        node = self.root
        while node or stack:
            # print(stack)
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.key, end="\n")
                node = node.right

    def inorder(self):
        self.inorder_()

#Поиск по дереву
    def find_(self, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        global CFT
        current = self.root
        while current:
            if val <= current.key:
                CFT += 1
                if  current.key == val:
                    print('Found:', current.key)
                    return
                elif current.left == None and current.key != val:
                    print("\n" + "No Value")
                current = current.left
            elif val > current.key:
                CFT += 1
                if current.key == val:
                    print('Found:', current.key)
                    return
                elif current.right == None and current.key != val:
                    print("\n" + "No Value")
                current = current.right

    def find(self, val):
        self.find_(val)

def SortTree(array):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        #t.inorder()

def FindTree(array,val):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        t.find(val)


# Линейный поиск
def lineF(A, key):
    i = 0
    M = 0
    t = len(A) - 1
    while True:
        if key == A[i]:
            print('LineSearch:\nFound:',A[i],'\nM =', M)
            return
        else:
            M += 1
        if t == i:
            print('LineSearch:\nNo Value\nM =', M)
            return
        i += 1

# Бинарный поиск
def BiSear(A, key):
    left = 0
    right = len(A)
    M = 0
    while right > left:
        middle = (left + right) // 2
        if A[middle] > key:
            M += 1
            right = middle
        else:
            M += 1
            left = middle
        if A[middle] == key:
            M += 1
            print("BSearch:\nFound:",A[left],"\nM =", M)
            return
    if A[middle] != key:
        print("BSearch:\n No Value","\n M =", M)
        return

##########################



csvArr = []
csvA = []

rowNum = 0
numEl = 0
y = 0

ML = 0
OM = 0
OQ = 0
OT = 0
MT = 0
CFT = 0
CM = 0
CQ = 0
BubArr = []
MerArr = []
QArr = []
TArr = []
re = 0
num = 0
value = 0
"""
Отсеивание по нужной дате
FirstDay = 315532800
SecondDay = 473299200
numEl = len(csvArr)

while numEl != 0:
    if csvArr[rowNum][1] >= FirstDay or csvArr[rowNum][1] <= SecondDay:
            csvA.append(csvArr[rowNum])
            f += 1
    rowNum += 1
    numEl -= 1

csvArr.clear()"""
print('How you want to test this programm?\n If you want to enter values, enter 1.\n If you want to generate values, enter 2.')
re = int(input())
if re == 2:
    print('Enter number of elements,')
    num = int(input())
    #print('CSV:\n', csvArr) f = open('Logs.txt', 'w')
    csvArr = [random.randint(0, num*100) for i in range(num)]
elif re == 1:
    print('Enter elements(>1)')
    csvArr = list(map(int, input().split(' ')))
"""
для работы с файлами с расширением *.csv 
else:
    with open('L70.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            csvArr.append(row)
"""
key = csvArr[random.randint(0, len(csvArr) - 1)]
print('Find:', key,'\n\n')

tic = time.time()
TArr = SortTree(csvArr)
tic = time.time() - tic
print('TreeSort:\nC =', OT,"\nM =",MT,"\nTime =", tic,'\n\n')

print('FindTree:')
tic = time.time()
f = FindTree(csvArr,key)
tic = time.time() - tic
print('C =', CFT,"\nTime =", tic,'\n\n')

tic = time.time()
QArr = QuickSort(csvArr)
tic = time.time() - tic
print('QSort:\nC =',OQ,"\nM =",CQ,'\nTime =', tic,'\n\n')

tic = time.time()
MerArr = MergeSort(csvArr)
tic = time.time() - tic
print('MergeSort:\nC =',OM,"\nM =",CM,'\nTime =', tic,'\n\n')

tic = time.time()
lineF(csvArr,key)
tic = time.time() - tic
print('Time =', tic,'\n\n')

tic = time.time()
BiSear(csvArr,key)
tic = time.time() - tic
print('Time =', tic,'\n\n')

print('BubbleSort:')
tic = time.time()
BubArr = BSort(csvArr)
tic = time.time() - tic
print('Time =',  tic)

