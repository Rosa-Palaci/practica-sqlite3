from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Estudiantes(db.Model):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    numero_lista = db.Column(db.Integer, nullable=False)
    grupo = db.Column(db.String(1), nullable=False)  
    genero = db.Column(db.String(50), nullable=False)  
    ciclo_escolar = db.Column(db.String(50), nullable=False)