"""
Kipsy Quevada
SSW-567-WS: SW Testing, Qual. Assur. & Maint
Fall 2018 | Professor Rich Kempinski
HW 01: Testing triangle classification
AMDG
"""
#---------------------------------------------------------------------------



# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if a == b and b == c: # do not test for a == c because redundant
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    elif a != b and b != c and c != a:
        return 'Scalene'
    elif (a+b) <= c or (a+c) <= b or (c+b) <= a:
        return 'NotATriangle'
    elif (b+c) == ((a) ** 2) or (a+c) == ((b) ** 2):
        return 'Right' 
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertNotEqual(classifyTriangle(3,4,5),'Right','Should also be Right, but correctly returns Scalene')
        self.assertNotEqual(classifyTriangle(3,4,10),'NotATriangle','Technically scalene because neither side is equal, but primarily NotATriangle because 3+4 < 10')
        self.assertNotEqual(classifyTriangle(0,1,2),'NotATriangle','Technically scalene because neither side is equal, but primarily NotATriangle because at least one side has no length')
        self.assertNotEqual(classifyTriangle(-1,2,3),'NotATriangle','Technically scalene because neither side is equal, but primarily NotATriangle because at least one side has negative length')
        self.assertNotEqual(classifyTriangle('a',2,3),'NotATriangle','Technically scalene because neither side is equal, but primarily NotATriangle because at least one side is not a number')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','Correctly returns Equilateral')
        self.assertNotEqual(classifyTriangle(1,1,1),'Isoceles','Correctly returns Equilateral')
        self.assertEqual(classifyTriangle(4,4,7),'Isoceles','Correctly returns Isoceles')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Correctly returns Scalene')



if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(10,10,10)
    
    # unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    