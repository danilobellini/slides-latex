SELECT 'Hello World' AS msg;  -- ";" é necessário no shell


-- DuckDB detecta (e converte) os tipos em muitos casos
VALUES (1, '2', 0, 1/4, true), (5, 'test', .25, 0.78, NULL);

-- Podemos converter tipos e aninhar queries/subqueries
SELECT x, y, y - x AS z FROM (
  SELECT
    col0::INT64 AS x,
    col1::INT64 AS y,  -- Trailing comma, é permitido!
  FROM (VALUES (1, 5), (3, 17), (4, 33), (7, 257))
);

-- Colunas podem ser do tipo lista, mas podemos "desaninhar"
SELECT range(15);
SELECT unnest(range(15)) AS idx;  -- Lista -> linhas
SELECT unnest([  -- List comprehension!
  format('{:2d} ** 2 -> {:03d}', x, x * x) FOR x IN range(15)
]) AS values;


-- Criando a partir de dados constantes
CREATE TABLE ir AS SELECT  -- Imposto de Renda CDB (e outros)
  col0 AS aliquota,
  col1 AS ate_dias_div_10,
FROM (VALUES (.225, 18), (.2, 36), (.175, 72), (.15, NULL));

-- Statements para "sondar" o que houve na criação
SHOW DATABASES;  -- Um único "catalog": a memória (memory)
SHOW TABLES;  -- Apenas a tabela que acaba de ser criada
FROM ir;  -- O "SELECT *" é implícito

-- Eis uma VIEW (aspas duplas em nomes de coluna c/ espaço)
CREATE OR REPLACE VIEW tabela_ir_completa AS SELECT
  format('{:.1f}%', aliquota * 100) AS "Alíquota CDB",
  ifnull(  -- Ou coalesce
    first(ate_dias_div_10) OVER (  -- Agregação por janela
      ORDER BY ate_dias_div_10
      ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
    ) * 10 + 1,
    0  -- Chamada de função não pode ter trailing comma
  ) || ' dias' AS "A partir de",  -- || concatena strings
  ifnull(ate_dias_div_10 * 10 || ' dias', 'Inf') AS "Até",
FROM ir;

-- Tabelas e views podem ser exportadas para CSV ou Parquet
FROM tabela_ir_completa;
COPY tabela_ir_completa TO 'tabela_ir_completa.csv';
FROM 'tabela_ir_completa.csv';  -- Lendo direto do CSV!
