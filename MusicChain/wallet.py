import random
import ecdsa
import hashlib
import os
import binascii

b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n % 58] + result
        n /= 58
    return result


def base58CheckEncode(version, payload):
    s = chr(version) + payload
    print(binascii.b2a_hex(s))
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
    print(binascii.b2a_hex(checksum))


def PrivateToPublic(s):
    signkey = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    verifykey = signkey.verifying_key
    return ('\04' + signkey.verifying_key.to_string()).encode('hex')


private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])

base58CheckEncode(0x80, private_key.decode('hex'))
