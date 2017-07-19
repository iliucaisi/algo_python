import sys

class stack(object):
	def __init__(self):
		self.elements = []
		self.min_stack = []

	def min(self):
		return self.min_stack[-1]
	def push(self, e):
		self.elements.append(e)
		if len(self.min_stack) == 0:
			self.min_stack.append(e) 
		elif e < self.min_stack[-1]:
			self.min_stack.append(e)
		else:
			self.min_stack.append(self.min_stack[-1])
	def pop(self):
		self.min_stack.pop()
		return self.elements.pop()


##################################################
#					main						 #
##################################################

str1 = sys.argv[1].split(',')

it = iter(str1)
numbers = []
while True:
	try:
		numbers.append(int(it.next()))
	except StopIteration:
		break
s_numbers = stack()
for i in numbers:
	s_numbers.push(i)

print "Min numbers is: "
print s_numbers.min()

