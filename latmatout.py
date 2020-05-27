#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:43:37 2019

@author:Naveen Kumar Vasudevan, 
        400107764,
        Doctoral Student, 
        The Xi Research Group, 
        Department of Chemical Engineering,
        McMaster University, 
        Hamilton, 
        Canada.
        
        naveenovan@gmail.com
        https://naveenovan.wixsite.com/kuroonai
"""

'''
usage instruction:

add latmatout.py file to the working directory and then import the function as follows,

from latmatout import latout

Then pass the array you want as a input to the function 

eg: let a = numpy.random.rand(6,6)

a = array([[0.91133437, 0.52537912, 0.19705271],
       [0.64498759, 0.36254855, 0.15332323],
       [0.25554104, 0.33672888, 0.53121465]])

then latout(a)

will give a latex format output of the form,

\[
M =
\begin{bmatrix}
0.9113 & 0.5254 & 0.1971 \\0.6450 & 0.3625 & 0.1533 \\0.2555 & 0.3367 & 0.5312 \\
\end{bmatrix}
\]

Copy this segment to the *.tex file.

'''

import numpy as np

def latout(a):
    print('\[\nM =\n\\begin{bmatrix}')
    for r in range(len(a)):
        if len(a.shape) == 1:
            if r == list(range(len(a)))[-1]:print(r'%.4f \\'%a[r], end = ''),
            else:print('%.4f & '%a[r], end = ''),
            #print(r'\\')
        
        else:
            for c in range(len(a[0,:])):
                if c == list(range(len(a[0,:])))[-1]:print(r'%.4f \\'%a[r,c], end = ''),
                else:print('%.4f & '%a[r,c], end = ''),

    print('\n\\end{bmatrix}\n\]')