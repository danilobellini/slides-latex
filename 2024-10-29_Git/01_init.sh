mkdir primeiro_repositorio
cd primeiro_repositorio
git init  # Cria o diretório .git/ sem nenhum commit

echo Hello World > hello_world.txt
git add hello_world.txt  # Coloca a alteração em "staging"
                         # (marcado para entrar no commit)

git commit  # Chama o editor para uma mensagem

git log  # Mostra a história de commits
git show  # Mostra o commit HEAD (referência padrão)
gitk  # Visualização em GUI (opcional, requer Tcl/Tk)
