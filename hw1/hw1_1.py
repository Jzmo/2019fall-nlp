#! /usr/bin/python
import sys
import random

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
def store_dict(line):
    key = line[1]
    value = line[2].split(' ')
    value = value[:value.index('')] if '' in value else value
    if key in dict_:
        dict_[key].append(value)
    else:
        dict_[key] = [value]

def random_tree(root):
    if root.val not in dict_:
        sent.append(root.val)
        return root.val
    else:
        leafs = random.choice(dict_[root.val])
        root.next = [Node(l) for l in leafs]
        for l in root.next:
            random_tree(l)            

    
if __name__ == '__main__':
    
    gr_path = sys.argv[1]
    n_sent = int(sys.argv[2]) if len(sys.argv) >2  else 1
    sent = []
    parse = []
    dict_ =  {}
    with open(gr_path,'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.rstrip().split('\t')
            if line[0]== '1':
                store_dict(line)
    f.close()
    print(dict_)

    for i in range(n_sent):
        root = Node('ROOT')
        random_tree(root)
        print(' '.join(sent))
        sent = []
    
    
