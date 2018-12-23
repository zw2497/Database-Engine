from optimizer import *
from ops import *
from compiler import *
import unittest
from db import Database
#from parse_sql import parse
import random
import timeit

	#These functions test whether your code is computing cardinalities correctly. 
    #We've hardcoded in values from our master databass. 
    
    #We're also checking whether your implementation beats the exhaustive_bestplan, 
    #which if you follow the suggested directions, should automatically happen.
    
class TestUnits(unittest.TestCase):

    def tearDown(x):
        print """"

########################################

PASSING THE TEST CASES DOES NOT MEAN YOUR OPTIMIZER IS WORKING since we are not asserting anything in them.

Make sure your query plan matches the one provided in the comments of each test case.

########################################
"""

   
    def test_card_cost(self):
        
        from db import Database

        f = From([
        Scan("data", "A"),
        Scan("data", "B"),
        ])
  
        preds = cond_to_func("(A.b = 2) and (A.b = B.c)")
        w = Filter(f, preds)
        print w
        db = Database()
        opt = Optimizer(db)

        print "Test 1 join plan"
        print opt(w)

        '''
        Below is what your code should output:

	Test 1 join plan
		Test 1 join plan
WHERE((A.b = 2.0) and (A.b = B.c))
  THETAJOIN(ON A.b = B.c)
    Scan(data AS A)
    Scan(data AS B)
.WHERE((A.a = 2.0) and (A.b = B.c) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d))
  FROM()
    Scan(data AS A)
    Scan(data AS B)
    Scan(data2 AS C)
    Scan(data AS D)
    Scan(data2 AS E)
    Scan(data AS F)
    Scan(data2 AS G)
        '''
        
    def test_selfjoin(self):
    #test that self joins work better than exhaustive best plan (w.r.t computation time)  

        from db import Database

        f = From([
        Scan("data", "A"),
        Scan("data", "B"),
        Scan("data", "C"),
        Scan("data", "D"),
        Scan("data", "E"),
        Scan("data", "F"),
        Scan("data", "G")
        ])
  
        preds = cond_to_func("(A.a = 2) and (A.b = B.f) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d)")
        w = Filter(f, preds)
        print w
        db = Database()
        opt = Optimizer(db)
        print "Test 2 join plan"
        print opt(w)


        '''
        Below is what your code should output:

Test 2 join plan
tested C True 646.666666667 1.0
tested D True 646.666666667 1.0
tested E True 646.666666667 1.0
tested F True 646.666666667 1.0
tested G True 646.666666667 1.0
tested C True 5159.48717949 1.0
tested D True 5159.48717949 1.0
tested E True 5159.48717949 1.0
tested F F.c = G.d 5159.48717949 1.0
tested C True 95415.8974359 1.0
tested D True 95415.8974359 1.0
tested E E.b = F.c 91313.3333333 0.5
tested C True 993877.435897 1.0
tested D D.a = E.b 928236.410256 0.2
tested C True 4538492.82051 1.0
WHERE((A.a = 2.0) and (A.b = B.f) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d))
  THETAJOIN(ON True)
    Scan(data AS C)
    THETAJOIN(ON D.a = E.b)
      Scan(data AS D)
      THETAJOIN(ON E.b = F.c)
        Scan(data AS E)
        THETAJOIN(ON F.c = G.d)
          Scan(data AS F)
          THETAJOIN(ON True)
            Scan(data AS G)
            THETAJOIN(ON A.b = B.f)
              Scan(data AS A)
              Scan(data AS B)
 
        '''
    def test_multijoin(self):
    #test that multi joins work better than exhaustive best plan (w.r.t computation time)  
    
        from db import Database

        f = From([
        Scan("data", "A"),
        Scan("data", "B"),
        Scan("data2", "C"),
        Scan("data", "D"),
        Scan("data2", "E"),
        Scan("data", "F"),
        Scan("data2", "G")
        ])
  
        preds = cond_to_func("(A.a = 2) and (A.b = B.c) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d)")
        w = Filter(f, preds)
        print w
        db = Database()
        opt = Optimizer(db)
        print "Test 3 join plan"
        print opt(w)

'''
Below is what your code should print:

Test 3 join plan
tested A True 862.0 1.0
tested B True 862.0 1.0
tested C True 862.0 1.0
tested F E.b = F.c 842.0 0.5
tested G True 862.0 1.0
tested A True 5242.0 1.0
tested B True 5242.0 1.0
tested C True 5242.0 1.0
tested G F.c = G.d 5242.0 1.0
tested A True 93242.0 1.0
tested B True 93242.0 1.0
tested C True 93242.0 1.0
tested A True 1853242.0 1.0
tested B True 1853242.0 1.0
tested A A.b = B.c 35453242.0 0.5
WHERE((A.a = 2.0) and (A.b = B.c) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d))
  THETAJOIN(ON A.b = B.c)
    Scan(data AS A)
    THETAJOIN(ON True)
      Scan(data AS B)
      THETAJOIN(ON True)
        Scan(data2 AS C)
        THETAJOIN(ON F.c = G.d)
          Scan(data2 AS G)
          THETAJOIN(ON E.b = F.c)
            Scan(data AS F)
            THETAJOIN(ON D.a = E.b)
              Scan(data AS D)
              Scan(data2 AS E)
.WHERE((A.a = 2.0) and (A.b = B.f) and (D.a = E.b) and (E.b = F.c) and (F.c = G.d))
  FROM()
    Scan(data AS A)
    Scan(data AS B)
    Scan(data AS C)
    Scan(data AS D)
    Scan(data AS E)
    Scan(data AS F)
    Scan(data AS G)
'''

if __name__ == '__main__':
  unittest.main()

