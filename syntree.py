#!/usr/bin/env python

class TreeNode(object):
    def __init__(self):
        self.label=None
        self.node_type=None
        self.word=None
        
    node_types=['terminal','constituent','pos']

class Tree(object):
    def __init__(self, delimiters=None, bracket_sym=None):
        if not delimiters:
            self.delimiters=[' ', '\t']
            self.bracket_sym=['(',')']
            self.bracket_sym_start=self.bracket_sym[0]
            self.bracket_sym_end=self.bracket_sym[1]

    def parse_brackets_string(self, brackets_string):
        
        pass

    def parse_brackets_string_helper(self, root, brackets_string):
        
        pass
