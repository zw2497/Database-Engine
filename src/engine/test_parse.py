import unittest
#import StringIO
#import pandas
import tempfile
import os.path

import interpretor
import optimizer
import ops
import db
from interpretor import PullBasedInterpretor
from optimizer import Optimizer
from ops import Limit
from db import Database
from parse_sql import parse 



import pandas.util.testing as pdt

db = Database()
opt = Optimizer(db)
interp = PullBasedInterpretor(db)

class TestUnits(unittest.TestCase):
  """Basic unit testing"""

  def queries_not_equal(self, q1, q2):
    ast1 = parse(q1)
    ast2 = parse(q2)
    self.assertNotEqual(str(ast1), str(ast2))

  def run_query(self, q):
    ast = parse(q)
    plan = opt(ast)
    return [row for row in interp(plan)]

  def test_parse_offset(self):
    """""" 
    parse("SELECT 1 FROM data LIMIT 1")
    parse("SELECT 1 FROM data LIMIT 1 OFFSET 1")
    parse("SELECT 1 FROM data LIMIT 1 OFFSET 1+1")
    parse("SELECT 1 FROM data LIMIT 1 OFFSET 1*1/2")

    #various syntactical errors
    with self.assertRaises(Exception):
      parse("SELECT 1 FROM data LIMIT 1 OFFSET")

    with self.assertRaises(Exception):
      parse("SELECT 1 FROM data OFFSET 1 LIMIT 1")

    with self.assertRaises(Exception):
      parse("SELECT 1 FROM data OFFSET 1 LIMIT 1+")

    with self.assertRaises(Exception):
      parse("SELECT 1 FROM data LIMIT 1 OFFSET 1?")

    with self.assertRaises(Exception):
      parse("SELECT 1 FROM data OFFSET 1")

    with self.assertRaises(Exception):
      parse("SELECT a FROM data LIMIT 1 OFFSET -1")

    #test expressions in offset
    with self.assertRaises(Exception):
      parse("SELECT a FROM data LIMIT 1 OFFSET 1-10")

    with self.assertRaises(Exception):
      parse("SELECT a FROM data LIMIT 1 OFFSET 10-12")

  def test_parse_table_operators(self):
    with self.assertRaises(Exception):
      parse("SELECT 1 UNION SELECT 2")
    with self.assertRaises(Exception):
      parse("SELECT 1 UNION (select 2)")

  def test_parse_where_expr(self):
    parse("SELECT 1 WHERE 1")
    parse("SELECT 1 WHERE a+b")
    parse("SELECT 1 WHERE a+b and a+b")
    parse("SELECT 1 WHERE a+b AND a+b")
    parse("SELECT 1 WHERE a+b and a+b and a+b")
    parse("SELECT 1 WHERE a+b and a+b AND a+b")
    parse("SELECT 1 WHERE a+b or a+b and a+b")
    parse("SELECT 1 WHERE a+b or a+b or a+b")
    parse("SELECT 1 WHERE a+b or a+b OR a+b")
    parse("SELECT 1 WHERE a+b or (a+b or a+b)")
    parse("SELECT 1 WHERE (a+b or a+b) or a+b")
    parse("SELECT 1 WHERE a like b")
    parse("SELECT 1 WHERE a like +b")
    parse("SELECT 1 WHERE a like +b and a like b")
    parse("SELECT 1 WHERE a like +b and a like +b")
    parse("SELECT 1 WHERE a between a and b")
    parse("SELECT 1 WHERE a between a and b and x=y")
    parse("SELECT 1 WHERE a between a and b and c and d")

  def test_parse_null_expr(self):
    parse("SELECT 1 is null")
    parse("SELECT 1 is not null")
    parse("SELECT 1 IS null")
    parse("SELECT null IS null")
    parse("SELECT null IS not null")
    parse("SELECT (1 + 2) is null")
    parse("SELECT (1 + 2) is not null")

  def test_parse_join_weird_tablenames(self):
    parse("SELECT 1 FROM `a`")
    parse("SELECT 1 FROM `a.b`")
    parse("SELECT 1 FROM `a.b.c`")
    parse("SELECT 1 FROM [a]")
    parse("SELECT 1 FROM [a.b]")
    parse("SELECT 1 FROM [a.b.c]")

  def test_parse_join_subquery(self):
    parse("SELECT 1 FROM (select 1)")
    parse("SELECT 1 FROM (select 1 from data)")
    parse("SELECT 1 FROM (select a,b from data)")
    parse("SELECT 1 FROM (select a,b from data) as d")
    parse("SELECT 1 FROM (select a,b from (select a, b from data)) as d")
    parse("SELECT 1 FROM function() as d")
    parse("SELECT 1 FROM function(1,2) as d")
    parse("SELECT 1 FROM function(data.*) as d")



if __name__ == '__main__':
  unittest.main()



"""
import click
from parse_expr import parse as parse_expr
from parse_sql import parse as parse_sql

if __name__ == "__main__":
  import click

  @click.command()
  @click.option("-e", type=str)
  @click.option("-q", type=str)
  def run(e=None, q=None):
    if e:
      print(e)
      ast = parse_expr(e)
      print(ast)
    if q:
      print(q)
      ast = parse_sql(q)
      print(ast)

  run()

"""
