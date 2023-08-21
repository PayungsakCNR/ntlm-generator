import hashlib,binascii
hash = hashlib.new('md4', "MyCrazyPass".encode('utf-16le')).digest()

passStr = str(binascii.hexlify(hash))

passSplit1 = passStr.split("'",1)[1]
passSplit2 = passSplit1.split("'",1)[0]

passFinal = passSplit2.upper()

print (passFinal)
