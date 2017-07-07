import sys
import re

def segmentate(data1):
    return re.split('\s\n+|\s+|,\s+|\'', data1)

def count_on_hash_map(str1):
    file1 = open(str1,'r')
    data1 = segmentate(file1.read())
    dict_data = {}
    it = iter(data1)
    while True:
        try:
            key = it.next()
            value = dict_data.get(key)
            if value != None:
                dict_data.update({key: value + 1})
            else:
                dict_data.update({key: 0})
            print "DEBUG key=", key, "value=", value
        except StopIteration:
            break
    file1.close()

    it = iter(data1)
    most_common = ''
    most_times = 0
    while True:
        try:
            key = it.next()
            value = dict_data.get(key)
            if value > most_times:
                most_common = key
                most_times = value
        except StopIteration:
            break;

    print "Most common string is: ", most_common, " times: ", most_times

##################################################
#                     main					  	 #     
##################################################
if len(sys.argv) != 2:
	print "Usage:"
	print "\tpython ", __file__, " <file>"
	exit(0)

str1 = sys.argv[1]
count_on_hash_map(str1)

