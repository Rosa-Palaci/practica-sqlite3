from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Estudiantes(db.Model):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    numero_lista = db.Column(db.Integer, nullable=False)
    grupo = db.Column(db.String(1), nullable=False)  
    genero = db.Column(db.String(50), nullable=False)  
    ciclo_escolar = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return "Numero de Lista: {}.\n Grupo: {}.\n Genero: {}.\n Ciclo Escolar: {}".format(
            self.numero_lista,
            self.grupo,
            self.genero,
            self.ciclo_escolar
        )
    
    def serialize(self):
        return {
            "id_estudiante": self.id_estudiante,
            "numero_lista": self.numero_lista,
            "grupo": self.grupo,
            "genero": self.genero,
            "ciclo_escolar": self.ciclo_escolar
        }
        