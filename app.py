from flask import Flask, jsonify, request, render_template
from Models import db, Estudiantes
from logging import exception


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/palac/OneDrive/Escritorio/practica-sqlites3/database/estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Aquí empiezan las rutas
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/loginEstudiantes")
def loginEstudiantes():
    return render_template("login_estudiantes.html")

@app.route("/loginProfesores")
def loginProfesores():
    return render_template("login_profesores.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/buscadorestudiante", methods = ["GET"])
def buscadorEstudiante():
    return render_template("buscadorestudiante.html")

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
    
@app.route("/api/findsestudiante", methods=["GET"])
def getEstudiante():
    try:
        fields = {}
        if "numero_lista" in request.args:
            fields["numero_lista"] = request.args["numero_lista"]
        if "grupo" in request.args:
            fields["grupo"] = request.args["grupo"]
        if "genero" in request.args:
            fields["genero"] = request.args["genero"]
        if "ciclo_escolar" in request.args:
            fields["ciclo_escolar"] = request.args["ciclo_escolar"]

        estudiante = Estudiantes.query.filter_by(**fields).first()
        if not estudiante:
            return jsonify({"msg":"Este estudiante no existe"}), 200
        else:
            return jsonify(estudiante.serialize()), 200
    except Exception:
        exception("[Server]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
#Añadir estudiantes y buscar mediante formularios

@app.route("/registroEstudiantes", methods = ["POST"])
def registroEstudiantes():
    try:
        numero_lista = request.form["numero_lista"]
        grupo = request.form["grupo"]
        genero = request.form["genero"]
        ciclo_escolar = request.form["ciclo_escolar"]

        estudiante = Estudiantes(numero_lista, str(grupo), str(genero), str(ciclo_escolar))

        db.session.add(estudiante)
        db.session.commit()

        return jsonify(estudiante.serialize()), 200

    except Exception:
        exception("\n[SERVER]: Error in route /registroEstudiantes. Log: \n")
        return jsonify({"msg": "Algo ha salido mal"}), 500

#Filtrar datos
@app.route("/api/buscardorestudiante", methods=["POST"])
def buscardorEstudianteForm():
    try:
        numEstudiante = request.form["numero_lista"]
        grupoEstudiante = request.form["grupo"]

        estudiante = Estudiantes.query.filter(
            Estudiantes.numero_lista.like(f"%{numEstudiante}%"),
            Estudiantes.grupo.like(f"%{grupoEstudiante}%")
        ).first()
        if not estudiante:
            return jsonify({"msg": "Este estudiante no existe"}), 200
        else:
            return jsonify(estudiante.serialize()), 200

    except Exception:
        exception("[SERVER]: Error in route /api/buscardorestudiante ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=4000)