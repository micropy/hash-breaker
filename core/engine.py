# dehasher/core/engine.py
from hashes.dehash_md5 import *
from hashes.dehash_sha1 import *
from hashes.dehash_sha256 import *
from hashes.dehash_sha512 import *
from hashes.dehash_bcrypt import *
import re

def engine(hash_str: str):
    expresion = re.match(r'^\$?SHA(?:256|512)?\$?(\w+)\$(\w+)$', hash_str)
    if expresion:
        group1, group2 = expresion.groups()
        hash = group1 if len(group1) in [64, 128] else group2
        salt = group2 if hash == group1 else group1
        print(hash, salt)

    hashes = {
        32 : 'md5',
        40 : 'sha1',
        64 : 'sha256',
        128 : 'sha512'
    }
    if len(hash) in hashes:
        hash_type = hashes.get(len(hash))
        print(hash_type)

    elif hash_str.startswith('$2a$') or hash_str.startswith('$2b$') or hash_str.startswith('$2y$'):
        print("bcrypt")
    else:
        print("Unknown hash type")
