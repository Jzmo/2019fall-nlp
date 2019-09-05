#! /usr/bin/python
import sys
import random
import argparse

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
def store_dict(line):
    key = line[1]
    value = line[2].split(' ')
    value = value[:value.index('')] if '' in value else value
    if key in dict_:
        dict_[key][0].append(value)
        dict_[key][1].append(int(line[0]))
    else:
        dict_[key] = ([value],[int(line[0])])

class CFG:
    def __init__(self, M, dict_):
        self.n_nd = None
        self.M = M
        self.sent = None
        self.dict_ = dict_

    def build(self,root):
        self.sent = []
        self.n_nd = 0
        self.random_tree(root)
        self.n_nd = 0
    def random_tree(self,root):
        if root.val not in self.dict_:
            self.sent.append(root.val)
            return
        else:
            self.n_nd +=1
            if self.n_nd >= self.M:
                self.sent.append('...')
                return
            leafs = random.choices(self.dict_[root.val][0],weights = self.dict_[root.val][1])[0]
            root.next = [Node(l) for l in leafs]
            for l in root.next:
                self.random_tree(l)
    def get_sent(self):
        return self.sent
    
    def print_tree(self, prefix,root,suffix):
        curr = root
        if not curr: print('(ROOT)')
        if curr.next is None:
            print(prefix + curr.val + suffix)
        else:
            last_nd = '('+curr.val+' '
            prefix += last_nd
            suffix += ')'
            for i,l in enumerate(curr.next):
                if i != 0:
                    prefix = ' '*len(prefix)
                if i != len(curr.next)-1:
                    self.print_tree(prefix,l,'')
                else:
                    self.print_tree(prefix,l,suffix)
        
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()    
    parser.add_argument('-t',action = 'store_true',required = False)
    parser.add_argument('res', nargs='*')
    
    args = parser.parse_args()
    use_parse = args.t
    res = args.res
    
    gr_path = res[0]
    n_sent = int(res[1]) if len(res) >1  else 1
    M = int(res[2]) if len(res) >2  else 450
    parse = []
    dict_ =  {}
    with open(gr_path,'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.rstrip().split('\t')
            if line[0].isnumeric():
                store_dict(line)
    f.close()


    for i in range(n_sent):
        print('============================================================')
        root = Node('ROOT')
        cfg = CFG(M,dict_)
        cfg.build(root)
        
        if use_parse:
            cfg.print_tree('',root,'')
        else:
            sent = cfg.get_sent()
            print(' '.join(sent))
    
