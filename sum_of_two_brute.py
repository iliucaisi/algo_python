import sys

def brute(str1, num):
    it=iter(str1.split(","))
    dict_digits = {}
    i = 1
    while True:
        try:
            dict_digits.update({int(it.next()): i})
            i = i + 1
	except StopIteration:
            break
    
    it = dict_digits.iteritems()
    while True:
        try:
            num_1 = it.next()
            index_num_1 = num_1[1]
            num_2 = num - num_1[0]
            index_num_2 = dict_digits.get(num_2)
            if index_num_2 is not None:
                if index_num_1 < index_num_2:
                    return index_num_1, index_num_2
                else:
                    return index_num_2, index_num_1
        except StopIteration:
            pass

##################################################
#			main			 #
##################################################

if len(sys.argv) != 3:
	print "Usage:"
	print "\tpython ", __file__, " <str1> <k>"
	print "\t<str1> separated by comma"
	exit(0)
str1 = sys.argv[1]
k = int(sys.argv[2])
print brute(str1, k) 
