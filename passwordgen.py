import string
import random

def gen():
    capital=string.ascii_uppercase
    small=string.ascii_lowercase
    number=string.digits
    symbol=string.punctuation

    pass_len=int(input("Enter the Password Length:"))
    s=[]
    s.extend(list(capital))
    s.extend(list(small))
    s.extend(list(number))
    s.extend(list(symbol))

    random.shuffle(s)
    passs=("".join(s[0:pass_len]))
    print(passs)





gen()