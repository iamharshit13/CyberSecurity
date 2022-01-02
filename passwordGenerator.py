import random
alphabets = 'abcdefgijklmnopqrstuvwxyz'
ALPHABETS = alphabets.upper()
specialChar = '!@#$%^&*()_'
digits = '0123456789'

def passgen(llen,ulen,slen,dlen):
    s=random.choices(alphabets,k=llen)
    l=(random.choices(ALPHABETS,k=ulen))
    sc=(random.choices(specialChar,k=slen))
    d=random.choices(digits,k=dlen)
    fpass=s+l+sc+d
    random.shuffle(fpass)
    a=""
    a=a.join(fpass)
    return a

llen=int(input("number of lowercase charecter:"))
ulen=int(input("number of UPPER charecter:"))
slen=int(input("number of special charecter:"))
dlen=int(input("number of digit charecter:"))

yourpass = passgen(llen, ulen, slen, dlen)
print()
print("Password:",yourpass)
print("Total length:",len(yourpass))
if len(yourpass)<8:
    print("(Warning: password having length of 8 or more are generally more secure)")