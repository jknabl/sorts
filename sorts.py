#!/usr/bin/python
from time import time
import random
#sorts a list of items
class Sort():
	def __init__(self, list):
		self.list = list
	def mergeSort(self, list=None):
		if list==None:
			list = self.list
		if len(list) < 2:	
			return list
		midpoint = len(list) / 2
		left = self.mergeSort(list[:midpoint])
		right = self.mergeSort(list[midpoint:])
		return self.merge(left, right)
	#helper funct'n for mergesort
	def merge(self, left, right):
		result = []
		i, j = 0, 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:]
		result += right[j:]
		return result
	def bubbleSort(self, list=None):
		if list==None:
			list = self.list
			swapped = True
			while swapped:
				swapped = False
				for x in range(0, len(list)-1):
					if list[x] > list[x+1]:
						list[x], list[x+1] = list[x+1], list[x]
						swapped = True
		return list
	def selectionSort(self, list=None):
		if list==None:
			list = self.list
		for x in range(0, len(list)-1):
			min = x
			for y in range(min+1, len(list)):
				if list[y] < list[min]:
					min = y
			list[x], list[min] = list[min], list[x]
		return list
	def insertionSort(self, list=None):
		if list==None:
			list = self.list
		for i in range(1, len(list)-1):
			item = list[i]
			while i > 0 and list[i-1] > item:
				list[i], i = list[i-1], i-1
			list[i] = item
		return list
	def shellSort(self, list=None):
		if list==None:
			list = self.list
		#gap sequence is Marcin Ciura's, as reproduced
		#on wiki. You can use any sequence as long as it
		#contains a 1 (1 ensures a complete sort)
		gaps = [701, 301, 132, 57, 23, 10, 4, 1]
		for gap in gaps:
			indx = 0
			for i in range(gap, len(list)):
				temp = list[i]
				for j in range(gap, i):
					if list[j-gap] > temp:
						list[j] = list[j-gap]
					indx = j
				list[indx] = temp
		return list
	def combSort(self, list=None):
		if list==None:
			list = self.list
		#based on gap concept like shell sort
		shrinkFactor = 1.247330950103979
		gap = len(list)
		swapped = True
		while swapped==True and gap > 1:
			gap = int(gap/shrinkFactor)
			if gap < 1:
				#min gap = 1
				gap = 1
			i = 0
			swapped = False
			while (i+gap) >= len(list):
				if list[i] > list[i+gap]:
					list[i], list[i+gap] = list[i+gap], list[i]
					swapped = True
				i += 1
		return list	
	def timedRun(self, func, list=None):
		"""Returns a 2-item list. i[0] is the sorted array,
		#i[1] is the runtime
		
		"""
		if list==None:
			list=self.list
		start = time()
		sorted = func(list)
		elapsed = (time() - start)
		return [sorted, elapsed]

#this is a helper function to easily generate a list
def generateList(items, low=1, high=100):
	#generates list of integers between an (optional) range of 
	#values. Default range is 1-100. 
	return [random.randint(low, high) for x in range(1, items)] 

def main():
	n = 10000
	low = 1
	high = 100
	testlist = generateList(n, low, high)
	sort = Sort(testlist)
	print "Merge sort took %s seconds." % sort.timedRun(sort.mergeSort)[1]
	print "Bubble sort took %s seconds." % sort.timedRun(sort.bubbleSort)[1]
	print "Selection sort took %s seconds." % sort.timedRun(sort.selectionSort)[1]
	print "Insertion sort took %s seconds." % sort.timedRun(sort.insertionSort)[1]
	print "Shell sort took %s seconds." % sort.timedRun(sort.shellSort)[1]
	print "Comb sort took %s seconds." % sort.timedRun(sort.combSort)[1]

if __name__ == '__main__':
	main()
