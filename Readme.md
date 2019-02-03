# MongApp

![Pytohn + MongoDB](https://i.ytimg.com/vi/qd1Ihy_djDc/maxresdefault.jpg)

Esta aplicação é somente um exemplo de API Flask com persistência de dados no MongoDB.
Ela usa os métodos GET e POST para interagir com o banco de dados.


## Preparando seu ambiente

para executar esta aplicação locamente execute os seguintes passos:

Clone este repositório

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências necessárias.

```bash
pip install -r requirements.txt
python app.py &
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

## Usando a API
Em um terminal ou usando o [Postman](https://www.getpostman.com/downloads/) execute um GET na URL http://localhost/api/users/lista para listar os usuários presentes no banco de dados.
```bash
curl http:/localhost/api/users/lista
```
Para cadastrar um usuário devemos efetuar um post passando as informações em formato [JSON](https://www.json.org/).
```bash
curl --header "Content-Type: application/json" --request POST --data '{"nome": "faker name", "sobrenome": "faker lastName", "email": "faker email", "password": "faker password", "defaultLanguage": "fakerdefaultLanguage", "dataNascimento": "faker nascimento", "endereco": "faker endereco", "areasInteresse": "faker areasInteresse", "escola": "faker escola", "statusEscola": "faker statusEscola"}' http:/localhost/api/users/cadastra
```
