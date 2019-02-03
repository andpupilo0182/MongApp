from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'appdata'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/appdata'
mongo = PyMongo(app)

#lista todos os usuarios do mongodb
@app.route('/api/users/lista', methods=['GET'])
def get_all_users():
  user = mongo.db.usuarios
  output = []
  for s in user.find():
    output.append({'nome' : s['nome'], 'sobrenome' : s['sobrenome'], 'email' : s['email'], 'password' : s['password'], 'defaultLanguage' : s['defaultLanguage'], 'dataNascimento' : s['dataNascimento'], 'endereco' : s['endereco'], 'areasInteresse' : s['areasInteresse'], 'escola' : s['escola'], 'statusEscola' : s['statusEscola']})
  return jsonify({'resultado' : output})

#cadastra o usuario no mongodb
@app.route('/api/users/cadastra', methods=['POST'])
def add_user():
  user = mongo.db.usuarios
  nome = request.json['nome']
  sobrenome = request.json['sobrenome']
  email = request.json['email']
  password = request.json['password']
  defaultLanguage = request.json['defaultLanguage']
  dataNascimento = request.json['dataNascimento']
  endereco = request.json['endereco']
  areasInteresse = request.json['areasInteresse']
  escola = request.json['escola']
  statusEscola = request.json['statusEscola']
  user_id = user.insert({'nome': nome, 'sobrenome': sobrenome, 'email': email, 'password': password, 'defaultLanguage': defaultLanguage, 'dataNascimento': dataNascimento, 'endereco': endereco, 'areasInteresse': areasInteresse, 'escola': escola, 'statusEscola': statusEscola})
  new_user = user.find_one({'_id': user_id })
  output = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'password': password, 'defaultLanguage': defaultLanguage, 'dataNascimento': dataNascimento, 'endereco': endereco, 'areasInteresse': areasInteresse, 'escola': escola, 'statusEscola': statusEscola}
  return jsonify({'Usuario cadastrado' : output})

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
