# MongApp com Docker

![Pytohn + MongoDB](https://i.ytimg.com/vi/qd1Ihy_djDc/maxresdefault.jpg)

Esta aplicação é somente um exemplo de API Flask com persistência de dados no MongoDB.
Ela usa os métodos GET e POST para interagir com o banco de dados, Foi criada somente para a resolução de um desafio em uma startup.


Payload para cadastro:

{

"nome": "Andre",

"sobrenome": "Ferreira",

"email": "faker email",

"password": "faker password",

"defaultLanguage": "faker defaultLanguage",

"dataNascimento": "faker nascimento",

"endereco": "faker endereco",

"areasInteresse": "faker areasInteresse",

"escola": "faker escola",

"statusEscola": "faker statusEscola"

}


## Preparando seu ambiente

para executar esta aplicação locamente execute os seguintes passos:

Clone este repositório

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências necessárias.

Efetue o deploy da imagem usando o Dockerfile.
```bash
 docker build -t mongapp .
```
Execute um contêiner de Mongodb.

```bash
docker pull mongo
docker run -dti --name mongodb --hostname mongodb -p 27017:27017 mongo
```
Instale o mongo client em sua maquina e crie uma database com a seguinte collection.
```bash
mongo mongodb://localhost
use appdata
db.createCollection("usuarios")
CTRL + D
```

Agora efetue o deploy do container da aplicação fazendo um link com o container do mongo criado anteriormente.
```bash
docker run -dti --name mongapp --hostname mongapp --link mongodb:mongodb mongapp
docker ps
```

## Usando a API
Em um terminal ou usando o [Postman](https://www.getpostman.com/downloads/) execute um GET na URL http://localhost/api/users/lista para listar os usuários presentes no banco de dados.
```bash
curl http:/localhost/api/users/lista
```
Para cadastrar um usuário devemos efetuar um post passando as informações em formato [JSON](https://www.json.org/).
```bash
curl --header "Content-Type: application/json" --request POST --data '{"nome": "faker name", "sobrenome": "faker lastName", "email": "faker email", "password": "faker password", "defaultLanguage": "fakerdefaultLanguage", "dataNascimento": "faker nascimento", "endereco": "faker endereco", "areasInteresse": "faker areasInteresse", "escola": "faker escola", "statusEscola": "faker statusEscola"}' http:/localhost/api/users/cadastra
```
