from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta principal (GET)
@app.route("/")
def home():
    return jsonify({
        "mensaje": "¡Servidor Flask funcionando con UV!",
        "estado": "exitoso"
    })

# Ruta con parámetros (POST)
@app.route("/saludo", methods=["POST"])
def saludo():
    data = request.get_json() or {}
    nombre = data.get("nombre", "Usuario")
    return jsonify({"respuesta": f"¡Hola, {nombre}!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)