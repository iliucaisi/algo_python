import sys
import random

def generate_number():
	return random.randint(0, MAX_INT - 1)
def generate_data(amount):
	print "DEBUG generate_data"
	try:
		data = open(DATA_FILE, 'a+')
		for i in range(0, amount):
			data.write(str(generate_number()))
			data.write('\n')
		data.close()
	except Exception as e:
		print "[ERROR] Failed to write"
		print e
		data.close()

def sort():
	print "DEBUG sort"
	bitmap = [0] * (MAX_INT)
	try:
		data = open(DATA_FILE, "r+")
		lines = data.readlines()
		data.close()
	except Exception as e:
		print "Failed to read file"
		print e
		data.close()

	for line in lines:
		i = int(line[:-1])
		if bitmap[i] & 3 == 0:
			bitmap[i] |= 1 
		elif bitmap[i] & 3 == 1:
			bitmap[i] &= 0
			bitmap[i] |= 2
		else:
			pass
		
	for i in range(0, len(bitmap)):
		if bitmap[i] & 3 == 2:
			print "Duplicated: ", i

##################################################
#						main					 #
##################################################

DATA_FILE="./data.txt"
MAX_INT=100000000

if len(sys.argv) != 2:
	print "Usage:"
	print "\tpython ", __file__, " <number>"
	print "\t<number> is the amount of numbers less MAX_INT"
	exit(0)

amount = int(sys.argv[1])
generate_data(amount)
sort()
