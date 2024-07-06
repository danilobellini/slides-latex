  python -m venv venv  # Criação de um ambiente virtual
  . venv/bin/activate  # Ou venv\Scripts\Activate.ps1 no Windows

  pip install duckdb                 # Não possui dependências!
  pip install fsspec                 # Acesso a arquivos em ZIP
  pip install pandas polars pyarrow  # Integrações (dados)
  pip install notebook jupysql       # Jupyter + plugin
  pip install duckdb-engine          # Integração com SQLAlchemy

  jupyter notebook  # Iniciar o servidor local p/ criar notebook
