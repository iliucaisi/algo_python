import sys

def remove_match(pattern_set, str1):
	len_str1 = len(str1)
	if len_str1 <= 0:
		return None
	i = 0
	removed = []
	while i < len_str1:
		if str1[i] not in pattern_set:
			removed.append(str1[i])
		i = i + 1
	return ''.join(removed)


##################################################
#                     Main                       #
##################################################

if len(sys.argv) != 3:
	print 'Usage:'
	print '\tpython ', __file__, '<pattern_set>', '<str1>'
	exit(0)				

pattern_set = set(sys.argv[1])
str1 = sys.argv[2]
 

print remove_match(pattern_set, str1)
