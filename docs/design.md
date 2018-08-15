# System Design

This document describes the design of the DataBass query engine.  You will find the bulk of the code under [src/engine/](../src/engine/).

#### Background

Database is a reasonably featured, but simple, in-memory database engine that can parse SQL queries, translate them into a query plan, perform simple optimizations such as join ordering, and run the query using either a push or pull-based execution model.  

The purpose is to provide an overview of how parts of an analytical database work together and introduce database concepts within the context of an end-to-end engine.  To do so, the engine does not support many things, such as transactions, recovery, memory-management, correct null value support, etc.

The engine is composed of the modules defined in Python files in the [src/engine/](../src/engine) folder:

* [db.py](../src/engine/db.py): this module manages the tables in the database.  It also keeps statistics about the tables that the optimizer can later use.
* [interpretor.py](../src/engine/interpretor.py): this module implements two types of execution methods.  The pull-based iterator method as described in class, and a push-based method that we briefly mentioned in class.  The assignments will focus on the pull-based iterator, however the push-based method is there for you to see how it could work.
* [ops.py](../src/engine/ops.py): this module implements the SQL operators and expression operators.  You will primarily edit this file to implement functionality.  Most of the code for the pull-based execution method is implemented as `__iter__` methods of the SQL operators defined in this file.
* [optimizer.py](../src/engine/optimizer.py): this module takes a query plan as input, and rewrites it to perform optimizations.  Your join order optimization assignment will primarily be implemented here.
* [parse_expr.py](../src/engine/parse_expr.py): this module is a simple parsing examples that only parses expressions and not queries.  You can play with it to get acquainted with how parsing works.
* [parse_sql.py](../src/engine/parse_sql.py): this module implements the subset of the SQL language that DataBass supports.  The parsing grammar rules also include those in `parse_expr`.
* [prompt.py](../src/engine/prompt.py): this is the DataBass client that you can use to write and execute SQL queries in the command line.


