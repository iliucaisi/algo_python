import sys

def swap_range(str1, start, end):
    if (end - start + 1) % 2 != 0:
        print "Invalid range, must have even numbers"
        return
    i = start
    while i < end:
        str1[i], str1[i + 1] = str1[i + 1], str1[i]
        i = i + 2
    return str1

def shuffle_brute(str1):
    len_str1 = len(str1)
    if len_str1 % 2 != 0:
        print "Invalid length, must have even numbers"
        return

    start = (len_str1 - 1) / 2
    end = start + 1
    while start > 0:
        swap_range(str1, start, end)
        start = start - 1
        end = end + 1

    return str1 

##################################################
#	            main	         	 #
##################################################

str1 = sys.argv[1].split(',')

print shuffle_brute(str1)
