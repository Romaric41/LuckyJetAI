def analyser(historique):

    if not historique:
        return "📭 Aucun historique disponible."

    total = len(historique)

    moyenne = sum(historique) / total
    maximum = max(historique)
    minimum = min(historique)

    hautes = len([x for x in historique if x >= 2])
    grosses = len([x for x in historique if x >= 5])

    frequence_haute = (hautes / total) * 100
    frequence_grosse = (grosses / total) * 100

    derniers_5 = historique[-5:]
    moyenne_5 = sum(derniers_5) / len(derniers_5)

    precedents = historique[-10:-5]

    if precedents:
        moyenne_precedents = sum(precedents) / len(precedents)

        if moyenne_5 > moyenne_precedents:
            tendance = "📈 Hausse récente"
        elif moyenne_5 < moyenne_precedents:
            tendance = "📉 Baisse récente"
        else:
            tendance = "⏳ Stable"

        comparaison = (
            f"📈 5 derniers : {moyenne_5:.2f}x\n"
            f"📊 5 précédents : {moyenne_precedents:.2f}x"
        )

    else:
        moyenne_precedents = 0
        tendance = "⏳ Pas assez de données"
        comparaison = "⏳ Pas assez de tours pour comparer"


    serie_basse = 0

    for x in reversed(historique):
        if x < 1.5:
            serie_basse += 1
        else:
            break


    score = 50

    if moyenne >= 2:
        score += 10

    if frequence_haute >= 50:
        score += 10

    if tendance == "📈 Hausse récente":
        score += 10

    if score > 100:
        score = 100


    return f"""
🔮 LuckyJet AI Pro v5.1

📊 Tours analysés : {total}

📈 Moyenne générale : {moyenne:.2f}x
🚀 Maximum : {maximum:.2f}x
📉 Minimum : {minimum:.2f}x

🚀 Tours ≥2x : {hautes}
💎 Tours ≥5x : {grosses}

📈 Fréquence ≥2x : {frequence_haute:.1f}%
💎 Fréquence ≥5x : {frequence_grosse:.1f}%

🔢 5 derniers tours :
{derniers_5}

📊 Comparaison récente :
{comparaison}

📡 Tendance : {tendance}

🔥 Série basse actuelle : {serie_basse}

🎯 Indice statistique : {score}%

⚠️ Analyse basée uniquement sur l'historique.
"""

