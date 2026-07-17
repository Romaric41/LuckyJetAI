def analyser(historique):

    if not historique:
        return "📭 Aucun historique disponible."

    total = len(historique)

    moyenne = sum(historique) / total
    maximum = max(historique)
    minimum = min(historique)

    hautes = len([x for x in historique if x >= 2])
    grosses = len([x for x in historique if x >= 5])
    petites = len([x for x in historique if x < 1.5])

    frequence_haute = (hautes / total) * 100
    frequence_grosse = (grosses / total) * 100

    # Série basse actuelle
    serie_basse = 0
    for x in reversed(historique):
        if x < 1.5:
            serie_basse += 1
        else:
            break

    # 5 derniers tours
    derniers_5 = historique[-5:]

    # Tendance simple
    if total >= 5:
        avant = sum(historique[-5:-2]) / 3
        recent = sum(historique[-2:]) / 2

        if recent > avant:
            tendance = "📈 Hausse"
        elif recent < avant:
            tendance = "📉 Baisse"
        else:
            tendance = "⏳ Stable"
    else:
        tendance = "⏳ Pas assez de données"


    score = 50

    if moyenne >= 2:
        score += 10

    if frequence_haute >= 50:
        score += 10

    if tendance == "📈 Hausse":
        score += 10

    if score > 100:
        score = 100


    return f"""
🔮 LuckyJet AI Pro v4

📊 Tours analysés : {total}

📈 Moyenne : {moyenne:.2f}x
🚀 Maximum : {maximum:.2f}x
📉 Minimum : {minimum:.2f}x

🚀 Tours ≥ 2x : {hautes}
💎 Tours ≥ 5x : {grosses}

📈 Fréquence ≥2x : {frequence_haute:.1f}%
💎 Fréquence ≥5x : {frequence_grosse:.1f}%

📡 Tendance : {tendance}

🔥 Série basse actuelle : {serie_basse}

🔢 5 derniers tours :
{derniers_5}

🎯 Indice statistique : {score}%

⚠️ Analyse basée uniquement sur l'historique.
"""

