from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database\\estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Aquí empiezan las rutas
@app.route("/")
def home():
    return "<h1>Hola Rosy</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=4000)