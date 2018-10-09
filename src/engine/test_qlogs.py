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

  def test_parse_sdss_queries(self):
    querytext = """SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
SELECT count(g.objID) FROM Galaxy as g, dbo.fGetNearbyObjEq( 115.866 , 40.5354 , 1.6894005 ) as d WHERE d.objID = g.objID
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469062987925
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004167733433
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004168192115
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004168192128
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063053507
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004168126653
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469600383058
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063446719
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063184604
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063381160
SELECT count(g.objID) FROM Galaxy as g, dbo.fGetNearbyObjEq( 115.866 , 40.5354 , 1.1262669 ) as d WHERE d.objID = g.objID
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004168061134
SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
SELECT  top 1   p.objID, p.run, p.rerun, p.camcol, p.field, p.obj,     p.type, p.ra, p.dec, p.u,p.g,p.r,p.i,p.z,    p.Err_u, p.Err_g, p.Err_r,p.Err_i,p.Err_z    FROM fGetNearbyObjEq(195,2.5,0.5) n, PhotoPrimary p    WHERE n.objID=p.objID
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063249986
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725468526248106
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063184602
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003630796894
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725468526248085
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725468526182582
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003630862447
SELECT count(g.objID) FROM Galaxy as g, dbo.fGetNearbyObjEq( 115.866 , 40.5354 , 0.84470023 ) as d WHERE d.objID = g.objID
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003630862456
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725468526248118
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003631452342
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063774212
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063184628
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007004168192131
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063643301
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 587725469063643260
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003631321239
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003631386743
SELECT count(g.objID) FROM Galaxy as g, dbo.fGetNearbyObjEq( 115.866 , 40.5354 , 0.56313347 ) as d WHERE d.objID = g.objID
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003631321255
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003631059105
select rowc_g,colc_g from BESTDR3..PhotoPrimary where objID = 588007003630993526"""

    for q in querytext.split("\n"):
      try:
        plan = parse(q)
      except Exception as e:
        print q
        print
        raise e



  def test_parse_evan_queries_easy(self):
    querytext = """
SELECT DISTINCT(httpRequest.status)
FROM `bluecore-qa.app_engine_logs.appengine_googleapis_com_request_log_20170915`
LIMIT 1000

SELECT protoPayload.startTime, protoPayload.method, protoPayload.resource, protoPayload.nickname
FROM [triggeredmail:app_engine_logs.appengine_googleapis_com_request_log_20170912]
WHERE protoPayload.nickname == 'evan.jones'
ORDER BY protoPayload.startTime
LIMIT 1000


SELECT protoPayload.startTime, protoPayload.method, protoPayload.resource, protoPayload.nickname
FROM [triggeredmail:app_engine_logs.appengine_googleapis_com_request_log_20170912]
WHERE protoPayload.resource LIKE '/api/rest/%/tjmaxx%' AND protoPayload.method != 'GET'
ORDER BY protoPayload.startTime
LIMIT 1000


SELECT protoPayload.startTime, lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_2017082*`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_2017082*`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170828`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170809`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170829`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170829`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%HTTPException%'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170829`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%HTTPException%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170829`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%HTTPException: Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170830`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%HTTPException: Deadline exceeded%' AND protoPayload.moduleId = 'chrono-gae'
LIMIT 1000

SELECT lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170830`, UNNEST(protoPayload.line) AS lines
WHERE lines.logMessage LIKE '%{"table_id":%'

SELECT
  requestId,
  UNIX_MICROS(timestamp) AS timestamp,
  timestamp AS timeHuman,
  message
FROM (
  SELECT
    protoPayload.requestId AS requestId,
    lines.time AS timestamp,
    lines.logMessage AS message
  FROM
    `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170830` AS t,
    UNNEST(t.protoPayload.line) AS lines
  WHERE
    protoPayload.moduleId LIKE '%bigquery%')
WHERE
  message LIKE 'Ran out of tries%'
  OR message LIKE '====%'
  OR message LIKE '{"table_id"%'
ORDER BY
  requestId

SELECT protoPayload.startTime, protoPayload.latency, protoPayload.resource, protoPayload.moduleId, protoPayload.instanceId
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170822`
WHERE protoPayload.latency>500 AND protoPayload.resource!="/_ah/background"
ORDER BY protoPayload.latency DESC
LIMIT 1000



SELECT protoPayload.startTime, protoPayload.latency, protoPayload.resource, protoPayload.moduleId
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170822`
WHERE protoPayload.latency>500 AND protoPayload.resource!="/_ah/background"
ORDER BY protoPayload.latency DESC
LIMIT 1000



SELECT protoPayload.startTime, protoPayload.latency, protoPayload.resource
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170822`
WHERE protoPayload.latency>500 AND protoPayload.resource!="/_ah/background"
LIMIT 1000


SELECT protoPayload.startTime, protoPayload.latency, protoPayload.resource
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170822`
WHERE protoPayload.latency>500 AND protoPayload.resource!="/background"
LIMIT 1000


SELECT lines.time, lines.logMessage
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_2017081*`, UNNEST(protoPayload.line) as lines
WHERE protoPayload.moduleId = 'integration-track' AND lower(lines.logMessage) LIKE '%overall deadline%'
LIMIT 1000


SELECT protoPayload.resource
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170824`
WHERE protoPayload.resource LIKE '/display_impression/%'
LIMIT 1000


SELECT httpRequest.requestUrl
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170824`
LIMIT 1000


SELECT httpRequest.requestUrl
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170824`
WHERE httpRequest.requestUrl LIKE '/display_impression/%'
LIMIT 1000


SELECT httpRequest.requestUrl
FROM `triggeredmail.app_engine_logs.appengine_googleapis_com_request_log_20170825`
WHERE httpRequest.requestUrl LIKE '/display_impression/%'
LIMIT 1000


SELECT httpRequest.requestUrl
FROM `bluecore-qa.app_engine_logs.appengine_googleapis_com_request_log_20170825`
WHERE httpRequest.requestUrl LIKE '/display_impression/%'
LIMIT 1000


SELECT protoPayload.line.time, LENGTH(protoPayload.line.logMessage)
FROM [bluecore-qa:app_engine_logs.appengine_googleapis_com_request_log_20170823]
WHERE protoPayload.resource='/wtf'
ORDER BY protoPayload.line.time DESC
LIMIT 1000


SELECT protoPayload.line.time, LENGTH(protoPayload.line.logMessage)
FROM [bluecore-qa:app_engine_logs.appengine_googleapis_com_request_log_20170823]
WHERE protoPayload.resource='/wtf'
ORDER BY protoPayload.line.time DESC
LIMIT 1000


SELECT protoPayload.line.time, LENGTH(protoPayload.line.logMessage)
FROM [bluecore-qa:app_engine_logs.appengine_googleapis_com_request_log_20170823]
WHERE protoPayload.resource='/wtf'
ORDER BY protoPayload.line.time
LIMIT 1000


SELECT protoPayload.line.time, LENGTH(protoPayload.line.logMessage)
FROM [bluecore-qa:app_engine_logs.appengine_googleapis_com_request_log_20170823]
WHERE protoPayload.resource='/wtf'
LIMIT 1000



SELECT COUNT(*) FROM `triggeredmail.coach.aggregate_purchase_201708`
WHERE order_id IS NULL OR order_id = '' 


SELECT identified.count / aggregate.count AS ratio FROM (
    SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
    SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT COUNT(*) FROM `triggeredmail.coach.aggregate_purchase_201708`
WHERE order_id IS NULL OR order_id = '' 


SELECT identified.count / aggregate.count AS ratio FROM (
    SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
    SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT COUNT(*) FROM `triggeredmail.coach.aggregate_purchase_201708`
WHERE order_id IS NULL OR order_id = '' 


SELECT identified.count / aggregate.count AS ratio FROM (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT COUNT(*) FROM `triggeredmail.coach.aggregate_purchase_201708`
WHERE order_id IS NULL OR order_id = '' 


SELECT identified.count / aggregate.count AS ratio FROM (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT identified.count / aggregate.count AS ratio FROM (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT identified.count / aggregate.count AS ratio FROM (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified


SELECT COUNT(*) FROM `triggeredmail.coach.aggregate_purchase_201708`
WHERE order_id IS NULL OR order_id = '' 


SELECT identified.count / aggregate.count AS ratio FROM (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.aggregate_viewed_product_201708`
) AS aggregate, (
  SELECT COUNT(*) AS count FROM `triggeredmail.coach.identified_viewed_product_201708`
) AS identified
    """
    queries = [""]
    for l in querytext.split("\n"):
      if l.strip() == "":
        queries.append("")
        continue
      queries[-1] += " " + l.strip()
    queries = filter(bool, queries)
    outputs = []

    for q in queries:
      try:
        plan = parse(q)
      except Exception as e:
        print q
        print
        raise e



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
