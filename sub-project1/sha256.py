import hashlib

def sha1(msg):
    print("Message:"+msg)
    s = hashlib.sha1()
    s.update(msg.encode('utf-8'))
    hashmsg = s.digest()
    print("HashValue:"+str(hashmsg))
    #print("outlen:"+str(len(hashmsg)))
    return hashmsg

def sha256(msg):
    print("Message:"+msg)
    s = hashlib.sha256()
    s.update(msg.encode('utf-8'))
    hashmsg = s.digest()
    print("HashValue:"+str(hashmsg))
    #print("outlen:"+str(len(hashmsg)))
    return hashmsg

def sha256_hex(msg):
    s = hashlib.sha256()
    s.update(msg.encode('utf-8'))
    hashmsg = s.hexdigest()
    return hashmsg


if __name__ == '__main__':
    print(sha256('test'))

