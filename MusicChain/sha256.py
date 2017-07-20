import hashlib

hash = hashlib.sha256(b'MusicBlockChain')
hex_dig = hash.hexdigest()
print(hex_dig)