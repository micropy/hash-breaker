import bcrypt
from core.load_wordlist import load_wordlist

def dehash_bcrypt(hash: str):
    load_wordlist()
    wordlist = load_wordlist()
    for password in wordlist:
        # Check if the password matches the hash
        if bcrypt.checkpw(password.encode(), hash.encode()):
            return password