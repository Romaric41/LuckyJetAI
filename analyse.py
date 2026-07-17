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
    derniers_10 = historique[-10:]
    derniers_20 = historique[-20:]
    derniers_50 = historique[-50:]


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
        tendance = "⏳ Pas assez de données"
        comparaison = "⏳ Pas assez de tours pour comparer"


    total_50 = len(derniers_50)

    moyenne_50 = sum(derniers_50) / total_50

    tours_2x_50 = len([x for x in derniers_50 if x >= 2])
    tours_5x_50 = len([x for x in derniers_50 if x >= 5])

    frequence_50 = (tours_2x_50 / total_50) * 100


    serie_basse = 0
    for x in reversed(historique):
        if x < 1.5:
            serie_basse += 1
        else:
            break


    serie_haute = 0
    for x in reversed(historique):
        if x >= 2:
            serie_haute += 1
        else:
            break


    score = 50
    raisons = []


    if moyenne >= 2:
        score += 10
        raisons.append("✅ Moyenne générale correcte")

    if frequence_haute >= 50:
        score += 10
        raisons.append("✅ Fréquence ≥2x acceptable")

    if tendance == "📈 Hausse récente":
        score += 10
        raisons.append("✅ Tendance récente positive")

    if serie_basse >= 3:
        score -= 10
        raisons.append("⚠️ Série basse détectée")


    if len(historique) < 10:
        raisons.append("⏳ Peu de données disponibles")


    if score > 100:
        score = 100

    if score < 0:
        score = 0


    if score >= 80:
        niveau = "🟢 Conditions statistiques fortes"
    elif score >= 50:
        niveau = "🟡 Conditions statistiques moyennes"
    else:
        niveau = "🔴 Conditions statistiques faibles"


    return f"""
🔮 LuckyJet AI Pro v5.5

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

🔟 10 derniers tours :
{derniers_10}

2️⃣0️⃣ 20 derniers tours :
{derniers_20}

5️⃣0️⃣ 50 derniers tours :
{derniers_50}


📊 Analyse des 50 derniers :
📈 Moyenne : {moyenne_50:.2f}x
🚀 Tours ≥2x : {tours_2x_50}
💎 Tours ≥5x : {tours_5x_50}
📊 Fréquence ≥2x : {frequence_50:.1f}%


📊 Comparaison récente :
{comparaison}

📡 Tendance : {tendance}

🔥 Série basse actuelle : {serie_basse}
🚀 Série haute actuelle : {serie_haute}


🎯 Indice statistique : {score}%

{niveau}

📌 Raisons :
{"\n".join(raisons)}

⚠️ Analyse basée uniquement sur l'historique.
"""

