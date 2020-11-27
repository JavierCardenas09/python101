from flask import Flask, jsonify

#iniciar instancia de flask
app = Flask(__name__, static_url_path="")


@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido={"id":1, "nombre" :"Juan", "apellido":"algun apellido"}
    segundo={"id":2, "nombre" :"Javier", "apellido":"Cardenas"}
    lista = [contenido, segundo]
    return jsonify(lista)


@app.route('/', methods=['GET'])
def saludo():
    return 'hola mundo'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
