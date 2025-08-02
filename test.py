import requests
from config import TOKEN
from printers.prints_menu import print_menu
from printers.prints_menu import print_help
from valyuta.valyuta_replece import valyuta_to_see
import time

get_messege_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
send_messege_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

last_update_id = None  

while True:

    params = {"offset": last_update_id + 1} if last_update_id else {}

    response = requests.get(get_messege_url, params=params, timeout=10)

    if response.status_code == 200:
        updates = response.json().get("result", [])

        if updates:
            for update in updates:
                last_update_id = update["update_id"]

                message = update.get("message", {})
                text = message.get("text", "")
                chat_id = message.get("chat", {}).get("id")

                if text.lower() == "/start":
                    reply_text = print_menu()
                else:
                    reply_text = valyuta_to_see(text)
                
                if text.lower() == "/help":
                    reply_text = print_help()

                send_data = {
                    "chat_id": chat_id,
                    "text": reply_text,
                    "parse_mode": "Markdown"
                }

                requests.post(send_messege_url, data=send_data)

    time.sleep(1) 


