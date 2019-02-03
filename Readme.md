MongAPP 

Esta aplicação é somente um exemplo de API Flask com persistencia de dados no MongoDB.
Ela usa os metodos GET e POST para interagir com o banco de dados.


Para executar a aplicação localmente baixe este rpositorio e execute python app.py&
Execute um container de Mongodb

docker pull mongo
docker run -dti --name mongodb --hostname mongodb -p 27017:27017 mongo

instale o mongo client em sua maquina e crie uma database com a seguinte collection
mongo mongodb://localhost
use appdata
db.createCollection("usuarios")
CTRL + D


Em um terminal ou usando o postman execute um GET na URL http://localhost/api/users/lista

Para listar no terminal execute o comando.
 curl http:/localhost/api/users/lista

Para cadastrar um usuario utilize o comando.
 curl --header "Content-Type: application/json" --request POST --data '{"nome": "faker name", "sobrenome": "faker lastName", "email": "faker email", "password": "faker password", "defaultLanguage": "fakerdefaultLanguage", "dataNascimento": "faker nascimento", "endereco": "faker endereco", "areasInteresse": "faker areasInteresse", "escola": "faker escola", "statusEscola": "faker statusEscola"}' http:/localhost/api/users/cadastra

Caso prefira voce pode utilizar o POstman.
https://www.getpostman.com/downloads/
