from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from sha256 import sha256

def keygen(uid):
    # 產生 256 位元隨機金鑰（32 位元組 = 256 位元）
    sessionkey = get_random_bytes(32)
    print("Encryption Key:"+str(sessionkey))

    #金鑰儲存位置
    keyPath = str(uid)+".bin"

    # 儲存金鑰
    with open(keyPath, "wb") as f:
        f.write(sessionkey)

    # 讀取金鑰
    with open(keyPath, "rb") as f:
        keyFromFile = f.read()

    # 檢查金鑰儲存
    assert sessionkey == keyFromFile, '金鑰不符'

    return sessionkey

def enc(msg, key):
    # 輸出的加密檔案名稱
    outputFile = 'encrypted.bin'

    # 以金鑰搭配 CBC 模式建立 cipher 物件
    cipher = AES.new(key, AES.MODE_CBC)

    # 將輸入資料加上 padding 後進行加密
    cipheredData = cipher.encrypt(pad(msg, AES.block_size))
    print("iv", str(cipher.iv))
    print("ivlen:", len(cipher.iv))
    print("cipher:"+str(cipheredData))
    print("cipherlen:"+str(len(cipheredData)))
    
    # 將初始向量與密文寫入檔案
    with open(outputFile, "wb") as f:
        f.write(cipher.iv)
        f.write(cipheredData)

def dec(cipheredData,iv,key):
    # 以金鑰搭配 CBC 模式與初始向量建立 cipher 物件
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # 解密後進行 unpadding
    originalData = unpad(cipher.decrypt(cipheredData), AES.block_size)

    # 輸出解密後的資料
    print("decrypt output:"+str(originalData))
    print("decryptlen:"+str(len(originalData)))
    with open("decrypt.bin", "wb") as f:
        f.write(originalData)


def main():
    #key = keygen('sessionkey1')
    s = 'My secret'
    print('----------SHA----------')
    key = sha256(s)
    print("shakeylen:",len(key))
    with open("AESkey.txt","wb") as f:
        f.write(key)

    with open("plaintext.txt","rb") as f:
        ptxt = f.read()
    print('----------AES----------')
    print("Plaintext:"+str(ptxt))
    enc(ptxt,key)

def main1():
    with open("encrypted.bin","rb") as f:
        iv = f.read(16)         # 讀取 16 位元組的初始向量
        ctxt = f.read() # 讀取其餘的密文
    with open("AESkey.txt","rb") as f:
        key = f.read()
    dec(ctxt,iv,key)
'''
    with open("eccdec.bin","rb") as fil:
        key = fil.read()
'''
if __name__ == "__main__":
    main()
    main1()
