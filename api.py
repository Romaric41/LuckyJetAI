from flask import Flask, request, jsonify
from database import ajouter_resultat, lire_historique

app = Flask(__name__)


@app.route("/")
def accueil():
    return "🚀 LuckyJet AI API en ligne"


@app.route("/ajouter", methods=["POST"])
def ajouter():
    data = request.json

    cote = float(data["cote"])

    ajouter_resultat(cote)

    return jsonify({
        "message": "Résultat enregistré",
        "cote": cote
    })


@app.route("/historique", methods=["GET"])
def historique():
    return jsonify(lire_historique())


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
