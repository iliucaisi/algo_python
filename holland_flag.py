import sys

def sort_colors(colors):
    begin = 0
    current = 0
    end = len(colors) - 1

    while current < end:
        if colors[current] == 0:
            colors[begin], colors[current] = colors[current], colors[begin]
            if begin == current:
                current = current + 1
            begin = begin + 1
        elif colors[current] == 1:
            current = current + 1
        elif colors[current] == 2:
            colors[current], colors[end] = colors[end], colors[current]
            end = end - 1
        else:
            print "Error color!"
            return
    return colors
##################################################
#	            main	         	 #
##################################################

if len(sys.argv) != 2:
	print "Usage:"
	print "\tpython ", __file__, " <colors>"
	print "\t<colors> separated by comma, 0 red, 1 white, 2 blue"
	exit(0)

it = iter(sys.argv[1].split(","))

colors = []
while True:
    try:
        colors.append(int(it.next()))
    except StopIteration:
        break
print "Sorted colors is: ", sort_colors(colors)

