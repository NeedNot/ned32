import sympy
import json
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1


p = str(input("input a prime: ")).replace(",", "")
q = str(input("input another prime: ")).replace(",", "").replace(",", "")
p = int(p)
q = int(q)
n = p * q

phi = (p-1)*(q-1)
x = 0
for i in range(phi-1):
    i = i + 42589
    x += 1
    if is_coprime(i, n):
        if is_coprime(i, phi):
            if x > 2000:
                break
            e = i
            print(e)
e = int(input("ok now which one should we use? "))

d = sympy.mod_inverse(e, phi)

data = {}
data['p'] = hex(p)[2:]
data['q'] = hex(q)[2:]
data['n'] = hex(n)[2:]
data['phi'] = hex(phi)[2:]
data['e'] = hex(e)[2:]
data['d'] = hex(d)[2:]

with open('keys.json', 'w') as outfile:
    json.dump(data, outfile)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)

