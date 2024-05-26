from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Estudiantes(db.Model):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    numero_lista = db.Column(db.Integer(50), nullable=False)
    grupo = db.Column(db.Enum('A', 'B', 'C'), nullable=False)
    genero = db.Column(db.Boolean, nullable=False) #True/False para masculino/femenino
    ciclo_escolar = db.Column(db.String(50), nullable=False)
