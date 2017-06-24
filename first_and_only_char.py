import sys

def count_all(str1):
	len_str1 = len(str1)
	if len_str1 <= 0:
		return None
	i = 0
	counts={}
	while i < len_str1:
		if counts.has_key(str(str1[i])) == False:
			counts.update({str(str1[i]):1})
		else:
			counts.update({str(str1[i]):  counts.get(str(str1[i])) + 1})
		i = i + 1

	return counts

def find_first_and_only(str1):
	len_str1 = len(str1)
	if len_str1 <= 0:
		return None
	counts = count_all(str1)
	i = 0
	while i < len_str1:
		if counts.get(str(str1[i])) == 1:
			return str1[i]
		i = i + 1
	return None

##################################################
#                     Main                       #
##################################################

str1 = sys.argv[1]
print find_first_and_only(str1)
