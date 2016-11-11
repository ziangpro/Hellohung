# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:01:01 2016

@author: jiang
"""


direct = "/home/jiang/Downloads/mogpl/puzzles/"

import numpy as np

def read_game(nom):
    f = open(direct+nom, 'r')
    n,m = f.readline().split()
    ls = []
    for i in range(int(n)):
        ls+=[list(f.readline().split())]
    f.close()
    return np.array(ls)
    
   
'''
mat1 = read_game('test/test1.text')
mat2 = read_game('test/test2.text')
mat3 = read_game('test/test3.text')
'''

def print_game(mat):
    for i in range(mat.shape[0]):
        print "\t".join(mat[i,:])

''' 
print_game(mat2)
'''


N=8



