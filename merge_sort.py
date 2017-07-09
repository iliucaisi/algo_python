import sys

def merge_sort(arr, start, end):
    if start >= end:
        return

    mid = start + ((end - start) >> 1)
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    # merge
    len_left = mid - start + 1
    left_arr = [0] * (len_left)
    for i in range(0, len_left):
        left_arr[i] = arr[start + i]
   
    len_right = end - mid
    right_arr = [0] * (len_right)
    for j in range(0, len_right):
        right_arr[j] = arr[mid + 1 + j]

    left = 0
    right = 0
    while left < len_left and right < len_right:
        if left_arr[left] < right_arr[right]:
            arr[start] = left_arr[left]
            left += 1
        else:
            arr[start] = right_arr[right]
            right += 1
        start += 1
    while left < len_left:
        arr[start] = left_arr[left]
        start += 1
        left += 1

    while right < len_right:
        arr[start] = right_arr[right]
        start += 1
        right += 1
##################################################
#                   main                         #
##################################################


if len(sys.argv) != 2:
    print "Usage:"
    print "\tpython ", __file__, " <sequence>"
    exit(0)
str1 = sys.argv[1].split(',')
it = iter(str1)

numbers = []
while True:
    try:
        numbers.append(int(it.next()))
    except StopIteration:
        break
merge_sort(numbers, 0, len(numbers) - 1)

print numbers


