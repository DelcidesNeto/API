from flask import Flask, jsonify, redirect
app = Flask(__name__)
json = {'id': 0, 'mensagem': 'Aguardando Mensagem...'}
@app.route('/', methods=['GET'])
def home():
    return jsonify(json)
@app.route('/<int:id_msg>/<msg>', methods=['GET'])
def mudar_json(id_msg, msg='Aguardando mensagem'):
    json['id'] = id_msg
    json['mensagem'] = msg
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
