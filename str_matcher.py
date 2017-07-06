import sys

def brute_match_with_wildcard(str1,str2):
    str1_len = len(str1)
    str2_len = len(str2)

    i = 0
    j = 0
    skip = False
    skip_count = 0
    matched=[]

    if str1_len == 1 and str1[0] == "*":
	print "Matched ", str2
	exit(0)

    while (i < str1_len) and (j < str2_len):
	if str1[i] == '*':
		skip = True
		i = i + 1
		continue
	if str1[i] == str2[j]:
		skip = False
		matched.append(str2[j])
		i = i + 1
	elif skip == True:
		matched.append(str2[j])
	elif str1[i] == "?":
		matched.append(str2[j])
		i = i + 1
	else:
		matched = []
		i = 0
	
	j = j + 1
    if skip == True:
	matched.append(str2[j:])

    print "Matched: ","".join(matched) 

def brute_match_without_wildcard(str1, str2):
    '''
    str1 - text string
    str2 - pattern string
    '''
    len_str1 = len(str1)
    len_str2 = len(str2)

    i = 0
    j = 0

    while i < len_str1 and j < len_str2:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == len_str2:
        return i - j
    else:
        return -1


##################################################
#	        	Main    		 #
##################################################			
str1 = sys.argv[1]
str2 = sys.argv[2]

# brute_match_with_wildcard(str1, str2)

print "Matched pattern index is: ", brute_match_without_wildcard(str1, str2)

