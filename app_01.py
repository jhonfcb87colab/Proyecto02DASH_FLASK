import os
import random
from flask import Flask, render_template, jsonify

# 1. Fuerza a Flask a encontrar la carpeta 'templates' sin importar dónde ejecutes el comando
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

# 2. Endpoint de la API que envía los datos al Dashboard
@app.route("/api/data")
def get_dashboard_data():
    return jsonify({
        "kpis": {
            "total_ventas": 128450,
            "transacciones": 1420,
            "ticket_promedio": 90.45,
            "satisfaccion": "94.8%"
        },
        "ventas_mensuales": {
            "labels": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
            "data": [12000, 19000, 15000, 22000, 28000, 24000, 31000]
        },
        "ventas_categoria": {
            "labels": ["Electrónica", "Ropa", "Hogar", "Juguetes", "Libros"],
            "data": [40, 25, 15, 12, 8]
        },
        "top_productos": [
            {"id": "PROD-01", "nombre": "Laptop Pro 15", "ventas": 340, "total": "$408,000"},
            {"id": "PROD-02", "nombre": "Smartphone X", "ventas": 510, "total": "$357,000"},
            {"id": "PROD-03", "nombre": "Audífonos Bluetooth", "ventas": 890, "total": "$89,000"},
            {"id": "PROD-04", "nombre": "Silla Ergonómica", "ventas": 120, "total": "$36,000"},
        ]
    })

# 3. Ruta principal que renderiza el HTML
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)