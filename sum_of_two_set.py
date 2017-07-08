from __future__ import print_function
import sys

def sum_of_k_number(left, current, right, summary, result):
    result[current] = True
    if left + current == summary:
        i = 1
        while i <= current:
            if result[i] == True:
                print(i, end='')
            i = i + 1
        print("")
    else:
        if left + current + current + 1 <= summary:
            sum_of_k_number(left + current, current + 1, right - current, summary, result)
        
        if left + current + right >= summary and left + current <= summary:
            result[current] = False
            sum_of_k_number(left, current + 1, right - current, summary, result)

##################################################
#			main			 #
##################################################

if len(sys.argv) != 3:
	print("Usage:")
	print("\tpython ", __file__, " <str1> <k>")
	print("\t<str1> separated by comma")
	exit(0)
upper = int(sys.argv[1])
summary = int(sys.argv[2])
result = [False for i in range(0, upper)]
sum_of_k_number(0, 1, (upper + 1) * upper / 2, summary, result)
