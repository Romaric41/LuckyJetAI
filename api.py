from flask import Flask, jsonify

from database import (
    lire_historique
)

from analyse import (
    analyser
)


app = Flask(__name__)


@app.route("/")
def accueil():
    return jsonify(
        {
            "nom": "LuckyJet AI",
            "version": "v6.0",
            "message": "🚀 API active"
        }
    )


@app.route("/historique")
def historique():

    data = lire_historique()

    return jsonify(
        {
            "total": len(data),
            "derniers_50": data[-50:]
        }
    )


@app.route("/analyse")
def analyse():

    data = lire_historique()

    resultat = analyser(data)

    return jsonify(
        {
            "analyse": resultat
        }
    )


@app.route("/stats")
def stats():

    data = lire_historique()

    if not data:
        return jsonify(
            {
                "message": "Aucun historique disponible"
            }
        )


    total = len(data)
    moyenne = sum(data) / total
    maximum = max(data)
    minimum = min(data)


    return jsonify(
        {
            "tours": total,
            "moyenne": round(moyenne, 2),
            "maximum": maximum,
            "minimum": minimum
        }
    )


@app.route("/rapport")
def rapport():

    data = lire_historique()

    resultat = analyser(data)

    return jsonify(
        {
            "rapport": resultat
        }
    )


if __name__ == "__main__":

    print("🚀 LuckyJet AI API v6.0 démarrée...")

    app.run(
        host="0.0.0.0",
        port=5000
    )

