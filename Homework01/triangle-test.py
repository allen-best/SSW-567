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
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        return 'Right'
    elif not(a == b or b == c or c == a):
        return 'Scalene'
    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSetRightTriangle(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(36,77,85),'Right','36,77,85 is a Right triangle')
        self.assertEqual(classifyTriangle(28,45,53),'Right','28,45,53 is a Right triangle')
        self.assertEqual(classifyTriangle(11,60,61),'Right','11, 60, 61 is a Right triangle')
    
    def testSetEquilateral(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a Equilateral triangle')
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 is a Equilateral triangle')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 is a Equilateral triangle')
        self.assertEqual(classifyTriangle(35,35,35),'Equilateral','35,35,35 is a Equilateral triangle')

    def testSetIsoceles(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,3),'Isoceles','3,4,3 is a Isoceles triangle')
        self.assertEqual(classifyTriangle(13,6,13),'Isoceles','3,4,5 is a Isoceles triangle')
        self.assertEqual(classifyTriangle(23,23,8),'Isoceles','3,4,5 is a Isoceles triangle')
        self.assertEqual(classifyTriangle(64,90,90),'Isoceles','3,4,5 is a Isoceles triangle')

    def testSetScalene(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','3,4,5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','3,4,5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(7,10,13),'Scalene','3,4,5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(17,86,12),'Scalene','3,4,5 is a Scalene triangle')

    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
