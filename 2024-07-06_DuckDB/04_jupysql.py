# Usar o JupySQL p/ salvar um CSV com as médias de todos os
# campos, separadas por tipo de iris (https://t.ly/gdUfb).

# Cria a conexão, como no slide anterior
import duckdb; conn = duckdb.connect(":memory:")

# "Mágicas" do JupySQL (apenas para notebook)
%load_ext sql
%sql conn --alias duckdb  # Ou o apelido que você quiser
%sql SELECT 2 ** 5  -- Exemplo (%%sql para bloco)
