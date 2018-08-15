from itertools import *
from collections import *
import timeit
from ops import *


def loopify(ast):
  """
  Assuming the AST is Project(Where(Join))
  Turn into nested for loop program
  """

  if not is_ast_valid(ast):
    raise Exception("AST did not conform to SELECT-PROJECT-JOIN pattern: %s" % ast)

  cond = ast.c.cond
  sources = ast.c.c.cs

  # setup sources as variables
  lines = []
  lines.append("# We assume that a database called 'db' has been defined ")
  #lines.append("from db import *\ndb = Database() ")

  fortemplate = """%sfor %s in db["%s"]:"""

  for idx, src in enumerate(sources):
    indent = " " * (idx * 2)
    code = fortemplate % (indent, src.alias, src.tablename)
    lines.append(code)
  indent += "  "
  lines.append("%sif (%s):" % (indent, cond.to_python()))
  lines.append("%s  %s" % (indent, project_to_code(ast, indent + "  ")))

  return "\n".join(lines)

  
def project_to_code(ast, indent=""):
  exprs, aliases = ast.exprs, ast.aliases
  todictline = lambda e, a: "%s  \"%s\": %s" % (indent, a, e.to_python()) 
  dictlines = [todictline(e, a) for e,a in zip(exprs, aliases)]

  return """print({\n%s\n%s})""" % (",\n".join(dictlines), indent)


def is_ast_valid(ast):
  if not isinstance(ast, Project):
    return False
  if not isinstance(ast.c, Filter):
    if isinstance(ast.c, From):
      ast.c = Filter(ast.c, "1")
    else:
      return False
  if not isinstance(ast.c.c, From):
    return False
  isscan = lambda op: isinstance(op, Scan)
  if not all(map(isscan, ast.c.c.cs)):
    return False
  return True

  
if __name__ == "__main__":
  from parse_sql import parse
  q = """SELECT t.a, r.b + r.b
         FROM data AS t, data AS r, data AS q, data AS p
         WHERE t.c = r.b AND p.a = q.a"""

  ast = parse(q)
  code = loopify(ast)

  print(code)
