from __future__ import print_function
import sys

class Node(object):
	def __init__(self, value, next_ref):
		self.value = value
		self.next_ref = next_ref

class SinglyLinkedList(object):
	def __init__(self, head):
		self.head = head
	def add(self, element):
		temp = Node(element, None)
		if self.head is None:
			self.head = temp
			return
		current = self.head
		while current.next_ref is not None:
			current = current.next_ref
		
		current.next_ref = temp

	def traverse(self):
		current = self.head
		while current is not None:
			print(current.value, ' ', end='')
			current = current.next_ref

	def reverse(self):
		pre = None
		current = self.head
		post = None
		while current is not None:
			post = current.next_ref
			current.next_ref = pre
			pre = current
			current = post
		
		self.head = pre		
			 
		
##################################################
#	            		main		         	 #	
##################################################

if len(sys.argv) != 2:
	print("Usage:")
	print("\tpython ", __file__, " <node_values>")
	print("\t<node_values> is separated by comma.")
	exit(0)

str1 = sys.argv[1].split(',')
linked_list = SinglyLinkedList(None)
for s in str1:
	linked_list.add(s)
print("Original: ")
linked_list.traverse()
linked_list.reverse()
print("Reversed: ")
linked_list.traverse()

