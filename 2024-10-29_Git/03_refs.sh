cria_commit_um_arquivo() {
  echo "# Arquivo vazio $1" > $1
  git add $1
  git commit -m "Insere $1"
}

mkdir segundo_repositorio && cd segundo_repositorio
git init

# Commit inicial na branch principal (master ou main)
cria_commit_um_arquivo raiz.py
git branch  # Permite ver a branch atual

# Nova branch "be-um" terá um commit acima de main
git checkout -b be-um  # "-b" cria uma nova branch, similar a
                       # git branch b1 && git checkout b1
cria_commit_um_arquivo b1.py

# Nova branch "be-dois" terá 2 commits acima de main
git checkout HEAD^  # O "^" representa "parent"
cria_commit_um_arquivo b2.py  # Ainda detached!
git tag estava-detached  # Cria uma tag (outra ref)
git checkout -b be-dois
cria_commit_um_arquivo b2_child.py

# Visualização
git log --oneline --all --graph
