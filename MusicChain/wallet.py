import random
import ecdsa
import hashlib
import os
import binascii
import codecs
import utils
import base58

b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n % 58] + result
        n /= 58
    return result


def base58CheckEncode(version, payload):
    s = chr(version) + payload
    s_bytes = s.encode()
    print(binascii.b2a_hex(s_bytes))
    checksum = hashlib.sha256(hashlib.sha256(s_bytes).digest()).digest()[0:4]
    print(binascii.b2a_hex(checksum))


def PrivateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(codecs.decode(s, 'hex'), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return ('04' + vk.to_string().hex())


"""
def PrivateToWif(key_hex):
    return utils.base58CheckEncode(0x80, key_hex.decode('hex'))

def PublicToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return utils.base58CheckEncode(0, ripemd160.digest())


def keyToAddr(s):
    return PublicToAddr(PrivateToPublic(s))
"""
"""
def PrivateToPublic(s):
    signkey = ecdsa.SigningKey.from_string()
    verifykey = signkey.get_verifying_key()
    return ('\04' + signkey.get_verifying_key()
    # return ('\04' + signkey.verifying_key.to_string()).encode('hex')
"""

private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])

# print(private_key)
# print(PrivateKeyToPublicKey(private_key))

testpvk = 'c1a1e4052d37408204b73b1b016825ccf03216a1e57220359834498fa88eedf0'
print(PrivateKeyToPublicKey(testpvk))