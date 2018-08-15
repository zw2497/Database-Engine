import traceback
import readline
import click

WELCOMETEXT = """Welcome to DeepBass.  
Type "help" for help, and "q" to exit"""


HELPTEXT = """
List of commands

[query]                           runs query string
PARSE EXPR [expression string]    parse and print AST for expression
PARSE Q [query string]            parse and print AST for query 
TRACE                             print stack trace of last error
SHOW TABLES                       print list of database tables
SHOW <tablename>                  print schema for <tablename>
"""



if __name__ == "__main__":

  @click.command()
  def main():
    print(WELCOMETEXT)
    service_inputs()

  def service_inputs():
    cmd = raw_input("> ").strip()

    import interpretor
    import optimizer
    import ops
    import db
    import parse_expr
    import parse_sql
    reload(interpretor)
    reload(optimizer)
    reload(ops)
    reload(db)
    reload(parse_expr)
    reload(parse_sql)
    from interpretor import PullBasedInterpretor, PushBasedInterpretor
    from optimizer import Optimizer
    from ops import Print, Project, Scan
    from db import Database
    from parse_expr import parse as _parse_expr
    from parse_sql import parse as _parse_sql

    db = Database()

    if cmd == "q":
      return

    elif cmd.startswith("help"):
      print(HELPTEXT)

    elif cmd.upper().startswith("TRACE"):
      traceback.print_exc()

    elif cmd.upper().startswith("PARSE EXPR"):
      e = cmd[len("PARSE EXPR"):]
      try:
        ast = _parse_expr(e)
        print(ast)
      except Exception as err:
        print("ERROR:", err)

    elif cmd.upper().startswith("PARSE Q"):
      q = cmd[len("PARSE Q"):]
      try:
        ast = _parse_sql(q)
        print(ast)
      except Exception as err:
        print("ERROR:", err)

    elif cmd.upper().startswith("SHOW TABLES"):
      for tablename in db.tablenames:
        print tablename
      
    elif cmd.upper().startswith("SHOW "):
      tname = cmd[len("SHOW "):].strip()
      if tname in db:
        print "Schema for %s" % tname
        t = db[tname]
        for field in t.fields:
          if t.rows:
            typ = type(t.rows[0][field])
          else:
            typ = "?"
          print field, "\t", typ
      else:
          print "%s not in database" % tname

    else:
      try:
        plan = _parse_sql(cmd)
        optimizer = Optimizer(db)
        interpretor = PullBasedInterpretor(db)
        #interpretor = PushBasedInterpretor(db)

        plan = optimizer(plan)
        print(plan)
        plan = Print(plan)
        interpretor(plan)
      except Exception as err:
        print("ERROR:", err)

    del db
    service_inputs()


  main()
