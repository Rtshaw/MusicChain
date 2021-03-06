import random
import ecdsa
import hashlib
import os
import binascii
import codecs
import utils
import base58
import base64

P = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def ripemd160(x):
    d = hashlib.new("ripemd160")
    d.update(x)
    return d


def base58encode(d):
    result = ""
    p = 0
    x = 0

    while d[0] == 0:
        result += '1'
        d = d[1:]

    for i, v in enumerate(d[::-1]):
        x += v * (256 ** i)

    while x > 58 ** (p + 1):
        p += 1
    while p >= 0:
        a, x = divmod(x, 58 ** p)
        result += b58[a]
        p -= 1
    return result

def PointAddress(p, q):
    xp, yp = p
    xq, yq = q

    if p == q:
        l = pow(2 * yp % P, P - 2, P) * (3 * xp * xp) % P
    else:
        l = pow(xq - xp, P - 2, P) * (yq - yp) % P

    xr = (l ** 2 - xp - xq) % P
    yr = (l * xp - l * xr - yp) % P

    return xr, yr


def PointMul(p, d):
    n = p
    q = None

    for i in range(256):
        if d & (1 << i):
            if q is None:
                q = n
            else:
                q = PointAddress(q, n)

        n = PointAddress(n, n)

    return q


def PointBytes(p):
    x, y = p
    return b'\x04' + x.to_bytes(32, 'big') + y.to_bytes(32, 'big')


def PrivateToWif(privatekey):
    wif = b'\x80' + privatekey
    chechsum = hashlib.sha256(hashlib.sha256(wif).digest()).digest()[0:4]
    wif += chechsum
    wif = base58encode(wif)

    return wif


def PrivateKeyToPublicKey(s):
    signkey = ecdsa.SigningKey.from_string(codecs.decode(s, 'hex'), curve=ecdsa.SECP256k1)
    verifykey = signkey.get_verifying_key()

    return ('04' + verifykey.to_string().hex())


def PublicToAddr(privatekey):
    q = PointMul(G, int.from_bytes(privatekey, 'big'))
    hash160 = ripemd160(hashlib.sha256(PointBytes(q)).digest()).digest()
    address = b'\x00' + hash160
    checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[0:4]
    address += checksum
    address = base58encode(address)

    return address


private_key = os.urandom(32)
privakey = private_key.hex()

print('Private Key 私鑰:')
print(privakey)
print('')
print('Public key 公鑰:')
print(PrivateKeyToPublicKey(privakey))
print('')
print('Private key to WIF (Hash公鑰):')
print(PrivateToWif(private_key))
print('')
print('Address:')
print(PublicToAddr(private_key))