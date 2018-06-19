"""
Search Algorithms: and Big O, Big Omega and Big Theta Notations:
Big O ~ Worst Case Scenario of Algorithm Time and Space Performance
Big Omega ~ Best/Super Lucky Case Scenario
Big Theta ~ When Big O == Big Omega
Performance os following algorithms:

1) Linear Search:  O(n)  bc of single for loop
2) Selection Sort: O(n^2) bc of double for loop each to search for smallest element & Swap untill array's end
3) Bubble Sort: O(n^2) bc of Loop over n and n comparisons & swappings until array's end in each loop
4) Merge Sort Search: O(nlogn) Split and merge, better time lots of memory for store splits
5) Binary Search: O(logn) bc we simple have to split n 2 times until 1 and compare with middles at each split
6)


"""
'''
from math import exp
class Stack(object):
	""" stack implementation"""
	def __init__(self):
		self.items = [] #empty list for elements

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) -1]

	def size(self):
		return len(self.items)

s = Stack()


def  reverse_string(string):
	m = Stack()
	nstr = ''
	for s in string:
		m.push(s)

	while not m.isEmpty():
		ns = m.pop()
		nstr  += ns

	return nstr

name = "Temptations"

print(name)
re_name = reverse_string(name)

print("\n" )

print(re_name)
'''


import math

def min_elt(list):
	''' Takes a list and returns smallest element and its index in list'''
	tiny = list[0]
	index = 0
	for v in range(len(list)):
		if list[v] < tiny:
			tiny = list[v]
			index = v
	return tiny,index


def selection_sort(rlist):
	""" Sort a list in ascending order and return sorted list!"""
	for i in range(len(rlist)):
		sm_lest = rlist[i]
		sm_index = i  ## Cannnot set the index = 0, It must be i  Chai!, What a bug!!!
		for j in range(i, len(rlist)): ##Loop over subrange
			if rlist[j] < sm_lest:
				sm_lest = rlist[j]
				sm_index = j
        #Now swap elements
		temp = rlist[i]
		rlist[i] = sm_lest
		rlist[sm_index] = temp
	print("Sorted List is ", rlist)  #return sorted list


def printlst(list, mystring):
	print(mystring)
	print(" = [")
	for v in list:
		print(v)
	print("]")

'''
glist = [-1, 10, -20, 11, 12, 8, 6, 5, 3, 2]
sm_elt, sm_index = min_elt(glist)
print("Smallest element is {} with index {}".format(sm_elt, sm_index))

dlist = [-1, 1, -10, 11, 14, 8, 6, 5, 3, 2]

print(dlist)
selection_sort(dlist)
print("Original List is = {}".format(dlist))

'''


def num_sort(nlist):
	for r in range(len(nlist)):
		smNum = nlist[r]
		smIndex = r
		for m in range(r, len(nlist)):
			if nlist[m] < smNum:
				smNum = nlist[m]
				smIndex = m

    	## swap True smallest  with fake smallest
		temp = nlist[r]
		nlist[r] = smNum
		nlist[smIndex] = temp

	print("Sorted List is now = ",  nlist)

#nwList = [-10, -50, -100, 1, 300, 10, 15, 50, 89]

#num_sort(nwList)

#selection_sort(nwList)

def swap(a, b):
	'''
	fuction swaps two elements
	:return:
	:param a:
	:param b:
	:return:
	'''
	temp = a
	a = b
	b = temp
	return a, b

def bubble_sort(list):
	'''
	Bubble Sort Algorithm!
	:param list:
	:return:
	'''
	swapped = True
	while swapped:
		swapped = False
		for j in range(len(list)-1):
			if list[j] > list[j+1]:
				temp = list[j]
				list[j] = list[j+1]
				list[j+1] = temp
				swapped = True
		if not swapped:
			break

	print("Bubble Sorted List = {}".format(list))


def binarySearch(array, value, low, high):
	"""
	Implements the Binary Search algorithm:
	Takes list, value to search for, low and high and begins searching the array
	by continuously comparing with the middle element of the list to find out which
	half of the  list would the element most likely be found.
	:param array:
	:param value:
	:param low:
	:param high:
	:return: True/False
	"""
	if low > high:
		print("Value not found!!")
		return True
	middle = int((low + high)/2)

	if value == array[middle]:
		print("Value found at {}".format(middle))
		return True
	elif value > array[middle]:
		return binarySearch(array, value, middle+1, high)
	else:
	    return(binarySearch(array, value, low, middle-1))


#mlist = [4,9,7,1,3,6,5]

#print("Original List List = {}".format(mlist))

#bubble_sort(mlist)
#l, r = 10, 9
#print(" (l, r) = ( {}, {} )".format(l, r))
#l, r = swap(l, r)
#print(" Now (l, r) = ( {}, {} )".format(l, r))

marray = [1, 3, 4, 5, 7, 9, 13, 15, -6, 17, 19]

#binarySearch(marray, -1, 4, 17)

#if __name__ == "__main__"

def biggest(list):
	bgst = list[0]
	bidx = 0
	for val in list:
		if val > bgst:
			bgst = val
			bidx = list.index(val)
	return bgst, bidx


#print("Biggest Value is ( %i, %i) \n"  % biggest(marray))
#print("Biggest Value is %i \n"  % biggest(marray))


"""
Linked list from scratch
"""


from urllib import request
def download_stock_data(url, stockSymbol):
    """Download csv files from web.
    """
    url_response = request.urlopen(url)
    url_texts = url_response.read()
    csv_file = str(stockSymbol) + ".csv"
    lines = str(url_texts).split("\n")
    f = open(csv_file, 'w')
    for line in lines:
        f.write(line + "\n")
    f.close()

	

def fibonacci(n):
    """
     static programming of recursion, limitation
    :param n:
    :return:
    """
    result = 1
    if n ==1 or n == 2:
        return result
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib_dynamic_prog(n):
    """
    using dynamic solution in recursion
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    temp = [None] * (n+1)
    temp[0] = 1
    temp[1] = 1
    temp[2] = 1
    for i in range(3, n+1):
        temp[i] = temp[i-1] + temp[i-2]
    return temp[n]


def factorial(n):
    if n == 0: return 1
    return n*factorial(n-1)

def fact(n):
    result = 1
    if n == 0: return result
    while True :
        result *=n
        n -= 1
        if n == 0: break
    return result


## Print pairs in array

def findpairs(array, k):
    print("___________________________________________")
    print("Brute Force: Found Pairs with sum = {}\n".format(k))
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == k:
                print( "({0}, {1})".format(array[i], array[j]))
    print("___________________________________________")




a = 7

"""
print("{0} Factorial = {1} \n".format(a, factorial(a)))
print("{0} Fact = {1} \n".format(a, fact(a)))
from time import time

start = time()
print("{0} Fibonacci = {1}\n".format(a, fibonacci(a)))
end = time()
runtime = end - start
print(" Fibonacci Recursion took %2f seconds" %runtime)

start = time()
print("{0} Dynamic Fibonacci = {1} \n".format(a, fib_dynamic_prog(a)))
end = time()
runtime = end - start
print(" Dynamic Fibonacci took %2f seconds" %runtime)

"""


k = 8
b = [1, 2, 5, 3, 4, 4, 9, 15, 7, 20, 25, 10, 8, 0]

findpairs(b, k)

print("{0} Fact = {1} \n".format(a, fact(a)))

print("{0} Factorial = {1} \n".format(a, factorial(a)))