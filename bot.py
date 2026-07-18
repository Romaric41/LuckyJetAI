from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TOKEN, BOT_NAME

from database import (
    initialiser,
    ajouter_resultat,
    lire_historique,
)

from analyse import analyser


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"""
🚀 {BOT_NAME}

Bienvenue !

Commandes disponibles :

/analyse - Analyse complète
/stats - Statistiques rapides
/rapport - Rapport intelligent
/aide - Liste des commandes

Envoie un multiplicateur exemple :
1.45
"""
    )


async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🤖 LuckyJet AI Pro v5.8

📌 Commandes disponibles :

/start
➡️ Démarrer le bot

/analyse
➡️ Analyse complète de l'historique

/stats
➡️ Statistiques rapides

/rapport
➡️ Rapport intelligent avec score

/aide
➡️ Afficher ce menu

📩 Enregistrement :
Envoie un multiplicateur.

Exemple :
1.45
"""
    )


async def analyse_commande(update: Update, context: ContextTypes.DEFAULT_TYPE):
    historique = lire_historique()

    resultat = analyser(historique)

    await update.message.reply_text(resultat)


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    historique = lire_historique()

    if not historique:
        await update.message.reply_text(
            "📭 Aucun résultat enregistré."
        )
        return

    total = len(historique)
    moyenne = sum(historique) / total
    maximum = max(historique)
    minimum = min(historique)

    await update.message.reply_text(
        f"""
📊 Stats rapides LuckyJet AI

📈 Tours : {total}
📈 Moyenne : {moyenne:.2f}x
🚀 Maximum : {maximum:.2f}x
📉 Minimum : {minimum:.2f}x
"""
    )


async def rapport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    historique = lire_historique()

    if not historique:
        await update.message.reply_text(
            "📭 Aucun résultat enregistré."
        )
        return

    resultat = analyser(historique)

    await update.message.reply_text(
        f"""
📋 LuckyJet AI Pro - Rapport v5.8

{resultat}
"""
    )


async def enregistrer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text.replace(",", ".")

    try:
        valeur = float(texte)

        ajouter_resultat(valeur)

        await update.message.reply_text(
            f"✅ Résultat enregistré : {valeur}x"
        )

    except ValueError:
        await update.message.reply_text(
            "❌ Envoie un nombre exemple : 1.45"
        )


initialiser()

app = Application.builder().token(TOKEN).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("aide", aide))
app.add_handler(CommandHandler("analyse", analyse_commande))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("rapport", rapport))


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        enregistrer
    )
)


print("🚀 LuckyJet AI Pro v5.8 démarré...")


app.run_polling()

