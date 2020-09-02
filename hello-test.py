import unittest
from helloWorld import printHelloWorld

class TestHello(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testHello(self): 
        self.assertEqual(printHelloWorld(),'Hello World!')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()