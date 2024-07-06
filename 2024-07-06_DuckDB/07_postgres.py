conn.sql("""
ATTACH
'dbname=pyse user=ducky password=sanca host=127.0.0.1'
AS remotedb (TYPE POSTGRES)
""")
conn.sql("SHOW DATABASES")

conn.sql("CREATE TABLE remotedb.single (value JSON)")
conn.sql("""
INSERT INTO remotedb.single
SELECT DISTINCT {'type': name}::JSON
FROM memory.iris
""")

conn.sql("""  -- Leitura com o próprio PostgreSQL
FROM postgres_query('remotedb',
  'SELECT * FROM single'
)
""")
