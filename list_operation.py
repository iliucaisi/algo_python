import sys

class MyArrayList:
	elementData = []
	size = 0	
	def __init__(self, elementData):
		self.elementData = elementData
		self.size = len(elementData)
	def contain(self, o):
		i = 0
		while i < self.size:
			if self.elementData[i] == o:
				return True
			i = i + 1	
		return False

	def remove_all(self, c):
		'''
			Set complement
		'''
		tempData = []
		r = 0
		w = 0
		while r < self.size:
			if(c.contain(self.elementData[r]) == False):
				tempData.append(self.elementData[r])
			r = r + 1
		return tempData
	
	def retain_all(self, c):
		'''
			Set intersection
		'''
	 	tempData = []
		r = 0
		w = 0
		while r < self.size:
			if(c.contain(self.elementData[r]) == True):
				tempData.append(self.elementData[r])
			r = r + 1
		return tempData
		
	def add_all(self, c):
		'''
			Set union
		'''
		self.elementData.append(c)


##################################################
#					Main						 #
##################################################

list1 = MyArrayList(sys.argv[1].split(","))
list2 = MyArrayList(sys.argv[3].split(","))
op = sys.argv[2]
operations = {'^': list1.retain_all, '+': list1.add_all(list2), '-': list1.remove_all(list2)}

print operations.get(op)
