#!/usr/bin/env python
#author : Chi Zhang
#org: SHRC, EECS, Peking University

import sys

class TreeNode(object):
    def __init__(self,label=None,node_type=None,word=None,children=None,word_span=None,string_span=None):
        self.label=label
        self.node_type=node_type
        self.word=word
        self.children=children
        self.word_span=word_span
        self.string_span=string_span
        self.parse_finished=False
        
    node_types=['terminal','constituent','pos']

class Tree(object):
    def __init__(self, delimiters=None, bracket_sym=None):
        if not delimiters:
            self.delimiters=[' ', '\t']
            self.bracket_sym=['(',')']
            self.bracket_sym_start=self.bracket_sym[0]
            self.bracket_sym_end=self.bracket_sym[1]
        self.nodes=None
        self.root=None

    def parse_brackets_string(self, brackets_string):
        states = ['start','error','bracket_sym_start','label_done','bracket_sym_end']
        state = 'start'
        i=0
        while i < len(brackets_string):
            if brackets_string[i] in self.delimiters:
                state='start'
                i+=1
                continue
            elif brackets_string[i] == bracket_sym_start:
                root=TreeNode("","constituent","",list(),(0,None),(i,None))
                state='bracket_sym_start'
                i+=1
                continue
            elif state=='bracket_sym_start' and brackets_string[i] not in self.delimiters:
                root.label+=brackets_string[i]
                i+=1
                continue
            elif state=='bracket_sym_start' and brackets_string[i] in self.delimiters:
                root,i=parse_brackets_string_helper(root, brackets_string[i:])
                root.parse_finished=True
                state='bracket_sym_end'
                continue
            else:
                state='error'
                print >> sys.stderr, 'brackets_string is not right, parsing failed!'
                break
        
        return root
        

    def parse_brackets_string_helper(self, root, brackets_string):
        states = ['start','error','bracket_sym_start','label_done','bracket_sym_end']
        i=0
        while i < len(brackets_string):
        pass
