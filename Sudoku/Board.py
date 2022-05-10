import numpy as np
from collections import defaultdict

class Board:

    board = {}
    row = 'ABCDEFGHI'
    col = '123456789'
    rows = []
    cols = []
    groups = []
    all = []
    peers = {}
    unis = {}
    boxes = []

    def __init__(self, start):

        self.boxes = [r + c for r in self.row for c in self.col]

        for val, key in zip(start, self.boxes):
            if val == '0':
                self.board[key] = '123456789'
            else:
                self.board[key] = val

        self.rows = [self.group(r, self.col) for r in self.row]
        self.cols = [self.group(self.row, c) for c in self.col]
        self.groups = [self.group(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

        self.all = self.rows + self.cols + self.groups

        self.units = self.extract_units(self.all, self.boxes)
        self.peers = self.extract_peers(self.units, self.boxes)


    
    def extract_peers(self, units, boxes):

        peers = defaultdict(set)  # set avoids duplicates
        for key_box in boxes:
            for unit in units[key_box]:
                for peer_box in unit:
                    if peer_box != key_box:
                    # defaultdict avoids this raising a KeyError when new keys are added
                        peers[key_box].add(peer_box)
        return peers

    def extract_units(self, unitlist, boxes):

        units = defaultdict(list)
        for current_box in boxes:
            for unit in unitlist:
                if current_box in unit:
                    # defaultdict avoids this raising a KeyError when new keys are added
                    units[current_box].append(unit)
        return units

    def group(self, A, B):

        return [x+y for x in A for y in B]
      

    def print(self, values):

        width = 1+max(len(values[s]) for s in self.boxes)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.row:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in self.col))
            if r in 'CF': print(line)
        print()
        
       
      
        




