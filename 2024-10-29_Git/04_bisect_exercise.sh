git clone https://github.com/sympy/sympy
cd sympy

# Inicia a busca por um commit
git bisect start  # Inicia a busca
git bisect new    # O commit atual é novo (posterior)
git checkout REF  # Alguma ref que seja antiga (qual?)
git bisect old    # Marca o commit como anterior
# ... em cada novo commit, é preciso verificar manualmente
# se ele é posterior ou anterior ao que se busca,
# e então chamar o git bisect new ou old para achar
# o próximo commit
git bisect reset  # Finaliza a busca
