from flask import Flask, jsonify, request
from Models import db, Estudiantes
from logging import exception


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/palac/OneDrive/Escritorio/practica-sqlites3/database/estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Aquí empiezan las rutas
@app.route("/")
def home():
    return "<h1>Hola Rosy</h1>"

@app.route("/api/estudiantes", methods=["GET"])
def getEstudiantes():
    try:
        estudiantes = Estudiantes.query.all()
        toReturn = [estudiante.serialize() for estudiante in estudiantes]
        return jsonify(toReturn), 200
        
    except Exception:
        exception("[Server]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
@app.route("/api/estudiante", methods=["GET"])
def getEstudianteByNumLista():
    try:
        numero_listaEstudiante = request.args["numero_lista"]
        estudiante = Estudiantes.query.filter_by(numero_lista = numero_listaEstudiante).first()
        if not estudiante:
            return jsonify({"msg":"Este estudiante no existe"}), 200
        else:
            return jsonify(estudiante.serialize()), 200
    except Exception:
        exception("[Server]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=4000)