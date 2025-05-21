from flask import Flask, render_template, request
import random
from tsp_solver import simulated_annealing, evalua_ruta, coord

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            T_MIN = float(request.form["T_MIN"])
            T_INICIAL = float(request.form["T_INICIAL"])
            VELOCIDAD_ENFRIAMIENTO = int(request.form["VELOCIDAD_ENFRIAMIENTO"])

            ruta = list(coord.keys())
            random.shuffle(ruta)

            mejor_ruta = simulated_annealing(ruta, T_INICIAL, T_MIN, VELOCIDAD_ENFRIAMIENTO)
            distancia_total = evalua_ruta(mejor_ruta)

            return render_template("index.html", ruta=mejor_ruta, distancia=round(distancia_total, 2))

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
