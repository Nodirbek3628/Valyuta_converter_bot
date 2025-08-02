def print_menu():
    return (
        "🇺🇿 *Assalomu alaykum!*\n"
        "🤖 Siz *Valyuta Konvertatsiya* botiga xush kelibsiz!\n\n"
        "💱 Ushbu bot orqali siz istalgan valyutani boshqa valyutaga avtomatik hisoblab olishingiz mumkin.\n\n"
        "📌 *Foydalanish tartibi:*\n"
        "👉 Faqat quyidagi formatda yozing: `USD-UZS-100`\n"
        "   (ya'ni: qaysi valyutadan - qaysi valyutaga - miqdori)\n\n"
        "✅ *Misollar:*\n"
        "   🔹 `USD-UZS-100` → 100 AQSH dollari necha so'm?\n"
        "   🔹 `UZS-USD-500000` → 500,000 so'm necha dollar?\n"
        "   🔹 `EUR-RUB-50` → 50 yevro necha rubl?\n"
        "   🔹 `GBP-USD-30` → 30 funt sterling necha dollar?\n"
        "   🔹 `JPY-USD-10000` → 10,000 yapon iyenasi necha dollar?\n"
        "   🔹 `AZN-UZS-25` → 25 ozarbayjon manati necha so'm?\n"
        "   🔹 `BRL-USD-100` → 100 braziliya reali necha dollar?\n"
        "   🔹 `AFN-USD-1000` → 1,000 afg'on afg'anisi necha dollar?\n\n"
        "🌐 Valyuta kodlari ISO 4217 standartida bo'lishi kerak (masalan: USD, EUR, GBP, RUB, UZS, KZT, CAD, JPY, va boshqalar).\n\n"
        "🕐 Kurslar O'zbekiston Markaziy Banki yoki boshqa ochiq API manbalaridan olinadi.\n\n"
        
    )

def print_help():
    return("ℹ️ Yordam: `USD` - AQSH dollari, `EUR` - Yevro, `UZS` - So'm,\n"
        "`RUB` - Rubl, `GBP` - Funt sterling, `JPY` - Yapon iyenasi,\n"
        "`AZN` - Ozarbayjon manati, `BRL` - Braziliya reali, `AFN` - Afg'on afg'anisi.")
