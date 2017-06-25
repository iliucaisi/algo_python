import sys

def find(str1, sub_str1):
	len_str1 = len(str1)
	len_sub_str1 = len(sub_str1)
	occurence = [0 for i in range(len_sub_str1)]
	char_index = [-1 for i in range(len_str1)]
	begin = 0
	end = 0
	head = 0
	rear = len(str1) - 1
	while end < len_str1:
		# check if end in sub_str1
		is_in = False
		i = 0
		while i < len_sub_str1:
			if sub_str1[i] == str1[end]:
				occurence[i] = occurence[i] + 1
				char_index[end] = i
				is_in = True
				break
			i = i + 1
	
		if is_in == True:
			while begin <= end:
				if char_index[begin] == -1:
					begin = begin + 1
				elif occurence[char_index[begin]] > 1:
					occurence[char_index[begin]] = occurence[char_index[begin]] - 1
					begin = begin + 1
				else:
					break
			i = 0	
			while i < len_sub_str1:
				if occurence[i] <= 0:
					break
				i = i + 1

			if i == len_sub_str1 and (end - begin) < (rear - head):
				head = begin
				rear = end

		end = end + 1

	print "Shortest substring: ", str1[head:rear+1]

##################################################
#					main						 #
##################################################

str1 = sys.argv[1]
sub_str1 = sys.argv[2]

find(str1, sub_str1)
