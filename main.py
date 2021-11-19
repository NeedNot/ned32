import json
import base64
with open('keys.json') as json_file:
    data = json.load(json_file)

p = int(data['p'], 16)
q = int(data['q'], 16)
n = int(data['n'], 16)
en = int(data['en'], 16)
phi = int(data['phi'], 16)
e = int(data['e'], 16)
d = int(data['d'], 16)

def ned32(x):
    i = int.from_bytes(x.encode('ASCII'), byteorder='big')
    print(i)
    if i >= n:
        return "number is too big"
    if en == "put someone else's mod here":
        return "please enter a mod in keys.json"
    msg = pow(i, e, en)
    return base64.b64encode(str(msg).encode('ascii')).decode('utf-8')
def dened32(x):
    x = x.rstrip("=") + "=="
    x = int(base64.b64decode(bytes(x.encode('ascii')).decode('utf-8')))
    if x >= n:
        return "number is too big"
    msg = pow(x, d, n)
    s = int.to_bytes(msg, length=100, byteorder='big').decode('ASCII').strip(chr(0))
    return s

x = input("encrypt or decrypt? (e/d): ")

if x == "e":
    x = str(input("enter something to encrypt: "))
    print(ned32(x))
if x == "d":
    x = str(input("enter something to decrypt: "))
    print(dened32(x))