import sys
import random

def generate_ip():
    ip = []
    i = 0
    while i < 4:
        ip.append(str(random.randint(0,2)))
        i += 1
    return '.'.join(ip)

def generate_file(file_name):
    ip_data = open(file_name, 'w+')
    i = 0
    try:
        while i < MAX_LINES:
            ip_data.write(generate_ip())
            ip_data.write('\n')
            i += 1
        ip_data.close()
    except Exception as e:
        print "Error Write Failed"
        print e
        ip_data.close()

def map_to_blocks(file_name):

    blocks = dict()
    try:
        for line in open(file_name).readlines():
            key = hash(line) % BLOCKS_NUMBER
            if blocks.get(key) is None:
                block = open(DATA_DIR+str(hash(line) % BLOCKS_NUMBER), 'a+')
                blocks.update({key: block})
            else:
                block = blocks.get(key)
            block.write(line)

        for block in blocks.values():
            block.close()
    except Exception as e:
        print "ERROR Failed to write"
        print e

    return blocks

def count_per_block(blocks):
    count_of_top = []
    count_per_ip = dict()
    for key in blocks.keys():
        count_per_ip.clear()
        
        try:
            block = open(DATA_DIR + str(key), "r+")
            lines = block.readlines()
            block.close()
        except Exception as e:
            print "ERROR Failed to read"
            print e
        for line in lines:
            value = count_per_ip.get(line[:-1])
            if value is None:
                count_per_ip.update({line[:-1]: 1})
            else:
                count_per_ip.update({line[:-1]: value + 1})
        
        flag = False
        for item in count_per_ip.items():
            if flag is False:
                max_item = item
                flag = True

            if max_item[1] < item[1]:
                max_item = item
        count_of_top.append(max_item)
    print "DEBUG count_of_top size:", len(count_of_top)
    return count_of_top

def sort_count(count_of_top):
    print "DEBUG sort_count+"
    print "Original count_of_top", count_of_top
    len_count = len(count_of_top)
    # create min heap
    i = (len_count - 1) / 2
    while  i > 0:
        j = i
        while j < len_count:
            if (2 * j + 2) < len_count and count_of_top[2 * j + 1][1] > count_of_top[2 * j +2][1]:
                if count_of_top[j][1] > count_of_top[2 * j + 2][1]:
                    count_of_top[j], count_of_top[2 * j + 2] = count_of_top[2 * j + 2], count_of_top[j]
                    j = 2 * j + 2
                    continue
            if (2 * j + 1) < len_count and count_of_top[j][1] > count_of_top[2 * j + 1][1]:
                count_of_top[j], count_of_top[2 * j + 1] = count_of_top[2 * j + 1], count_of_top[j]
            j = 2 * j + 1
        i -= 1

    print "Min heap: ", count_of_top
    
    unsorted = len_count - 1

    while unsorted > 0:
        count_of_top[0], count_of_top[unsorted] = count_of_top[unsorted], count_of_top[0]
        unsorted -= 1
        j = 0
        while j < unsorted:
            if (2 * j + 2) < unsorted and count_of_top[2 * j + 1][1] > count_of_top[2 * j +2][1]:
                if count_of_top[j][1] > count_of_top[2 * j + 2][1]:
                    count_of_top[j], count_of_top[2 * j + 2] = count_of_top[2 * j + 2], count_of_top[j]
                    j = 2 * j + 2
                    continue
            if (2 * j + 1) < unsorted and count_of_top[j][1] > count_of_top[2 * j + 1][1]:
                count_of_top[j], count_of_top[2 * j + 1] = count_of_top[2 * j + 1], count_of_top[j]
            j = 2 * j + 1
    
    print "Sorted count_of_top: ", count_of_top
    print "DEBUG sort_count-"
    return count_of_top

##################################################
#                   main                         #
##################################################
MAX_LINES=100
BLOCKS_NUMBER=5
DATA_DIR="data/"
if len(sys.argv) != 2:
    print "Usage:"
    print "\t python ", __file__, "<file>"
    print "\t <file> ips."
    exit(0)
file_name = sys.argv[1]
generate_file(file_name)
blocks = map_to_blocks(file_name)
count_of_top = count_per_block(blocks)
sort_count(count_of_top)
print "Top 1: ", count_of_top[0]
