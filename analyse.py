def analyser(historique):

    if not historique:
        return "📭 Aucun historique disponible."

    total = len(historique)

    moyenne = sum(historique) / total

    hautes = len([x for x in historique if x >= 2.00])
    grosses = len([x for x in historique if x >= 5.00])
    petites = len([x for x in historique if x < 1.50])

    frequence_haute = (hautes / total) * 100
    frequence_grosse = (grosses / total) * 100


    # Série basse actuelle
    serie_basse = 0
    for x in reversed(historique):
        if x < 1.50:
            serie_basse += 1
        else:
            break


    # Analyse de tendance
    if total >= 10:
        anciens = historique[-20:-10]
        recents = historique[-10:]

        moyenne_ancienne = sum(anciens) / len(anciens)
        moyenne_recente = sum(recents) / len(recents)

        if moyenne_recente > moyenne_ancienne:
            tendance = "📈 Hausse"
        elif moyenne_recente < moyenne_ancienne:
            tendance = "📉 Baisse"
        else:
            tendance = "➡️ Stable"

    else:
        tendance = "⏳ Pas assez de données"


    derniers = historique[-20:]


    score = 50

    if moyenne >= 2:
        score += 10

    if frequence_haute >= 40:
        score += 10

    if serie_basse >= 3:
        score += 10

    if tendance == "📈 Hausse":
        score += 10

    if score > 100:
        score = 100


    return (
        "🔮 LuckyJet AI Pro v3\n\n"
        f"📊 Tours analysés : {total}\n"
        f"📈 Moyenne : {moyenne:.2f}x\n\n"
        f"🚀 ≥ 2.00x : {hautes}\n"
        f"💎 ≥ 5.00x : {grosses}\n"
        f"📉 < 1.50x : {petites}\n\n"
        f"📡 Tendance : {tendance}\n"
        f"🔥 Série basse : {serie_basse}\n\n"
        f"📈 Fréquence ≥2x : {frequence_haute:.1f}%\n"
        f"💎 Fréquence ≥5x : {frequence_grosse:.1f}%\n\n"
        f"🔢 Derniers tours : {derniers}\n\n"
        f"🎯 Score statistique : {score}%\n\n"
        "⚠️ Analyse basée uniquement sur l'historique."
    )
