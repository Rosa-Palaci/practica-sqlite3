from flask import Flask
from Models import db, Estudiantes


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/palac/OneDrive/Escritorio/practica-sqlites3/database/estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Aquí empiezan las rutas
@app.route("/")
def home():
    return "<h1>Hola Rosy</h1>"

@app.route("/api/estudiantes")
def getEstudiantes():
    estudiantes = Estudiantes.query.all()
    print(estudiantes)
    return "<h1>Estudiantes</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=4000)