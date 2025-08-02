
# import requests

# def valyuta_to_see(text: str):
    
#     val1, val2, amount = text.strip().split("-")
#     amount = float(amount)

#     url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
#     response = requests.get(url)

#     if response.status_code != 200:
#         return "API bilan bog'lanishda xatolik yuz berdi."

#     values = response.json()

#     kurslar = {val['Ccy'].lower(): float(val['Rate'].replace(',', '')) for val in values}

#     if val1.lower() not in kurslar or val2.lower() not in kurslar:
#         return "Kiritilgan valyutalardan biri topilmadi."

#     result = kurslar[val1.lower()] * amount / kurslar[val2.lower()]

#     return f"{amount} {val1.upper()} = {result:.2f} {val2.upper()}"

# import requests
# from pprint import pprint


import requests

def valyuta_to_see(text: str):
    try:
        val1, val2, amount = text.strip().split("-")
        amount = float(amount)

        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"  
        response = requests.get(url)

        if response.status_code != 200:
            return "❌ API bilan bog'lanishda xatolik yuz berdi."

        values = response.json()

        kurslar = {
            val['Ccy'].lower(): float(val['Rate'].replace(',', ''))
            for val in values
        }

        kurslar['uzs'] = 1.0  
        

        if val1.lower() not in kurslar or val2.lower() not in kurslar:
            return f"❌ Valyutalardan biri topilmadi: {val1.upper()} yoki {val2.upper()}"

        result = kurslar[val1.lower()] * amount / kurslar[val2.lower()]

        return f"✅ {amount} {val1.upper()} = {result:.2f} {val2.upper()}"

    except ValueError:
        return "❌ Format xato! Masalan: USD-UZS-100 tarzida yozing."
    except Exception as e:
        return f"❌ Xatolik: {e}"

        

                
        