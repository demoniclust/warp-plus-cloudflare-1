import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import asyncio
from Config import Config
import telepot

bot = telepot.Bot(Config.BOT_TOKEN)

bot.sendMessage(Config.LOG_CHAT_ID,
                'WARP+ Logging start.') 	

os.system("title WARP-PLUS-CLOUDFLARE")
os.system('cls' if os.name == 'nt' else 'clear')

referrer = Config.LICENSE_KEY

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		bot.sendMessage(Config.LOG_CHAT_ID,
                         f"[Error]\n\n{error}")	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] WORK ON ID: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		print("[*] After 18 seconds, a new request will be sent.")
		
  
		# bot-logger
		bot.sendMessage(Config.LOG_CHAT_ID,
                       	 f"\n{g} GB has been successfully added to your account."
                         f"\nTotal: {g} Good {b} Bad"
                         "\nAfter 18 seconds, a new request will be sent."
                         "\nRunning by: @spookyanii")
		time.sleep(18)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")	
		bot.sendMessage(Config.LOG_CHAT_ID,
                  "\nError when connecting to server."
                  f"\nTotal: {g} Good {b} Bad")