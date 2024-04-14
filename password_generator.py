import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "./,;:-#+*!&%$?<>"

upper, lower, num, symb = True, True, True, True
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if  num:
    all += digits
if symb:
    all += symbols

length = 8
amount = 2

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)



