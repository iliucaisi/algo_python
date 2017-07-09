import sys
import random

def generate_number():
	return random.randint(0, MAX_INT)
def generate_data(amount):
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
	bitmap = [0] * (MAX_INT/32)
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
		bitmap[i / 32] |= 1 << i % 32

	for i in range(0, len(bitmap)):
		bit = 1
		bucket = bitmap[i]
		while bucket != 0:
			if bucket & 1 == 1:
				print (32 * i) + bit - 1
			bucket >>= 1
			bit += 1	

##################################################
#						main					 #
##################################################

DATA_FILE="./data.txt"
MAX_INT=1000000000

if len(sys.argv) != 2:
	print "Usage:"
	print "\tpython ", __file__, " <number>"
	print "\t<number> is the amount of numbers less MAX_INT"
	exit(0)

amount = int(sys.argv[1])
generate_data(amount)
sort()
