from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "clave_secreta"


def verificar(numero, intento):
    if intento < numero:
        return "mayor"
    elif intento > numero:
        return "menor"
    else:
        return "adivinaste"


@app.route("/", methods=["GET", "POST"])
def inicio():

    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 100)
        session["intentos"] = 0

    mensaje = ""

    if request.method == "POST":
        intento = int(request.form["intento"])
        session["intentos"] += 1

        resultado = verificar(session["numero_secreto"], intento)

        if resultado == "adivinaste":
            mensaje = f"🎉 ¡Adivinaste! Lo lograste en {session['intentos']} intentos."

            session["numero_secreto"] = random.randint(1, 100)
            session["intentos"] = 0
        else:
            mensaje = f"Pista: el número es {resultado}."

    return render_template("index.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
