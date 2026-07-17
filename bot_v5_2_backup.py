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
        f"🤖 Bienvenue sur {BOT_NAME}\n\n"
        "Commandes disponibles :\n"
        "/analyse - Analyse avancée\n"
        "/stats - Statistiques rapides\n\n"
        "Envoie un multiplicateur exemple : 1.45"
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
        f"📊 Stats rapides LuckyJet AI\n\n"
        f"🎯 Tours : {total}\n"
        f"📈 Moyenne : {moyenne:.2f}x\n"
        f"🚀 Maximum : {maximum:.2f}x\n"
        f"📉 Minimum : {minimum:.2f}x"
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
app.add_handler(CommandHandler("analyse", analyse_commande))
app.add_handler(CommandHandler("stats", stats))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, enregistrer)
)

print("🚀 LuckyJet AI Pro démarré...")

app.run_polling()
