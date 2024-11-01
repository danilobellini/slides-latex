# Danilo J. S. Bellini LaTeX Slides

Esses são slides de palestras que apresentei em algum
evento de comunidade.

Esta coletânea não é completa,
ela inclui apenas o que foi feito utilizando o LaTeX.
Entre outros materiais disponíveis,
há ainda as palestras cujo material foi feito
com base no Jupyter Notebook (disponíveis no
  [repositório notebooks](https://github.com/danilobellini/notebooks))
ou no LibreOffice Impress (disponíveis no
  [SlideShare](https://www.slideshare.net/djsbellini)).

<table>
  <thead>
    <th>Data</th>
    <th>Evento</th>
    <th>Título</th>
  </thead>
  <tbody>
    <tr>
      <td>2018-07-14</td>
      <td><a href="https://www.meetup.com/pt-BR/Grupy-SP/events/252450253/">Just Python</a></td>
      <td><a href="2018-07-14_Just_Python_Numbers/slides.pdf">
        Números no Python!
      </a></td>
    </tr>
    <tr>
      <td>2018-08-25</td>
      <td><a href="https://2018.flask.python.org.br">Flask Conf</a></td>
      <td><a href="2018-08-25_Sanic/slides.pdf">
        Introdução ao Sanic - O Flask Assíncrono
      </a></td>
    </tr>
    <tr>
      <td>2018-10-18</td>
      <td>Semana da informática na ETEC Uirapuru</td>
      <td><a href="2018-10-18_Security/slides.pdf">
        Segurança da Informação -
        Um apanhado geral sobre criptografia,
        acesso e vulnerabilidades,
        incluindo exemplos práticos em Python e Shell
      </a></td>
    </tr>
    <tr>
      <td>2019-03-09</td>
      <td><a href="http://grupyabc.org/grupy-abc/meetups/2019/03/09/grupy-abc-primeiro-encontro-do-ano.html">Encontro do GruPy-ABC na FATEC de Mauá</a></td>
      <td><a href="2019-03-09_Sanic/slides.pdf">
        Sanic 18.12 LTS - Novos recursos e websockets
      </a></td>
    </tr>
    <tr>
      <td>2019-05-04</td>
      <td><a href="https://cryptorave.org/">CryptoRave</a></td>
      <td><a href="2019-05-04_Tomb/slides.pdf">
        Tomb - Do GPG à esteganografia na prática
      </a></td>
    </tr>
    <tr>
      <td>2019-08-12</td>
      <td><a href="https://www.facebook.com/SSIUSP/">IX Semana de Sistemas de Informação @ EACH-USP</a></td>
      <td><a href="2019-08-12_Cryptography/slides.pdf">
        Introdução à Criptografia - Fundamentos e aplicação prática
      </a></td>
    </tr>
    <tr>
      <td>2019-11-09</td>
      <td><a href="https://www.meetup.com/pt-BR/Grupy-SP/events/265618918/">Just Python 3.0</a></td>
      <td><a href="2019-11-09_Walrus/slides.pdf">
        Assignment expressions do zero ao anti-herói:
        O novo "walrus" do Python 3.8 – PEP 572
      </a></td>
    </tr>
    <tr>
      <td>2024-07-06</td>
      <td><a href="https://sudeste.python.org.br/">Python Sudeste</a></td>
      <td><a href="2024-07-06_DuckDB/slides.pdf">
        DuckDB: Uma revolução pra quem trabalha com dados
      </a></td>
    </tr>
    <tr>
      <td>2024-07-07</td>
      <td><a href="https://sudeste.python.org.br/">Python Sudeste</a></td>
      <td><a href="2024-07-07_AST/slides.pdf">
        AST: O que é e como usar o módulo padrão?
      </a></td>
    </tr>
    <tr>
      <td>2024-10-29</td>
      <td><a href="https://www.secompufscar.com.br/">SECOMP UFSCar</a></td>
      <td><a href="2024-10-29_Git/slides.pdf">
        Controle de versão com git
      </a></td>
    </tr>
  </tbody>
</table>

Os diretórios de cada apresentação contém o código fonte em LaTeX.
Em geral, por renderizar as cores do código com o pacote `minted`
(que internamente usa o `pygments`),
é necessário usar `-shell-escape` para renderizar.
Resumidamente, o comando para gerar o PDF manualmente é:

```
pdflatex -shell-escape slides.tex && pdflatex -shell-escape slides.tex
```
