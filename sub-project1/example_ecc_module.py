from ecdsa import SigningKey, VerifyingKey, SECP256k1
import hashlib
from sha256 import sha256
from ecdsakey_transfer import ecelgenc, ecelgdec, tranclass_Point

def ECC_KeyGen():
    print("-----key----------------------")
    sk = SigningKey.generate(curve=SECP256k1) # uses NIST256p
    print("sklen:",len(str(sk.to_string())))
    print("sk", str(sk.privkey.secret_multiplier))
    with open("eccsk.pem","wb") as f:
        f.write(sk.to_pem())
    vk = sk.verifying_key
    with open("eccpk.pem","wb") as f:
        f.write(vk.to_pem())
    print("vklen:",len(str(vk.to_string())))

def EC_ElG_Encrypt(plaintext, pk):
    print("-----encrypt------------------")
    x = int(pk.pubkey.point.x())
    y = int(pk.pubkey.point.y())
    pub_key = tranclass_Point(x, y)
    print('pub:', pub_key)
    cipher = ecelgenc(plaintext, pub_key)
    return cipher

def EC_ElG_Decrypt(cipher, sk):
    pri_key = sk.privkey.secret_multiplier
    print('prikey:', pri_key)
    print("-----decrypt------------------")
    msg = ecelgdec(cipher, pri_key)
    return msg

def ECDSA_Sign(msg,sk):
    shamsg = sha256(msg)
    print("-----sign---------------------")
    signature = sk.sign(shamsg)
    #print(signature)
    print("signature:",str(signature))
    return signature
    #assert vk.verify(signature, b"message")

def ECDSA_Verify(msg, pk, signature):
    print("-----verify------------------------")
    shamsg = sha256(msg)
    print("sha256:", shamsg)
    output = pk.verify(signature,shamsg)
    print(output)
    return output

if __name__ == '__main__':
    ECC_KeyGen()
    with open("eccsk.pem","rb") as f:
        sk = SigningKey.from_pem(f.read())
    with open("eccpk.pem","rb") as f:
        pk = VerifyingKey.from_pem(f.read())

    plaintext = b'this is elg_encrypt'
    cipher = EC_ElG_Encrypt(plaintext, pk)
    msg = EC_ElG_Decrypt(cipher, sk)
    with open('decmsg.txt','wb')as f:
        f.write(msg)

    msg = 'this is ecdsa'
    signature = ECDSA_Sign(msg, sk)
    verifyoutput = ECDSA_Verify(msg, pk, signature)
