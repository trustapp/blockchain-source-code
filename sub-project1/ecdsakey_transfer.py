from ecc.curve import secp256k1
from ecc.key import gen_keypair
from ecc.cipher import ElGamal
import sys
from sha256 import sha256
from ecc.curve import Point

default_length = 16

def str_to_class(word):
    return Point(word)

def block_data(data,bs):
    for i in range(0, len(data), bs):
        yield data[i:i+bs]
def tranclass_Point(x, y, curve = secp256k1):
    #elg = ElGamal(curve)
    return Point(x, y, curve)

# Encrypt using ElGamal algorithm
def ecelgenc(plaintext, pub_key, curve = secp256k1):
    cipher_elg = ElGamal(curve)
    encipher = []
    data_len = len(str(plaintext))
    if data_len < default_length:
        C1, C2 = cipher_elg.encrypt(plaintext, pub_key)
        encipher.append(C1)
        encipher.append(C2)
    else:
        for dat in block_data(plaintext,default_length):
            C1, C2 = cipher_elg.encrypt(dat, pub_key)
            encipher.append(C1)
            encipher.append(C2)

    print("encipher:",encipher)
    return encipher

# Decrypt
def ecelgdec(encipher, pri_key, curve = secp256k1):
    decipher = b""
    cipher_elg = ElGamal(curve)
    for i in range(0,len(encipher),2):
        #print("dat0", encipher[i])
        #print("dat1", encipher[i+1])
        cur_text = cipher_elg.decrypt(pri_key, encipher[i],encipher[i+1])
        decipher += cur_text

    print("decrypt:",decipher)
    return decipher

plaintext = b'this is elg.py'
pri_key =  86771072921863548814618211630176114507777096857857245614951953340130353561253
x = 68329132431806711158772925968980819821423615324491817844360271788567425783114
y = 64793056157796919884719732456754165381244580758542756678579364961246758834564
pub_key = tranclass_Point(x, y)
cipher = ecelgenc(plaintext, pub_key)
msg = ecelgdec(cipher, pri_key)

