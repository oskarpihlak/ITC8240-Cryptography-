import math

asd=65
for i in range(0, 1584):
    if (i*asd) % 1584 == 1:
        print(i, (i*asd) % 1584)
value=10
enc1 = (value**asd) % 1691
#dec1 = (enc1**317 & 1691)

print("CRACKING")
print()
for i in range(-5000, 1584):

    if (enc1**i % 1691 == value):
        print(f"{enc1}^{i} % 1691 == {value};    {asd}*{i}%mod 1584={(asd*i)%1584}")

#print(enc1, dec1)
print((enc1**(-463)) % 1691)





print("ddadadadada")
for i in range(0, 10000):
    asd22 = (2**i) % 1691
    if (asd22**65) % 1691 == 2:
        print(i)




sss=(2**(-463)) % 1691
print(sss)
print((sss**65) % 1691)
