import requests
import time

API_URL = "https://api.telegram.org/bot"
API_CATS_URL = "https://api.thecatapi.com/v1/images/search"
BOT_TOKEN = ""
ERROR_TEXT = "Котики устали фотографироваться, попробуй позже!"

def main():
    offset = -2
    counter = 0
    cat_response: requests.Response
    cat_link: str


    while True:
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates.get("result"):
            for result in updates.get("result"):
                offset = result.get("update_id")
                chat_id = result.get("message").get("from").get("id")
                cat_response = requests.get(API_CATS_URL)
                if cat_response.status_code == 200:
                    cat_link = cat_response.json()[0].get("url")
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                    print(f"Ещё один котик был отправлен {result.get("message").get("chat").get("first_name")}")
                else: 
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

        time.sleep(1)


if __name__ == "__main__":
    main()
