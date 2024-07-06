import duckdb

# Rodando um SQL sem parâmetros em duckdb.default_connection
duckdb.sql("SELECT 'Outro ' || 'hello world' AS msg")

# O ideal é criar uma conexão para isolar e facilitar testes
# (Use conn.sql(...).show() caso queira exibir em um script)
conn = duckdb.connect(":memory:")  # Podia ser um "arquivo.db"
conn.sql("SELECT {'mais': 1, 'hello': 'world'} AS struct_msg")

# Algo similar, mas com parâmetros, devolvendo uma tupla
conn.execute("SELECT $primeiro + $segundo", {
    "primeiro": 2,
    "segundo": 1.2,
}).fetchone()  # .fetchall() devolveria lista de tuplas

# Os tipos devolvidos são diferentes dependendo do método
#   .execute -> DuckDBPyConnection (conexão e cursor)
#   .sql -> DuckDBPyRelation (resultado de uma query)
# Mas ambos possuem fetchone/fetchall e outros que veremos

# O arquivo CSV não precisa estar na sua máquina!
conn.sql("FROM read_csv('https://t.ly/gdUfb')")
# Funciona com a URL resolvida do shortener? Sem o read_csv?

conn.sql("""-- Ao invés de fazer um download a cada query...
CREATE TABLE iris AS FROM read_csv('https://t.ly/gdUfb')
""")
