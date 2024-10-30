git config --global user.name 'Fulano de Tal'
git config --global user.email 'fulano@exemplo.com.br'
git config --global core.editor vim  # Opcional

# --global é a configuração do usuário (~/.gitconfig)
# --local  é a configuração do repositório (.git/config)

git config -l --show-scope # Mostra a configuração
man git config  # A seção "Variables" pode ser útil
